---
title: 页面级别
slug: legacy-guides/navigation/main/levels
legacySource: docs/Usage Guidelines/navigation/main/levels.md
legacyUrl: /docs/Usage Guidelines/navigation/main/levels/
sidebar:
  order: 3
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 id="page-levels">Page Levels</h1>

<p>Sometimes you will want to create a page with many children. First, it is recommended that you store related pages together in a directory. For example, in these docs, we keep all of the written documentation pages in the <code class="language-plaintext highlighter-rouge">./docs</code> directory, and each of the sections in subdirectories like <code class="language-plaintext highlighter-rouge">./docs/Usage Guidelines/ui-components</code> and <code class="language-plaintext highlighter-rouge">./docs/Usage Guidelines/utilities</code>. This gives us an organization like this:</p>

<div class="language-plaintext lh-0 highlighter-rouge"><div class="highlight"><pre class="highlight"><code>┌─ ...
├─ (Jekyll files)
├─ docs
    ├─ configuration.md
    ├─ ui-components
        ├─ index.md (parent page)
        ├─ buttons.md
        ├─ callouts.md
        ├─ code
            ├─ index.md (parent page)
            └─ line-numbers.md
        ├─ labels.md
        ├─ tables.md
        └─ typography.md
    ├─ ...
    └─ MIGRATION.md
├─ index.md (home page)
├─ (Jekyll files)
└─ ...
</code></pre></div></div>

<h2 class="text-delta" id="example-page-with-no-parents">Example: page with no parents</h2>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nn">---</span>
<span class="na">title</span><span class="pi">:</span> <span class="s">UI Components</span>
<span class="na">nav_order</span><span class="pi">:</span> <span class="m">3</span>
<span class="nn">---</span>
</code></pre></div></div>

<p>Here we’re setting up the UI Components landing page that is available at URL <code class="language-plaintext highlighter-rouge">/docs/Usage Guidelines/ui-components</code>, which is ordered second in the main navigation.</p>

<p>The navigation links for all pages with children come with an expander. When you click the expander, the display of the children is toggled, so you can expand or collapse all the children displays, regardless of which page is currently active.</p>

<h2 id="child-pages">Child Pages</h2>

<p>On child pages, simply set the <code class="language-plaintext highlighter-rouge">parent</code> front matter to the parent page’s <code class="language-plaintext highlighter-rouge">title</code>, and set a navigation order (relative to pages having the same parent).</p>

<h3 class="text-delta" id="example-creating-a-child-page">Example: creating a child page</h3>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nn">---</span>
<span class="na">title</span><span class="pi">:</span> <span class="s">Buttons</span>
<span class="na">parent</span><span class="pi">:</span> <span class="s">UI Components</span>
<span class="na">nav_order</span><span class="pi">:</span> <span class="m">2</span>
<span class="nn">---</span>
</code></pre></div></div>

<p>The Buttons page appears as a child of UI Components and appears second in the UI Components pages.</p>

<blockquote class="new-title">
  <p>New (v0.10.0)</p>

  <p>The <code class="language-plaintext highlighter-rouge">has_children</code> field is now redundant (and ignored, except when significant for backwards compatibility).</p>
</blockquote>

<h2 id="multi-level-child-pages">Multi-level Child Pages</h2>

<p>Child pages can themselves have children, to any number of levels.</p>

<h3 class="text-delta" id="example-pages-with-recursive-children">Example: pages with (recursive) children</h3>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nn">---</span>
<span class="na">title</span><span class="pi">:</span> <span class="s">Main Navigation</span>
<span class="na">parent</span><span class="pi">:</span> <span class="s">Navigation</span>
<span class="na">nav_order</span><span class="pi">:</span> <span class="m">1</span>
<span class="nn">---</span>
</code></pre></div></div>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nn">---</span>
<span class="na">title</span><span class="pi">:</span> <span class="s">Ancestry</span>
<span class="na">parent</span><span class="pi">:</span> <span class="s">Main Navigation</span>
<span class="na">nav_order</span><span class="pi">:</span> <span class="m">4</span>
<span class="nn">---</span>
</code></pre></div></div>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nn">---</span>
<span class="na">title</span><span class="pi">:</span> <span class="s">X</span>
<span class="na">parent</span><span class="pi">:</span> <span class="s">Ancestry</span>
<span class="nn">---</span>
</code></pre></div></div>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nn">---</span>
<span class="na">title</span><span class="pi">:</span> <span class="s">Y</span>
<span class="na">parent</span><span class="pi">:</span> <span class="s">Ancestry</span>
<span class="nn">---</span>
</code></pre></div></div>

<p>This creates the following navigation structure:</p>

<div class="language-plaintext lh-0 highlighter-rouge"><div class="highlight"><pre class="highlight"><code>┌─ ...
├─ ...
├─ Navigation
    ├─ ...
    ├─ Main Navigation
        ├─ ...
        ├─ Ancestry
            ├─ X
            └─ Y
        ├─ ...
        └─ ...
    ├─ ...
    └─ ...
├─ ...
└─ ...
</code></pre></div></div>


</div>
