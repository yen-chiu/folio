---
title: 祖先
slug: legacy-guides/navigation/main/ancestry
legacySource: docs/Usage Guidelines/navigation/main/ancestry.md
legacyUrl: /docs/Usage Guidelines/navigation/main/ancestry/
sidebar:
  order: 4
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 id="ancestry">Ancestry</h1>

<p>If no two pages on your website have the same <code class="language-plaintext highlighter-rouge">title</code>, you only need to set the <code class="language-plaintext highlighter-rouge">parent</code> titles to fix the hierarchy. You can also have the same <code class="language-plaintext highlighter-rouge">title</code> on pages that have no children, provided that they have different parent pages.</p>

<p>If two parents have the same <code class="language-plaintext highlighter-rouge">title</code>, but different grandparents, you can set their <code class="language-plaintext highlighter-rouge">grand_parent</code> titles to distinguish between their parents. The <code class="language-plaintext highlighter-rouge">grand_parent</code> title needs to be the same as the <code class="language-plaintext highlighter-rouge">parent</code> of the <code class="language-plaintext highlighter-rouge">parent</code>.</p>

<h2 class="text-delta" id="example-distinguishing-parents-with-grand_parent">Example: distinguishing parents with <code class="language-plaintext highlighter-rouge">grand_parent</code></h2>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nn">---</span>
<span class="na">title</span><span class="pi">:</span> <span class="s">T</span>
<span class="na">parent</span><span class="pi">:</span> <span class="s">S</span>
<span class="na">grand_parent</span><span class="pi">:</span> <span class="s">X</span>
<span class="nn">---</span>
</code></pre></div></div>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nn">---</span>
<span class="na">title</span><span class="pi">:</span> <span class="s">T</span>
<span class="na">parent</span><span class="pi">:</span> <span class="s">S</span>
<span class="na">grand_parent</span><span class="pi">:</span> <span class="s">Y</span>
<span class="nn">---</span>
</code></pre></div></div>

<p>The <code class="language-plaintext highlighter-rouge">ancestor</code> field of a page generalizes <code class="language-plaintext highlighter-rouge">grand_parent</code> to higher levels.</p>

<p>The following pages illustrate <code class="language-plaintext highlighter-rouge">parent</code> disambiguation using <code class="language-plaintext highlighter-rouge">grand_parent</code> and <code class="language-plaintext highlighter-rouge">ancestor</code> titles. Some descendants of both <a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/x/">Page X</a> and <a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/y/">Page Y</a> have the same title, so references to those descendants as <code class="language-plaintext highlighter-rouge">parent</code> always require disambiguation.</p>

<ul>
  <li><a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/x/">X</a> is a parent page</li>
  <li><a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/xs/">S</a> is the only child of <a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/x/">X</a>. The <code class="language-plaintext highlighter-rouge">parent</code> reference to <a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/x/">X</a> is unambiguous.</li>
  <li><a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/xt/">T</a> is the only child of <a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/xs/">S</a>. Its <code class="language-plaintext highlighter-rouge">parent</code> is disambiguated by its <code class="language-plaintext highlighter-rouge">grand_parent</code>.</li>
  <li><a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/xu/">U</a> is the only child of <a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/xt/">T</a>. Its <code class="language-plaintext highlighter-rouge">parent</code> is disambiguated by its <code class="language-plaintext highlighter-rouge">ancestor</code>.</li>
  <li><a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/y/">Y</a> is a sibling of <a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/x/">X</a>.</li>
  <li><a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/ys/">S</a> is the only child of <a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/y/">Y</a>. The <code class="language-plaintext highlighter-rouge">parent</code> reference to <a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/y/">Y</a> is unambiguous.</li>
  <li><a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/yt/">T</a> is the only child of <a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/ys/">S</a>. Its <code class="language-plaintext highlighter-rouge">parent</code> is disambiguated by its <code class="language-plaintext highlighter-rouge">ancestor</code></li>
  <li><a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/yu/">U</a> is the only child of <a href="/WendellManual/docs/Usage%20Guidelines/navigation/main/yt/">T</a>. Its <code class="language-plaintext highlighter-rouge">parent</code> is disambiguated by its <code class="language-plaintext highlighter-rouge">ancestor</code>.</li>
</ul>



</div>
