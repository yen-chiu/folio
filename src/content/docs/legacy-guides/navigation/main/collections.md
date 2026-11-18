---
title: 收藏
slug: legacy-guides/navigation/main/collections
legacySource: docs/Usage Guidelines/navigation/main/collections.md
legacyUrl: /docs/Usage Guidelines/navigation/main/collections/
sidebar:
  order: 5
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 id="collections">Collections</h1>

<p>By default, the navigation includes only <a href="https://jekyllrb.com/docs/pages/">normal pages</a>.
However, you can configure Just the Docs to include also pages from <a href="https://jekyllrb.com/docs/collections/">Jekyll collections</a>.</p>

<blockquote class="note">
  <p>You store collection pages in directories that start with an underscore (<code class="language-plaintext highlighter-rouge">_</code>), e.g., <code class="language-plaintext highlighter-rouge">_tests</code>. You won’t see your <code class="language-plaintext highlighter-rouge">tests</code> collection pages in the navigation if you store them in a <code class="language-plaintext highlighter-rouge">tests</code> directory!<sup id="fnref:1"><a href="#fn:1" class="footnote" rel="footnote" role="doc-noteref">1</a></sup></p>
</blockquote>

<h2 class="text-delta" id="example-defining-custom-collections">Example: defining custom collections</h2>

<p>To define a Jekyll <code class="language-plaintext highlighter-rouge">tests</code> collection named <code class="language-plaintext highlighter-rouge">Tests</code> in your main navigation, store its pages in the <code class="language-plaintext highlighter-rouge">_tests</code> directory, and add the following to <code class="language-plaintext highlighter-rouge">_config.yml</code>:</p>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">collections</span><span class="pi">:</span>
  <span class="na">tests</span><span class="pi">:</span>
    <span class="na">output</span><span class="pi">:</span> <span class="kc">true</span>

<span class="na">just_the_docs</span><span class="pi">:</span>
  <span class="na">collections</span><span class="pi">:</span>
    <span class="na">tests</span><span class="pi">:</span>
      <span class="na">name</span><span class="pi">:</span> <span class="s">Tests</span>
</code></pre></div></div>

<p>Together with the <code class="language-plaintext highlighter-rouge">name</code> to be used for a collection in the navigation, you can configure the following options:</p>

<ul>
  <li><code class="language-plaintext highlighter-rouge">nav_exclude: true</code> to exclude the entire collection from the main navigation</li>
  <li><code class="language-plaintext highlighter-rouge">nav_fold: true</code> to fold the collection, instead of showing links to all its top-level pages<sup id="fnref:2"><a href="#fn:2" class="footnote" rel="footnote" role="doc-noteref">2</a></sup></li>
  <li><code class="language-plaintext highlighter-rouge">search_exclude: true</code> to exclude all the collection pages from search results</li>
</ul>

<p>The main navigation for all your normal pages (if any) is displayed before those in collections. When <em>all</em> your pages are in a single collection, its name is not displayed.</p>

<h2 class="text-delta" id="example-multiple-collections">Example: multiple collections</h2>

<p>You can configure multiple collections. This creates categories in the main navigation with the configured names.</p>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">collections</span><span class="pi">:</span>
  <span class="na">tests</span><span class="pi">:</span>
    <span class="na">output</span><span class="pi">:</span> <span class="kc">true</span>
  <span class="na">tutorials</span><span class="pi">:</span>
    <span class="na">output</span><span class="pi">:</span> <span class="kc">true</span>

<span class="na">just_the_docs</span><span class="pi">:</span>
  <span class="na">collections</span><span class="pi">:</span>
    <span class="na">tests</span><span class="pi">:</span>
      <span class="na">name</span><span class="pi">:</span> <span class="s">Tests</span>
      <span class="na">search_exclude</span><span class="pi">:</span> <span class="kc">true</span>
    <span class="na">tutorials</span><span class="pi">:</span>
      <span class="na">name</span><span class="pi">:</span> <span class="s">Tutorials</span>
      <span class="na">nav_fold</span><span class="pi">:</span> <span class="kc">true</span>
</code></pre></div></div>

<p>The navigation for each collection is a separate name space for page titles: a page in one collection cannot be the <code class="language-plaintext highlighter-rouge">parent</code> of a page in a different collection, nor of a normal page.</p>

<hr />
<div class="footnotes" role="doc-endnotes">
  <ol>
    <li id="fn:1">
      <p>You can optionally specify a directory to store all your collections. For example, if you specify <code class="language-plaintext highlighter-rouge">collections_dir: my_collections</code> in <code class="language-plaintext highlighter-rouge">_config.yml</code>, you should then store the pages of the <code class="language-plaintext highlighter-rouge">tests</code> collection in the <code class="language-plaintext highlighter-rouge">my_collections/_tests</code> directory. <a href="#fnref:1" class="reversefootnote" role="doc-backlink">&#8617;</a></p>
    </li>
    <li id="fn:2">

      <p>When JavaScript is disabled in the browser, all folded collections are automatically expanded,
since clicking expander symbols has no effect. <a href="#fnref:2" class="reversefootnote" role="doc-backlink">&#8617;</a></p>
    </li>
  </ol>
</div>


</div>
