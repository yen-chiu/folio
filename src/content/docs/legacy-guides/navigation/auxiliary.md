---
title: 辅助链接
slug: legacy-guides/navigation/auxiliary
legacySource: docs/Usage Guidelines/navigation/auxiliary.md
legacyUrl: /docs/Usage Guidelines/navigation/auxiliary/
sidebar:
  order: 2
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 id="auxiliary-links">Auxiliary Links</h1>

<p>恁可以向网站添加辅助链接列表，该列表显示在所有页面的右上角。恁可以通过在网站的 <code class="language-plaintext highlighter-rouge">_config.yml</code> 文件中添加 <code class="language-plaintext highlighter-rouge">aux_links</code> <a href="/WendellManual/docs/Usage%20Guidelines/configuration/#aux-links">配置选项</a> 来实现此目的。</p>

<h2 class="text-delta" id="example-auxiliary-link">Example Auxiliary Link</h2>

<p>该网站有一个辅助链接: “GitHub”。它使用以下代码呈现:</p>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">aux_links</span><span class="pi">:</span>
  <span class="na">GitHub</span><span class="pi">:</span>
    <span class="pi">-</span> <span class="s">https://github.com</span>
</code></pre></div></div>


</div>
