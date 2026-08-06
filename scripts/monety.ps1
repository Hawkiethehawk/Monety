#!/usr/bin/env pwsh
<#
Monety CLI — 部署与管理入口

用法:
  monety build              重新构建网页端（从 monety/ 生成 viewer/index.html）
  monety start              启动本地网页服务（默认 8888，可用 MONETY_PORT 覆盖）
  monety stop               停止本地网页服务
  monety restart            重启本地网页服务
  monety status             显示项目、Git 与网页服务状态
  monety push [message]     构建 + 提交 + 推送 gitee
  monety update             从 gitee 拉取最新版本并重新构建、重启
  monety help               显示帮助
#>
[CmdletBinding()]
param(
    [Parameter(Position = 0)][string]$Command = "help",
    [Parameter(ValueFromRemainingArguments = $true)][string[]]$Rest
)

$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $PSScriptRoot
$SkillRoot = Join-Path $ProjectRoot "monety"
$ViewerRoot = Join-Path $ProjectRoot "viewer"
$BuildScript = Join-Path $ProjectRoot "scripts\build-skill-viewer.ps1"
$Port = if ($env:MONETY_PORT) { [int]$env:MONETY_PORT } else { 8888 }
$ViewerUrl = "http://127.0.0.1:$Port"

function Test-ViewerUp {
    try {
        $client = [System.Net.Sockets.TcpClient]::new()
        $task = $client.ConnectAsync("127.0.0.1", $Port)
        if (-not $task.Wait(1500)) {
            $client.Dispose()
            return $false
        }
        $client.Dispose()
        return $true
    } catch {
        return $false
    }
}

function Invoke-Build {
    Write-Host "🔧 重新构建网页端..." -ForegroundColor Cyan
    & powershell -NoProfile -ExecutionPolicy Bypass -File $BuildScript
    if ($LASTEXITCODE -ne 0) {
        throw "构建失败，请检查 build-skill-viewer.ps1 输出"
    }
    Write-Host "✅ 构建完成: $ViewerRoot\index.html" -ForegroundColor Green
}

function Start-Viewer {
    if (Test-ViewerUp) {
        Write-Host "📡 网页服务已在运行: $ViewerUrl" -ForegroundColor Green
        return
    }
    Write-Host "📡 启动网页服务: $ViewerUrl" -ForegroundColor Cyan
    Start-Process -FilePath "python" -ArgumentList "-m", "http.server", "$Port", "--bind", "127.0.0.1", "--directory", $ViewerRoot -WindowStyle Hidden
    Start-Sleep -Seconds 2
    if (Test-ViewerUp) {
        Write-Host "✅ 已启动: $ViewerUrl" -ForegroundColor Green
    } else {
        Write-Error "❌ 启动失败：端口未响应"
    }
}

function Stop-Viewer {
    $conns = Get-NetTCPConnection -State Listen -ErrorAction SilentlyContinue | Where-Object { $_.LocalPort -eq $Port }
    if (-not $conns) {
        Write-Host "网页服务未在运行" -ForegroundColor Yellow
        return
    }
    $conns | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }
    Start-Sleep -Milliseconds 800
    if (Test-ViewerUp) {
        Write-Warning "停止失败：端口仍被占用"
    } else {
        Write-Host "✅ 已停止" -ForegroundColor Green
    }
}

function Restart-Viewer {
    Stop-Viewer
    Start-Sleep -Seconds 1
    Start-Viewer
}

function Show-Status {
    Write-Host "📍 Monety 项目: $ProjectRoot"
    Write-Host "   Skill 目录 : $SkillRoot"
    Write-Host "   Viewer 目录: $ViewerRoot"
    $gitLine = git -C $ProjectRoot status -sb 2>$null | Select-Object -First 1
    Write-Host "   Git        : $gitLine"
    if (Test-ViewerUp) {
        Write-Host "   网页服务   : 🟢 运行中 $ViewerUrl"
    } else {
        Write-Host "   网页服务   : ⚪ 未运行（monety start）"
    }
}

function Invoke-Push {
    param([string]$Message)
    Invoke-Build
    git -C $ProjectRoot add -A
    $pending = git -C $ProjectRoot status --porcelain
    if (-not $pending) {
        Write-Host "没有需要提交的改动" -ForegroundColor Yellow
        return
    }
    if ([string]::IsNullOrWhiteSpace($Message)) {
        $Message = "Update monety skill and viewer"
    }
    git -C $ProjectRoot commit -m $Message
    git -C $ProjectRoot push origin master
    Write-Host "✅ 已推送 gitee" -ForegroundColor Green
}

function Invoke-Update {
    Write-Host "🔄 从 gitee 拉取最新版本..." -ForegroundColor Cyan
    git -C $ProjectRoot pull --rebase
    Invoke-Build
    Restart-Viewer
    Write-Host "✅ 更新完成" -ForegroundColor Green
}

function Show-Help {
    Write-Host @"
Monety CLI

用法: monety <command> [options]

命令:
  build              重新构建网页端（从 monety/ 生成 viewer/index.html）
  start              启动本地网页服务（默认 8888，可用 MONETY_PORT 覆盖）
  stop               停止本地网页服务
  restart            重启本地网页服务
  status             显示项目、Git 与网页服务状态
  push [message]     构建 + 提交 + 推送 gitee
  update             从 gitee 拉取最新版本并重新构建、重启
  help               显示帮助

环境变量:
  MONETY_PROJECT_DIR   项目目录（部署脚本自动设置）
  MONETY_PORT          网页服务端口（默认 8888）
"@
}

switch ($Command.ToLower()) {
    "build"    { Invoke-Build }
    "start"    { Start-Viewer }
    "stop"     { Stop-Viewer }
    "restart"  { Restart-Viewer }
    "status"   { Show-Status }
    "push"     { Invoke-Push -Message ($Rest -join " ") }
    "update"   { Invoke-Update }
    "help"     { Show-Help }
    default    {
        Write-Error "未知命令: $Command"
        Show-Help
    }
}
