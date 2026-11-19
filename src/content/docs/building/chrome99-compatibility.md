---
title: 博客 Chrome 99 兼容性补丁报告
description: 补丁清单、验证记录与未来移除指南。
sidebar:
  order: 15
---


- 日期：2026-11-19
- 目标浏览器：公司电脑 Chrome 99.0.4844.51（64 位）
- 项目：yen-chiu/yen-chiu-astro
- 原则：保留现代浏览器体验，旧浏览器使用渐进回退。本文记录的是已实施补丁，不代表全站已在真实 Chrome 99 完成验收。

## 补丁清单与撤销方法

|提交|修改位置|问题与处理|以后如何移除|
|---|---|---|---|
|1de17da|src/pages/index.astro|首屏与滚动间距的 svh 在 Chrome 99 被忽略；在现代声明前增加 vh 回退。用户已确认首屏恢复。|最低支持版本不再需要旧视口回退时，仅删除对应 vh 声明，保留 svh。|
|bfac369|astro.config.ts|增加 vite.build.cssTarget: chrome99，使构建转换不兼容 CSS 语法。|提升浏览器基线时调整 cssTarget，须重新验证构建产物。|
|bfac369|src/assets/styles/global.css|补充平铺的深色代码文字规则、Shiki 深色变量缺省值和清晰行号颜色。|兼容性规则可合并回基础样式；提高对比度的配色并非必须删除。|
|6a9b808|src/components 下的弹窗及搜索样式|文件管理器、知识图谱、搜索、标签云、赞助弹窗、外观面板与移动导航的 dvh 尺寸前增加 vh 回退。|逐处删除 dvh 前相邻的 vh 回退；保留现代声明。|
|11f58d2|src/layouts/ContentLayout.astro|三栏布局由百分比边距加 transform 居中改为计算左边距；侧栏增加横向边界和长词换行。用户确认左栏可以看见。|属于布局修正，可继续保留；若重新设计三栏，整体替换该布局块，不建议机械回退。|
|65c960e|src/assets/styles/global.css|代码行号背景依赖 :has(code) 才获得定位祖先；旧浏览器出现约 2.75rem 宽的游离长条。给 .astro-code 无条件 position:relative。用户确认长条消失。|建议永久保留这条定位约束，即使取消 Chrome 99 支持也无须删除。|
|89ea5e8|src/plugins/shiki-custom-transformers.ts、src/assets/styles/global.css|带标题代码块在构建时标记 has-code-title 类，用类选择器替代 :has(div.title)，避免标题留白与行号背景偏移规则失效。|建议永久保留；如改回 :has，须同时删除生成类与相应类规则。|
|89ea5e8|src/components/giscus/Giscus.astro|通过 MutationObserver 检测评论 iframe，并设置 giscus-ready 类隐藏加载提示，替代 :has。|恢复现代选择器时，同时移除 observer 和类规则；不要单独删除一半。|
|89ea5e8|src/assets/styles/global.css|不支持 color-mix 时，为 .highlight 与 .post-preview 设置可读的主题色回退。|删除对应 @supports not 块；需确认所有目标浏览器支持 color-mix。|
|89ea5e8|src/layouts/BaseLayout.astro|页面最低高度添加 min-h-screen，保留 min-h-[100dvh] 供现代浏览器使用。|基线升级后可删除 min-h-screen；验证生成样式顺序。|

## 相关但并非 Chrome 99 专用的修复

a2bd360 移除了 CustomHeader.astro 的 transition:persist，避免跨版本导航时旧 DOM 与新作用域样式混用，导致小猫、文字与星光竖排。建议保留；如恢复持久化导航，必须先验证跨版本及站内跳转场景。

## 验证记录与限制

- 本轮 89ea5e8：Astro 检查覆盖 216 个文件，0 errors、0 warnings、2 hints。
- Windows 本地完整打包在 esbuild 临时文件清理阶段遇到 Access is denied；不把它算作本地构建通过。
- 本轮 GitHub Actions 44455025934 完成且结论 success，包含云端构建和发布。
- 前述补丁均已通过对应 GitHub Pages 发布流程。首屏和游离长条已有用户现场确认；其他补丁仍需实际设备进一步验收。
- 当前没有在真实 Chrome 99 中执行全站自动化测试，因此不承诺所有第三方脚本和全部交互均兼容。

## 升级后删除建议

不要直接回退所有提交：这些提交中同时包含对比度和布局修正。应按上表逐项移除纯兼容回退，每次构建并检查：首屏、文章深浅主题、带标题代码块、侧栏、文件管理器、图谱、搜索、评论加载、手机弹窗和站内导航。

## 后续关注

仍存在少量非关键 :has() 渐进增强（例如代码末尾空行隐藏），不影响核心阅读；部分 color-mix 装饰效果在旧浏览器会降级。原生 inert 的旧版行为、第三方评论与图表脚本尚未完成真实 Chrome 99 验证。后续如需严格支持，应使用独立测试设备验证，避免仅依赖构建目标推断运行时兼容性。
