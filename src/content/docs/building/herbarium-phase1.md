---
title: 岁月标本馆 · 第一期技术设计与实施任务书
description: Vesper 年度档案的交互、数据口径、实施步骤与验收标准。
slug: building/herbarium-phase1
sidebar:
  order: 16
---

# 岁月标本馆 · The Herbarium

> 把一年的风，夹进时间的书页。

- **项目**：Vesper（https://yenchiu.com/）
- **仓库**：[yen-chiu/yen-chiu.github.io](https://github.com/yen-chiu/yen-chiu.github.io)
- **阶段**：Phase 1 / MVP
- **立项日期**：2026-11-21
- **状态**：开发中；本文为设计基线，不代表已上线
- **原则**：真实数据优先、静态构建、来源可追溯；未经批准不合并或部署

## 一、目标与范围

「一树春秋」模拟树木随时间成长，「岁月标本馆」保存每一生长年度的真实记录，「那年今日」解释 3 月 12 日的历史与建站意义。

一期必须实现：

1. 独立 `/herbarium` 索引与 `/herbarium/[year]` 年份页面，支持年份切换、直接分享、浏览器前进后退。
2. 归档真实公开博客文章和 Folio 文档，区分日期来源、草稿和重复 URL。
3. 按建站周年统计主分支可达 Git 提交，注明统计口径、生成时间与仓库 SHA。
4. 提供年度重要事件与私人手记的可维护数据结构。
5. 「一树春秋」日期与标本馆年度双向跳转，模拟树形与历史证据明确区分。
6. 缺失值、部分记录、未经核验的数据分别标注，展示来源与局限。

一期不包含数据库、访客留言、AI 年度总结、历史 Stars/Forks 推测、3D 场景或复杂动画。

## 二、周年区间与状态

建站日为 **2023-03-12**；按 **Asia/Shanghai** 计算，采用左闭右开区间 `[start,endExclusive)`：

| 标本 | 周期 | 初始状态 |
| --- | --- | --- |
| 001 / 2023 | 2023-03-12—2024-03-12（不含终点） | pending |
| 002 / 2024 | 2024-03-12—2025-03-12（不含终点） | pending |
| 003 / 2025 | 2025-03-12—2026-03-12（不含终点） | pending |
| 004 / 2026 | 2026-03-12—2027-03-12（不含终点） | open |

`open` 生长中、`pending` 待核验、`sealed` 已封存、`revised` 有记录的修订。时间到期不等于自动封存。

## 三、页面与交互

首页：标题「岁月标本馆 / The Herbarium」、副标题、按年度排列的标本卡（编号、周期、状态、可核验摘要）、最近已封存年度入口；没有已封存档案时明确说明。

年度页顺序：标本封面 → 年度指标 → 文章/Folio 列表 → Git 提交摘要 → 重要事件时间线 → 年度手记 → 来源与完整性 → 返回年轮树。年份切换使用真实链接，保持网站现有主题、SEO、键盘可访问性、320px 移动端布局与 `prefers-reduced-motion`。

## 四、作品数据

博客：使用现有 Astro `blog` collection，排除 `draft`，取 `publishDate`；使用现有 `getPostPath` 生成稳定 URL。Folio 是独立仓库 [yen-chiu/folio](https://github.com/yen-chiu/folio)，**不得把主站的 docs collection 当作 Folio 全量内容**。需建立显式的公开作品清单或经审核的导出快照；只纳入具备可信首次公开日期的条目。未知日期保留 `null` 并说明，不按文件修改时间猜测。

建议记录 `id,type,title,url,publishedAt,updatedAt,tags,dateSource`。按首次公开日期归档；修订不能当作新作品重复计数。

## 五、Git 提交统计

优先在构建前或独立数据生成脚本中从完整 Git 历史提取 `main` 可达提交；使用 committer timestamp，转换为 Asia/Shanghai 后按周年区间过滤。合并提交计入；不等同于 GitHub Contributions。输出统计口径、生成时间、`HEAD SHA` 和年度数量。浅克隆时不得悄悄生成不完整数字；历史重写可能影响重算结果。封存后若变动应保留修订说明。

## 六、事件与年度手记

事件字段：`id,date,type,title,description,sourceUrls,verification`；类型可包括 `launch/release/redesign/publication/migration/personal/other`，核验状态为 `verified/manual/unverified`。未核验事件不得当作确定史实。

手记字段：`title,writtenAt,contentPath,visibility,status`。仅构建公开且已发布的手记，私人草稿必须从构建产物中排除。不得编造个人经历或历史信件。

## 七、年度数据模型与来源

建议按 `src/data/herbarium/YYYY.json` 维护，包含：

```json
{
  "schemaVersion": 1,
  "year": 2025,
  "specimenId": "003",
  "period": {"start": "2025-03-12", "endExclusive": "2026-03-12", "timezone": "Asia/Shanghai"},
  "status": "pending",
  "title": null,
  "metrics": {"articles": null, "folio": null, "commits": null},
  "works": [],
  "milestones": [],
  "letter": null,
  "provenance": {"generatedAt": null, "repositorySha": null, "sources": [], "limitations": []}
}
```

自动生成时间区间、公开文章与可验证 Folio 作品、Git 统计；人工维护年度标题、事件、手记和修订记录。**`null` 表示未知，`0` 表示确认零。** 展示 `available/partial/missing/unverified` 等完整性信息，来源区至少包含数据来源、仓库 SHA、生成时间、统计口径和已知限制。

## 八、与年轮树整合

在树卡加入「查看这一年的标本」，按当前选定日期映射至年度 URL；标本页提供「回到那年的树下」，使用经过验证的 `/about?treeDate=YYYY-MM-DD#vesper-tree` 或与组件一致的参数。必须核验现有 GrowingTree 的初始化与 Astro 客户端路由行为，不能凭空假设参数已实现。树形属于算法模拟，档案属于有证据的历史记录。

## 九、实施阶段

- **A 审计**：确认主站路由、blog/docs collection、独立 Folio 内容源、PR #11 状态、构建工作流和现有 UI。
- **B 数据层**：周年区间工具、Schema、作品适配、完整 Git 历史统计、来源/缺失状态、边界测试。
- **C 页面层**：标本馆首页与年度详情、年份切换、作品、事件、手记、来源说明。
- **D 整合**：树与标本双向导航、URL 参数校验、客户端路由兼容。
- **E 验证**：Astro 构建、统计复核、链接/SEO、移动端、键盘、减少动画、缺失状态和回归测试。

## 十、验收与交付

- [ ] `/herbarium` 与各年度 URL 正常访问和分享。
- [ ] 年份切换与浏览器历史正常。
- [ ] 博客/Folio 归档仅使用真实公开作品、可追溯日期，不重复。
- [ ] Git 统计可独立复核；无完整历史时不伪造结果。
- [ ] 事件有核验状态，私人草稿不公开。
- [ ] 年轮树双向跳转且历史模拟明确标注。
- [ ] 未知值不显示为零，来源与局限可查看。
- [ ] 现有导航、搜索、外观、知识图谱不回归。
- [ ] Astro 构建/类型检查/移动端/SEO 测试通过。

开发使用 `feat/vesper-herbarium` 独立分支，中英双语 commit 与 PR 描述；先检查 PR #11 是否已合并。若未合并，先独立开发数据与页面，再处理年轮树依赖。提交 PR、测试报告、变更清单、统计来源及未解决问题；**未经用户批准不得合并、直接提交 main 或部署**。
