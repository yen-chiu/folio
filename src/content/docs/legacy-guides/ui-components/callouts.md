---
title: 标注
slug: legacy-guides/ui-components/callouts
legacySource: docs/Usage Guidelines/ui-components/callouts.md
legacyUrl: /docs/Usage Guidelines/ui-components/callouts/
sidebar:
  order: 7
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 class="d-inline-block" id="标注">标注</h1>

<p class="label label-green">新 (v0.4.0)</p>

<p>Markdown 不支持标注。但是，恁可以使用 kramdown 支持的 Markdown 扩展将文本样式设置为标注: <a href="https://kramdown.gettalong.org/quickref.html#block-attributes"><em>block IALs</em></a>。</p>

<p>常见的标注类型包括 <code class="language-plaintext highlighter-rouge">highlight</code>、<code class="language-plaintext highlighter-rouge">important</code>、<code class="language-plaintext highlighter-rouge">new</code>、<code class="language-plaintext highlighter-rouge">note</code> 和 <code class="language-plaintext highlighter-rouge">warning</code>。</p>

<p class="warning">这些标注名称<em>不是</em>由主题预先定义的: 恁需要定义自己的名称。</p>

<p>当恁 <a href="/WendellManual/docs/Usage%20Guidelines/configuration/#callouts">配置</a> 标注的 <code class="language-plaintext highlighter-rouge">color</code> 和 (可选) <code class="language-plaintext highlighter-rouge">title</code> 后，恁可以将其应用到段落，或者应用到包含多个段落的引用块，如下图所示。<sup id="fnref:postfix"><a href="#fn:postfix" class="footnote" rel="footnote" role="doc-noteref">1</a></sup></p>

<h2 class="no_toc text-delta" id="an-untitled-callout">An untitled callout</h2>

<div class="language-markdown highlighter-rouge"><div class="highlight"><pre class="highlight"><code>{: .highlight }
A paragraph
</code></pre></div></div>

<p class="highlight">A paragraph</p>

<h2 class="no_toc text-delta" id="a-single-paragraph-callout">A single paragraph callout</h2>

<div class="language-markdown highlighter-rouge"><div class="highlight"><pre class="highlight"><code>{: .note }
A paragraph
</code></pre></div></div>

<p class="note">A paragraph</p>

<div class="language-markdown highlighter-rouge"><div class="highlight"><pre class="highlight"><code>{: .note-title }
<span class="gt">&gt; My note title</span>
<span class="gt">&gt;</span>
<span class="gt">&gt; A paragraph with a custom title callout</span>
</code></pre></div></div>

<blockquote class="note-title">
  <p>My note title</p>

  <p>A paragraph with a custom title callout</p>
</blockquote>

<h2 class="no_toc text-delta" id="a-multi-paragraph-callout">A multi-paragraph callout</h2>

<div class="language-markdown highlighter-rouge"><div class="highlight"><pre class="highlight"><code>{: .important }
<span class="gt">&gt; A paragraph</span>
<span class="gt">&gt;</span>
<span class="gt">&gt; Another paragraph</span>
<span class="gt">&gt;</span>
<span class="gt">&gt; The last paragraph</span>
</code></pre></div></div>

<blockquote class="important">
  <p>A paragraph</p>

  <p>Another paragraph</p>

  <p>The last paragraph</p>
</blockquote>

<div class="language-markdown highlighter-rouge"><div class="highlight"><pre class="highlight"><code>{: .important-title }
<span class="gt">&gt; My important title</span>
<span class="gt">&gt;</span>
<span class="gt">&gt; A paragraph</span>
<span class="gt">&gt;</span>
<span class="gt">&gt; Another paragraph</span>
<span class="gt">&gt;</span>
<span class="gt">&gt; The last paragraph</span>
</code></pre></div></div>

<blockquote class="important-title">
  <p>My important title</p>

  <p>A paragraph</p>

  <p>Another paragraph</p>

  <p>The last paragraph</p>
</blockquote>

<h2 class="no_toc text-delta" id="an-indented-callout">An indented callout</h2>

<div class="language-markdown highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gt">&gt; {: .highlight }</span>
  A paragraph
</code></pre></div></div>

<blockquote>
  <p class="highlight">A paragraph</p>
</blockquote>

<h2 class="no_toc text-delta" id="indented-multi-paragraph-callouts">Indented multi-paragraph callouts</h2>

<div class="language-markdown highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="gt">&gt; {: .new }</span>
<span class="gt">&gt; &gt; A paragraph</span>
<span class="gt">&gt; &gt;</span>
<span class="gt">&gt; &gt; Another paragraph</span>
<span class="gt">&gt; &gt;</span>
<span class="gt">&gt; &gt; The last paragraph</span>
</code></pre></div></div>

<blockquote>
  <blockquote class="new">
    <p>A paragraph</p>

    <p>Another paragraph</p>

    <p>The last paragraph</p>
  </blockquote>
</blockquote>

<h2 class="no_toc text-delta" id="nested-callouts">Nested callouts</h2>

<div class="language-markdown highlighter-rouge"><div class="highlight"><pre class="highlight"><code>{: .important }
<span class="gt">&gt; {: .warning }</span>
<span class="gt">&gt; A paragraph</span>
</code></pre></div></div>

<blockquote class="important">
  <p class="warning">A paragraph</p>
</blockquote>

<h2 class="no_toc text-delta" id="opaque-background">Opaque background</h2>

<div class="language-markdown highlighter-rouge"><div class="highlight"><pre class="highlight"><code>{: .important }
<span class="gt">&gt; {: .opaque }</span>
<span class="gt">&gt; &lt;div markdown="block"&gt;</span>
<span class="gt">&gt; {: .warning }</span>
<span class="gt">&gt; A paragraph</span>
<span class="gt">&gt; &lt;/div&gt;</span>
</code></pre></div></div>

<blockquote class="important">
  <div class="opaque">
    <p class="warning">A paragraph</p>
  </div>
</blockquote>
<div class="footnotes" role="doc-endnotes">
  <ol>
    <li id="fn:postfix">

      <p>You can put the callout markup either before or after its content. <a href="#fnref:postfix" class="reversefootnote" role="doc-backlink">&#8617;</a></p>
    </li>
  </ol>
</div>


</div>
