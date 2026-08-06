---
title: "流量分组规则(新)"
source: "https://help.toponad.net/cn/docs/liu-liang-fen-zu-gui-ze-xin"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2026-04-21"
category_path: ["Open API接入指南", "附录", "流量分组规则(新)"]
content_sha256: "59079f1579ff5fcc5209505d93b80c3e6bd252617b3d2543ab72b092e1ed2210"
knowledge_role: "reference_only"
has_article_body: true
---

# 流量分组规则(新)

## 规则类型 (RuleType) 枚举值

| 类型值 | 规则名称 | 支持的方法 | Content 格式说明 |
| --- | --- | --- | --- |
| **0** | 地区（集合） | 包含(0)、不包含(1) | JSON 字符串数组，如 `["CN","US"]`，具体参考国家短码 |
| **2** | 天（星期）（集合） | 包含(0) | JSON 字符串数组，值范围 `"0"`-`"6"`（0=周日），如 `["1","2","3","4","5"]` |
| **3** | 网络类型（集合） | 包含(0) | JSON 字符串数组，**必须小写**，可选值：`2g`, `3g`, `4g`, `5g`, `wifi` |
| **4** | 小时（区间） | 区间内(4) | JSON 二维数组 `[["0000","2359"]]`，每段为 HHmm 格式，起点≤终点 |
| **5** | 自定义规则 | 自定义(6) | 自定义格式字符串 |
| **8** | 应用版本号（集合） | 包含(0)、不包含(1)、大于(7)、小于(8) | JSON 字符串数组，如 `["1.0.0","2.0.0"]` |
| **9** | SDK版本号（集合） | 包含(0)、不包含(1)、大于(7)、小于(8) | JSON 字符串数组，版本号格式：`"[\"12.36.21\"]"` |
| **10** | 设备类型（集合） | 包含(0)、不包含(1) | JSON 字符串数组，**必须小写**，可选值：`iphone`, `ipad`, `pc` |
| **11** | 设备品牌（集合） | 包含(0)、不包含(1) | JSON 字符串数组，**大小写敏感，传递小写**，可选值见下方 |
| **12** | 系统版本（集合） | 包含(0)、不包含(1)、大于(7)、小于(8) | JSON 字符串数组，如 `["14.0","15.0"]` |
| **16** | 时区 | 等于(9) | 整数，范围 -12 到 12 |
| **17** | 设备ID（集合） | 包含(0) | JSON 字符串数组 `"[\"65665\"]"` |
| **20** | 安装时间-小时 | 大于(7)、小于(8) | 正整数，表示距安装时刻的小时数 |
| **23** | 渠道（集合） | 包含(0)、不包含(1)、模糊匹配(11) | JSON 字符串数组 `"[\"google\"]"` |
| **24** | 子渠道（集合） | 包含(0)、不包含(1)、模糊匹配(11) | JSON 字符串数组 `"[\"google\"]"` |
| **25** | IDFA状态（值） | 等于(9) | 字符串 `"1"`(有IDFA) 或 `"2"`(无IDFA) |
| **29** | 日期时间（区间） | 区间内(4) | JSON 二维数组 `[["2024-01-01","2024-12-31"]]`，支持多时间段 |
| **30** | 应用版本号 | 包含(0)、不包含(1)、大于等于(2)、小于等于(3) | 单值或 JSON 数组，`"[\"12.36.21\"]"` |
| **31** | 安装来源 | 包含(0)、不包含(1) | JSON 字符串数组 `"[\"google\"]"` |
| **33** | 用户数量 | 包含(0)、不包含(1)、大于等于(2)、小于等于(3)、区间内(4) | 整数或 JSON 数组/区间 `"[\"445555\"]"` |
| **35** | 快应用版本 | 大于(7)、小于(8)、等于(9) | 整数 |
| **36** | SDK预策略 | 等于(9) | 字符串 `"0"` 或 `"1"`，该策略和其他策略互斥 |
| **37** | 冷启动请求 | 等于(9) | 字符串 `"0"` 或 `"1"`，0=否，1=是 |
| **38** | 用户值（区间） | 区间内(4) | JSON 二维数组 `[["0","1000"]]`，数值范围 0-80000 |
| **39** | 快应用宿主版本 | 大于(7)、等于(9)、小于(8) | 字符串，不能为空 |
| **43** | 人群包 | 包含(0)、不包含(1) | JSON 单元素数组如 `["90"]`，仅支持单选，id为对应人群包规则id |
| **46** | 设备型号 | 包含(0)、不包含(1) | JSON 整数数组，元素为设备型号id，具体见枚举 |
| **48** | 设备内存 | 包含(0)、不包含(1) | JSON 字符串数组，可选值：`"1"`-`"7"` |
| **52** | CPU架构 | 包含(0)、不包含(1) | JSON 字符串数组，可选值见下方 |
| **53** | 新版自定义规则 | 自定义V2(12) | JSON 数组，每项包含 key/value/type/rule，见下方详细说明 |
| **54** | 风控设备 | 包含(0) | JSON 字符串数组，可选key：`isroot`, `s_c`, `a_cl`, `s_d`, `isagent`, `u_a`, `d_s`，示例 `"[\"isroot\"]"` |

---

## 规则方法 (RuleMethod) 枚举值

| 方法值 | 名称 | 说明 |
| --- | --- | --- |
| 0 | 包含 | 设备属性在集合中 |
| 1 | 不包含 | 设备属性不在集合中 |
| 2 | 大于等于 | 值 ≥ 指定值 |
| 3 | 小于等于 | 值 ≤ 指定值 |
| 4 | 区间内 | 值在指定区间内 `[[low,high],...]` |
| 5 | 区间外 | 值在指定区间外（暂不支持） |
| 6 | 自定义 | 自定义规则格式 |
| 7 | 大于 | 值 > 指定值 |
| 8 | 小于 | 值 < 指定值 |
| 9 | 等于 | 值 == 指定值 |
| 10 | 不等于 | 值 != 指定值 |
| 11 | 模糊匹配 | 支持通配符匹配（渠道/子渠道） |
| 12 | 自定义V2 | 新版自定义规则（key-value 类型） |

---

## 字段类型 (Type) 枚举值（用于 RuleType=53）

| 类型值 | 名称 | 说明 |
| --- | --- | --- |
| 1 | 字符串类型 | 支持包含/不包含规则 |
| 2 | int 类型 | 支持 大于等于/小于等于/大于/小于/等于/不等于/区间内 规则 |
| 3 | float 类型 | 同 int 类型 |

---

## 新版自定义规则 (RuleType=53) 详细说明

### Content 格式

json
复制代码

```
[
  {
    "key": "字段名",
    "value": "字段值",
    "type": 1,
    "rule": 0
  }
]
```

### 字段说明

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| key | string | 字段名称，**不能为空** |
| value | string | 字段值，**不能为空**；多值用 `,` 分隔 |
| type | int | 字段类型：1=字符串，2=int，3=float |
| rule | int | 匹配规则，按 type 区分 |

### 按 Type 的 Rule 取值

| Type | 支持的 Rule | 说明 |
| --- | --- | --- |
| 1 (字符串) | 0=包含, 1=不包含 | value 多值用 `,` 分隔 |
| 2 (int) | 2=大于等于, 3=小于等于, 7=大于, 8=小于, 9=等于, 10=不等于, 4=区间内 | 单值或 JSON 数组 `["10","20"]` |
| 3 (float) | 同 int 类型 | 同上 |

### 示例

json
复制代码

```
// 字符串包含
[{"key":"os","value":"android,ios","type":1,"rule":0}]

// int 大于等于
[{"key":"level","value":"10","type":2,"rule":2}]

// float 区间内
[{"key":"score","value":"[\"60.5\",\"90.0\"]","type":3,"rule":4}]
```

---

## 特殊规则说明

### 1. 时区关联规则

当使用以下规则时，系统会自动关联时区规则（默认东八区）：

- 类型 2 (天)
- 类型 4 (小时)
- 类型 26 (安装时间自然天)
- 类型 29 (日期时间)

### 2. 安装时间规则唯一性

以下安装时间相关规则**不检验类型+方法唯一性**，可以同时存在：

- 类型 20 (安装时间-小时)
- 类型 21 (安装时间-天)
- 类型 22 (安装时间-周)
- 类型 26 (安装时间-自然天)

---

## 可选值汇总

### 网络类型 (RuleType=3)

`2g`, `3g`, `4g`, `5g`, `wifi`（必须小写）

### 性别值 (RuleType=7)

`"0"` (未知), `"1"` (男), `"2"` (女)

### 设备类型 (RuleType=10)

`iphone`, `ipad`, `pc`（必须小写）

### 设备品牌 (RuleType=11)

Apple, Acer, Advan, Amazon, Asus, Blackshark, Coolpad, GIONEE, Google, Hisense, Honor, HTC, Huawei, Infinix, Lanix, LeEco, Lenovo, LGE, Meitu, Meizu, MetroPCS, Motorola, Nokia, Nubia, OnePlus, OPPO, Qcom, Realme, Redmi, Samsung, Sharp, Smartfren, Smartisan, Sony, TCL, Tecno, Verizon, Vivo, Xiaomi, ZTE, 360 (必须小写)

### 广告格式 (RuleType=15)

`0`(native), `1`(rewarded\_video), `2`(banner), `3`(interstitial), `4`(splash), `50`(stream)
"id" "name"

### IDFA状态 (RuleType=25)

`"1"` (有IDFA), `"2"` (无IDFA)

### 设备型号 (RuleType=46)

"1" "1st Gen iPod"
"2" "2nd Gen iPod"
"3" "3rd Gen iPod"
"4" "4th Gen iPod"
"5" "5th Gen iPod"
"6" "6th Gen iPod"
"7" "7th Gen iPod"
"8" "iPad"
"9" "iPad 3G"
"10" "2nd Gen iPad"
"11" "2nd Gen iPad GSM"
"12" "2nd Gen iPad CDMA"
"13" "2nd Gen iPad New Revision"
"14" "3rd Gen iPad"
"15" "3rd Gen iPad CDMA"
"16" "3rd Gen iPad GSM"
"17" "iPad mini"
"18" "iPad mini GSM+LTE"
"19" "iPad mini CDMA+LTE"
"20" "4th Gen iPad"
"21" "4th Gen iPad GSM+LTE"
"22" "4th Gen iPad CDMA+LTE"
"23" "iPad Air (WiFi)"
"24" "iPad Air (GSM+CDMA)"
"25" "1st Gen iPad Air (China)"
"26" "iPad mini Retina (WiFi)"
"27" "iPad mini Retina (GSM+CDMA)"
"28" "iPad mini Retina (China)"
"29" "iPad mini 3 (WiFi)"
"30" "iPad mini 3 (GSM+CDMA)"
"31" "iPad Mini 3 (China)"
"32" "iPad mini 4 (WiFi)"
"33" "4th Gen iPad mini (WiFi+Cellular)"
"34" "iPad Air 2 (WiFi)"
"35" "iPad Air 2 (Cellular)"
"36" "iPad Pro (9.7 inch, WiFi)"
"37" "iPad Pro (9.7 inch, WiFi+LTE)"
"38" "iPad Pro (12.9 inch, WiFi)"
"39" "iPad Pro (12.9 inch, WiFi+LTE)"
"40" "iPad (2017)"
"41" "iPad Pro 2nd Gen (WiFi)"
"42" "iPad Pro 2nd Gen (WiFi+Cellular)"
"43" "iPad Pro 10.5-inch 2nd Gen"
"44" "iPad 6th Gen (WiFi)"
"45" "iPad 6th Gen (WiFi+Cellular)"
"46" "iPad 7th Gen 10.2-inch (WiFi)"
"47" "iPad 7th Gen 10.2-inch (WiFi+Cellular)"
"48" "iPad Pro 11 inch 3rd Gen (WiFi)"
"49" "iPad Pro 11 inch 3rd Gen (1TB, WiFi)"
"50" "iPad Pro 11 inch 3rd Gen (WiFi+Cellular)"
"51" "iPad Pro 11 inch 3rd Gen (1TB, WiFi+Cellular)"
"52" "iPad Pro 12.9 inch 3rd Gen (WiFi)"
"53" "iPad Pro 12.9 inch 3rd Gen (1TB, WiFi)"
"54" "iPad Pro 12.9 inch 3rd Gen (WiFi+Cellular)"
"55" "iPad Pro 12.9 inch 3rd Gen (1TB, WiFi+Cellular)"
"56" "iPad Pro 11 inch 4th Gen (WiFi)"
"57" "iPad Pro 11 inch 4th Gen (WiFi+Cellular)"
"58" "iPad Pro 12.9 inch 4th Gen (WiFi)"
"59" "iPad Pro 12.9 inch 4th Gen (WiFi+Cellular)"
"60" "iPad mini 5th Gen (WiFi)"
"61" "iPad mini 5th Gen"
"62" "iPad Air 3rd Gen (WiFi)"
"63" "iPad Air 3rd Gen"
"64" "iPad 8th Gen (WiFi)"
"65" "iPad 8th Gen (WiFi+Cellular)"
"66" "iPad 9th Gen (WiFi)"
"67" "iPad 9th Gen (WiFi+Cellular)"
"68" "iPad mini 6th Gen (WiFi)"
"69" "iPad mini 6th Gen (WiFi+Cellular)"
"70" "iPad Air 4th Gen (WiFi)"
"71" "iPad Air 4th Gen (WiFi+Cellular)"
"72" "iPad Pro (11-inch) (3rd generation)"
"73" "iPad Pro 12.9 inch 5th Gen"
"74" "iPad Air 5th Gen (WiFi)"
"75" "iPad Air 5th Gen (WiFi+Cellular)"
"76" "iPad 10th Gen"
"77" "iPad Pro 11 inch 4th Gen"
"78" "iPad Pro 12.9 inch 6th Gen"
"79" "iPad Air 6th Gen"
"80" "iPad Air 7th Gen"
"81" "iPad Pro 11 inch 5th Gen"
"82" "iPad Pro 12.9 inch 7th Gen"
"83" "iPhone Simulator"
"84" "iPhone"
"85" "iPhone 3G"
"86" "iPhone 3GS"
"87" "iPhone 4"
"88" "iPhone 4 GSM Rev A"
"89" "iPhone 4 CDMA"
"90" "iPhone 4S"
"91" "iPhone 5 (GSM)"
"92" "iPhone 5 (GSM+CDMA)"
"93" "iPhone 5C (GSM)"
"94" "iPhone 5C (Global)"
"95" "iPhone 5S (GSM)"
"96" "iPhone 5S (Global)"
"97" "iPhone 6 Plus"
"98" "iPhone 6"
"99" "iPhone 6s"
"100" "iPhone 6s Plus"
"101" "iPhone SE (GSM)"
"102" "iPhone 7"
"103" "iPhone 7 Plus"
"104" "iPhone 8"
"105" "iPhone 8 Plus"
"106" "iPhone X Global"
"107" "iPhone X GSM"
"108" "iPhone XS"
"109" "iPhone XS Max"
"110" "iPhone XS Max Global"
"111" "iPhone XR"
"112" "iPhone 11"
"113" "iPhone 11 Pro"
"114" "iPhone 11 Pro Max"
"115" "iPhone SE 2nd Gen"
"116" "iPhone 12 Mini"
"117" "iPhone 12"
"118" "iPhone 12 Pro"
"119" "iPhone 12 Pro Max"
"120" "iPhone 13 Pro"
"121" "iPhone 13 Pro Max"
"122" "iPhone 13 Mini"
"123" "iPhone 13"
"124" "iPhone SE 3rd Gen"
"125" "iPhone 14"
"126" "iPhone 14 Plus"
"127" "iPhone 14 Pro"
"128" "iPhone 14 Pro Max"
"129" "iPhone 15"
"130" "iPhone 15 Plus"
"131" "iPhone 15 Pro"
"132" "iPhone 15 Pro Max"

### 设备内存 (RuleType=48)

'1' => '[0-1) GB',
'2' => '[1-2) GB',
'3' => '[2-3) GB',
'4' => '[3-4) GB',
'5' => '[4-6) GB',
'6' => '[6-8) GB',
'7' => '>=8 GB',

### CPU架构 (RuleType=52)

`armeabi`, `armeabi-v7a`, `arm64-v8a`, `x86`, `x86_64`, `mips`, `mips64`

### 风控设备字段 (RuleType=54)

`isroot`, `s_c`, `a_cl`, `s_d`, `isagent`, `u_a`, `d_s`
