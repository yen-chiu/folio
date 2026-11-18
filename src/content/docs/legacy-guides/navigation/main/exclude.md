---
title: 排除页面
slug: legacy-guides/navigation/main/exclude
legacySource: docs/Usage Guidelines/navigation/main/exclude.md
legacyUrl: /docs/Usage Guidelines/navigation/main/exclude/
sidebar:
  order: 2
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 id="excluding-pages">Excluding Pages</h1>

<p>For specific pages that you do not wish to include in the main navigation (e.g., a 404 page or a landing page) set <code class="language-plaintext highlighter-rouge">nav_exclude: true</code> in their front matter.</p>

<h2 class="text-delta" id="example-using-nav_exclude">Example: using <code class="language-plaintext highlighter-rouge">nav_exclude</code></h2>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nn">---</span>
<span class="na">layout</span><span class="pi">:</span> <span class="s">default</span>
<span class="na">title</span><span class="pi">:</span> <span class="m">404</span>
<span class="na">nav_exclude</span><span class="pi">:</span> <span class="kc">true</span>
<span class="na">permalink</span><span class="pi">:</span> <span class="s">/404</span>
<span class="nn">---</span>
</code></pre></div></div>

<p>The <code class="language-plaintext highlighter-rouge">nav_exclude</code> parameter does not affect the <a href="/WendellManual/docs/Usage%20Guidelines/navigation/parents/">breadcrumbs</a>, nor the <a href="/WendellManual/docs/Usage%20Guidelines/navigation/children/">lists of child pages</a>, which you can use to access pages excluded from the main navigation.</p>

<p>Pages with no <code class="language-plaintext highlighter-rouge">title</code> are automatically excluded from the main navigation, except when they are in collections (where Jekyll provides default titles based on file names).</p>

<p>Child pages are automatically excluded from the main navigation when their parent page is excluded.</p>

<p class="warning">It is currently possible to exclude all the child pages of a page from the main navigation by setting <code class="language-plaintext highlighter-rouge">has_children: false</code> in its front matter. However, the <code class="language-plaintext highlighter-rouge">has_children</code> parameter may be ignored altogether in a future release, so it is better to use the <code class="language-plaintext highlighter-rouge">nav_exclude</code> parameter on each child page.</p>


</div>
