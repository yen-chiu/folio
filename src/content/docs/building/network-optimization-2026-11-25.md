---
title: Vesper · 大陆访问优化实施与验收报告
description: 2026-11-25 网络优化的代码交付、三网测速、Cloudflare 缓存配置、自动刷新验收与后续验证计划。
slug: building/network-optimization-2026-11-25
sidebar:
  order: 19
---

> 记录已经完成的工作，也记录尚未证明的结果。

- **项目**：YenChiu / Vesper
- **站点**：[yenchiu.com](https://yenchiu.com/)
- **报告日期**：2026-11-25（北京时间）
- **代码基线**：主站 main，`07075167d89cb68a36f3c749489f7420ed2f4bfb`
- **状态**：代码、缓存命中及部署自动清除已验收；完整三网提速对比、定时探针实际运行及香港节点对比待核验。
- **公开范围**：仅记录工程配置、公开响应标头及聚合测速结果；不保存令牌、账户标识符、私人配置或包含凭据的截图。

## 一、背景与目标

主站使用 Astro 静态构建，经 GitHub Pages 部署，由 Cloudflare 提供域名代理及 CDN；摄影衍生图采用公开 R2 CDN，私有原图备份独立。Folio 与 Echora 是同域不同路径的独立项目，Avatar Studio 为独立管理工具。

本轮以不迁移源站、不采购服务器、不牺牲正文可用性为前提，减少不必要的跨境请求，提升公开内容的缓存命中率，建立可重复的测试及发布流程。

Cloudflare 全球 CDN 不等同于中国大陆 CDN。缓存命中减少回源，但不能保证访客连接到邻近机房，也不能消除跨境网络拥堵。大陆线路改善必须以真实测量为准。

## 二、实施结果

| 阶段 | 项目 | 交付与状态 |
| --- | --- | --- |
| P0 | 大陆三网测速 | ITDOG 已采集初步样本；尚无严格配对的完整优化前后基线 |
| P0 | 第三方依赖审计 | 移除全站 jsDelivr、Giscus、DummyJSON 预连接提示；加入构建 HTML 资源审计 |
| P0 | Cloudflare 缓存 | 公开 HTML 已观察到 HIT，静态资源长期缓存规则已存在 |
| P1 | 弱网自适应 | 外观设置加入自动、标准、节省流量；节省流量关闭搜索预热并使用静态头像 |
| P1 | 按需加载 | Astro 预取改为 tap，Giscus 点击加载并提供失败提示，文件管理器首次打开动态导入；保留已有搜索与图谱的动态导入 |
| P1 | 部署后精确刷新 | Cloudflare 最小权限令牌与仓库变量配置；手动部署 #456 全部任务成功 |
| P2 | PWA 离线缓存 | 已访问公开导航页网络优先，Astro 静态资源缓存优先；浏览器回归通过 |
| P2 | 性能监测 | 定时及手动探针工作流已合并；实际监测报告待查阅 |
| P2 | 香港节点 A/B | 仅完成测量方案，未购买节点、未执行对比 |

不擅自复制 Wikimedia Commons 音源，不禁用主动播放的音乐，也不根据国家 IP 强制降低网站质量。未更改主站 DNS、TLS 模式、真实摄影索引或 R2 数据。

## 三、三网测速与证据口径

来源：2026-11-25 站主提供的 ITDOG HTTP 测速截图，测试目标为公开首页及博客列表。表中为平台显示的平均总耗时，单位秒，不是浏览器完整页面渲染时间，也不是 TTFB。

| 样本 | 进度 | 电信 | 联通 | 移动 | 全节点平均 |
| --- | --- | ---: | ---: | ---: | ---: |
| 首页，早期截图 | 约 33%，未完成 | 约 1.83 | 约 3.46 | 未完成 | 约 2.03 |
| 博客列表，早期截图 | 333 节点，100% | 1.561 | 6.436 | 1.310 | 2.746 |
| 首页，配置初始 HTML 缓存后 | 332 节点，100% | 约 1.82 | 约 6.2 | 约 1.32 | 约 2.77 |

最后一次完整首页截图中访问失败计数为 26。这里保留平台原始计数，不假设所有失败均由 Cloudflare 导致，也不将不同页面或未完成样本直接做百分比比较。

初步结论：这些样本中联通表现弱于电信、移动；存在超过 10 秒的慢节点。由于页面、节点数量、时刻及缓存状态不完全相同，不能据此宣称提速比例，亦不能断言缓存使速度变慢。

### 缓存响应标头核验

三网各取一个上海成功请求，截图显示：

| 运营商及检测点 | HTTP | CF-Cache-Status | Age | Cache-Control | CF-Ray 后缀 |
| --- | --- | --- | ---: | --- | --- |
| 移动 · 上海 | HTTP/2 200 | HIT | 215 | max-age=600 | LHR |
| 电信 · 上海10 | HTTP/2 200 | HIT | 215 | max-age=600 | AMS |
| 联通 · 上海5 | HTTP/2 200 | HIT | 215 | max-age=600 | LAX |
| 后续电信 · 上海10 | HTTP/2 200 | HIT | 1 | max-age=600 | AMS |

前三个样本响应时间标头为 2026-11-25 06:51:27 UTC（北京时间 14:51:27）；后续样本为 06:57:12 UTC（14:57:12）。后续截图未显示完整被测 URL，因此不据此确认扩大后的所有路径均命中。

- `cf-cache-status: HIT` 是 Cloudflare 缓存命中的直接证据；`x-cache`、`x-proxy-cache` 等为其他缓存层标头，不应与之混淆。
- `cache-control: max-age=600` 表明响应给出的缓存新鲜度指令为 600 秒；实际边缘缓存行为还受规则及源站响应影响。
- `content-encoding: br` 表示样本使用 Brotli；HTTP/2 已实际使用，`alt-svc: h3` 仅说明 HTTP/3 被通告支持，并不证明本次使用了 HTTP/3。
- LHR（伦敦）、AMS（阿姆斯特丹）、LAX（洛杉矶）表明样本对应海外 Cloudflare 处理节点，不能当作完整路由追踪，也不能代表该运营商所有请求。
- 三个 HIT 样本证明缓存机制可用，不代表全站、全网命中率或线路问题已解决。

## 四、Cloudflare 配置记录

控制台曾有两条有效规则：写作台上传图片绕过边缘缓存，以及 hashed assets long cache。保留写作台绕过规则。静态资源旧规则匹配 `/_astro/`，截图显示边缘与浏览器 TTL 均为一年；收紧主域、GET/HEAD 和错误状态 TTL 是本轮提出的建议，未取得修改后完整保存截图，因此不把这些额外调整当作已独立验证的配置。

新建 `Vesper - HTML Cache`，先匹配首页与博客列表，观察 HIT 后将范围扩大至公开博客、摄影、音乐与站内文档目录。以下为本轮指导使用的完整表达式；控制台截图只显示前部及字符数，最终保存后的完整文本仍需站主对照。

```text
(
  http.host eq "yenchiu.com"
  and http.request.method in {"GET" "HEAD"}
  and http.request.uri.query eq ""
  and not any(http.request.headers.names[*] eq "authorization")
  and not any(http.request.headers.names[*] eq "cookie")
  and (
    http.request.uri.path eq "/"
    or (
      ends_with(http.request.uri.path, "/")
      and (
        starts_with(http.request.uri.path, "/blog/")
        or starts_with(http.request.uri.path, "/gallery/")
        or starts_with(http.request.uri.path, "/music/")
        or starts_with(http.request.uri.path, "/docs/")
      )
    )
  )
)
```

缓存资格选择 Eligible for cache；边缘 TTL 使用缓存控制标头（无标头时用 Cloudflare 默认 TTL）；浏览器 TTL 尊重源站；缓存键保持默认。不要对 HTML 强制使用一年浏览器 TTL。继续排除 `/folio/`、`/echora/`、管理域名、鉴权、带查询参数的请求、动态 JSON 与 SW，不设置跨全域的 Cache Everything。

若出现陈旧页面或异常缓存，先停用新规则并检查相应 URL；不要为一次更新清除整个区域的缓存。错误状态码长期缓存应避免。控制台现行规则、TTL 及权限以实际配置为准。

## 五、发布自动化与安全验收

主站 GitHub Actions 在 build 阶段生成本次 dist 对应的公开 URL 清单，部署成功后才运行独立的 purge-cache。PR 不执行清除；哈希资源、Folio、Echora、管理/API 路径及 R2 对象不进入该清单。只按 URL 分批刷新，不调用全区域清除。

| GitHub 配置名称 | 类型 | 用途 |
| --- | --- | --- |
| CF_CACHE_PURGE_TOKEN | Repository secret | 仅当前 zone 的 Cache Purge 权限 |
| CF_ZONE_ID | Repository variable | 区域标识 |
| CF_CACHE_PURGE_ENABLED | Repository variable | 值为 true 时启用自动刷新 |

本报告不记录任何实际令牌或区域 ID。令牌不需要 DNS、Workers、R2 管理权限；GitHub 托管 runner 出口变化时，不应误设固定 IP 限制。令牌到期或撤销后需轮换。若怀疑泄露立即撤销并重新创建，而非仅修改仓库变量。

### 实际验收：Deploy to GitHub Pages #456

站主手动运行 main，提交 `0707516`，2026-11-25 15:11 左右（北京时间，依据截图相对时间估计）。随后提供的任务详情确认：

| Job | 状态 | 耗时 |
| --- | --- | ---: |
| build | 成功 | 51 秒 |
| deploy | 成功 | 13 秒 |
| purge-cache | 成功 | 12 秒 |
| 整个工作流 | 成功，3 个作业通过 | 1 分 29 秒 |

截图足以确认三个作业均成功，自动刷新功能不再处于跳过状态。当前 GitHub 查询接口未提供此次手动运行的详细日志，故没有核验具体清除 URL 数、批次数或每个边缘节点的传播结果，不编造这些数据。

## 六、代码交付与测试

主站 [PR #48](https://github.com/yen-chiu/yen-chiu.github.io/pull/48) 已于 2026-11-25 合并，合并提交 [0707516](https://github.com/yen-chiu/yen-chiu.github.io/commit/07075167d89cb68a36f3c749489f7420ed2f4bfb)。

初次网络浏览器 CI 在未缓存离线页面断言处失败：预期 503，实际 404。改用测试专用回环代理真实断开传输连接，保留在线 404、离线缓存 200、未缓存离线 503、恢复联网等断言，未把错误结果改成通过条件。修复提交 `aae46ff51c9a4e4978b440e8ea8b65a85f7a931f` 后：

- [Deploy to GitHub Pages / PR 构建 #454](https://github.com/yen-chiu/yen-chiu.github.io/actions/runs/45559178553)：成功。
- [Network browser validation #2](https://github.com/yen-chiu/yen-chiu.github.io/actions/runs/45559178450)：成功。
- PR 合并后的正式部署以及手动部署 #456 均在站主截图中显示成功。

核心维护入口：

| 文件 | 职责 |
| --- | --- |
| astro.config.ts / BaseHead.astro | 预取策略与全局连接提示 |
| src/components/giscus/Giscus.astro | 评论主动加载及失败提示 |
| src/components/appearance/ | 网络模式与动效偏好 |
| src/components/categories/CategoryBrowserOverlay.astro | 文件管理器按需导入 |
| public/sw.js | 有界公开离线缓存 |
| scripts/network-build-audit.mjs | 构建产物中的显式第三方资源及 HTML 大小 |
| scripts/network-probe.mjs | 区域可运行的 HTTPS 探针 |
| scripts/network-optimization.test.mjs / network-browser-check.mjs | 网络策略、真实浏览器回归 |
| scripts/cache-purge-manifest.mjs / cache-purge.mjs | 公开 URL 清单与精确刷新 |
| .github/workflows/deploy.yml / network-probe.yml | 发布与周期性监测 |

离线缓存限制：公开顶层导航页面最多 20 条、单条 512 KiB；Astro 静态资源最多 64 条、单条 2 MiB（解压后）。不预下载全站，不缓存第三方、音频、R2、私有应用、查询 URL、鉴权或 Range 请求。HTML 网络优先，仅连接失败时回退；未缓存页面显示离线提示。实际设备的站内客户端路由离线能力仍需独立验证。

## 七、后续复测与香港节点决策

定时探针计划为每日 UTC 02:17、12:17（北京时间 10:17、20:17），报告保留 14 天。GitHub 托管 runner 仅代表其实际出口，不是大陆三网测量节点；当前未取得实际探针结果，不填写运行次数或测速数字。

本机更新 main 后，在可信的大陆三网测试机执行：

```bash
node scripts/network-probe.mjs --label=湖南电信 --samples=3 --out=network-probe.json
```

对同一 URL、同一运营商及地域节点、相近时刻重复测量，区分冷/热缓存，记录成功率、DNS、TCP、TLS、TTFB、总耗时、响应大小和 CF-Ray。优先白天及 19–23 时各测多轮；保留失败样本，比较中位数及 P95。小样本 P95 仅作参考。浏览器侧另测 LCP、CLS、交互和资源瀑布图。不能用 HTTP 探针代替完整页面体验。

待取得真实香港候选 HTTPS 地址后，再用同版本内容及相近缓存策略执行 A/B：

```bash
node scripts/network-probe.mjs --base=https://实际测试域名 --label=香港候选-湖南电信 --samples=3 --out=hk-probe.json
```

先判断联通峰时失败和长尾延迟是否仍然存在，再评估香港线路成本、稳定性和合规条件。不依据单次 Ping、地理距离或商家线路宣传直接购买。

## 八、结项判断与待办

- [x] 前端网络优化代码合并、构建与浏览器专项通过。
- [x] Cloudflare 公开 HTML 缓存命中有三网样本证据。
- [x] 部署成功后的缓存清除 job 在正式环境运行成功。
- [ ] 核实扩大后的博客、摄影、音乐和文档各路径命中及排除规则。
- [ ] 检查定时探针真实报告，补充大陆三网可配对的重复样本。
- [ ] 确认实际设备 PWA 离线体验与更新后的内容一致性。
- [ ] 如复测确有必要，进行香港候选节点对比。

本轮工程交付与自动化验收完成；**大陆访问提速幅度尚未量化，线路级优化不作已完成结论。**

## 九、资料与回滚

- [主站网络优化维护手册](https://github.com/yen-chiu/yen-chiu.github.io/blob/main/docs/network/README.md)：详细配置、测速、维护与回滚。
- [主站发布工作流](https://github.com/yen-chiu/yen-chiu.github.io/actions/workflows/deploy.yml)
- [定时性能监测](https://github.com/yen-chiu/yen-chiu.github.io/actions/workflows/network-probe.yml)
- [ITDOG HTTP 测速](https://www.itdog.cn/http/)
- [Cloudflare Cache Rules](https://developers.cloudflare.com/cache/how-to/cache-rules/)
- [Cloudflare Purge API](https://developers.cloudflare.com/api/resources/cache/methods/purge/)
- [Cloudflare China Network](https://developers.cloudflare.com/china-network/)

若自动清除异常，将 CF_CACHE_PURGE_ENABLED 改为 false；必要时撤销令牌并单独处理已确认的缓存 URL。前端问题通过新 PR 回滚，不覆盖 Git 历史；离线策略回滚需发布可清理旧缓存的新版 worker。Cloudflare 规则和 GitHub 代码分别维护，不假定代码回滚会自动恢复控制台。

此报告依据本次公开代码、CI 记录和站主提供的界面及测速截图归档；未独立测量大陆线路，未取得香港候选或所有控制台保存后的完整配置。后续测试须以带日期的修订补充，保留原验收口径。
