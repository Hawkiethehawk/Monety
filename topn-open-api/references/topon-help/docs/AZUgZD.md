---
title: "[新]三方广告平台详细参数"
source: "https://help.toponad.net/cn/docs/AZUgZD"
captured_at: "2026-07-21T08:07:23Z"
site_modified: "2026-07-01"
category_path: ["Open API接入指南", "附录", "[新]三方广告平台详细参数"]
content_sha256: "1fcba78407ec48ad8111ef63af8ea6ef051369ed29e6693ae373d41b80ac1286"
knowledge_role: "reference_only"
has_article_body: true
---

# [新]三方广告平台详细参数

> 注意：
>
> 1. 所有的Key和Value数据类型均为String
> 2. 对于支持的竞价类型：如无特殊说明，则表示支持类型所有广告位样式（激励，插屏等）都是一样
> 3. 对于auth\_content：（所有的Key对应的Value的值都是String类型）Key名称后面带(必填)表示广告平台账号管理Api1创建/修改广告平台无论是否开通报表，都需要传该属性
> 4. 对于app\_auth\_content：所有的Key对应的Value的值都是String类型
> 5. 对于adsource\_token：（所有的key对应的value的值都是String类型）Key名称后面带(唯一)的参数表示第三方平台的广告源唯一标识，多个key(唯一)标识组合唯一，同一个三方平台的广告源唯一标识不允许创建重复的TopOn广告源

| 广告平台ID | 广告平台名称 | 支持的竞价类型 | auth\_content | app\_auth\_content | 广告样式 | adsource\_token   注意：无特殊说明所有属性都是必传 | adsource\_token  每个Key对应的Value枚举说明 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | meta | 服务端竞价 | - | app\_id  app\_token  property\_id | native | unit\_id(唯一)  unit\_type  height | unit\_type（广告位类型）枚举值：0（原生广告（自渲染））；1（原生横幅广告（模板渲染））；2（原生广告（模板渲染））；3（原生横幅广告（自渲染））；  height（高度，unit\_type=1时必传）枚举值：50；100；120； |
|  |  |  |
| rewarded\_video | unit\_id(唯一)  unit\_type | unit\_type（广告位类型）枚举值：1（激励视频）；2（激励插屏）； |
| banner | unit\_id(唯一)  size | size（广告源尺寸）枚举值：320x50；320x90；300x250； |
| interstitial | unit\_id(唯一) | - |
| 2 | Admob | 1.自定义关联admob时：客户端竞价  2.官聚admob时：服务端竞价 | account\_id  oauth\_key | app\_id | native | unit\_id(唯一)  media\_ratio  render\_type  template\_type  button\_type | media\_ratio（素材长宽比）枚举值：0（未指定）；1（任意尺寸）；2（横屏尺寸）；3（竖屏尺寸）；4（正方形尺寸）；  render\_type（渲染方式）枚举值：1（开发者自渲染）；2（TopOn模板渲染）；  template\_type（模板类型，render\_type=2时必传）枚举值：1（左图右文）；2（左文右图）；3（上图下文）；4（上文下图）；  button\_type（点击区域，render\_type=2时必传）枚举值：1（全屏点击）；2（按钮可点）； |
| rewarded\_video | unit\_id(唯一)  unit\_type | unit\_type（广告位类型）枚举值：1（激励视频）；2（插页式激励广告）； |
| banner | unit\_id(唯一)  size  admob\_clbn\_sw | size（广告源尺寸）枚举值：320x50；320x100；300x250；468x60；728x90；  admob\_clbn\_sw（折叠式横幅广告）枚举值：1（否）；2（底部）；3（顶部）； |
| interstitial | unit\_id(唯一) | - |
| splash | unit\_id(唯一)  orientation | orientation（屏幕方向）枚举值：1（竖屏）；2（横屏）； |
| 3 | Inmobi | 客户端竞价  服务端竞价 | username  password  apikey  app\_id(必填) | - | native | unit\_id(唯一)  render\_type  template\_type  button\_type | render\_type（渲染方式）枚举值：1（开发者自渲染）；2（TopOn模板渲染）；  template\_type（模板类型，render\_type=2时必传）枚举值：1（左图右文）；2（左文右图）；3（上图下文）；4（上文下图）；  button\_type（点击区域，render\_type=2时必传）枚举值：1（全屏点击）；2（按钮可点）； |
| rewarded\_video | unit\_id(唯一) | - |
| banner | unit\_id(唯一)  size | size（广告源尺寸）枚举值：320x50；300x250； |
| interstitial | unit\_id(唯一) | - |
| 5 | Applovin | 无 | sdkkey(必填)  apikey | - | rewarded\_video | zone\_id(唯一) | - |
| banner | zone\_id(唯一)  size | size（广告源尺寸）枚举值：320x50；300x250； |
| interstitial | zone\_id(唯一) | - |
| 6 | Mintegral | 服务端竞价 | skey  secret  sdkkey(必填) | appid | native | placement\_id  unitid(唯一)  unit\_type  video\_muted  video\_autoplay  close\_button | unit\_type（广告位类型）枚举值：0（自定义渲染）；1（自动渲染）；  video\_muted（视频静音）枚举值：0（静音）；1（不静音）；  video\_autoplay（自动播放视频）枚举值：1（仅WiFi）；2（手动点击）；3（总是）；  close\_button（关闭按钮）枚举值：0（显示）；1（隐藏）； |
| rewarded\_video | placement\_id  unitid(唯一)  video\_muted | video\_muted（视频静音）枚举值：0（静音）；1（不静音）； |
| banner | placement\_id  unitid(唯一)  size | size（广告源尺寸）枚举值：320x50；300x250；320x90；smar； |
| interstitial | placement\_id  unitid(唯一)  video\_muted  is\_video | is\_video（广告位类型）枚举值：0（插屏图片，MTG后台已下线）；1（新插屏广告）  video\_muted（视频静音）枚举值：0（静音）；1（不静音） |
| splash | placement\_id  unitid(唯一)  orientation  allows\_skip  countdown | orientation（屏幕方向）枚举值：1（竖屏）；2（横屏）；  allows\_skip（可跳过）枚举值：0（不可跳过）；1（可跳过）  countdown（倒计时时间）枚举值：2~10（单位秒） |
| 8 | Tencent | 客户端竞价  服务端竞价 | account\_id  secret\_key | app\_id | native | unit\_id(唯一)  unit\_type  video\_muted  video\_autoplay  video\_duration | unit\_type（广告位类型）枚举值：1（原生广告/详情页插入广告）；2（信息流广告/详情页插入广告）；3（视频贴片广告，优量汇渲染）；4（视频贴片广告，开发者自渲染）  video\_muted（视频静音）枚举值：0（不静音）；1（静音）；  video\_autoplay（自动播放视频）枚举值：0（仅WiFi）；1（总是）；2（手动点击）；  video\_duration:（视频最大时长）枚举值：5~61（单位秒）；0（代表不限）； |
| rewarded\_video | unit\_id(唯一)  unit\_type  video\_muted  video\_autoplay  video\_duration | unit\_type（广告位类型）枚举值：1（激励视频）；2（奖励式插屏广告）；  video\_muted（视频静音）枚举值：0（不静音）；1（静音）；  video\_autoplay（自动播放视频）枚举值：0（仅WiFi）；1（总是）；  video\_duration:（视频最大时长）枚举值：5~61（单位秒）；0（代表不限）； |
| banner | unit\_id(唯一)  size | size（广告源尺寸）枚举值：320x50； |
| interstitial | unit\_id(唯一)  is\_fullscreen  video\_muted  video\_autoplay  video\_duration | is\_fullscreen（是否全屏）枚举值：0（弹窗插屏）；1（全屏插屏）；  video\_muted（视频静音）枚举值：0（不静音）；1（静音）；  video\_autoplay（自动播放视频）枚举值：0（仅WiFi）；1（总是）；2（手动点击）；  video\_duration:（视频最大时长）枚举值：5~61（单位秒）；0（代表不限）； |
| splash | unit\_id(唯一)  ~~zoomoutad\_sw~~ | ~~zoomoutad\_sw（开屏V+）枚举值：1（不使用开屏V+）；2（使用开屏V+）；~~ |
| 9 | Chartboost | 无 | user\_id  user\_signature | app\_id  app\_signature | rewarded\_video | location(唯一) | - |
| banner | location(唯一)  size | size（广告源尺寸）枚举值：320x50；300x250；728x90 |
| interstitial | location(唯一) | - |
| 11 | Ironsource | 服务端竞价 | ~~username~~  secret\_key  refresh\_token | app\_key | rewarded\_video | instance\_id(唯一) | - |
| banner | instance\_id(唯一)  size | size（广告源尺寸）枚举值：320x50；320x90；300x250；smart； |
| interstitial | instance\_id(唯一) | - |
| 12 | UnityAd | 无 | apikey  organization\_core\_id | game\_id | rewarded\_video | placement\_id(和game\_id组合唯一) | - |
| banner | placement\_id(和game\_id组合唯一)  size | size（广告源尺寸）枚举值：320x50；468x60；728x90； |
| interstitial | placement\_id(和game\_id组合唯一) | - |
| 13 | Vungle | 服务端竞价 | apikey  account\_id(必填) | app\_id | native | placement\_id(唯一)  render\_type  template\_type  button\_type | render\_type（渲染方式）枚举值：1（开发者自渲染）；2（TopOn模板渲染）；  template\_type（模板类型，render\_type=2时必传）枚举值：1（左图右文）；2（左文右图）；3（上图下文）；4（上文下图）；  button\_type（点击区域，render\_type=2时必传）枚举值：1（全屏点击）；2（按钮可点）； |
| rewarded\_video | placement\_id(唯一) | - |
| banner | placement\_id(唯一)  size\_type  unit\_type | unit\_type（广告位类型）枚举值：0（横幅广告）；1（中矩形横幅广告）；2（Inline）；  size\_type（广告源尺寸）枚举值：0（300x250）；2（320x50）；3（300x50）；4（728x90）；5（自定义尺寸）    注意：  unit\_type=0时：size\_type只能传2；3；4；  unit\_type=1时：size\_type只能传0 |
| interstitial | placement\_id(唯一) | - |
| splash | placement\_id(唯一) | - |
| 14 | AdColony | 服务端竞价 | user\_credentials | app\_id | rewarded\_video | zone\_id(唯一) | - |
| banner | zone\_id(唯一)  size | size（广告源尺寸）枚举值：320x50；300x250；728x90；160x600； |
| interstitial | zone\_id(唯一) | - |
| 15 | 穿山甲 | 客户端端竞价 | user\_id  role\_id  secure\_key | app\_id | native | slot\_id(唯一)  is\_video  layout\_type | is\_video（广告位类型）枚举值：0（信息流广告）；1（Draw信息流广告）；2（Banner广告）；3（插屏广告）；4（视频贴片广告）；  layout\_type（原生类型，is\_video=0/1时必传，其它情况传0即可）枚举值：0（个性化模板）；1（自渲染）； |
| rewarded\_video | slot\_id(唯一)  personalized\_template | personalized\_template（模板）枚举值：0（自渲染）；1（模板渲染）； |
| banner | slot\_id(唯一)  layout\_type  size | layout\_type（广告源类型）枚举值：1（横幅广告）；  size（广告源尺寸）枚举值：640x100（320x50）；600x90（300x45）；600x150（300x75）；600x500（300x250）；600x400（300x200）；600x300（300x150）；600x260（300x130）；690x388（345x194） |
| interstitial | slot\_id(唯一) | - |
| splash | slot\_id(唯一)  zoomoutad\_sw | zoomoutad\_sw（开屏V+）枚举值：1（不使用开屏V+）；2（使用开屏V+）； |
| 22 | Baidu | 客户端竞价（横幅样式不支持） | access\_key | app\_id | native | ad\_place\_id(唯一)  unit\_type  video\_autoplay  cta\_button  button\_type  dl\_type | unit\_type（原生类型）枚举值：0（返回元素）；1（智能优选-自渲染）；2（智能优选-优选渲染）；3（竖版视频）；  video\_autoplay（自动播放视频，unit\_type=3时必传）枚举值：1（是/默认）；2（否）；  cta\_button（CTA按钮，unit\_type=1时必传）枚举值：0（默认）；1（显示CTA）；2（不显示CTA）；  button\_type（点击区域，unit\_type=1时必传）枚举值：0（默认）；1（全屏）；2（仅按钮区域）；  dl\_type（应用下载设置，unit\_type=1时必传）枚举值：0（默认）；1（无二次确认弹窗）；2（显示二次确认弹窗）； |
| rewarded\_video | ad\_place\_id(唯一) | - |
| banner（已下线，如需继续使用，请咨询百度） | ad\_place\_id(唯一) | - |
| interstitial | ad\_place\_id(唯一)  unit\_type | unit\_type（广告位类型）枚举值：1（全屏视频）；2（插屏-智选模板）； |
| splash | ad\_place\_id(唯一) | - |
| 28 | 快手 | 客户端竞价  服务端竞价 | access\_key  security\_key  account\_id(必填) | app\_id  app\_name | native | position\_id(唯一)  unit\_type  layout\_type  shake\_type | unit\_type（广告位类型）枚举值：0（信息流广告）；1（Draw视频广告）；  layout\_type（原生类型，unit\_typ=0时必传）枚举值：0（自渲染）；1（模板）；  shake\_type（摇一摇开关，layout\_type=1时必传）枚举值：1（开）；2（关）； |
| rewarded\_video | position\_id(唯一)  orientation  video\_muted | orientation（方向）枚举值：1（竖屏）；2（横屏）；  video\_muted（视频静音）枚举值：0（不静音）；1（静音）； |
| banner | position\_id(唯一)  size | size（广告源尺寸）枚举值：320x50；300x45； |
| interstitial | position\_id(唯一)  is\_video  video\_muted  orientation | is\_video（广告位类型）枚举值：~~0（插屏广告）；1（全屏视频广告）~~ 0(新插屏)；  video\_muted（视频静音）枚举值：0（不静音）；1（静音）；  orientation（方向）枚举值：1（竖屏）；2（横屏）； |
| splash | position\_id(唯一) | - |
| 29 | Sigmob | 客户端竞价 | public\_key  secret\_key | app\_id  app\_key | native | placement\_id(唯一) | - |
| rewarded\_video | placement\_id(唯一) | - |
| interstitial | placement\_id(唯一) | - |
| splash | placement\_id(唯一) | - |
| 34 | Yandex | 服务端竞价 | - | - | native | unit\_id(唯一)  unit\_type | unit\_type（广告位类型）枚举值：0（自渲染）；1（模板渲染）； |
| rewarded\_video | unit\_id(唯一) | - |
| banner | unit\_id(唯一)  size | size（广告源尺寸）枚举值：1（240x400）；2（300x250）；3（300x300）；4（320x100）；5（320x50）；6（400x240）；7（728x90）；8（Full\_Screen）； |
| interstitial | unit\_id(唯一) | - |
| splash | unit\_id(唯一) | - |
| 37 | Fyber | 无 | publisher\_id  consumer\_key  consumer\_secret | app\_id | rewarded\_video | spot\_id(唯一) | - |
| banner | spot\_id(唯一) | - |
| interstitial | spot\_id(唯一)  video\_muted | video\_muted（视频静音）枚举值：0（不静音）；1（静音）； |
| 39 | Huawei Ads | 客户端竞价 | - | client\_id  client\_secret | native | ad\_id(唯一)  orientation  video\_muted  multi\_img | orientation（方向）枚举值：0（任意）；1（竖屏）；2（横屏）；  video\_muted（视频静音）枚举值：0（静音）；1（不静音）；  multi\_img（是否支持多图）枚举值：1（是）；2（否）； |
| rewarded\_video | ad\_id(唯一) | - |
| banner | ad\_id(唯一)  size | size（广告源尺寸）枚举值：320x50；320x100；300x250；360x57；360x144；smart；468x60；728x90； |
| interstitial | ad\_id(唯一) | - |
| splash | ad\_id(唯一) | - |
| 49 | mimo(米盟) | 无 | dev\_id  app\_secret   ```   ``` | app\_id  app\_name | native | unit\_id(唯一)   unit\_type | unit\_type（广告位类型）枚举值：1（模板渲染）；2（自渲染）； |
| rewarded\_video | unit\_id(唯一) | - |
| banner | unit\_id(唯一) | - |
| interstitial | unit\_id(唯一) | - |
| splash | unit\_id(唯一)  sys\_sp | sys\_sp(系统开屏广告) 枚举值：1是2否 |
| 59 | Bigo | 服务端竞价 | developer\_id  token | app\_id | native | slot\_id(唯一)  render\_type  template\_type  button\_type | render\_type（渲染方式）枚举值：1（开发者自渲染）；2（TopOn模板渲染）；  template\_type（模板类型，render\_type=2时必传）枚举值：1（左图右文）；2（左文右图）；3（上图下文）；4（上文下图）；  button\_type（点击区域，render\_type=2时必传）枚举值：1（全屏点击）；2（按钮可点）； |
| rewarded\_video | slot\_id(唯一) | - |
| banner | slot\_id(唯一)  size | size（广告源尺寸）枚举值：320x50；300x250； |
| interstitial | slot\_id(唯一) | - |
| splash | slot\_id(唯一) | - |
| 65 | BidMachine | 服务端竞价 | account  password | source\_id | native | unit\_id(唯一) | - |
| rewarded\_video | unit\_id(唯一) | - |
| banner | unit\_id(唯一)  size | size（广告源尺寸）枚举值：320x50；300x250；728x90; |
| interstitial | unit\_id(唯一) | - |
| splash | unit\_id(唯一) | - |
| 66 | ADX(仅限编辑ADX广告源) |  |  |  | native | layout\_type  模板参数：  close\_button  video\_autoplay  video\_muted  nv\_tmpl\_id | layout\_type（广告模板）枚举值：0自渲染 1模板  模板参数：  video\_muted（视频静音）枚举值：0（静音）；1（不静音）；  video\_autoplay（自动播放视频）枚举值：1（仅WiFi）；2（手动点击）；3（总是）；  close\_button（关闭按钮）枚举值：0（显示）；1（隐藏）；  nv\_tmpl\_id（原生广告模板样式；多选） 枚举值：  1：左图右文 2：左文右图 3：上图下文 4：上文下图 5：文字浮层 |
| banner | close\_button size | close\_button（关闭按钮）枚举值：0（显示）；1（隐藏）；  size(广告源尺寸) 枚举值："320x50", "320x90", "300x250", "728x90" |
| interstitial | unit\_type | unit\_type（素材类型） 枚举值：1（视频和图片）2（图片）  v\_m(视频静音) 枚举值：0（是）；1（否） |
| rewarded\_video | v\_m  s\_c\_t\_sw | v\_m(视频静音) 枚举值：0（是）；1（否）   s\_c\_t\_sw（视频可提前关闭）枚举值：1（是）；2（否）  为确保符合政策规定，自 SDK v6.2.77 起，对于中国大陆的应用，  视频关闭按钮将不再支持自定义调整。  具体交互将遵守当地法律法规进行适配 |
| splash | orientation countdown allows\_skip | orientation（屏幕方向）枚举值：1（竖屏）；2（横屏）；  allows\_skip（可跳过）枚举值：0（不可跳过）；1（可跳过）  countdown（倒计时时间）枚举值：2~10（单位秒） |
| 77 | Kwai | 客户端竞价 | publisher\_ id apikey | app\_id app\_token | rewarded\_video | tagid(唯一) | - |
| interstitial | tagid(唯一) | - |
| 79 | Vivo | 客户端竞价 | account\_name  secret\_key | media\_id | native | pos\_id(唯一)  unit\_type  video\_autoplay | unit\_type(广告位类型)：枚举：0 原生自渲染；  1原生模板化  video\_autoplay (自动播放视频) 枚举：0 仅WiFi网络；1 总是；2点击播放 |
| rewarded\_video | pos\_id(唯一) | - |
| banner | pos\_id(唯一) | - |
| interstitial | pos\_id(唯一)  unit\_type | unit\_type（插屏素材类型）枚举：1半屏 ；2全屏； |
| splash | pos\_id(唯一)  orientation | orientation （屏幕方向）枚举：1竖屏；2横屏； |
| 83 | TaurusX | 服务端竞价 | token | app\_id | native | placement\_id(唯一)  unit\_type | unit\_type（原生类型）枚举值：1（模板渲染）；2（自渲染）； |
| rewarded\_video | placement\_id(唯一)  video\_muted | video\_muted（视频静音）枚举值：0（不静音）；1（静音）； |
| banner | placement\_id(唯一)  size | size（广告源尺寸）枚举值：300x250；320x50； |
| interstitial | placement\_id(唯一)  video\_muted | video\_muted（视频静音）枚举值：0（不静音）；1（静音）； |
| splash | placement\_id(唯一) | - |
| 84 | Smaato | 服务端竞价 | client\_id client\_secret | pub\_id | native | unit\_id(唯一)  unit\_type | unit\_type（原生类型）枚举值：1（模板渲染）；2（自渲染）； |
| rewarded\_video | unit\_id(唯一) | - |
| banner | unit\_id(唯一)  size | size（广告源尺寸）枚举值：300x250；320x50；~~120x600~~；728x90； |
| interstitial | unit\_id(唯一) | - |
| splash | unit\_id(唯一) | - |
| 93 | AdMateX(美数) | 客户端竞价 | agent\_id token | app\_id secure | native | unit\_id(唯一)  unit\_type  video\_muted | unit\_type（广告位类型）枚举值：0（信息流广告）  video\_muted（视频静音）枚举值：0（不静音）；1（静音）； |
| rewarded\_video | unit\_id(唯一)  video\_muted | video\_muted（视频静音）枚举值：0（不静音）；1（静音）； |
| banner | unit\_id(唯一) | - |
| interstitial | unit\_id(唯一)  unit\_type  click\_close | unit\_type（广告位类型）枚举值：0（信息流广告）  click\_close（点击后关闭）枚举值：0（否）；1（是）； |
| splash | unit\_id(唯一)  click\_close | click\_close（点击后关闭）枚举值：0（否）；1（是）； |
| 95 | Beizi(倍孜) | 客户端竞价 | app\_key secret | app\_id | native | unit\_id(唯一)  unit\_type  template\_type | unit\_type（渲染方式）枚举值：0（自渲染）；1（模板渲染）；  template\_type（广告位类型，unit\_type=1时必传）枚举值：1（模板1.0）；2（模板2.0）；4（左两文右一图）；5（上图下文）； |
| rewarded\_video | unit\_id(唯一)  template\_type | template\_type（广告位类型）枚举值：1（模板1.0）；2（模板2.0）； |
| ~~banner~~ | ~~unit\_id(唯一)~~ | ~~-~~ |
| interstitial | unit\_id(唯一)  template\_type | template\_type（广告位类型）枚举值：1（模板1.0）；2（模板2.0）； |
| splash | unit\_id(唯一) | - |
| 96 | Octopus(章鱼广告) | 客户端竞价 | auth\_code user\_name | app\_id | native | unit\_id(唯一)  unit\_type | unit\_type （渲染方式）0：自渲染（默认）1：模板渲染 3：Draw模板 |
| rewarded\_video | unit\_id(唯一) | - |
| banner | unit\_id(唯一) | - |
| interstitial | unit\_id(唯一)  unit\_type | unit\_type （渲染方式）0：插屏 1：全屏视频 |
| splash | unit\_id(唯一) | - |
