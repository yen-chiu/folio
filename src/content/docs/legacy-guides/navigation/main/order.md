---
title: 页面排序
slug: legacy-guides/navigation/main/order
legacySource: docs/Usage Guidelines/navigation/main/order.md
legacyUrl: /docs/Usage Guidelines/navigation/main/order/
sidebar:
  order: 1
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 id="ordering-pages">Ordering Pages</h1>

<p>To specify a page order, you can use the <code class="language-plaintext highlighter-rouge">nav_order</code> parameter in the front matter of the pages.</p>

<h2 class="text-delta" id="example-using-nav_order">Example: using <code class="language-plaintext highlighter-rouge">nav_order</code></h2>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nn">---</span>
<span class="na">title</span><span class="pi">:</span> <span class="s">Customization</span>
<span class="na">nav_order</span><span class="pi">:</span> <span class="m">6</span>
<span class="nn">---</span>
</code></pre></div></div>

<p>The parameter values determine the order of the top-level pages, and of child pages with the same parent. You can reuse the same parameter values (e.g., integers starting from 1) for the child pages of different parents.</p>

<p>The parameter values can be numbers (integers, floats<sup id="fnref:floats"><a href="#fn:floats" class="footnote" rel="footnote" role="doc-noteref">1</a></sup>) and/or strings. When you omit <code class="language-plaintext highlighter-rouge">nav_order</code> parameters, they default to the titles of the pages, which are ordered alphabetically. Pages with numerical <code class="language-plaintext highlighter-rouge">nav_order</code> parameters always come before those with strings or default <code class="language-plaintext highlighter-rouge">nav_order</code> parameters. If you want to make the page order independent of the page titles, you can set explicit <code class="language-plaintext highlighter-rouge">nav_order</code> parameters on all pages.</p>

<p class="warning">The order of pages with equal <code class="language-plaintext highlighter-rouge">nav_order</code> parameters is unstable: it may change with each build.</p>

<p>By default, all Capital letters come before all lowercase letters; you can add <code class="language-plaintext highlighter-rouge">nav_sort: case_insensitive</code> in the configuration file to ignore the case.<sup id="fnref:case-insensitive"><a href="#fn:case-insensitive" class="footnote" rel="footnote" role="doc-noteref">2</a></sup></p>

<p>Enclosing strings in quotation marks in front matter is optional, unless they contain “<code class="language-plaintext highlighter-rouge">[</code>”, “<code class="language-plaintext highlighter-rouge">]</code>”, “<code class="language-plaintext highlighter-rouge">{</code>”, “<code class="language-plaintext highlighter-rouge">}</code>”, “<code class="language-plaintext highlighter-rouge">,</code>”, “<code class="language-plaintext highlighter-rouge">: </code>”, or “<code class="language-plaintext highlighter-rouge"> #</code>”. Boolean, integer, and float values are treated as strings when enclosed in quotation marks.</p>

<hr />

<div class="footnotes" role="doc-endnotes">
  <ol>
    <li id="fn:floats">
      <p>Jekyll treats each integer <em>N</em> as equal to the corresponding float <em>N.0</em>. <a href="#fnref:floats" class="reversefootnote" role="doc-backlink">&#8617;</a></p>
    </li>
    <li id="fn:case-insensitive">
      <p><em>Note for users of previous versions of Just the Docs:</em> The option <code class="language-plaintext highlighter-rouge">nav_sort: case_insensitive</code> previously affected the ordering of numerical <code class="language-plaintext highlighter-rouge">nav_order</code> parameters: e.g., <code class="language-plaintext highlighter-rouge">10</code> came before <code class="language-plaintext highlighter-rouge">2</code>. Also, all pages with explicit <code class="language-plaintext highlighter-rouge">nav_order</code> parameters previously came before all pages with default parameters. Both were potentially confusing, and they have now been eliminated. <a href="#fnref:case-insensitive" class="reversefootnote" role="doc-backlink">&#8617;</a></p>
    </li>
  </ol>
</div>


</div>
