# Folio

把经验写成可查阅的知识。

[在线预览](https://yenchiu.com/folio/) · [原文档站](https://yenchiu.com/WendellManual/)

Folio 是从 WendellManual 迁移的独立文档站。以 Astro + Starlight 静态构建，按博客指南、建站笔记、资料导航、其他笔记与旧主题参考组织内容。

## 迁移范围

- 基线：原仓库提交 e925feaa124b4e625d45da157f0755c28e8bcda1。
- 95 个页面和 33 个静态资源，原始快照、SHA-256 与地址映射保存在 migration/。
- 48 个常规文档继续使用 Markdown；47 个旧主题复杂页面保留 HTML 存档并标注历史用途。
- 新站增加独立首页、入门页、迁移说明与分类执行记录。
- 原站入口保持运行，Folio 作为并行预览；本轮没有切换旧站地址。

## 本地开发

使用 Node.js 24 和 Python 3.11+。Python 只用于构建后的标准库链接检查；不需要安装 Ruby 或 Jekyll。

```sh
npm ci
npm run dev
# http://localhost:4321/folio/
```

```sh
node scripts/legacy-urls.test.mjs
node scripts/legacy-render.test.mjs
npm run build
# 构建到 dist/，随后检查迁移完整性、资源、链接、锚点和搜索文件
npm run preview
```

首次迁移的正文与代码完整性复核：python scripts/audit-content-fidelity.py。该检查用于初次迁移验收，不阻止今后有意修改文档内容。

## 维护

正文位于 src/content/docs/；新文档放入对应目录即可纳入侧栏。侧栏读取标题与 sidebar.order，子目录可以使用同名 Markdown 文件作为概览。

历史 HTML 的兼容处理集中在 src/plugins/legacy-content.mjs。仅覆盖 Footer 来补充历史代码复制和按需图表加载，保留 Starlight 原生搜索、主题、导航、编辑链接与分页。

原始快照在 migration/source/，构建不执行旧模板，也不从旧站在线抓取内容。scripts/export-jekyll.rb 仅记录一次性迁移时的导出方法，不参与日常构建。

## 发布与记录

GitHub Actions 使用锁文件安装依赖、运行回归和构建后检查，再部署到 /folio/。PR 只验证，不部署。

- [迁移记录](https://yenchiu.com/folio/building/folio-migration/)
- [待办与依赖告警](https://yenchiu.com/folio/building/folio-migration/issues/)
- migration/validation/ 包含构建、正文核对和依赖审计结果。

## License

代码及原模板许可证见 LICENSE.txt。迁入的文档内容版权归原作者所有；历史 Just the Docs 文档保留其来源和许可。
