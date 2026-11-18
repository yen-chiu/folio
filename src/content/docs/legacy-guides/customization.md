---
title: 定制
slug: legacy-guides/customization
legacySource: docs/Usage Guidelines/customization.md
legacyUrl: /docs/Usage Guidelines/customization/
sidebar:
  order: 6
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 class="no_toc" id="customization">Customization</h1>

<h2 class="no_toc text-delta" id="table-of-contents">Table of contents</h2>

<ol id="markdown-toc">
  <li><a href="#配色方案" id="markdown-toc-配色方案">配色方案</a>    <ol>
      <li><a href="#示例-预览深色配色方案" id="markdown-toc-示例-预览深色配色方案">示例: 预览深色配色方案</a></li>
    </ol>
  </li>
  <li><a href="#custom-schemes" id="markdown-toc-custom-schemes">Custom schemes</a>    <ol>
      <li><a href="#define-a-custom-scheme" id="markdown-toc-define-a-custom-scheme">Define a custom scheme</a></li>
      <li><a href="#use-a-custom-scheme" id="markdown-toc-use-a-custom-scheme">Use a custom scheme</a></li>
      <li><a href="#switchable-custom-scheme" id="markdown-toc-switchable-custom-scheme">Switchable custom scheme</a></li>
    </ol>
  </li>
  <li><a href="#override-and-define-new-variables" id="markdown-toc-override-and-define-new-variables">Override and define new variables</a></li>
  <li><a href="#override-and-completely-custom-styles" id="markdown-toc-override-and-completely-custom-styles">Override and completely custom styles</a></li>
  <li><a href="#override-includes" id="markdown-toc-override-includes">Override includes</a>    <ol>
      <li><a href="#custom-toc-heading" id="markdown-toc-custom-toc-heading">Custom TOC Heading</a></li>
      <li><a href="#custom-footer" id="markdown-toc-custom-footer">Custom Footer</a></li>
      <li><a href="#custom-head" id="markdown-toc-custom-head">Custom Head</a></li>
      <li><a href="#custom-header" id="markdown-toc-custom-header">Custom Header</a></li>
      <li><a href="#custom-nav-footer" id="markdown-toc-custom-nav-footer">Custom Nav Footer</a></li>
      <li><a href="#custom-search-placeholder" id="markdown-toc-custom-search-placeholder">Custom Search Placeholder</a></li>
    </ol>
  </li>
  <li><a href="#custom-layouts-and-includes" id="markdown-toc-custom-layouts-and-includes">Custom layouts and includes</a>    <ol>
      <li><a href="#default-layout-and-includable-components" id="markdown-toc-default-layout-and-includable-components">Default layout and includable components</a></li>
      <li><a href="#alternative-layouts-and-example-minimal" id="markdown-toc-alternative-layouts-and-example-minimal">Alternative layouts and example (<code class="language-plaintext highlighter-rouge">minimal</code>)</a></li>
      <li><a href="#default-layout-and-inheritance-chain" id="markdown-toc-default-layout-and-inheritance-chain">Default layout and inheritance chain</a></li>
      <li><a href="#overridden-default-jekyll-layouts" id="markdown-toc-overridden-default-jekyll-layouts">Overridden default Jekyll layouts</a></li>
    </ol>
  </li>
</ol>

<hr />

<h2 id="配色方案">配色方案</h2>

<p>Just the Docs 支持两种配色方案: 浅色（默认）和深色。</p>

<p>要启用配色方案，请在站点的 <code class="language-plaintext highlighter-rouge">_config.yml</code> 文件中设置 <code class="language-plaintext highlighter-rouge">color_scheme</code> 参数:</p>

<h3 id="示例-预览深色配色方案">示例: 预览深色配色方案</h3>

<div class="language-yaml no_toc text-delta highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Color scheme supports "light" (default) and "dark"</span>
<span class="na">color_scheme</span><span class="pi">:</span> <span class="s">dark</span>
</code></pre></div></div>

<p><button class="btn js-toggle-dark-mode">Preview dark color scheme</button></p>

<script>
const toggleDarkMode = document.querySelector('.js-toggle-dark-mode');

jtd.addEvent(toggleDarkMode, 'click', function(){
  if (jtd.getTheme() === 'dark') {
    jtd.setTheme('light');
    toggleDarkMode.textContent = 'Preview dark color scheme';
  } else {
    jtd.setTheme('dark');
    toggleDarkMode.textContent = 'Return to the light side';
  }
});
</script>

<h3 class="d-inline-block no_toc" id="deprecated-legacy_light">deprecated: <code class="language-plaintext highlighter-rouge">legacy_light</code></h3>

<p class="label label-green">New (v0.4.2)</p>

<p>In Just the Docs version <code class="language-plaintext highlighter-rouge">0.4.2</code>, we changed the default syntax highlighting theme for the <code class="language-plaintext highlighter-rouge">light</code> color scheme to have higher contrast. Users who want to use the old highlighting need to explicitly opt-in with the deprecated <code class="language-plaintext highlighter-rouge">legacy_light</code> color scheme. In a future major release of Just the Docs, we will remove this color scheme.</p>

<h2 id="custom-schemes">Custom schemes</h2>

<h3 id="define-a-custom-scheme">Define a custom scheme</h3>

<p>You can add custom schemes.
If you want to add a scheme named <code class="language-plaintext highlighter-rouge">foo</code> (can be any name) just add a file <code class="language-plaintext highlighter-rouge">_sass/color_schemes/foo.scss</code> (replace <code class="language-plaintext highlighter-rouge">foo</code> by your scheme name)
where you override theme variables to change colors, fonts, spacing, etc.</p>

<p class="note">Since the default color scheme is <code class="language-plaintext highlighter-rouge">light</code>, your custom scheme is implicitly based on the variable settings used by the <code class="language-plaintext highlighter-rouge">light</code> scheme.</p>

<p>If you want your custom scheme to be based on the <code class="language-plaintext highlighter-rouge">dark</code> scheme, you need to start your file with the following line:</p>

<div class="language-scss highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">@import</span> <span class="s2">"./color_schemes/dark"</span><span class="p">;</span>
</code></pre></div></div>

<p>You can define custom schemes based on other custom schemes in the same way.</p>

<p>Available variables are listed in the <a href="https://github.com/just-the-docs/just-the-docs/tree/main/_sass/support/_variables.scss">_variables.scss</a> file.</p>

<p>For example, to change the link color from the purple default to blue, include the following inside your scheme file:</p>

<h4 class="no_toc text-delta" id="example-custom-link-color">Example: custom link color</h4>

<div class="language-scss highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$link-color</span><span class="p">:</span> <span class="nv">$blue-000</span><span class="p">;</span>
</code></pre></div></div>

<p>Keep in mind that changing a variable will not automatically change the value of other variables that depend on it.
For example, the default link color (<code class="language-plaintext highlighter-rouge">$link-color</code>) is set to <code class="language-plaintext highlighter-rouge">$purple-000</code>. However, redefining <code class="language-plaintext highlighter-rouge">$purple-000</code> in a custom color scheme will not automatically change <code class="language-plaintext highlighter-rouge">$link-color</code> to match it.
Instead, each variable that relies on previously-cascaded values must be manually reimplemented by copying the dependent rules from <code class="language-plaintext highlighter-rouge">_variables.scss</code> — in this case, rewriting <code class="language-plaintext highlighter-rouge">$link-color: $purple-000;</code>.</p>

<p><em>Note:</em> Editing the variables directly in <code class="language-plaintext highlighter-rouge">_sass/support/variables.scss</code> is not recommended and can cause other dependencies to fail.
Please use scheme files.</p>

<h3 id="use-a-custom-scheme">Use a custom scheme</h3>

<p>To use the custom color scheme, only set the <code class="language-plaintext highlighter-rouge">color_scheme</code> parameter in your site’s <code class="language-plaintext highlighter-rouge">_config.yml</code> file:</p>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">color_scheme</span><span class="pi">:</span> <span class="s">foo</span>
</code></pre></div></div>

<h3 id="switchable-custom-scheme">Switchable custom scheme</h3>

<p>If you want to be able to change the scheme dynamically, for example via javascript, just add a file <code class="language-plaintext highlighter-rouge">assets/css/just-the-docs-foo.scss</code> (replace <code class="language-plaintext highlighter-rouge">foo</code> by your scheme name)
with the following content:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>---
---
{% include css/just-the-docs.scss.liquid color_scheme="foo" %}
</code></pre></div></div>

<p>This allows you to switch the scheme via the following javascript.</p>

<div class="language-js highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nx">jtd</span><span class="p">.</span><span class="nf">setTheme</span><span class="p">(</span><span class="dl">"</span><span class="s2">foo</span><span class="dl">"</span><span class="p">)</span>
</code></pre></div></div>

<h2 class="d-inline-block" id="override-and-define-new-variables">Override and define new variables</h2>

<p class="label label-green">New (v0.4.0)</p>

<p>To define new SCSS variables or functions, place SCSS code in <code class="language-plaintext highlighter-rouge">_sass/custom/setup.scss</code>. This should <em>not</em> be used for defining custom styles (see the next section) or overriding color scheme variables (in this case, you should create a new color scheme).</p>

<p>This is most commonly-used to define <a href="/WendellManual/docs/Usage%20Guidelines/configuration/#callouts">custom callout colors</a>. For example,</p>

<div class="language-scss highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1">// _sass/custom/setup.scss</span>
<span class="nv">$pink-000</span><span class="p">:</span> <span class="mh">#f77ef1</span><span class="p">;</span>
<span class="nv">$pink-100</span><span class="p">:</span> <span class="mh">#f967f1</span><span class="p">;</span>
<span class="nv">$pink-200</span><span class="p">:</span> <span class="mh">#e94ee1</span><span class="p">;</span>
<span class="nv">$pink-300</span><span class="p">:</span> <span class="mh">#dd2cd4</span><span class="p">;</span>
</code></pre></div></div>

<p>In particular: this file is imported <em>after</em> the theme’s variables and functions are defined, but <em>before</em> any CSS classes are emitted.</p>

<h2 id="override-and-completely-custom-styles">Override and completely custom styles</h2>

<p>For styles that aren’t defined as SCSS variables, you may want to modify specific CSS classes.
Additionally, you may want to add completely custom CSS specific to your content.
To do this, put your styles in the file <code class="language-plaintext highlighter-rouge">_sass/custom/custom.scss</code>.
This will allow for all overrides to be kept in a single file, and for any upstream changes to still be applied.</p>

<h3 class="no_toc text-delta" id="example-custom-print-styles">Example: custom print styles</h3>

<p>For example, if you’d like to add your own styles for printing a page, you could add the following styles.</p>

<div class="language-scss highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1">// Print-only styles.</span>
<span class="k">@media</span> <span class="n">print</span> <span class="p">{</span>
  <span class="nc">.side-bar</span><span class="o">,</span>
  <span class="nc">.page-header</span> <span class="p">{</span>
    <span class="nl">display</span><span class="p">:</span> <span class="nb">none</span><span class="p">;</span>
  <span class="p">}</span>
  <span class="nc">.main-content</span> <span class="p">{</span>
    <span class="nl">max-width</span><span class="p">:</span> <span class="nb">auto</span><span class="p">;</span>
    <span class="nl">margin</span><span class="p">:</span> <span class="m">1em</span><span class="p">;</span>
  <span class="p">}</span>
<span class="p">}</span>
</code></pre></div></div>

<h2 id="override-includes">Override includes</h2>

<p>You can customize the theme by overriding any of the custom <a href="https://jekyllrb.com/docs/includes/">Jekyll includes</a> files that it provides.</p>

<p>To do this, create an <code class="language-plaintext highlighter-rouge">_includes</code> directory and make a copy of the specific file you wish to modify. The content in this file will override the theme defaults. You can learn more about this process in the Jekyll docs for <a href="https://jekyllrb.com/docs/themes/#overriding-theme-defaults">Overriding theme defaults</a>.</p>

<p>Just the Docs provides the following custom includes files:</p>

<h3 class="d-inline-block" id="custom-toc-heading">Custom TOC Heading</h3>

<p class="label label-green">New (v0.4.0)</p>

<p><code class="language-plaintext highlighter-rouge">_includes/toc_heading_custom.html</code></p>

<p>If the page has any child pages, and <code class="language-plaintext highlighter-rouge">has_toc</code> is not set to <code class="language-plaintext highlighter-rouge">false</code>, this content appears as a heading above the <a href="/WendellManual/docs/Usage%20Guidelines/navigation/children/">auto-generating list of child pages</a> after the page’s content.</p>

<h4 class="no_toc" id="example-changing-toc-heading">Example: changing TOC heading</h4>

<p>To change the default TOC heading to “Contents”, create <code class="language-plaintext highlighter-rouge">_includes/toc_heading_custom.html</code> and add:</p>
<div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nt">&lt;h2</span> <span class="na">class=</span><span class="s">"text-delta"</span><span class="nt">&gt;</span>Contents<span class="nt">&lt;/h2&gt;</span>
</code></pre></div></div>

<p>The (optional) <code class="language-plaintext highlighter-rouge">text-delta</code> class makes the heading appear as <strong class="text-delta">Contents</strong> .</p>

<h3 id="custom-footer">Custom Footer</h3>

<p><code class="language-plaintext highlighter-rouge">_includes/footer_custom.html</code></p>

<p>This content appears at the bottom of every page’s main content. More info for this include can be found in the <a href="/WendellManual/docs/Usage%20Guidelines/configuration/#footer-content">Configuration - Footer content</a>.</p>

<h3 id="custom-head">Custom Head</h3>

<p><code class="language-plaintext highlighter-rouge">_includes/head_custom.html</code></p>

<p>Any HTML added to this file will be inserted before the closing <code class="language-plaintext highlighter-rouge">&lt;head&gt;</code> tag. This might include additional <code class="language-plaintext highlighter-rouge">&lt;meta&gt;</code>, <code class="language-plaintext highlighter-rouge">&lt;link&gt;</code>, or <code class="language-plaintext highlighter-rouge">&lt;script&gt;</code> tags.</p>

<p>The <code class="language-plaintext highlighter-rouge">&lt;head&gt;</code> tag automatically includes a link to an existing favicon if you set <code class="language-plaintext highlighter-rouge">favicon_ico</code> to the corresponding path in your configuration, or if the path to the favicon is <code class="language-plaintext highlighter-rouge">/favicon.ico</code>.</p>

<h3 id="custom-header">Custom Header</h3>

<p><code class="language-plaintext highlighter-rouge">_includes/header_custom.html</code></p>

<p>Content added to this file appears at the top of every page’s main content between the site search and auxiliary links if they are enabled. If <code class="language-plaintext highlighter-rouge">search_enabled</code> were set to false and <code class="language-plaintext highlighter-rouge">aux_links</code> were removed, the content of <code class="language-plaintext highlighter-rouge">header_custom.html</code> would occupy the space at the top of every page.</p>

<h3 class="d-inline-block" id="custom-nav-footer">Custom Nav Footer</h3>

<p class="label label-green">New (v0.4.0)</p>

<p><code class="language-plaintext highlighter-rouge">_includes/nav_footer_custom.html</code></p>

<p>Any content added to this file will appear at the bottom left of the page below the site’s navigation. By default an attribution to Just the Docs is displayed which reads, <code class="language-plaintext highlighter-rouge">This site uses Just the Docs, a documentation theme for Jekyll.</code>.</p>

<h3 class="d-inline-block" id="custom-search-placeholder">Custom Search Placeholder</h3>

<p class="label label-green">New (v0.4.0)</p>

<p><code class="language-plaintext highlighter-rouge">_includes/search_placeholder_custom.html</code></p>

<p>Content added to this file will replace the default placeholder text in the search bar (and its <code class="language-plaintext highlighter-rouge">aria-label</code>), after stripping HTML and leading/trailing whitespace. By default, the content of the include is:</p>

<div class="language-liquid highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Search <span class="cp">{{</span><span class="nv">site</span><span class="p">.</span><span class="nv">title</span><span class="cp">}}</span>
</code></pre></div></div>

<p>Override this file to render a custom placeholder. One common use-case is internationalization; for example,</p>

<div class="language-liquid highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Chercher notre site
</code></pre></div></div>

<p>would make the placeholder text “Chercher notre site”. <a href="https://jekyllrb.com/docs/liquid/">Liquid code</a> (including <a href="https://jekyllrb.com/docs/variables/">Jekyll variables</a>) is also supported.</p>

<h2 class="d-inline-block" id="custom-layouts-and-includes">Custom layouts and includes</h2>

<p class="label label-green">New (v0.4.0)</p>

<p class="label label-yellow">Advanced</p>

<p>Just the Docs uses Jekyll’s powerful <a href="https://jekyllrb.com/docs/layouts/">layouts</a> and <a href="https://jekyllrb.com/docs/includes/">includes</a> features to generate and compose various elements of the site. Jekyll users and developers can extend or replace existing layouts and includes to customize the entire site layout.</p>

<h3 id="default-layout-and-includable-components">Default layout and includable components</h3>

<p>The <code class="language-plaintext highlighter-rouge">default</code> layout is inherited by most of the “out-of-the-box” pages provided by Just the Docs. It composes various re-usable components of the site, including the sidebar, navbar, footer, breadcrumbs, and various imports. Most users who create new pages or layouts will inherit from <code class="language-plaintext highlighter-rouge">default</code>.</p>

<p>Here is a simplified code example of what it looks like:</p>

<div class="language-liquid highlighter-rouge"><div class="highlight"><pre class="highlight"><code>&lt;!-- a simplified version of _layouts/default.html --&gt;
&lt;html&gt;
<span class="cp">{%</span><span class="w"> </span><span class="nt">include</span><span class="w"> </span>head.html<span class="w"> </span><span class="cp">%}</span>
&lt;body&gt;
  <span class="cp">{%</span><span class="w"> </span><span class="nt">include</span><span class="w"> </span>icons/icons.html<span class="w"> </span><span class="cp">%}</span>
  <span class="cp">{%</span><span class="w"> </span><span class="nt">include</span><span class="w"> </span>components/sidebar.html<span class="w"> </span><span class="cp">%}</span>
  <span class="cp">{%</span><span class="w"> </span><span class="nt">include</span><span class="w"> </span>components/header.html<span class="w"> </span><span class="cp">%}</span>
  <span class="cp">{%</span><span class="w"> </span><span class="nt">include</span><span class="w"> </span>components/breadcrumbs.html<span class="w"> </span><span class="cp">%}</span>

  <span class="cp">{%</span><span class="w"> </span><span class="nt">if</span><span class="w"> </span><span class="nv">site</span><span class="p">.</span><span class="nv">heading_anchors</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="kc">false</span><span class="w"> </span><span class="cp">%}</span>
    <span class="cp">{%</span><span class="w"> </span><span class="nt">include</span><span class="w"> </span>vendor/anchor_headings.html<span class="w"> </span><span class="na">html</span><span class="o">=</span><span class="nv">content</span><span class="w"> </span>...<span class="w"> </span><span class="cp">%}</span>
  <span class="cp">{%</span><span class="w"> </span><span class="nt">else</span><span class="w"> </span><span class="cp">%}</span>
    <span class="cp">{{</span><span class="w"> </span><span class="nv">content</span><span class="w"> </span><span class="cp">}}</span>
  <span class="cp">{%</span><span class="w"> </span><span class="nt">endif</span><span class="w"> </span><span class="cp">%}</span>

  <span class="cp">{%</span><span class="w"> </span><span class="nt">if</span><span class="w"> </span><span class="nv">page</span><span class="p">.</span><span class="nv">has_children</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="kc">true</span><span class="w"> </span><span class="ow">and</span><span class="w"> </span><span class="nv">page</span><span class="p">.</span><span class="nv">has_toc</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="kc">false</span><span class="w"> </span><span class="cp">%}</span>
    <span class="cp">{%</span><span class="w"> </span><span class="nt">include</span><span class="w"> </span>components/children_nav.html<span class="w"> </span><span class="cp">%}</span>
  <span class="cp">{%</span><span class="w"> </span><span class="nt">endif</span><span class="w"> </span><span class="cp">%}</span>

  <span class="cp">{%</span><span class="w"> </span><span class="nt">include</span><span class="w"> </span>components/footer.html<span class="w"> </span><span class="cp">%}</span>

  <span class="cp">{%</span><span class="w"> </span><span class="nt">if</span><span class="w"> </span><span class="nv">site</span><span class="p">.</span><span class="nv">search_enabled</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="kc">false</span><span class="w"> </span><span class="cp">%}</span>
    <span class="cp">{%</span><span class="w"> </span><span class="nt">include</span><span class="w"> </span>components/search_footer.html<span class="w"> </span><span class="cp">%}</span>
  <span class="cp">{%</span><span class="w"> </span><span class="nt">endif</span><span class="w"> </span><span class="cp">%}</span>

  <span class="cp">{%</span><span class="w"> </span><span class="nt">if</span><span class="w"> </span><span class="nv">site</span><span class="p">.</span><span class="nv">mermaid</span><span class="w"> </span><span class="cp">%}</span>
    <span class="cp">{%</span><span class="w"> </span><span class="nt">include</span><span class="w"> </span>components/mermaid.html<span class="w"> </span><span class="cp">%}</span>
  <span class="cp">{%</span><span class="w"> </span><span class="nt">endif</span><span class="w"> </span><span class="cp">%}</span>
&lt;/body&gt;
&lt;/html&gt;
</code></pre></div></div>

<h4 class="no_toc" id="component-summary">Component summary</h4>

<p class="warning">Defining a new <code class="language-plaintext highlighter-rouge">_includes</code> with the same name as any of these components will significantly change the existing layout. Please proceed with caution when adjusting them.</p>

<p>To briefly summarize each component:</p>

<ul>
  <li><code class="language-plaintext highlighter-rouge">_includes/head.html</code> is the entire <code class="language-plaintext highlighter-rouge">&lt;head&gt;</code> tag for the site; this imports stylesheets, various JavaScript files (ex: analytics, mermaid, search, and Just the Docs code), and SEO / meta information.</li>
  <li><code class="language-plaintext highlighter-rouge">_includes/icons/icons.html</code> imports all SVG icons that are used throughout the site. Some, such as those relating to search or code snippet copying, are only loaded when those features are enabled.</li>
  <li><code class="language-plaintext highlighter-rouge">_includes/components/sidebar.html</code> renders the sidebar, containing the site header, navigation links, external links, collections, and nav footer.</li>
  <li><code class="language-plaintext highlighter-rouge">_includes/components/header.html</code> renders the navigation header, containing the search bar, custom header, and aux links</li>
  <li><code class="language-plaintext highlighter-rouge">_includes/components/breadcrumbs.html</code> renders the breadcrumbs feature</li>
  <li><code class="language-plaintext highlighter-rouge">vendor/anchor_headings.html</code> is a local copy of Vladimir Jimenez’s <a href="https://github.com/allejo/jekyll-anchor-headings">jekyll-anchor-headings</a> snippet</li>
  <li><code class="language-plaintext highlighter-rouge">_includes/components/children_nav.html</code> renders a list of nav links to child pages on parent pages</li>
  <li><code class="language-plaintext highlighter-rouge">_includes/components/footer.html</code> renders the bottom-of-page footer</li>
  <li><code class="language-plaintext highlighter-rouge">_includes/components/search_footer.html</code> renders DOM elements that are necessary for the search bar to work</li>
  <li><code class="language-plaintext highlighter-rouge">_includes/components/mermaid.html</code> initializes mermaid if the feature is enabled</li>
</ul>

<p>Each of these components can be overridden individually using the same process described in the <a href="#override-includes">Override includes</a> section. In particular, the granularity of components should allow users to replace certain components (such as the sidebar) without having to adjust the rest of the code.</p>

<p>Future versions may subdivide components further; we guarantee that we will only place them in folders (ex <code class="language-plaintext highlighter-rouge">components/</code>, <code class="language-plaintext highlighter-rouge">icons/</code>, or a new <code class="language-plaintext highlighter-rouge">js/</code>) to avoid top-level namespace collisions.</p>

<h3 id="alternative-layouts-and-example-minimal">Alternative layouts and example (<code class="language-plaintext highlighter-rouge">minimal</code>)</h3>

<p>Users can develop custom layouts that compose, omit, or add components differently. We provide one first-class example titled <code class="language-plaintext highlighter-rouge">minimal</code>, which disables the navigation sidebar. To see an example, visit the <a href="/WendellManual/docs/Usage Guidelines/minimal-test/">minimal layout test</a> page.</p>

<p>Users can indicate this alternative layout in page front matter:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>---
layout: minimal
title: Minimal layout test
---
</code></pre></div></div>

<p>Similarly, users and developers can create other alternative layouts using Just the Docs’ reusable includable components.</p>

<h3 id="default-layout-and-inheritance-chain">Default layout and inheritance chain</h3>

<p>Under the hood,</p>

<ul>
  <li><code class="language-plaintext highlighter-rouge">default</code> inherit from the <code class="language-plaintext highlighter-rouge">table_wrappers</code> layout, which wraps all HTML <code class="language-plaintext highlighter-rouge">&lt;table&gt;</code> tags with a <code class="language-plaintext highlighter-rouge">div .table-wrapper</code></li>
  <li><code class="language-plaintext highlighter-rouge">table_wrappers</code> inherits from <code class="language-plaintext highlighter-rouge">vendor/compress</code>, which is a local copy of Anatol Broder’s <a href="https://github.com/penibelst/jekyll-compress-html">jekyll-compress-html</a> Jekyll plugin</li>
</ul>

<p>The <code class="language-plaintext highlighter-rouge">minimal</code> layout inherits from the <code class="language-plaintext highlighter-rouge">default</code> but assigns <code class="language-plaintext highlighter-rouge">nav_enabled: false</code> to disable the navigation sidebar.</p>

<h3 id="overridden-default-jekyll-layouts">Overridden default Jekyll layouts</h3>

<p>By default, Jekyll (and its default theme <code class="language-plaintext highlighter-rouge">minima</code>) provide the <code class="language-plaintext highlighter-rouge">about</code>, <code class="language-plaintext highlighter-rouge">home</code>, <code class="language-plaintext highlighter-rouge">page</code>, and <code class="language-plaintext highlighter-rouge">post</code> layouts. In Just the Docs, we override all of these layouts with the <code class="language-plaintext highlighter-rouge">default</code> layout. Each of those layouts is simply:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>---
layout: default
---

{{ content }}
</code></pre></div></div>



</div>
