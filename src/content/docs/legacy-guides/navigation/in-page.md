---
title: 页内导航
slug: legacy-guides/navigation/in-page
legacySource: docs/Usage Guidelines/navigation/in-page.md
legacyUrl: /docs/Usage Guidelines/navigation/in-page/
sidebar:
  order: 5
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 class="no_toc" id="in-page-navigation">In-Page Navigation</h1>

<h2 class="no_toc text-delta" id="table-of-contents">Table of Contents</h2>

<ol id="markdown-toc">
  <li><a href="#generating-table-of-contents" id="markdown-toc-generating-table-of-contents">Generating Table of Contents</a></li>
  <li><a href="#omitting-heading-from-table-of-contents" id="markdown-toc-omitting-heading-from-table-of-contents">Omitting Heading from Table of Contents</a></li>
  <li><a href="#collapsible-table-of-contents-with-details-and-summary" id="markdown-toc-collapsible-table-of-contents-with-details-and-summary">Collapsible Table of Contents (with <code class="language-plaintext highlighter-rouge">&lt;details&gt;</code> and <code class="language-plaintext highlighter-rouge">&lt;summary&gt;</code>)</a></li>
  <li><a href="#back-to-top-doc" id="markdown-toc-back-to-top-doc">Back to Top</a></li>
</ol>

<p>To support in-page navigation, you can generate a <em>Table of Contents</em> (TOC) with links to headings, like the one shown above, as well as a link to the top of the page.</p>

<h2 id="generating-table-of-contents">Generating Table of Contents</h2>

<p>To generate a <em>Table of Contents</em> in a page, you use Kramdown’s <code class="language-plaintext highlighter-rouge">{:toc}</code> method, immediately after the start of a list. This will automatically generate a list of anchor links to various sections of the page, based on headings and heading levels.</p>

<h2 id="omitting-heading-from-table-of-contents">Omitting Heading from Table of Contents</h2>

<p>If you want to omit a particular heading from the TOC, follow it immediately by <code class="language-plaintext highlighter-rouge">{: .no_toc }</code> (possibly together with other CSS class names).</p>

<div class="language-markdown highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gh"># In-Page Navigation</span>
{: .no_toc }

<span class="gu">## Table of Contents</span>
{: .no_toc .text-delta }
<span class="p">
1.</span> TOC
{:toc}
</code></pre></div></div>

<p>This example omits the top-level heading (<code class="language-plaintext highlighter-rouge">In-Page Navigation</code>) from the TOC, as well as the heading for the <em>Table of Contents</em> itself.</p>

<p>To get an unordered list, replace <code class="language-plaintext highlighter-rouge">1. TOC</code> by <code class="language-plaintext highlighter-rouge">- TOC</code> in the above example.</p>

<h2 id="collapsible-table-of-contents-with-details-and-summary">Collapsible Table of Contents (with <code class="language-plaintext highlighter-rouge">&lt;details&gt;</code> and <code class="language-plaintext highlighter-rouge">&lt;summary&gt;</code>)</h2>

<p>You can make the Table of Contents collapsible using the <code class="language-plaintext highlighter-rouge">&lt;details&gt;</code> and <code class="language-plaintext highlighter-rouge">&lt;summary&gt;</code> elements, as in the following example.</p>

<div class="language-markdown highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nt">&lt;details</span> <span class="na">open</span> <span class="na">markdown=</span><span class="s">"block"</span><span class="nt">&gt;</span>
  <span class="nt">&lt;summary&gt;</span>
    Table of contents
  <span class="nt">&lt;/summary&gt;</span>
  {: .text-delta }
<span class="p">1.</span> TOC
{:toc}
<span class="nt">&lt;/details&gt;</span>
</code></pre></div></div>

<p>The attribute <code class="language-plaintext highlighter-rouge">open</code> (which expands the Table of Contents by default) and the styling (here with <code class="language-plaintext highlighter-rouge">text-delta</code>) are optional.</p>

<p class="note"><code class="language-plaintext highlighter-rouge">{:toc}</code> can be used only once on each page.</p>

<h2 id="back-to-top-doc">Back to Top</h2>

<p class="warning">The default id for a section with heading “Back to Top” is <code class="language-plaintext highlighter-rouge">"back-to-top"</code>.
To avoid invalid HTML, sites that set the <code class="language-plaintext highlighter-rouge">back_to_top</code> configuration variable
should override the default id for such sections. The Markdown source file for
the current page uses <code class="language-plaintext highlighter-rouge">## Back to Top {#back-to-top-doc}</code>.</p>

<p>You can add a link from the bottom of each page to its top. You do this by including the <code class="language-plaintext highlighter-rouge">back_to_top</code> configuration option in your site’s <code class="language-plaintext highlighter-rouge">_config.yml</code> file, together with <code class="language-plaintext highlighter-rouge">back_to_top_text</code> for the anchor link.</p>

<h3 class="no_toc" id="example">Example</h3>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">back_to_top</span><span class="pi">:</span> <span class="kc">true</span>
<span class="na">back_to_top_text</span><span class="pi">:</span> <span class="s2">"</span><span class="s">Back</span><span class="nv"> </span><span class="s">to</span><span class="nv"> </span><span class="s">top"</span>
</code></pre></div></div>

<p class="warning">Back-to-top links currently appear only when <em>other</em> configuration options require footer generation!</p>


</div>
