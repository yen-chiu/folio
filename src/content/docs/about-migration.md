---
title: 关于这次迁移
sidebar:
  hidden: true
---

Folio 是文档库的新入口，采用独立的名称与书页标识。

## 内容范围

本次从 WendellManual 迁入 95 个页面，包含文档正文、旧首页及主题附录，并保留 33 个原有静态资源。
常规文档继续使用 Markdown；旧主题的复杂演示保留原渲染内容，页面顶部明确标注历史用途。

## 分类与查找

内容分为博客指南、建站笔记、资料导航、其他笔记和旧主题参考。全文搜索、页内目录和深浅主题使用文档框架的原生功能。

## 来源与备份

原始文档的来源、提交版本与校验值记在仓库的 migration/manifest.json，原始 Markdown 留存在 migration/source/。
迁移过程中未替换原站入口；[原文档站](https://yenchiu.com/WendellManual/)继续可用。

[查看 Folio 仓库](https://github.com/yen-chiu/folio)
