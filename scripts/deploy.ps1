# Monety 一键部署脚本 (Windows PowerShell)
# 用法:
#   irm https://gitee.com/Hawkiethehawk/Monety/raw/master/scripts/deploy.ps1 | iex
#   或: powershell -ExecutionPolicy Bypass -File scripts\deploy.ps1  (在已克隆的仓库内)
param(
    [string]$InstallDir = $PWD.Path
)

$ErrorActionPreference = "Stop"
$RepoUrl = "https://gitee.com/Hawkiethehawk/Monety.git"

function Register-MonetyShellIntegration {
    param(
        [Parameter(Mandatory = $true)]
        [string]$ProjectDir
    )

    $resolvedProjectDir = (Resolve-Path -LiteralPath $ProjectDir).Path
    [Environment]::SetEnvironmentVariable("MONETY_PROJECT_DIR", $resolvedProjectDir, "User")
    $env:MONETY_PROJECT_DIR = $resolvedProjectDir

    $profilePath = $PROFILE
    if ([string]::IsNullOrWhiteSpace($profilePath)) {
        Write-Host "[!] 未找到 PowerShell profile，已仅设置 MONETY_PROJECT_DIR" -ForegroundColor Yellow
        return
    }

    $profileDir = Split-Path -Parent $profilePath
    New-Item -ItemType Directory -Force -Path $profileDir | Out-Null
    if (-not (Test-Path -LiteralPath $profilePath)) {
        New-Item -ItemType File -Force -Path $profilePath | Out-Null
    }

    $marker = "# >>> Monety default project >>>"
    $profileText = Get-Content -Raw -LiteralPath $profilePath
    if ($profileText -notmatch [regex]::Escape($marker)) {
        $profileBlock = @'
# >>> Monety default project >>>
function monety {
    $projectDir = $env:MONETY_PROJECT_DIR
    if ([string]::IsNullOrWhiteSpace($projectDir)) {
        throw "MONETY_PROJECT_DIR is not set. Run the Monety deployment script again."
    }
    $cli = Join-Path $projectDir "scripts\monety.ps1"
    if (-not (Test-Path -LiteralPath $cli)) {
        throw "Monety CLI not found: $cli"
    }
    Set-Location -LiteralPath $projectDir
    & $cli @args
}
# <<< Monety default project <<<
'@
        if (-not [string]::IsNullOrWhiteSpace($profileText) -and -not $profileText.EndsWith([Environment]::NewLine)) {
            Add-Content -LiteralPath $profilePath -Value ""
        }
        Add-Content -LiteralPath $profilePath -Value $profileBlock
        Write-Host "[✓] 已配置 PowerShell monety 包装函数" -ForegroundColor Green
    } else {
        Write-Host "[✓] PowerShell monety 包装函数已存在" -ForegroundColor Green
    }

    Write-Host "[✓] 已设置默认项目目录: $resolvedProjectDir" -ForegroundColor Green
}

if ($env:MONETY_INSTALL_DIR) {
    $InstallDir = $env:MONETY_INSTALL_DIR
}

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "  Monety 一键部署 (Windows)" -ForegroundColor Cyan
Write-Host "  安装目录: $InstallDir" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# ── 1. 克隆 ──
if (Test-Path "$InstallDir\monety\SKILL.md") {
    Write-Host "[✓] 仓库已存在，跳过克隆" -ForegroundColor Green
} elseif (Test-Path "$InstallDir\.git") {
    Write-Host "[✓] 检测到 git 仓库" -ForegroundColor Green
    $remote = git -C $InstallDir remote get-url origin 2>$null
    if ($remote -match 'monety') {
        Write-Host "[✓] 确认 Monety 仓库" -ForegroundColor Green
    } else {
        Write-Host "[!] 当前目录非 Monety 仓库，克隆到子目录..." -ForegroundColor Yellow
        $InstallDir = Join-Path $InstallDir "Monety"
        git clone $RepoUrl $InstallDir
    }
} else {
    Write-Host "[✓] 克隆仓库到当前目录..." -ForegroundColor Green
    if ($InstallDir -match '^[A-Z]:\\$' -or (Test-Path $InstallDir)) {
        $InstallDir = Join-Path $InstallDir "Monety"
        Write-Host "  将安装到: $InstallDir" -ForegroundColor Yellow
    } else {
        New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null
    }
    git clone $RepoUrl $InstallDir
}

Set-Location $InstallDir
$InstallDir = (Get-Location).Path

# ── 2. Python 依赖 ──
Write-Host "[✓] 检查 Python 依赖..." -ForegroundColor Green
try {
    python -c "import openpyxl" 2>$null
    Write-Host "[✓] openpyxl 已安装" -ForegroundColor Green
} catch {
    Write-Host "[✓] 安装 openpyxl..." -ForegroundColor Green
    pip install openpyxl
}

# ── 3. 默认项目目录与 PowerShell 包装 ──
Write-Host "[✓] 配置 monety 默认项目目录..." -ForegroundColor Green
Register-MonetyShellIntegration -ProjectDir $InstallDir

# ── 4. 验证 ──
Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "[✓] 部署完成！" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  项目目录 : $InstallDir"
Write-Host "  默认目录 : 新开的 PowerShell 会自动定位到上述项目目录"
Write-Host "  网页端   : monety start   (http://127.0.0.1:8888)"
Write-Host "  重新构建 : monety build"
Write-Host "  推送到线 : monety push"
Write-Host ""
Write-Host "  下一步 — 启动网页端:" -ForegroundColor Yellow
Write-Host '    monety start'
Write-Host ""
Write-Host "  或查看状态: monety status" -ForegroundColor Yellow
