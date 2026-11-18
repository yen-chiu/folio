---
title: 代码
slug: legacy-guides/ui-components/code
legacySource: docs/Usage Guidelines/ui-components/code/index.md
legacyUrl: /docs/Usage Guidelines/ui-components/code/
sidebar:
  order: 6
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 class="no_toc" id="code">Code</h1>

<h2 class="no_toc text-delta" id="table-of-contents">Table of contents</h2>

<ol id="markdown-toc">
  <li><a href="#inline-code" id="markdown-toc-inline-code">Inline code</a></li>
  <li><a href="#syntax-highlighted-code-blocks" id="markdown-toc-syntax-highlighted-code-blocks">Syntax highlighted code blocks</a></li>
  <li><a href="#code-blocks-with-rendered-examples" id="markdown-toc-code-blocks-with-rendered-examples">Code blocks with rendered examples</a></li>
  <li><a href="#mermaid-diagram-code-blocks" id="markdown-toc-mermaid-diagram-code-blocks">Mermaid diagram code blocks</a>    <ol>
      <li><a href="#using-a-local-mermaid-library" id="markdown-toc-using-a-local-mermaid-library">Using a local mermaid library</a></li>
      <li><a href="#using-mermaid-with-asciidoc" id="markdown-toc-using-mermaid-with-asciidoc">Using mermaid with AsciiDoc</a></li>
    </ol>
  </li>
  <li><a href="#copy-button" id="markdown-toc-copy-button">Copy button</a></li>
</ol>

<hr />

<h2 id="inline-code">Inline code</h2>

<p>Code can be rendered inline by wrapping it in single back ticks.</p>

<div class="code-example">
  <p>Lorem ipsum dolor sit amet, <code class="language-plaintext highlighter-rouge">&lt;inline code snippet&gt;</code> adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>

  <h2 class="no_toc" id="heading-with-inline-code-snippet-in-it">Heading with <code class="language-plaintext highlighter-rouge">&lt;inline code snippet&gt;</code> in it.</h2>
</div>
<div class="language-markdown highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Lorem ipsum dolor sit amet, <span class="sb">`&lt;inline code snippet&gt;`</span> adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

<span class="gu">## Heading with `&lt;inline code snippet&gt;` in it.</span>
</code></pre></div></div>

<hr />

<h2 id="syntax-highlighted-code-blocks">Syntax highlighted code blocks</h2>

<p>Use Jekyll’s built-in syntax highlighting with Rouge for code blocks by using three backticks, followed by the language name:</p>

<div class="code-example">
  <div class="language-js highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1">// Javascript code with syntax highlighting.</span>
<span class="kd">var</span> <span class="nx">fun</span> <span class="o">=</span> <span class="kd">function</span> <span class="nf">lang</span><span class="p">(</span><span class="nx">l</span><span class="p">)</span> <span class="p">{</span>
  <span class="nx">dateformat</span><span class="p">.</span><span class="nx">i18n</span> <span class="o">=</span> <span class="nf">require</span><span class="p">(</span><span class="dl">'</span><span class="s1">./lang/</span><span class="dl">'</span> <span class="o">+</span> <span class="nx">l</span><span class="p">)</span>
  <span class="k">return</span> <span class="kc">true</span><span class="p">;</span>
<span class="p">}</span>
</code></pre></div>  </div>
</div>

<figure class="highlight"><pre><code class="language-markdown" data-lang="markdown"><span class="p">```</span><span class="nl">js
</span><span class="c1">// Javascript code with syntax highlighting.</span>
<span class="kd">var</span> <span class="nx">fun</span> <span class="o">=</span> <span class="kd">function</span> <span class="nf">lang</span><span class="p">(</span><span class="nx">l</span><span class="p">)</span> <span class="p">{</span>
  <span class="nx">dateformat</span><span class="p">.</span><span class="nx">i18n</span> <span class="o">=</span> <span class="nf">require</span><span class="p">(</span><span class="dl">'</span><span class="s1">./lang/</span><span class="dl">'</span> <span class="o">+</span> <span class="nx">l</span><span class="p">)</span>
  <span class="k">return</span> <span class="kc">true</span><span class="p">;</span>
<span class="p">}</span>
<span class="p">```</span></code></pre></figure>

<p>Syntax highlighting, line numbers, and HTML compression do not work together; <strong>the combination of these features generates invalid HTML that renders incorrectly</strong>. To learn more, see <a href="/WendellManual/docs/Usage%20Guidelines/ui-components/code/line-numbers/">“Code with line numbers”</a>.</p>

<hr />

<h2 id="code-blocks-with-rendered-examples">Code blocks with rendered examples</h2>

<p>To demonstrate front end code, sometimes it’s useful to show a rendered example of that code. After including the styles from your project that you’ll need to show the rendering, you can use a <code class="language-plaintext highlighter-rouge">&lt;div&gt;</code> with the <code class="language-plaintext highlighter-rouge">code-example</code> class, followed by the code block syntax. If you want to render your output with Markdown instead of HTML, use the <code class="language-plaintext highlighter-rouge">markdown="1"</code> attribute to tell Jekyll that the code you are rendering will be in Markdown format… This is about to get meta…</p>

<div class="code-example">

  <div class="code-example">

    <p><a href="https://just-the-docs.com" class="btn">Link button</a></p>

  </div>
  <div class="language-markdown highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="p">[</span><span class="nv">Link button</span><span class="p">](</span><span class="sx">https://just-the-docs.com</span><span class="p">)</span>{: .btn }
</code></pre></div>  </div>

</div>

<figure class="highlight"><pre><code class="language-markdown" data-lang="markdown"><span class="nt">&lt;div</span> <span class="na">class=</span><span class="s">"code-example"</span> <span class="na">markdown=</span><span class="s">"1"</span><span class="nt">&gt;</span>

<span class="p">[</span><span class="nv">Link button</span><span class="p">](</span><span class="sx">https://just-the-docs.com</span><span class="p">)</span>{: .btn }

<span class="nt">&lt;/div&gt;</span>
<span class="p">```</span><span class="nl">markdown
</span><span class="p">[</span><span class="nv">Link button</span><span class="p">](</span><span class="sx">https://just-the-docs.com</span><span class="p">)</span>{: .btn }
<span class="p">```</span></code></pre></figure>

<hr />

<h2 class="d-inline-block" id="mermaid-diagram-code-blocks">Mermaid diagram code blocks</h2>

<p class="label label-green">New (v0.4.0)</p>

<p><a href="https://mermaid-js.github.io/mermaid/">Mermaid</a> allows you to add diagrams and visualizations using Markdown code blocks. <strong>It is disabled by default</strong>. However, you can turn on support for mermaid by adding a <code class="language-plaintext highlighter-rouge">mermaid</code> key to your <code class="language-plaintext highlighter-rouge">_config.yml</code>.</p>

<p>The minimum configuration requires a <code class="language-plaintext highlighter-rouge">version</code> key (matching a version in <a href="https://cdn.jsdelivr.net/npm/mermaid/">jsDelivr</a>):</p>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">mermaid</span><span class="pi">:</span>
  <span class="c1"># Version of mermaid library</span>
  <span class="c1"># Pick an available version from https://cdn.jsdelivr.net/npm/mermaid/</span>
  <span class="na">version</span><span class="pi">:</span> <span class="s2">"</span><span class="s">9.1.3"</span>
</code></pre></div></div>

<p>Additional configuration options are loaded through <code class="language-plaintext highlighter-rouge">_includes/mermaid_config.js</code>. By default, the contents of the file are the empty object:</p>

<div class="language-js highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1">// _includes/mermaid_config.js</span>
<span class="p">{}</span>
</code></pre></div></div>

<p>This loads the default settings.</p>

<p>The contents of this object should follow <a href="https://mermaid.js.org/config/configuration.html">mermaid’s configuration API</a>. For example, to override the theme, change <code class="language-plaintext highlighter-rouge">_includes/mermaid_config.js</code> to:</p>

<div class="language-js highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1">// _includes/mermaid_config.js</span>
<span class="p">{</span>
  <span class="nl">theme</span><span class="p">:</span> <span class="dl">"</span><span class="s2">forest</span><span class="dl">"</span>
<span class="p">}</span>
</code></pre></div></div>

<p>Once mermaid is installed, it can be used in markdown files. The markdown for a simple flowchart example might look like the following:</p>

<figure class="highlight"><pre><code class="language-markdown" data-lang="markdown"><span class="p">```</span><span class="nl">mermaid
</span><span class="sb">graph TD;
    accTitle: the diamond pattern
    accDescr: a graph with four nodes: A points to B and C, while B and C both point to D
    A--&gt;B;
    A--&gt;C;
    B--&gt;D;
    C--&gt;D;</span>
<span class="p">```</span></code></pre></figure>

<p>which renders:</p>

<div class="folio-mermaid-source" data-mermaid-source="graph TD;
    accTitle: the diamond pattern
    accDescr: a graph with four nodes: A points to B and C, while B and C both point to D
    A--&gt;B;
    A--&gt;C;
    B--&gt;D;
    C--&gt;D;
"><pre><code class="language-mermaid">graph TD;
    accTitle: the diamond pattern
    accDescr: a graph with four nodes: A points to B and C, while B and C both point to D
    A--&gt;B;
    A--&gt;C;
    B--&gt;D;
    C--&gt;D;
</code></pre></div>

<p><em>Note: for demonstration purposes, we’ve enabled mermaid on this site. It is still disabled by default, and users need to opt-in to use it.</em></p>

<h3 id="using-a-local-mermaid-library">Using a local mermaid library</h3>

<p>To load a local version of mermaid, also use the <code class="language-plaintext highlighter-rouge">path</code> key to specify the location of the library; e.g.</p>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">mermaid</span><span class="pi">:</span>
  <span class="na">version</span><span class="pi">:</span> <span class="s2">"</span><span class="s">10.1.0"</span>
  <span class="c1"># for (v10+)</span>
  <span class="na">path</span><span class="pi">:</span> <span class="s2">"</span><span class="s">/assets/js/mermaid.esm.min.mjs"</span>
  <span class="c1"># for (&lt;v10):</span>
  <span class="c1"># path: "/assets/js/mermaid.min.js"</span>
  <span class="c1"># Note: copy both `mermaid.esm.min.mjs` (v10+) or `mermaid.min.js` (&lt;v10) and the associated</span>
  <span class="c1"># `.map` file from the specified version of `mermaid/dist` to `/assets/js/`.</span>
</code></pre></div></div>

<p>For mermaid versions <code class="language-plaintext highlighter-rouge">&gt;=10</code>, this file is imported directly as an ESM module (rather than as a plain <code class="language-plaintext highlighter-rouge">&lt;script&gt;</code> tag); users should use the <code class="language-plaintext highlighter-rouge">mermaid.esm.min.mjs</code> file. In contrast, for mermaid versions <code class="language-plaintext highlighter-rouge">&lt;10</code>, this file is loaded as a script tag; it should be a standalone CJS file (i.e. <code class="language-plaintext highlighter-rouge">mermaid.min.js</code>).</p>

<p class="warning">Mermaid versions <code class="language-plaintext highlighter-rouge">10.0</code> - <code class="language-plaintext highlighter-rouge">10.1</code> (and possibly, future releases) still encode relative imports in <code class="language-plaintext highlighter-rouge">mermaid.esm.min.mjs</code>. Local users must copy <em>all</em> of the contents of the <code class="language-plaintext highlighter-rouge">dist</code> folder to the specified path (preserving the relative location of the files). Just the Docs is actively monitoring mermaid releases; an upstream fix is planned.</p>

<h3 id="using-mermaid-with-asciidoc">Using mermaid with AsciiDoc</h3>

<p>Users of <a href="https://asciidoc.org/">AsciiDoc</a> (e.g. via <a href="https://github.com/asciidoctor/jekyll-asciidoc">jekyll-asciidoc</a>) may need additional configuration to use mermaid.</p>

<p>By default, AsciiDoc generates HTML markup that mermaid cannot properly parse. The simplest way to resolve this is to use a <a href="https://docs.asciidoctor.org/asciidoc/latest/pass/pass-block/">passthrough block</a>:</p>

<figure class="highlight"><pre><code class="language-asciidoc" data-lang="asciidoc">++++
&lt;pre class="language-mermaid"&gt;
graph TD;
    accTitle: the diamond pattern
    accDescr: a graph with four nodes: A points to B and C, while B and C both point to D
    A--&gt;B;
    A--&gt;C;
    B--&gt;D;
    C--&gt;D;
&lt;/pre&gt;
++++</code></pre></figure>

<p>Alternatively, community member <a href="https://github.com/flyx">@flyx</a> has contributed a Ruby extension that does not require extra markup. The extension is available <a href="https://gist.github.com/flyx/9fff080cf4edc95d495bc661a002232c">as a GitHub Gist</a>. Thank you to <a href="https://github.com/flyx">@flyx</a>!</p>

<p>The <a href="https://docs.asciidoctor.org/diagram-extension/latest/">asciidoctor-diagram</a> extension which also supports mermaid is not recommended for use with Just the Docs, since it requires separate configuration e.g. for theming, and is known to not be trivial to set up.</p>

<h2 class="d-inline-block" id="copy-button">Copy button</h2>

<p class="label label-green">New (v0.4.0)</p>

<p>The copy button for code blocks can be enabled or disabled via the <code class="language-plaintext highlighter-rouge">enable_copy_code_button</code> key in <code class="language-plaintext highlighter-rouge">_config.yml</code>. By default, the value of this key is <code class="language-plaintext highlighter-rouge">false</code>; users need to opt-in.</p>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># For copy button on code</span>
<span class="na">enable_copy_code_button</span><span class="pi">:</span> <span class="kc">true</span>
</code></pre></div></div>

<p>Note that this feature requires JavaScript; if JavaScript is disabled in the browser, this feature will not work. In addition, this feature uses <code class="language-plaintext highlighter-rouge">navigator.clipboard</code>, which is only available in <a href="https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts">secure contexts</a> (such as over HTTPS). If the site is viewed in an insecure context, the copy button will not work (<a href="https://github.com/just-the-docs/just-the-docs/issues/1202">relevant issue: #1202</a>).</p>


</div>
