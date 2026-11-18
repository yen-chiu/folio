---
title: 搜索
slug: legacy-guides/search
legacySource: docs/Usage Guidelines/search.md
legacyUrl: /docs/Usage Guidelines/search/
sidebar:
  order: 7
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 class="no_toc" id="搜索">搜索</h1>

<h2 class="no_toc text-delta" id="目录">目录</h2>

<ol id="markdown-toc">
  <li><a href="#在配置中启用搜索" id="markdown-toc-在配置中启用搜索">在配置中启用搜索</a>    <ol>
      <li><a href="#search-granularity" id="markdown-toc-search-granularity">Search granularity</a></li>
      <li><a href="#search-previews" id="markdown-toc-search-previews">Search previews</a></li>
      <li><a href="#search-tokenizer" id="markdown-toc-search-tokenizer">Search tokenizer</a></li>
      <li><a href="#display-url-in-search-results" id="markdown-toc-display-url-in-search-results">Display URL in search results</a></li>
      <li><a href="#display-search-button" id="markdown-toc-display-search-button">Display search button</a></li>
      <li><a href="#focus-search-bar-with-a-keyboard-shortcut" id="markdown-toc-focus-search-bar-with-a-keyboard-shortcut">Focus search bar with a keyboard shortcut</a></li>
    </ol>
  </li>
  <li><a href="#hiding-pages-from-search" id="markdown-toc-hiding-pages-from-search">Hiding pages from search</a></li>
  <li><a href="#generate-search-index-when-used-as-a-gem" id="markdown-toc-generate-search-index-when-used-as-a-gem">Generate search index when used as a gem</a></li>
  <li><a href="#custom-content-for-search-index" id="markdown-toc-custom-content-for-search-index">Custom content for search index</a>    <ol>
      <li><a href="#example-adding-custom-usage-and-examples-fields" id="markdown-toc-example-adding-custom-usage-and-examples-fields">Example: adding custom <code class="language-plaintext highlighter-rouge">usage</code> and <code class="language-plaintext highlighter-rouge">examples</code> fields</a></li>
    </ol>
  </li>
</ol>

<hr />

<p>Just the Docs 使用 <a href="https://lunrjs.com">lunr.js</a> 添加由 Jekyll 生成的 JSON 索引支持的客户端搜索界面。
所有搜索结果都显示在自动完成样式的界面中（没有搜索结果页面）。
默认情况下，所有生成的 HTML 页面都使用以下数据点进行索引:</p>

<ul>
  <li>页面标题</li>
  <li>页面内容</li>
  <li>页面 URL</li>
</ul>

<h2 id="在配置中启用搜索">在配置中启用搜索</h2>

<p>在恁网站的 <code class="language-plaintext highlighter-rouge">_config.yml</code> 中，启用搜索:</p>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Enable or disable the site search</span>
<span class="c1"># Supports true (default) or false</span>
<span class="na">search_enabled</span><span class="pi">:</span> <span class="kc">true</span>
</code></pre></div></div>

<h3 id="search-granularity">Search granularity</h3>

<p>Pages are split into sections that can be searched individually.
The sections are defined by the headings on the page.
Each section is displayed in a separate search result.</p>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Split pages into sections that can be searched individually</span>
<span class="c1"># Supports 1 - 6, default: 2</span>
<span class="na">search.heading_level</span><span class="pi">:</span> <span class="m">2</span>
</code></pre></div></div>

<h3 id="search-previews">Search previews</h3>

<p>A search result can contain previews that show where the search words are found in the specific section.</p>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Maximum amount of previews per search result</span>
<span class="c1"># Default: 3</span>
<span class="na">search.previews</span><span class="pi">:</span> <span class="m">3</span>

<span class="c1"># Maximum amount of words to display before a matched word in the preview</span>
<span class="c1"># Default: 5</span>
<span class="na">search.preview_words_before</span><span class="pi">:</span> <span class="m">5</span>

<span class="c1"># Maximum amount of words to display after a matched word in the preview</span>
<span class="c1"># Default: 10</span>
<span class="na">search.preview_words_after</span><span class="pi">:</span> <span class="m">10</span>
</code></pre></div></div>

<h3 id="search-tokenizer">Search tokenizer</h3>

<p>The default is for hyphens to separate tokens in search terms:
<code class="language-plaintext highlighter-rouge">gem-based</code> is equivalent to <code class="language-plaintext highlighter-rouge">gem based</code>, matching either word.
To allow search for hyphenated words:</p>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Set the search token separator</span>
<span class="c1"># Default: /[\s\-/]+/</span>
<span class="c1"># Example: enable support for hyphenated search words</span>
<span class="na">search.tokenizer_separator</span><span class="pi">:</span> <span class="s">/[\s/]+/</span>
</code></pre></div></div>

<h3 id="display-url-in-search-results">Display URL in search results</h3>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Display the relative url in search results</span>
<span class="c1"># Supports true (default) or false</span>
<span class="na">search.rel_url</span><span class="pi">:</span> <span class="kc">false</span>
</code></pre></div></div>

<h3 id="display-search-button">Display search button</h3>

<p>The search button displays in the bottom right corner of the screen and triggers the search input when clicked.</p>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Enable or disable the search button that appears in the bottom right corner of every page</span>
<span class="c1"># Supports true or false (default)</span>
<span class="na">search.button</span><span class="pi">:</span> <span class="kc">true</span>
</code></pre></div></div>

<h3 id="focus-search-bar-with-a-keyboard-shortcut">Focus search bar with a keyboard shortcut</h3>

<p>Just the Docs supports focusing the search bar input with a keyboard shortcut. After setting the <code class="language-plaintext highlighter-rouge">search.focus_shortcut_key</code> config item key, users who press <kbd>Ctrl</kbd> + <code class="language-plaintext highlighter-rouge">search.focus_shortcut_key</code> (or on macOS, <kbd>Command</kbd> + <code class="language-plaintext highlighter-rouge">search.focus_shortcut_key</code>) will focus the search bar.</p>

<p>Note that this feature is <strong>disabled by default</strong>. <code class="language-plaintext highlighter-rouge">search.focus_shortcut_key</code> should be a <a href="https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key">valid value from <code class="language-plaintext highlighter-rouge">KeyboardEvent.key</code></a>; this involves all ASCII alphanumeric values, as well as modifier keys.</p>

<p>For example,</p>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">search</span><span class="pi">:</span>
    <span class="na">focus_shortcut_key</span><span class="pi">:</span> <span class="s1">'</span><span class="s">k'</span>
</code></pre></div></div>

<p>Will make <kbd>Ctrl</kbd> + <kbd>K</kbd> focus the search bar for Windows users (and <kbd>Command</kbd> + <kbd>K</kbd> on macOS).</p>

<h2 id="hiding-pages-from-search">Hiding pages from search</h2>

<p>Sometimes you might have a page that you don’t want to be indexed for the search nor to show up in search results, e.g., a 404 page.
To exclude a page from search, add the <code class="language-plaintext highlighter-rouge">search_exclude: true</code> parameter to the page’s YAML front matter:</p>

<div class="language-yaml no_toc highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nn">---</span>
<span class="na">layout</span><span class="pi">:</span> <span class="s">default</span>
<span class="na">title</span><span class="pi">:</span> <span class="s">Page not found</span>
<span class="na">nav_exclude</span><span class="pi">:</span> <span class="kc">true</span>
<span class="na">search_exclude</span><span class="pi">:</span> <span class="kc">true</span>
<span class="nn">---</span>

</code></pre></div></div>

<h2 id="generate-search-index-when-used-as-a-gem">Generate search index when used as a gem</h2>

<p>If you use Just the Docs as a remote theme, you do not need the following steps.</p>

<p>If you use the theme as a gem, you must initialize the search by running this <code class="language-plaintext highlighter-rouge">rake</code> command that comes with <code class="language-plaintext highlighter-rouge">just-the-docs</code>:</p>

<div class="language-bash highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>bundle <span class="nb">exec </span>just-the-docs rake search:init
</code></pre></div></div>

<p>This command creates the <code class="language-plaintext highlighter-rouge">assets/js/zzzz-search-data.json</code> file that Jekyll uses to create your search index.
Alternatively, you can create the file manually with <a href="https://github.com/yen-chiu/WendellManual/blob/main/assets/js/zzzz-search-data.json">this content</a>.</p>

<h2 class="d-inline-block" id="custom-content-for-search-index">Custom content for search index</h2>

<p class="label label-green">New (v0.4.0)</p>

<p class="label label-yellow">Advanced</p>

<p>By default, the search feature indexes a page’s <code class="language-plaintext highlighter-rouge">.content</code>, <code class="language-plaintext highlighter-rouge">.title</code>, and <em>some</em> headers within the <code class="language-plaintext highlighter-rouge">.content</code>. Other data (e.g. front matter, files in <code class="language-plaintext highlighter-rouge">_data</code> and <code class="language-plaintext highlighter-rouge">assets</code>) is not indexed. Users can customize what is indexed.</p>

<blockquote class="warning">
  <p>Customizing search indices is an advanced feature that requires Javascript and Liquid knowledge.</p>
</blockquote>

<ol>
  <li>When Just the Docs is a local or gem theme, ensure <code class="language-plaintext highlighter-rouge">assets/js/zzzz-search-data.json</code> is up-to-date with <a href="#generate-search-index-when-used-as-a-gem">Generate search index when used as a gem</a>.</li>
  <li>Add a new file named <code class="language-plaintext highlighter-rouge">_includes/lunr/custom-data.json</code>. Insert custom Liquid code that reads your data (e.g. the page object at <code class="language-plaintext highlighter-rouge">include.page</code>) then generates custom Javascript fields that hold the custom data you want to index. Verify these fields in the generated <code class="language-plaintext highlighter-rouge">assets/js/search-data.json</code>.</li>
  <li>Add a new file named <code class="language-plaintext highlighter-rouge">_includes/lunr/custom-index.js</code>. Insert custom Javascript code that reads your custom Javascript fields and inserts them into the search index. You may want to inspect <code class="language-plaintext highlighter-rouge">assets/js/just-the-docs.js</code> to better understand the code.</li>
</ol>

<h3 class="text-delta" id="example-adding-custom-usage-and-examples-fields">Example: adding custom <code class="language-plaintext highlighter-rouge">usage</code> and <code class="language-plaintext highlighter-rouge">examples</code> fields</h3>

<p>This example adds front matter <code class="language-plaintext highlighter-rouge">usage</code> and <code class="language-plaintext highlighter-rouge">examples</code> fields to the search index.</p>

<p><code class="language-plaintext highlighter-rouge">_includes/lunr/custom-data.json</code> custom code reads the page <code class="language-plaintext highlighter-rouge">usage</code> and <code class="language-plaintext highlighter-rouge">examples</code> fields, normalizes the text, and writes the text to custom Javascript <code class="language-plaintext highlighter-rouge">myusage</code> and <code class="language-plaintext highlighter-rouge">myexamples</code> fields. Javascript fields are similar yet <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON#javascript_and_json_differences">not the same as JSON</a>. <code class="language-plaintext highlighter-rouge">jsonify</code> will probably work for most scenarios.</p>

<div class="language-liquid highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="cp">{%-</span><span class="w"> </span><span class="nt">capture</span><span class="w"> </span><span class="nv">newline</span><span class="w"> </span><span class="cp">%}</span>
<span class="cp">{%</span><span class="w"> </span><span class="nt">endcapture</span><span class="w"> </span><span class="cp">-%}</span>
"myusage": <span class="cp">{{</span><span class="w"> </span><span class="nv">include</span><span class="p">.</span><span class="nv">page</span><span class="p">.</span><span class="nv">usage</span><span class="w"> </span><span class="p">|</span><span class="w"> </span><span class="nf">markdownify</span><span class="w"> </span><span class="p">|</span><span class="w"> </span><span class="nf">replace</span><span class="p">:</span><span class="nv">newline</span><span class="p">,</span><span class="s1">' '</span><span class="w"> </span><span class="p">|</span><span class="w"> </span><span class="nf">strip_html</span><span class="w"> </span><span class="p">|</span><span class="w"> </span><span class="nf">normalize_whitespace</span><span class="w"> </span><span class="p">|</span><span class="w"> </span><span class="nf">strip</span><span class="w"> </span><span class="p">|</span><span class="w"> </span><span class="nf">jsonify</span><span class="w"> </span><span class="cp">}}</span>,
"myexamples": <span class="cp">{{</span><span class="w"> </span><span class="nv">include</span><span class="p">.</span><span class="nv">page</span><span class="p">.</span><span class="nv">examples</span><span class="w"> </span><span class="p">|</span><span class="w"> </span><span class="nf">markdownify</span><span class="w"> </span><span class="p">|</span><span class="w"> </span><span class="nf">replace</span><span class="p">:</span><span class="nv">newline</span><span class="p">,</span><span class="s1">' '</span><span class="w"> </span><span class="p">|</span><span class="w"> </span><span class="nf">strip_html</span><span class="w"> </span><span class="p">|</span><span class="w"> </span><span class="nf">normalize_whitespace</span><span class="w"> </span><span class="p">|</span><span class="w"> </span><span class="nf">strip</span><span class="w"> </span><span class="p">|</span><span class="w"> </span><span class="nf">jsonify</span><span class="w"> </span><span class="cp">}}</span>,
</code></pre></div></div>

<p><code class="language-plaintext highlighter-rouge">_includes/lunr/custom-index.js</code> custom code is inserted into the Javascript loop of <code class="language-plaintext highlighter-rouge">assets/js/just-the-docs.js</code>. All custom Javascript fields are accessed as fields of <code class="language-plaintext highlighter-rouge">docs[i]</code> such as <code class="language-plaintext highlighter-rouge">docs[i].myusage</code>. Finally, append your custom fields on to the already existing <code class="language-plaintext highlighter-rouge">docs[i].content</code>.</p>

<div class="language-javascript highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kd">const</span> <span class="nx">content_to_merge</span> <span class="o">=</span> <span class="p">[</span><span class="nx">docs</span><span class="p">[</span><span class="nx">i</span><span class="p">].</span><span class="nx">content</span><span class="p">,</span> <span class="nx">docs</span><span class="p">[</span><span class="nx">i</span><span class="p">].</span><span class="nx">myusage</span><span class="p">,</span> <span class="nx">docs</span><span class="p">[</span><span class="nx">i</span><span class="p">].</span><span class="nx">myexamples</span><span class="p">];</span>
<span class="nx">docs</span><span class="p">[</span><span class="nx">i</span><span class="p">].</span><span class="nx">content</span> <span class="o">=</span> <span class="nx">content_to_merge</span><span class="p">.</span><span class="nf">join</span><span class="p">(</span><span class="dl">'</span><span class="s1"> </span><span class="dl">'</span><span class="p">);</span>
</code></pre></div></div>


</div>
