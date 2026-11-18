---
title: 主导航
slug: legacy-guides/navigation/main
legacySource: docs/Usage Guidelines/navigation/main/index.md
legacyUrl: /docs/Usage Guidelines/navigation/main/
sidebar:
  order: 1
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 id="main-navigation">Main Navigation</h1>

<p>The main navigation for your Just the Docs site is at the left side of the page on large screens, and at the top (behind a tap) on small screens.</p>

<p>You need to specify the <code class="language-plaintext highlighter-rouge">title</code> of each page in its front matter. Page titles are independent of file names and directory structure. The navigation uses the title of the page as an anchor for links to the page.</p>

<p>By default, links to all pages appear in the main navigation at the top level, ordered alphabetically by their titles. By adding further fields to the front matter of individual pages, you can <a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/order/">change their order</a>, <a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/exclude/">exclude pages</a>, and change their <a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/levels/">parent pages</a>.</p>

<blockquote class="new-title">
  <p>New (v0.10.0)</p>

  <p>The main navigation can be structured as a multi-level menu of unlimited depth:
pages can always have child pages.</p>
</blockquote>

<p>For the construction of the navigation display to work (and to avoid potential confusion when browsing) <strong><em>the page titles on your site need to satisfy the following requirements:</em></strong></p>

<ul>
  <li>Top-level pages must have different titles.</li>
  <li>Pages with the same parent must have different titles.</li>
  <li>The title of each page must be different from the titles of all its child pages, and from the titles of their child pages, etc.</li>
</ul>

<blockquote class="new-title">
  <p>New (v0.10.0)</p>

  <p>If <em>all</em> the pages of your site have different titles, you need only to specify the <code class="language-plaintext highlighter-rouge">title</code> of each page, and the <code class="language-plaintext highlighter-rouge">parent</code> title of each lower-level page.<sup id="fnref:1"><a href="#fn:1" class="footnote" rel="footnote" role="doc-noteref">1</a></sup></p>
</blockquote>

<p>If your site has pages with the same title, you need to avoid confusion when you reference that title as <code class="language-plaintext highlighter-rouge">parent</code> on other pages. When the pages with the same title have different <code class="language-plaintext highlighter-rouge">parent</code> pages, you can distinguish between them using the <code class="language-plaintext highlighter-rouge">grand_parent</code> parameter.</p>

<blockquote class="new-title">
  <p>New (v0.10.0)</p>

  <p>For deeper navigation structures, you can specify the title of a grandparent or higher level page as an <code class="language-plaintext highlighter-rouge">ancestor</code> title.</p>
</blockquote>

<hr />
<div class="footnotes" role="doc-endnotes">
  <ol>
    <li id="fn:1">
      <p>Previous versions of Just the Docs restricted the navigation to three levels. You also needed to specify <code class="language-plaintext highlighter-rouge">has_children: true</code> on all parent pages, and a <code class="language-plaintext highlighter-rouge">grand_parent</code> title on all grandchild pages. The <code class="language-plaintext highlighter-rouge">has_children</code> parameter is now redundant, and the <code class="language-plaintext highlighter-rouge">grand_parent</code> parameter can usually be omitted. <a href="#fnref:1" class="reversefootnote" role="doc-backlink">&#8617;</a></p>
    </li>
  </ol>
</div>


</div>
