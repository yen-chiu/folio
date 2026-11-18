---
title: 子页面
slug: legacy-guides/navigation/children
legacySource: docs/Usage Guidelines/navigation/children.md
legacyUrl: /docs/Usage Guidelines/navigation/children/
sidebar:
  order: 4
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 id="child-pages">Child Pages</h1>

<p>默认情况下，所有父页面底部都会自动出现所谓的“目录”，显示所有子页面的链接。</p>

<p>要禁用此自动列表，请在父页面的封面中设置“has_toc: false”。</p>

<h2 class="text-delta" id="example-disabling-table-of-contents">Example: disabling table of contents</h2>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nn">---</span>
<span class="na">title</span><span class="pi">:</span> <span class="s">UI Components</span>
<span class="na">nav_order</span><span class="pi">:</span> <span class="m">3</span>
<span class="na">has_toc</span><span class="pi">:</span> <span class="kc">false</span>
<span class="nn">---</span>
</code></pre></div></div>


</div>
