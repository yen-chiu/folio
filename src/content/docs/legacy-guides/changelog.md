---
title: 变更日志
slug: legacy-guides/changelog
legacySource: CHANGELOG.md
legacyUrl: /CHANGELOG/
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 id="changelog">CHANGELOG</h1>

<p>All notable user-facing changes to this project are documented in this file.</p>

<p class="highlight">The project underwent a major maintenance shift in March 2022.</p>

<h2 id="head">HEAD</h2>

<p class="note">This website is built from the <code class="language-plaintext highlighter-rouge">HEAD</code> of the <code class="language-plaintext highlighter-rouge">main</code> branch of the theme repository.</p>

<p>Code changes to <code class="language-plaintext highlighter-rouge">main</code> that are <em>not</em> in the latest release:</p>

<ul>
  <li>N/A</li>
</ul>

<p>Docs changes made since the latest release:</p>

<ul>
  <li>N/A</li>
</ul>

<h2 id="release-v0100">Release v0.10.0</h2>

<p>Hi folks! This minor release adds one of our most-requested features: unlimited multi-level navigation (also known as recursive navigation). Huge thanks to <a href="https://github.com/pdmosses">@pdmosses</a> for his wonderful work in implementing this feature!</p>

<p>This release should be a straightforward upgrade for all users of Just the Docs. Thank you for your continued support!</p>

<h3 id="using-release-v0100">Using Release <code class="language-plaintext highlighter-rouge">v0.10.0</code></h3>

<p>Users who have not pinned the theme version will be <strong>automatically upgraded to <code class="language-plaintext highlighter-rouge">v0.9.0</code> the next time they build their site</strong>.</p>

<p>To use this release explicitly as a remote theme:</p>

<div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.10.0</span>
</code></pre></div></div>

<p>To use this version explicitly as a gem-based theme, pin the version in your <code class="language-plaintext highlighter-rouge">Gemfile</code> and re-run <code class="language-plaintext highlighter-rouge">bundle install</code> or <code class="language-plaintext highlighter-rouge">bundle update just-the-docs</code>:</p>

<div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.10.0"</span>
</code></pre></div></div>

<p>To use and pin a previous version of the theme, replace the <code class="language-plaintext highlighter-rouge">0.10.0</code> with the desired release tag.</p>

<h3 id="new-features">New Features</h3>

<ul>
  <li>Added: Allow unlimited multi-level navigation by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1431">#1431</a></li>
</ul>

<h3 id="documentation">Documentation</h3>

<ul>
  <li>Added: Allow unlimited multi-level navigation by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1440">#1440</a></li>
  <li>Added: sitemap (via <code class="language-plaintext highlighter-rouge">jekyll-sitemap</code> plugin) by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1531">#1530</a></li>
  <li>Fixed: (non-systemic) accessibility issues flagged by aXe by <a href="https://github.com/mattxwang">@mattxwang</a> in [#1531]</li>
</ul>

<h2 id="release-v090">Release v0.9.0</h2>

<p>Hi folks! This minor release adds a <code class="language-plaintext highlighter-rouge">nav_enabled</code> set of variables to enable/disable the navigation at a site, layout, and page level — and uses that to add search and auxilary links to the <code class="language-plaintext highlighter-rouge">minimal</code> layout. In addition, it fixes <code class="language-plaintext highlighter-rouge">search-data.json</code> corruption with default layouts and some minor CSS/SCSS issues.</p>

<p>This release should be a straightforward upgrade for all users of Just the Docs. Thank you for your continued support!</p>

<h3 id="using-release-v090">Using Release <code class="language-plaintext highlighter-rouge">v0.9.0</code></h3>

<p>Users who have not pinned the theme version will be <strong>automatically upgraded to <code class="language-plaintext highlighter-rouge">v0.9.0</code> the next time they build their site</strong>.</p>

<p>To use this release explicitly as a remote theme:</p>

<div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.9.0</span>
</code></pre></div></div>

<p>To use this version explicitly as a gem-based theme, pin the version in your <code class="language-plaintext highlighter-rouge">Gemfile</code> and re-run <code class="language-plaintext highlighter-rouge">bundle install</code> or <code class="language-plaintext highlighter-rouge">bundle update just-the-docs</code>:</p>

<div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.9.0"</span>
</code></pre></div></div>

<p>To use and pin a previous version of the theme, replace the <code class="language-plaintext highlighter-rouge">0.9.0</code> with the desired release tag.</p>

<h3 id="new-features-1">New Features</h3>

<ul>
  <li>Added: <code class="language-plaintext highlighter-rouge">nav_enabled</code> site, layout, and page-level variable to selectively show or hide the side/mobile menu by <a href="https://github.com/kevinlin1">@kevinlin1</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1441">#1441</a></li>
  <li>Added: site-wide search bar and auxiliary links to the <code class="language-plaintext highlighter-rouge">minimal</code> layout by <a href="https://github.com/kevinlin1">@kevinlin1</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1441">#1441</a></li>
</ul>

<h3 id="bugfixes">Bugfixes</h3>

<ul>
  <li>Fixed: protect <code class="language-plaintext highlighter-rouge">search-data.json</code> file from front matter default for layout by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1468">#1468</a></li>
  <li>Fixed: Sass mixed declarations by <a href="https://github.com/bobvandevijver">@bobvandevijver</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1495">#1495</a></li>
  <li>Fixed: redundant <code class="language-plaintext highlighter-rouge">monospace</code> in <code class="language-plaintext highlighter-rouge">pre</code>, <code class="language-plaintext highlighter-rouge">code</code>, <code class="language-plaintext highlighter-rouge">kbd</code>, <code class="language-plaintext highlighter-rouge">samp</code> reset by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1508">#1508</a></li>
</ul>

<h3 id="documentation-1">Documentation</h3>

<ul>
  <li>Docs: Explained the <code class="language-plaintext highlighter-rouge">nav_enabled</code> variables as an alternative to using the minimal layout <a href="https://github.com/kevinlin1">@kevinlin1</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1441">#1441</a>.</li>
</ul>

<h3 id="new-contributors">New Contributors</h3>

<ul>
  <li><a href="https://github.com/bobvandevijver">@bobvandevijver</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1495">#1495</a></li>
</ul>

<h2 id="release-v082">Release v0.8.2</h2>

<p>Hi everyone! This patch release fixes a bug where a default layout with unrestricted <code class="language-plaintext highlighter-rouge">scope</code> (<code class="language-plaintext highlighter-rouge">path: ""</code>) breaks JavaScript functionality. Users who do not use a default layout with unrestricted <code class="language-plaintext highlighter-rouge">scope</code> should not be affected. This should be a straightforward upgrade for all users. Thank you to <a href="https://github.com/pdmosses">@pdmosses</a> for triaging and fixing the bug!</p>

<h3 id="bugfixes-1">Bugfixes</h3>

<ul>
  <li>Fixed: Protect theme JS file from front matter default for layout by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1447">#1447</a></li>
</ul>

<h2 id="release-v081">Release v0.8.1</h2>

<p>Hi folks! This patch release fixes a bug introduced in <code class="language-plaintext highlighter-rouge">0.8.0</code> that affects users who build their sites in strict mode. It is a straightforward upgrade that should require no manual migration changes. Thank you to <a href="https://github.com/Zarthus">@Zarthus</a> for quickly catching and fixing this bug!</p>

<h3 id="bugfixes-2">Bugfixes</h3>

<ul>
  <li>Fixed: Liquid filter typo in breadcrumb component (<code class="language-plaintext highlighter-rouge">strip</code> instead of <code class="language-plaintext highlighter-rouge">trim</code>) by <a href="https://github.com/Zarthus">@Zarthus</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1434">#1434</a></li>
</ul>

<h3 id="documentation-2">Documentation</h3>

<ul>
  <li>Build docs site using strict mode and <code class="language-plaintext highlighter-rouge">strict_filters</code> by <a href="https://github.com/Zarthus">@Zarthus</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1435">#1435</a></li>
</ul>

<h3 id="new-contributors-1">New Contributors</h3>

<ul>
  <li><a href="https://github.com/Zarthus">@Zarthus</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1434">#1434</a></li>
</ul>

<h2 id="release-v080">Release v0.8.0</h2>

<p>Hi folks! This first minor release of 2024 has a short number of changes: a large improvement of build times for large sites, a new keyboard shortcut to focus the search bar, and sidebar navigation bugfixes for “pretty” URLs (with <code class="language-plaintext highlighter-rouge">.html</code> omitted) and the clickable area on Safari. This release has no explicit breaking changes and should be a straightforward upgrade for most (if not all) users.</p>

<h3 id="using-release-v080">Using Release <code class="language-plaintext highlighter-rouge">v0.8.0</code></h3>

<p>Users who have not pinned the theme version will be <strong>automatically upgraded to <code class="language-plaintext highlighter-rouge">v0.8.0</code> the next time they build their site</strong>.</p>

<p>To use this release explicitly as a remote theme:</p>

<div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.8.0</span>
</code></pre></div></div>

<p>To use this version explicitly as a gem-based theme, pin the version in your <code class="language-plaintext highlighter-rouge">Gemfile</code> and re-run <code class="language-plaintext highlighter-rouge">bundle install</code> or <code class="language-plaintext highlighter-rouge">bundle update just-the-docs</code>:</p>

<div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.8.0"</span>
</code></pre></div></div>

<p>To use and pin a previous version of the theme, replace the <code class="language-plaintext highlighter-rouge">0.8.0</code> with the desired release tag.</p>

<h3 id="new-features-2">New Features</h3>

<ul>
  <li>Added: configurable keyboard shortcut to focus search input by <a href="https://github.com/kcromanpl-bajra">@kcromanpl-bajra</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1411">#1411</a></li>
</ul>

<h3 id="bugfixes-3">Bugfixes</h3>

<ul>
  <li>Fixed: quicker build by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1397">#1397</a></li>
  <li>Fixed: incorrect navigation when <code class="language-plaintext highlighter-rouge">.html</code> omitted from URL by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1374">#1374</a></li>
  <li>Fixed: incorrect positioning of clickable area for navigation links on Safari by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1403">#1403</a></li>
</ul>

<h3 id="documentation-3">Documentation</h3>

<ul>
  <li>Add documentation to “Navigation Structure” on grouping pages with collections by <a href="https://github.com/mitchnemirov">@mitchnemirov</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1390">#1390</a></li>
</ul>

<h3 id="new-contributors-2">New Contributors</h3>

<ul>
  <li><a href="https://github.com/mitchnemirov">@mitchnemirov</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1390">#1390</a></li>
  <li><a href="https://github.com/kcromanpl-bajra">@kcromanpl-bajra</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1411">#1411</a></li>
</ul>

<h2 id="release-v070">Release v0.7.0</h2>

<p>Hi folks! This is a minor release that adds a new configuration option for opening external links in a new tab and provides many bugfixes (in both correctness and performance) for Just the Docs users with large sites. We anticipate that for most users, this is a straightforward upgrade. However, it introduces some potentially-breaking <em>internal</em> changes to undocumented features of the theme.</p>

<h3 id="migrating-to-v070">Migrating to <code class="language-plaintext highlighter-rouge">v0.7.0</code></h3>

<p><strong>Migration</strong>: users will need to migrate if:</p>

<ul>
  <li>they overrode <code class="language-plaintext highlighter-rouge">_includes/nav.html</code>, which has moved to <code class="language-plaintext highlighter-rouge">_includes/components/nav.html</code></li>
  <li>they have an element with the IDs <code class="language-plaintext highlighter-rouge">jtd-nav-activation</code> or <code class="language-plaintext highlighter-rouge">jtd-head-nav-stylesheet</code></li>
</ul>

<p>For more, refer to the <a href="https://just-the-docs.com/MIGRATION/">migration guide</a>.</p>

<h3 id="using-release-v070">Using Release <code class="language-plaintext highlighter-rouge">v0.7.0</code></h3>

<p>Users who have not pinned the theme version will be <strong>automatically upgraded to <code class="language-plaintext highlighter-rouge">v0.7.0</code> the next time they build their site</strong>.</p>

<p>To use this release explicitly as a remote theme:</p>

<div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.7.0</span>
</code></pre></div></div>

<p>To use this version explicitly as a gem-based theme, pin the version in your <code class="language-plaintext highlighter-rouge">Gemfile</code> and re-run <code class="language-plaintext highlighter-rouge">bundle install</code> or <code class="language-plaintext highlighter-rouge">bundle update just-the-docs</code>:</p>

<div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.7.0"</span>
</code></pre></div></div>

<p>To use and pin a previous version of the theme, replace the <code class="language-plaintext highlighter-rouge">0.7.0</code> with the desired release tag.</p>

<h3 id="new-features-3">New Features</h3>

<ul>
  <li>Added: configuration options for opening external links in new tab by <a href="https://github.com/CarbonNeuron">@CarbonNeuron</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1360">#1360</a></li>
</ul>

<h3 id="bugfixes-4">Bugfixes</h3>

<ul>
  <li>Fixed: remove href from the navigation link to the current page by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1356">#1356</a></li>
  <li>Fixed: improve build time by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1358">#1358</a></li>
  <li>Fixed: erroneous parentheses in <code class="language-plaintext highlighter-rouge">site_nav</code> conditional by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1366">#1366</a></li>
  <li>Fixed: navigation scroll to active link regression by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1367">#1367</a></li>
  <li>Fixed: invalid CSS rules in head elements by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1368">#1368</a></li>
  <li>Fixed: accidental disabling of forward-declared stylesheets by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1373">#1373</a></li>
</ul>

<p class="warning"><a href="https://github.com/just-the-docs/just-the-docs/pull/1358">#1358</a> moved <code class="language-plaintext highlighter-rouge">_includes/nav.html</code> to the <code class="language-plaintext highlighter-rouge">_includes/components</code> directory,
Users who were overriding that file will need to adjust their sites accordingly.</p>

<h3 id="documentation-4">Documentation:</h3>

<ul>
  <li>Docs: fix typos in <code class="language-plaintext highlighter-rouge">CHANGELOG</code> and <code class="language-plaintext highlighter-rouge">MIGRATION</code> by <a href="https://github.com/thapasusheel">@thapasusheel</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1377">#1377</a></li>
</ul>

<h3 id="new-contributors-3">New Contributors</h3>

<ul>
  <li><a href="https://github.com/CarbonNeuron">@CarbonNeuron</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1360">#1360</a></li>
  <li><a href="https://github.com/thapasusheel">@thapasusheel</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1377">#1377</a></li>
</ul>

<h2 id="release-v062">Release v0.6.2</h2>

<p>Hi all, this is a small patch release that includes two changes: adding a missing Windows emoji font fallback, and removing some (now-unused) code introduced in 0.6.</p>

<h3 id="bugfixes-5">Bugfixes</h3>

<ul>
  <li>Fixed: Windows emoji font fallback by <a href="https://github.com/flanakin">@flanakin</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1337">#1337</a></li>
  <li>Removed: unused <code class="language-plaintext highlighter-rouge">.passive</code> toggle in navigation by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1335">#1335</a></li>
</ul>

<h3 id="new-contributors-4">New Contributors</h3>

<ul>
  <li><a href="https://github.com/flanakin">@flanakin</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1337">#1337</a></li>
</ul>

<h2 id="release-v061">Release v0.6.1</h2>

<p>Hi all, this is a small patch release that only includes one change: resolving a bug introduced in 0.6.0 that causes a JS error for pages excluded from navigation.</p>

<h3 id="bugfixes-6">Bugfixes</h3>

<ul>
  <li>Fixed: JS error for pages excluded from navigation by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1332">#1332</a></li>
</ul>

<h2 id="release-v060">Release v0.6.0</h2>

<p>Hi all, this is a minor release that introduces performance improvements for build times on large sites, correctly sets the <code class="language-plaintext highlighter-rouge">color-scheme</code> property, and fixes invalid HTML. However, it introduces some potentially-breaking <em>internal</em> changes to undocumented features of the theme.</p>

<h3 id="migrating-to-v060">Migrating to <code class="language-plaintext highlighter-rouge">v0.6.0</code></h3>

<p><strong>Migration</strong>: users will need to migrate if:</p>

<ul>
  <li>they have an existing <code class="language-plaintext highlighter-rouge">_includes</code> file named <code class="language-plaintext highlighter-rouge">favicon.html</code>, <code class="language-plaintext highlighter-rouge">head_nav.html</code>, or <code class="language-plaintext highlighter-rouge">css/activation.scss.liquid</code></li>
  <li>they have code that refers to <code class="language-plaintext highlighter-rouge">#main-content-wrap</code></li>
  <li>they override the default <code class="language-plaintext highlighter-rouge">light</code> theme’s code, or the theme-loading logic</li>
  <li>they have different favicons for different pages</li>
</ul>

<p>For more, refer to the <a href="https://just-the-docs.com/MIGRATION/">migration guide</a>.</p>

<h3 id="using-release-v060">Using Release <code class="language-plaintext highlighter-rouge">v0.6.0</code></h3>

<p>Users who have not pinned the theme version will be <strong>automatically upgraded to <code class="language-plaintext highlighter-rouge">v0.6.0</code> the next time they build their site</strong>.</p>

<p>To use this release explicitly as a remote theme:</p>

<div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.6.0</span>
</code></pre></div></div>

<p>To use this version explicitly as a gem-based theme, pin the version in your <code class="language-plaintext highlighter-rouge">Gemfile</code> and re-run <code class="language-plaintext highlighter-rouge">bundle install</code> or <code class="language-plaintext highlighter-rouge">bundle update just-the-docs</code>:</p>

<div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.6.0"</span>
</code></pre></div></div>

<p>To use and pin a previous version of the theme, replace the <code class="language-plaintext highlighter-rouge">0.6.0</code> with the desired release tag.</p>

<h3 id="new-features-and-bugfixes">New Features and Bugfixes</h3>

<ul>
  <li>Added: <code class="language-plaintext highlighter-rouge">$color-scheme</code> theme variable to specify <code class="language-plaintext highlighter-rouge">color-scheme</code> for <code class="language-plaintext highlighter-rouge">:root</code> by <a href="https://github.com/sigv">@sigv</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1280">#1280</a></li>
  <li>Fixed: build times for large sites by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1244">#1244</a></li>
  <li>Fixed: missing closing <code class="language-plaintext highlighter-rouge">&lt;/button&gt;</code> tag in <code class="language-plaintext highlighter-rouge">sidebar.html</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1304">#1304</a></li>
  <li>Fixed: removed duplicate <code class="language-plaintext highlighter-rouge">#main-content-wrap</code> minimal and default layouts by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1305">#1305</a></li>
</ul>

<h3 id="documentation-5">Documentation</h3>

<p class="warning">The theme docs are unversioned, and already reflect the above changes.</p>

<p>Docs changes:</p>

<ul>
  <li>A <a href="/WendellManual/docs/Usage%20Guidelines/configuration/#fn:js-disabled">footnote</a> in the configuration docs explains how disabling JavaScript affects the display of navigation links when browsing folded collections.</li>
  <li>Invalid HTML has been removed from most documentation examples.</li>
</ul>

<h3 id="new-contributors-5">New Contributors</h3>

<ul>
  <li><a href="https://github.com/sigv">@sigv</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1280">#1280</a></li>
</ul>

<h2 id="release-v054">Release v0.5.4</h2>

<p>Hi all, this is a small patch release that only includes one change: fixing a style clash between Mermaid’s labels and Just the Docs’ labels.</p>

<p><em>Note: for subsequent patch releases, we will omit migration instructions (for brevity). In all cases, immediate migration should be backwards-compatible. Refer to previous major or minor update instructions for more information.</em></p>

<h3 id="bugfixes-7">Bugfixes</h3>

<ul>
  <li>Fixed: Mermaid labels inheriting theme <code class="language-plaintext highlighter-rouge">.label</code> styling by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1278">#1278</a></li>
</ul>

<h2 id="release-v053">Release v0.5.3</h2>

<p>Hi all, this is a minor patch release that only includes one change: changing all text-based CSS properties to use <code class="language-plaintext highlighter-rouge">rem</code> instead of hard-coded <code class="language-plaintext highlighter-rouge">px</code> values. This has two effects:</p>

<ol>
  <li>All deprecation warnings are now fixed on build; you should now get a clean build with <code class="language-plaintext highlighter-rouge">jekyll build</code>.</li>
  <li>We have <strong>deprecated the <code class="language-plaintext highlighter-rouge">$root-font-size</code> SCSS variable</strong>. We will remove it in an upcoming release of the theme.</li>
</ol>

<p>If you use the stock Just the Docs theme, this release should have no impact on your final built site. If you change the <code class="language-plaintext highlighter-rouge">$root-font-size</code> SCSS variable, you might experience light layout shifts.</p>

<h3 id="using-release-v053">Using Release <code class="language-plaintext highlighter-rouge">v0.5.3</code></h3>

<p>Users who have not pinned the theme version will be <strong>automatically upgraded to <code class="language-plaintext highlighter-rouge">v0.5.3</code> the next time they build their site</strong>.</p>

<p>To use this release explicitly as a remote theme:</p>

<div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.5.3</span>
</code></pre></div></div>

<p>To use this version explicitly as a gem-based theme, pin the version in your <code class="language-plaintext highlighter-rouge">Gemfile</code> and re-run <code class="language-plaintext highlighter-rouge">bundle install</code> or <code class="language-plaintext highlighter-rouge">bundle update just-the-docs</code>:</p>

<div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.5.3"</span>
</code></pre></div></div>

<p>To use and pin a previous version of the theme, replace the <code class="language-plaintext highlighter-rouge">0.5.3</code> with the desired release tag.</p>

<h3 id="bugfixes-8">Bugfixes</h3>

<ul>
  <li>Fixed: font-size scaling for text-related CSS properties by using <code class="language-plaintext highlighter-rouge">rem</code> instead of fixed <code class="language-plaintext highlighter-rouge">px</code> values; deprecate <code class="language-plaintext highlighter-rouge">$root-font-size</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1169">#1169</a></li>
</ul>

<h2 id="release-v052">Release v0.5.2</h2>

<p>Hi all, this is a minor patch release that mostly focuses on accessibility. Since we follow semantic versioning, this should be a smooth upgrade with no breaking changes.</p>

<p>In addition, the theme docs website has a new canonical URL: <a href="https://just-the-docs.com">https://just-the-docs.com</a>. We’ve also retroactively published the theme docs website for version <code class="language-plaintext highlighter-rouge">v0.3.3</code> at <a href="https://v0-3-3-docs.just-the-docs.com/">https://v0-3-3-docs.just-the-docs.com/</a>. Thank you to our GitHub sponsors for funding our domain name!</p>

<h3 id="using-release-v052">Using Release <code class="language-plaintext highlighter-rouge">v0.5.2</code></h3>

<p>Users who have not pinned the theme version will be <strong>automatically upgraded to <code class="language-plaintext highlighter-rouge">v0.5.2</code> the next time they build their site</strong>.</p>

<p>To use this release explicitly as a remote theme:</p>

<div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.5.2</span>
</code></pre></div></div>

<p>To use this version explicitly as a gem-based theme, pin the version in your <code class="language-plaintext highlighter-rouge">Gemfile</code> and re-run <code class="language-plaintext highlighter-rouge">bundle install</code> or <code class="language-plaintext highlighter-rouge">bundle update just-the-docs</code>:</p>

<div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.5.2"</span>
</code></pre></div></div>

<p>To use and pin a previous version of the theme, replace the <code class="language-plaintext highlighter-rouge">0.5.2</code> with the desired release tag.</p>

<h3 id="bugfixes-9">Bugfixes</h3>

<ul>
  <li>Fixed: liquid variable leakage in navigation components by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1243">#1243</a></li>
  <li>Fixed: ARIA roles and labels for search, header, logo, mobile menu button, and main content by <a href="https://github.com/joelhawksley">@joelhawksley</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1259">#1259</a></li>
  <li>Fixed: ARIA labels for all anchors with <code class="language-plaintext highlighter-rouge">href="#"</code>; adds <code class="language-plaintext highlighter-rouge">aria-pressed</code> information for toggles by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1262">#1262</a></li>
</ul>

<h3 id="new-contributors-6">New Contributors</h3>

<ul>
  <li><a href="https://github.com/joelhawksley">@joelhawksley</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1259">#1259</a></li>
</ul>

<h2 id="release-v051">Release v0.5.1</h2>

<p>Hi all, this is a very small minor patch release that has two small behavioral bugfixes: fixing a regression introduced in <code class="language-plaintext highlighter-rouge">v0.5.0</code> on Safari versions <code class="language-plaintext highlighter-rouge">&lt;16.4</code> (broken media query), and the copy code button providing incorrect feedback in insecure browser contexts. This should be a smooth upgrade with no breaking changes.</p>

<p>As always, we’d love your feedback. <a href="https://github.com/just-the-docs/just-the-docs/issues">Open an issue</a> or <a href="https://github.com/just-the-docs/just-the-docs/discussions">start a discussion</a> for bug reports, feature requests, and any other feedback. Thanks for continuing to use Just the Docs!</p>

<h3 id="using-release-v051">Using Release <code class="language-plaintext highlighter-rouge">v0.5.1</code></h3>

<p>Users who have not pinned the theme version will be <strong>automatically upgraded to <code class="language-plaintext highlighter-rouge">v0.5.1</code> the next time they build their site</strong>.</p>

<p>To use this release explicitly as a remote theme:</p>

<div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.5.1</span>
</code></pre></div></div>

<p>To use this version explicitly as a gem-based theme, pin the version in your <code class="language-plaintext highlighter-rouge">Gemfile</code> and re-run <code class="language-plaintext highlighter-rouge">bundle install</code> or <code class="language-plaintext highlighter-rouge">bundle update just-the-docs</code>:</p>

<div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.5.1"</span>
</code></pre></div></div>

<p>To use and pin a previous version of the theme, replace the <code class="language-plaintext highlighter-rouge">0.5.1</code> with the desired release tag.</p>

<h3 id="bugfixes-10">Bugfixes</h3>

<ul>
  <li>Fixed: disable copy code button in insecure contexts <a href="https://github.com/rmoff">@rmoff</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1226">#1226</a></li>
  <li>Fixed: context-based media feature not supported by Safari <code class="language-plaintext highlighter-rouge">&lt;16.4</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1240">#1240</a></li>
</ul>

<h3 id="documentation-6">Documentation</h3>

<ul>
  <li>Added: document copy code button requiring secure context by <a href="https://github.com/rmoff">@rmoff</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1225">#1225</a></li>
  <li>Fixed: typo (“them” → “theme”) in MIGRATION.md by <a href="https://github.com/waldyrious">@waldyrious</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1219">#1219</a></li>
  <li>Fixed: <code class="language-plaintext highlighter-rouge">font-weight</code> typo (Utilities &gt; Typography) by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1229">#1229</a></li>
  <li>Fixed: <code class="language-plaintext highlighter-rouge">just the docs</code> typo in migration guide by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1230">#1230</a></li>
</ul>

<h3 id="new-contributors-7">New Contributors</h3>
<ul>
  <li><a href="https://github.com/rmoff">@rmoff</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1225">#1225</a></li>
</ul>

<h2 id="release-v050">Release v0.5.0</h2>

<p>Hope your April is going well! This new release of Just the Docs is relatively minor. It has one <strong>breaking change</strong>: we’ve reverted the import order of <code class="language-plaintext highlighter-rouge">setup.scss</code> to be <em>before</em> color schemes. In addition, we include two requested fixes: color contrast issues with <code class="language-plaintext highlighter-rouge">::selection</code> and using Just the Docs with mermaid versions <code class="language-plaintext highlighter-rouge">&gt;=10</code>.</p>

<p>We’ve marked this as a minor version bump due to the breaking change. In the next section, we briefly outline what migration steps should be. Users who did not migrate to <code class="language-plaintext highlighter-rouge">v0.4.2</code> or who do not have a custom <code class="language-plaintext highlighter-rouge">setup.scss</code> are guaranteed no breaking changes.</p>

<p>As always, we’d love your feedback. <a href="https://github.com/just-the-docs/just-the-docs/issues">Open an issue</a> or <a href="https://github.com/just-the-docs/just-the-docs/discussions">start a discussion</a> for bug reports, feature requests, and any other feedback. Thanks for continuing to use Just the Docs!</p>

<h3 id="migrating-to-v050">Migrating to <code class="language-plaintext highlighter-rouge">v0.5.0</code></h3>

<p><strong>Migration</strong>: users with a custom <code class="language-plaintext highlighter-rouge">setup.scss</code> cannot rely on variables or functions defined in <code class="language-plaintext highlighter-rouge">color_scheme</code>. This reverts to the behaviour in <code class="language-plaintext highlighter-rouge">v0.4.1</code>. Users should instead move those variables or functions to the <code class="language-plaintext highlighter-rouge">color_scheme</code> files themselves.</p>

<p>For more, refer to the <a href="https://just-the-docs.com/MIGRATION/">migration guide</a>.</p>

<h3 id="using-release-v050">Using Release <code class="language-plaintext highlighter-rouge">v0.5.0</code></h3>

<p>Users who have not pinned the theme version will be <strong>automatically upgraded to <code class="language-plaintext highlighter-rouge">v0.5.0</code> the next time they build their site</strong>.</p>

<p>To use this release explicitly as a remote theme:</p>

<div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.5.0</span>
</code></pre></div></div>

<p>To use this version explicitly as a gem-based theme, pin the version in your <code class="language-plaintext highlighter-rouge">Gemfile</code> and re-run <code class="language-plaintext highlighter-rouge">bundle install</code> or <code class="language-plaintext highlighter-rouge">bundle update just-the-docs</code>:</p>

<div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.5.0"</span>
</code></pre></div></div>

<p>To use and pin a previous version of the theme, replace the <code class="language-plaintext highlighter-rouge">0.5.0</code> with the desired release tag.</p>

<h3 id="bugfixes-11">Bugfixes</h3>

<ul>
  <li><strong>Reverted (breaking)</strong>: “Fix import order for <code class="language-plaintext highlighter-rouge">setup.scss</code> (#1184)” by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1209">#1209</a></li>
  <li>Fixed: color contrast issues with <code class="language-plaintext highlighter-rouge">::selection</code> (reverting to browser defaults) <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1208">#1208</a></li>
  <li>Fixed: mermaid <code class="language-plaintext highlighter-rouge">v10</code>, bundle all mermaid code in component by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1190">#1190</a></li>
  <li>Removed: unused images (<code class="language-plaintext highlighter-rouge">just-the-docs.png</code>, <code class="language-plaintext highlighter-rouge">search.svg</code>) by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1107">#1107</a></li>
  <li>Removed: <code class="language-plaintext highlighter-rouge">CODE_OF_CONDUCT</code>, <code class="language-plaintext highlighter-rouge">docker-compose</code>, and <code class="language-plaintext highlighter-rouge">Dockerfile</code> files from site by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1187">#1187</a></li>
</ul>

<p><strong>Full Changelog</strong>: <a href="https://github.com/just-the-docs/just-the-docs/compare/v0.4.2...v0.5.0">https://github.com/just-the-docs/just-the-docs/compare/v0.4.2…v0.5.0</a></p>

<h2 id="release-v042">Release v0.4.2</h2>

<p>Hello! We’re back again with another small release. Like <code class="language-plaintext highlighter-rouge">v0.4.1</code>, this release is a <a href="https://semver.org/">semver patch</a>: it only includes bugfixes, and is fully backwards-compatible.</p>

<p>The big highlight of this theme is fixing our light scheme code highlighting contrast issues; this was one of our most-requested features! This change is fully backwards-compatible; users can <a href="https://just-the-docs.com/docs/customization/#deprecated-legacy_light">opt-in to our old highlighting theme</a> by using <code class="language-plaintext highlighter-rouge">legacy_light</code> instead of <code class="language-plaintext highlighter-rouge">light</code>.</p>

<p>As always, we’d love your feedback. <a href="https://github.com/just-the-docs/just-the-docs/issues">Open an issue</a> or <a href="https://github.com/just-the-docs/just-the-docs/discussions">start a discussion</a> for bug reports, feature requests, and any other feedback. Thanks for continuing to use Just the Docs!</p>

<h3 id="using-release-v042">Using Release <code class="language-plaintext highlighter-rouge">v0.4.2</code></h3>

<p>Users who have not pinned the theme version will be <strong>automatically upgraded to <code class="language-plaintext highlighter-rouge">v0.4.2</code> the next time they build their site</strong>.</p>

<p>To use this release explicitly as a remote theme:</p>

<div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.4.2</span>
</code></pre></div></div>

<p>To use this RC explicitly as a gem-based theme, pin the version in your <code class="language-plaintext highlighter-rouge">Gemfile</code> and re-run <code class="language-plaintext highlighter-rouge">bundle install</code> or <code class="language-plaintext highlighter-rouge">bundle update just-the-docs</code>:</p>

<div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.4.2"</span>
</code></pre></div></div>

<p>To use and pin a previous version of the theme, replace the <code class="language-plaintext highlighter-rouge">0.4.2</code> with the desired release tag.</p>

<h3 id="bugfixes-12">Bugfixes</h3>

<ul>
  <li>Fixed: light scheme code highlighting contrast issues; updated to use Atom’s One Light colors, consolidate theme variables by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1166">#1166</a></li>
  <li>Fixed: duplicate import of <code class="language-plaintext highlighter-rouge">color_schemes</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1173">#1173</a></li>
  <li>Fixed: import order for <code class="language-plaintext highlighter-rouge">setup.scss</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1184">#1184</a></li>
  <li>Removed: unused dark syntax themes by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1192">#1192</a></li>
</ul>

<h3 id="documentation-7">Documentation</h3>

<ul>
  <li>Added: docs for using mermaid with AsciiDoc by <a href="https://github.com/flyx">@flyx</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1182">#1182</a></li>
</ul>

<p><strong>Full Changelog</strong>: <a href="https://github.com/just-the-docs/just-the-docs/compare/v0.4.1...v0.4.2">https://github.com/just-the-docs/just-the-docs/compare/v0.4.1…v0.4.2</a></p>

<h2 id="release-v041">Release v0.4.1</h2>

<p>Hello! We hope you’ve been enjoying the new <code class="language-plaintext highlighter-rouge">v0.4.0</code>; we appreciate all the feedback we’ve gotten already! As promised, future releases will be small with simple steps to upgrade. This is one of them! <code class="language-plaintext highlighter-rouge">v0.4.1</code> is a <a href="https://semver.org/">semver patch</a>: it only includes bugfixes, and is fully backwards-compatible.</p>

<p>As always, we’d love your feedback. <a href="https://github.com/just-the-docs/just-the-docs/issues">Open an issue</a> or <a href="https://github.com/just-the-docs/just-the-docs/discussions">start a discussion</a> for bug reports, feature requests, and any other feedback. Thanks for continuing to use Just the Docs!</p>

<h3 id="using-release-v041">Using Release <code class="language-plaintext highlighter-rouge">v0.4.1</code></h3>

<p>Users who have not pinned the theme version will be <strong>automatically upgraded to <code class="language-plaintext highlighter-rouge">v0.4.1</code> the next time they build their site</strong>.</p>

<p>To use this release explicitly as a remote theme:</p>

<div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.4.1</span>
</code></pre></div></div>

<p>To use this RC explicitly as a gem-based theme, pin the version in your <code class="language-plaintext highlighter-rouge">Gemfile</code> and re-run <code class="language-plaintext highlighter-rouge">bundle install</code> or <code class="language-plaintext highlighter-rouge">bundle update just-the-docs</code>:</p>

<div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.4.1"</span>
</code></pre></div></div>

<p>To use and pin a previous version of the theme, replace the <code class="language-plaintext highlighter-rouge">0.4.1</code> with the desired release tag.</p>

<h3 id="bugfixes-13">Bugfixes</h3>

<ul>
  <li>Fixed: allow later versions of <code class="language-plaintext highlighter-rouge">bundler</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1165">#1165</a></li>
  <li>Fixed: AsciiDoc code block styling by <a href="https://github.com/flyx">@flyx</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1168">#1168</a></li>
  <li>Fixed: main content negative margin for viewports in <code class="language-plaintext highlighter-rouge">[$md, $nav-width + $content-width]</code> by <a href="https://github.com/Dima-369">@Dima-369</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1177">#1177</a></li>
  <li>Removed: unused <code class="language-plaintext highlighter-rouge">OneDarkJekyll</code> files by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1167">#1167</a></li>
</ul>

<h3 id="documentation-8">Documentation</h3>

<ul>
  <li>Fixed: re-add <code class="language-plaintext highlighter-rouge">jekyll-github-metadata</code> to docs site by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1108">#1108</a></li>
</ul>

<h3 id="new-contributors-8">New Contributors</h3>

<ul>
  <li><a href="https://github.com/flyx">@flyx</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1168">#1168</a></li>
  <li><a href="https://github.com/Dima-369">@Dima-369</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1177">#1177</a></li>
</ul>

<p><strong>Full Changelog</strong>: <a href="https://github.com/just-the-docs/just-the-docs/compare/v0.4.0...v0.4.1">https://github.com/just-the-docs/just-the-docs/compare/v0.4.0…v0.4.1</a></p>

<h2 id="release-v040">Release v0.4.0</h2>

<p>We’re so excited to release Just the Docs <code class="language-plaintext highlighter-rouge">v0.4.0</code>. This release has been almost a year in the making - after our new maintenance team has taken over the project, we’ve added two years of backlogged features and bugfixes to modernize the theme. This CHANGELOG will summarize some of the key changes, discuss migrations strategies, and outline broad future plans for this theme.</p>

<h3 id="brief-overview---highlighted-changes">Brief Overview - Highlighted Changes</h3>

<p><code class="language-plaintext highlighter-rouge">v0.4.0</code> contains many new features and bugfixes. We enumerate all of them in further sections in this changelog; however, we’d like to call out some of the most-requested changes:</p>

<ul>
  <li>better support for dark theme: dark highlighting, search input color</li>
  <li><a href="https://just-the-docs.com/docs/ui-components/callouts/">callouts</a>, a new design component to highlight content</li>
  <li><a href="https://just-the-docs.com/docs/ui-components/code/#mermaid-diagram-code-blocks">configuring mermaid.js</a>, a markdown-native diagram visualization library</li>
  <li><a href="https://just-the-docs.com/docs/ui-components/code/#copy-button">copy code button</a> for code snippets</li>
  <li>external navigation links</li>
  <li>major improvements to nav generation efficiency and robustness</li>
  <li>minor improvements to built-in accessibility (SVG icons, nav titles, skip to main content)</li>
  <li><a href="https://just-the-docs.com/docs/customization/#custom-layouts-and-includes">modularized site components</a> (advanced feature)</li>
  <li><a href="https://just-the-docs.com/docs/customization/#override-includes">new custom includes</a>: table of contents heading, navigation panel footer, search placeholder, lunr search indices</li>
  <li>bugfixes involving WEBrick and Ruby 3, Liquid processing in CSS comments, nested task lists, relative URLs, scroll navigation, corrupted search data from rake, breadcrumbs, and more!</li>
  <li>more documentation for <a href="https://just-the-docs.com/docs/customization/#override-includes">custom includes</a>, this changelog, and the <a href="https://just-the-docs.com/MIGRATION/">migration guide</a></li>
</ul>

<p><em>After usage instructions and the roadmap, we enumerate all changes from <code class="language-plaintext highlighter-rouge">v0.3.3</code>.</em></p>

<h3 id="using-release-v040">Using Release <code class="language-plaintext highlighter-rouge">v0.4.0</code></h3>

<p>Unlike pre-releases, <code class="language-plaintext highlighter-rouge">v0.4.0</code> is a new semver minor release for the theme. That means that users who have not pinned the theme version will be <strong>automatically upgraded to <code class="language-plaintext highlighter-rouge">v0.4.0</code> the next time they build their site</strong>.</p>

<p>To use this release explicitly as a remote theme:</p>

<div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.4.0</span>
</code></pre></div></div>

<p>To use this RC explicitly as a gem-based theme, pin the version in your <code class="language-plaintext highlighter-rouge">Gemfile</code> and re-run <code class="language-plaintext highlighter-rouge">bundle install</code> or <code class="language-plaintext highlighter-rouge">bundle update just-the-docs</code>:</p>

<div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.4.0"</span>
</code></pre></div></div>

<p>If you would prefer to not upgrade, you can enforce that explicitly:</p>

<ol>
  <li>pin your gem version in your <code class="language-plaintext highlighter-rouge">Gemfile</code>, like so
    <div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.3.3"</span>
</code></pre></div>    </div>
  </li>
  <li>freeze the <code class="language-plaintext highlighter-rouge">remote_theme</code>, like so
    <div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.3.3</span>
</code></pre></div>    </div>
  </li>
</ol>

<h3 id="migration-guide-and-strategies">Migration Guide and Strategies</h3>

<p>We’ve developed a new <a href="https://just-the-docs.com/MIGRATION/">migration guide</a> for users to migrate from version <code class="language-plaintext highlighter-rouge">v0.3.3</code> to <code class="language-plaintext highlighter-rouge">v0.4.0</code>. It outlines major changes in project maintenance (e.g. new repository link, team) as well as breaking changes that may break your site (and potential solutions). We suggest that all users refer to the guide before manually upgrading their site.</p>

<p><strong>For the vast majority of users, we do not anticipate that this will be a breaking change.</strong> The major touch points are surrounding new includes, navigation (ordering, pages, and collections), the favicon, and a shift to relative URLs. However, users who heavily customize the theme (primarily by overriding includes) will likely have to make minor changes.</p>

<p>Given the length of features added in this release, users may want to incrementally upgrade through the pre-releases. To follow this approach, read this changelog from <code class="language-plaintext highlighter-rouge">v0.4.0.rc1</code> to <code class="language-plaintext highlighter-rouge">v0.4.0.rc5</code>; this breaks down the release into small chunks, each of which should be easier to upgrade. <code class="language-plaintext highlighter-rouge">v0.4.0.rc5</code> is identical to this release.</p>

<p>For support with migrating to <code class="language-plaintext highlighter-rouge">v0.4.0</code>, <a href="https://github.com/just-the-docs/just-the-docs/issues">open an issue</a> or <a href="https://github.com/just-the-docs/just-the-docs/discussions">start a discussion</a> and let us know!</p>

<h3 id="roadmap-whats-next">Roadmap (What’s Next?)</h3>

<p>Moving forward, we plan to release more frequently with smaller, bite-sized changes. This should make it easier for users to upgrade in the future!</p>

<p>Broadly, many features are still on the radar. We anticipate the rest of <code class="language-plaintext highlighter-rouge">v0.4.x</code> to be bugfixes surrounding this new release.</p>

<p>For version <code class="language-plaintext highlighter-rouge">v0.5</code>, our roadmap includes:</p>

<ul>
  <li>a theme toggle (light/dark mode), with automatic theme switching based on browser preferences</li>
  <li>better GDPR compliance for analytics</li>
  <li>multi-level/recursive navigation (unlimited hierarchy of child pages)</li>
</ul>

<p>In future versions, we also plan on:</p>

<ul>
  <li>adding better dark theme defaults</li>
  <li>adding better internationalization support</li>
  <li>exploring offline PDF generation</li>
  <li>improving accessibility within the theme</li>
  <li>improving search functionality</li>
  <li>refactoring and improving the robustness of our codebase</li>
</ul>

<p>Have ideas for what’s next, or want to get involved? <a href="https://github.com/just-the-docs/just-the-docs/issues">Open an issue</a> or <a href="https://github.com/just-the-docs/just-the-docs/discussions">start a discussion</a> and let us know! We’re looking for more contributors and maintainers to help us develop the theme.</p>

<h3 id="new-features-4">New Features</h3>

<ul>
  <li>Added: Combination by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/578">#578</a>
    <ul>
      <li>Added: dark highlighting in <a href="https://github.com/just-the-docs/just-the-docs/pull/463">#463</a></li>
      <li>Added: pages and collections in <a href="https://github.com/just-the-docs/just-the-docs/pull/448">#448</a></li>
      <li>Added: callouts in <a href="https://github.com/just-the-docs/just-the-docs/pull/466">#466</a></li>
      <li>Fixed: breadcrumb behaviour … by <a href="https://github.com/AdityaTiwari2102">@AdityaTiwari2102</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/477">#477</a></li>
      <li>Fixed: prevent rake command corrupting search data in <a href="https://github.com/just-the-docs/just-the-docs/pull/495">#495</a> (also listed below)</li>
      <li>Fixed: nested lists in <a href="https://github.com/just-the-docs/just-the-docs/pull/496">#496</a></li>
      <li>Fixed: set color for search input in <a href="https://github.com/just-the-docs/just-the-docs/pull/498">#498</a> (also listed below)</li>
      <li>Fixed: sites with no child pages (no PR)</li>
      <li>Fixed: TOC/breadcrumbs for multiple collections in <a href="https://github.com/just-the-docs/just-the-docs/pull/494">#494</a></li>
      <li>Added: collection configuration option <code class="language-plaintext highlighter-rouge">nav_fold</code> (no PR)</li>
      <li>Fixed: indentation and color for folded collection navigation (no PR)</li>
      <li>Fixed: scroll navigation to show the link to the current page in <a href="https://github.com/just-the-docs/just-the-docs/pull/639">#639</a></li>
      <li>Fixed: Replace all uses of <code class="language-plaintext highlighter-rouge">absolute_url</code> by <code class="language-plaintext highlighter-rouge">relative_url</code>, by <a href="https://github.com/svrooij">@svrooij</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/544">#544</a></li>
    </ul>
  </li>
  <li>Added: custom favicon <code class="language-plaintext highlighter-rouge">_includes</code> by <a href="https://github.com/burner1024">@burner1024</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/364">#364</a></li>
  <li>Added: set color for search input by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/498">#498</a></li>
  <li>Added: search placeholder configuration by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/613">#613</a></li>
  <li>Added: ‘child_nav_order’ front matter to be able to sort navigation pages in reverse by <a href="https://github.com/jmertic">@jmertic</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/726">#726</a></li>
  <li>Added: <code class="language-plaintext highlighter-rouge">nav_footer_custom</code> include by <a href="https://github.com/nathanjessen">@nathanjessen</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/474">#474</a></li>
  <li>Added: style fixes for jekyll-asciidoc by <a href="https://github.com/alyssais">@alyssais</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/829">#829</a></li>
  <li>Added: mermaid.js support by <a href="https://github.com/nascosto">@nascosto</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/857">#857</a></li>
  <li>Added: support for external navigation links by <a href="https://github.com/SPGoding">@SPGoding</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/876">#876</a></li>
  <li>Added: refactor <code class="language-plaintext highlighter-rouge">mermaid</code> config to use <code class="language-plaintext highlighter-rouge">mermaid_config.js</code> include, only require <code class="language-plaintext highlighter-rouge">mermaid.version</code> in <code class="language-plaintext highlighter-rouge">_config.yml</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/909">#909</a></li>
  <li>Added: accessible titles to nested page nav toggle by <a href="https://github.com/JPrevost">@JPrevost</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/950">#950</a></li>
  <li>Added: better title styling for AsciiDoc examples by <a href="https://github.com/alyssais">@alyssais</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/944">#944</a></li>
  <li>Added: docs for custom search placeholder by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/939">#939</a></li>
  <li>Added: provide ability to skip to main content by <a href="https://github.com/JPrevost">@JPrevost</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/949">#949</a></li>
  <li>Added: styling for <code class="language-plaintext highlighter-rouge">&lt;blockquote&gt;</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/965">#965</a></li>
  <li>Added: custom include for TOC heading by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/980">#980</a></li>
  <li>Added: experimental nav optimization for simple cases by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/992">#992</a></li>
  <li>Added: support multiple Google Analytics tracking IDs, document UA -&gt; GA4 switch by <a href="https://github.com/MichelleBlanchette">@MichelleBlanchette</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1029">#1029</a></li>
  <li>Added: copy code button to code snippets by <a href="https://github.com/simonebortolin">@simonebortolin</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/945">#945</a></li>
  <li>Added: restore simple configuration of <code class="language-plaintext highlighter-rouge">favicon.ico</code> via <code class="language-plaintext highlighter-rouge">site.static_files</code> by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1095">#1095</a></li>
  <li>Added: modularize site components by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1058">#1058</a></li>
  <li>Added: includes for custom <code class="language-plaintext highlighter-rouge">lunr</code> Liquid and JS code by <a href="https://github.com/diablodale">@diablodale</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1068">#1068</a></li>
  <li>Added: new <code class="language-plaintext highlighter-rouge">_sass/custom/setup.scss</code> for variable definition by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1135">#1135</a></li>
  <li>Added: configuration key to load a local version of mermaid by <a href="https://github.com/fabrik42">@fabrik42</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1153">#1153</a></li>
</ul>

<h3 id="bugfixes-14">Bugfixes</h3>

<ul>
  <li>Fixed: prepend <code class="language-plaintext highlighter-rouge">site.collections_dir</code> if exists by <a href="https://github.com/alexsegura">@alexsegura</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/519">#519</a></li>
  <li>Fixed: nested task lists (#517) by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/855">#855</a></li>
  <li>Fixed: suppress Liquid processing in CSS comments by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/686">#686</a></li>
  <li>Fixed: prevent rake command from corrupting search data by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/495">#495</a></li>
  <li>Fixed: anchor heading links should be visible on focus by <a href="https://github.com/jacobhq">@jacobhq</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/846">#846</a></li>
  <li>Fixed: add <code class="language-plaintext highlighter-rouge">overflow-x: auto</code> to <code class="language-plaintext highlighter-rouge">figure.highlight</code> by <a href="https://github.com/iridazzle">@iridazzle</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/727">#727</a></li>
  <li>Fixed: add <code class="language-plaintext highlighter-rouge">overflow-wrap: word-break</code> to <code class="language-plaintext highlighter-rouge">body</code> by <a href="https://github.com/iridazzle">@iridazzle</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/889">#889</a></li>
  <li>Fixed: vertical alignment for consecutive labels by <a href="https://github.com/Eisverygoodletter">@Eisverygoodletter</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/893">#893</a></li>
  <li>Fixed: allow links to wrap by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/905">#905</a></li>
  <li>Fixed: nav scroll feature and absolute/relative URLs by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/898">#898</a></li>
  <li>Fixed: exclude <code class="language-plaintext highlighter-rouge">vendor/</code> in Jekyll config by <a href="https://github.com/manuelhenke">@manuelhenke</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/941">#941</a></li>
  <li>Fixed: improve build time of navigation panel by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/956">#956</a></li>
  <li>Fixed: spacing issue when search is disabled by <a href="https://github.com/henryiii">@henryiii</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/960">#960</a></li>
  <li>Fixed: active grandchild link class by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/962">#962</a></li>
  <li>Fixed: HTML validation issues (W3C validator) by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/964">#964</a></li>
  <li>Fixed: link styling now uses <code class="language-plaintext highlighter-rouge">text-decoration</code> values by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/967">#967</a></li>
  <li>Fixed: cleaning up Jekyll excludes by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/985">#985</a></li>
  <li>Fixed: docs, narrow styling for code highlighting with line numbers by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/974">#974</a></li>
  <li>Fixed: default syntax highlighting in custom color schemes <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/986">#986</a></li>
  <li>Fixed: incorrect disambiguation in generated TOCs by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/999">#999</a></li>
  <li>Fixed: duplicated external links in collections by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1001">#1001</a></li>
  <li>Fixed: import order of <code class="language-plaintext highlighter-rouge">custom.scss</code>; puts at end by <a href="https://github.com/deseo">@deseo</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1010">#1010</a></li>
  <li>Fixed: top-level active link styling by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1015">#1015</a></li>
  <li>Fixed: external links for sites with no pages by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1021">#1021</a></li>
  <li>Fixed: duplicate <code class="language-plaintext highlighter-rouge">title</code> if <code class="language-plaintext highlighter-rouge">jekyll-seo-tag</code> not in users’s plugins by <a href="https://github.com/Tom-Brouwer">@Tom-Brouwer</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1040">#1040</a></li>
  <li>Fixed: removes (duplicate) <code class="language-plaintext highlighter-rouge">favicon.html</code>, shifts content to <code class="language-plaintext highlighter-rouge">head_custom.html</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1027">#1027</a></li>
  <li>Fixed: add <code class="language-plaintext highlighter-rouge">reversed</code>, deprecate <code class="language-plaintext highlighter-rouge">desc</code> for nav <code class="language-plaintext highlighter-rouge">child_nav_order</code> by <a href="https://github.com/jmertic">@jmertic</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1061">#1061</a></li>
  <li>Fixed: <code class="language-plaintext highlighter-rouge">child.child_nav_order</code> to <code class="language-plaintext highlighter-rouge">node.child_nav_order</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1065">#1065</a></li>
  <li>Fixed: remove all uses of <code class="language-plaintext highlighter-rouge">/</code> as SASS division by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1074">#1074</a>
    <ul>
      <li>note: this was originally merged as <a href="https://github.com/just-the-docs/just-the-docs/pull/1074">#1074</a> with a bug; it was reverted in <a href="https://github.com/just-the-docs/just-the-docs/pull/1076">#1076</a>, and then reimplemented in <a href="https://github.com/just-the-docs/just-the-docs/pull/1077">#1077</a></li>
    </ul>
  </li>
  <li>Fixed: skip nav collection generation when site has no pages by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1092">#1092</a></li>
  <li>Fixed: standardize SCSS with <code class="language-plaintext highlighter-rouge">declaration-block-no-redundant-longhand-properties</code> by <a href="https://github.com/simonebortolin">@simonebortolin</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1102">#1102</a></li>
  <li>Fixed: incorrect <code class="language-plaintext highlighter-rouge">padding</code> property value pair in <code class="language-plaintext highlighter-rouge">labels.scss</code> by <a href="https://github.com/SConaway">@SConaway</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1104">#1104</a></li>
  <li>Fixed: various bugs with copy code button by <a href="https://github.com/simonebortolin">@simonebortolin</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1096">#1096</a></li>
  <li>Fixed: replace inline styling for <code class="language-plaintext highlighter-rouge">&lt;svg&gt;</code> icons by <a href="https://github.com/captn3m0">@captn3m0</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1110">#1110</a></li>
  <li>Fixed: incorrect <code class="language-plaintext highlighter-rouge">padding</code> property value pair in <code class="language-plaintext highlighter-rouge">search.scss</code> by <a href="https://github.com/kevinlin1">@kevinlin1</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1123">#1123</a></li>
  <li>Fixed: minor spacing and comment nits by <a href="https://github.com/EricFromCanada">@EricFromCanada</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1128">#1128</a></li>
  <li>Fixed: exclude images from being bundled with gem by <a href="https://github.com/m-r-mccormick">@m-r-mccormick</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1142">#1142</a></li>
  <li>Fixed: dark theme code block background, line number colors by <a href="https://github.com/m-r-mccormick">@m-r-mccormick</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1124">#1124</a></li>
  <li>Fixed: copy code button interaction with kramdown line numbers by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1143">#1143</a></li>
</ul>

<h3 id="maintenance">Maintenance</h3>

<ul>
  <li>Added: VScode devcontainer by <a href="https://github.com/max06">@max06</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/783">#783</a></li>
  <li>Added: <code class="language-plaintext highlighter-rouge">webrick</code> to <code class="language-plaintext highlighter-rouge">Gemfile</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/799">#799</a></li>
  <li>Added: ‘This site is powered by Netlify.’ to the footer by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/797">#797</a></li>
  <li>Updated: new repo path by <a href="https://github.com/pmarsceill">@pmarsceill</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/775">#775</a></li>
  <li>Updated: rename <code class="language-plaintext highlighter-rouge">master</code> -&gt; <code class="language-plaintext highlighter-rouge">main</code> by <a href="https://github.com/pmarsceill">@pmarsceill</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/776">#776</a></li>
  <li>Updated: README by <a href="https://github.com/pmarsceill">@pmarsceill</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/777">#777</a></li>
  <li>Updated: Code of Conduct to Contributor Covenant v2.1 by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/790">#790</a></li>
  <li>Updated: CI files, Ruby &amp; Node Versions by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/820">#820</a></li>
  <li>Updated: Stylelint to v14, extend SCSS plugins, remove primer-* configs, resolve issues by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/821">#821</a></li>
  <li>Deleted: unused script directory by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/937">#937</a></li>
  <li>Vendor: update <code class="language-plaintext highlighter-rouge">jekyll-anchor-headings</code>, <code class="language-plaintext highlighter-rouge">lunr.js</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1071">#1071</a></li>
</ul>

<h3 id="documentation-9">Documentation</h3>

<ul>
  <li>Added: docs on how to break an <code class="language-plaintext highlighter-rouge">ol</code> by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/856">#856</a></li>
  <li>Added: docs for custom includes by <a href="https://github.com/nathanjessen">@nathanjessen</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/806">#806</a></li>
  <li>Added: document caveat about variable dependencies by <a href="https://github.com/waldyrious">@waldyrious</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/555">#555</a></li>
  <li>Added: docs on how to use <code class="language-plaintext highlighter-rouge">custom_head</code> to add a custom favicon by <a href="https://github.com/UnclassedPenguin">@UnclassedPenguin</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/814">#814</a></li>
  <li>Added: docs load mermaid.js by default by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/935">#935</a></li>
  <li>Added: warning about mandatory <code class="language-plaintext highlighter-rouge">_</code>-prefix for collections by <a href="https://github.com/max06">@max06</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1091">#1091</a></li>
  <li>Added:  migration guide by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1059">#1059</a></li>
  <li>Added: label new features introduced in <code class="language-plaintext highlighter-rouge">v0.4</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1138">#1138</a></li>
  <li>Fixed: <code class="language-plaintext highlighter-rouge">ol</code> on <code class="language-plaintext highlighter-rouge">index.md</code> by <a href="https://github.com/pmarsceill">@pmarsceill</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/778">#778</a></li>
  <li>Fixed: image link in Markdown kitchen sink by <a href="https://github.com/JeffGuKang">@JeffGuKang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/221">#221</a></li>
  <li>Fixed: images in Markdown kitchen sink by <a href="https://github.com/dougaitken">@dougaitken</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/782">#782</a></li>
  <li>Fixed: clearer label of link to Jekyll quickstart by <a href="https://github.com/waldyrious">@waldyrious</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/549">#549</a></li>
  <li>Fixed: remove extra spaces in component docs by <a href="https://github.com/MichelleBlanchette">@MichelleBlanchette</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/554">#554</a></li>
  <li>Fixed: double “your” typo in <code class="language-plaintext highlighter-rouge">index.md</code> by <a href="https://github.com/sehilyi">@sehilyi</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/499">#499</a></li>
  <li>Fixed: “you” -&gt; “your” typo in <code class="language-plaintext highlighter-rouge">index.md</code> by <a href="https://github.com/nathanjessen">@nathanjessen</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/473">#473</a></li>
  <li>Fixed: spacing in toc example by <a href="https://github.com/henryiii">@henryiii</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/835">#835</a></li>
  <li>Fixed: typo in <code class="language-plaintext highlighter-rouge">README</code> on <code class="language-plaintext highlighter-rouge">_config.yml</code> by <a href="https://github.com/ivanskodje">@ivanskodje</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/891">#891</a></li>
  <li>Fixed: missing code fence in navigation structure docs by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/906">#906</a></li>
  <li>Fixed: table of contents on search docs by <a href="https://github.com/robinpokorny">@robinpokorny</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/940">#940</a></li>
  <li>Fixed: broken docs link (custom footer) by <a href="https://github.com/olgarithms">@olgarithms</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/951">#951</a></li>
  <li>Fixed: clarify version docs by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/955">#955</a></li>
  <li>Fixed: typo in changelog links <a href="https://github.com/koppor">@koppor</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1000">#1000</a></li>
  <li>Fixed: two bugs in “Customization” (custom favicon, new annotation) by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1090">#1090</a></li>
  <li>Fixed: “View Typography Utilities” link by <a href="https://github.com/agabrys">@agabrys</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1130">#1130</a></li>
  <li>Fixed: broken relative page links by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1106">#1106</a></li>
  <li>Fixed: clarify steps to add custom <code class="language-plaintext highlighter-rouge">lunr</code> index code by <a href="https://github.com/diablodale">@diablodale</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1139">#1139</a></li>
  <li>Updated: homepage (focus: new features, conciseness, deduplication) by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1018">#1018</a></li>
  <li>Updated: README (focus: new features, conciseness, deduplication) by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1019">#1019</a></li>
  <li>Updated: <code class="language-plaintext highlighter-rouge">README</code> demo video by <a href="https://github.com/codewithfan">@codewithfan</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1097">#1097</a></li>
</ul>

<h3 id="new-contributors-9">New Contributors</h3>

<ul>
  <li><a href="https://github.com/AdityaTiwari2102">@AdityaTiwari2102</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/477">#477</a></li>
  <li><a href="https://github.com/svrooij">@svrooij</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/544">#544</a></li>
  <li><a href="https://github.com/alexsegura">@alexsegura</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/519">#519</a></li>
  <li><a href="https://github.com/burner1024">@burner1024</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/364">#364</a></li>
  <li><a href="https://github.com/JeffGuKang">@JeffGuKang</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/221">#221</a></li>
  <li><a href="https://github.com/dougaitken">@dougaitken</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/782">#782</a></li>
  <li><a href="https://github.com/max06">@max06</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/783">#783</a></li>
  <li><a href="https://github.com/sehilyi">@sehilyi</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/499">#499</a></li>
  <li><a href="https://github.com/nathanjessen">@nathanjessen</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/473">#473</a></li>
  <li><a href="https://github.com/waldyrious">@waldyrious</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/549">#549</a></li>
  <li><a href="https://github.com/MichelleBlanchette">@MichelleBlanchette</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/554">#554</a></li>
  <li><a href="https://github.com/henryiii">@henryiii</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/835">#835</a></li>
  <li><a href="https://github.com/jmertic">@jmertic</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/726">#726</a></li>
  <li><a href="https://github.com/jacobhq">@jacobhq</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/846">#846</a></li>
  <li><a href="https://github.com/UnclassedPenguin">@UnclassedPenguin</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/814">#814</a></li>
  <li><a href="https://github.com/alyssais">@alyssais</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/829">#829</a></li>
  <li><a href="https://github.com/nascosto">@nascosto</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/857">#857</a></li>
  <li><a href="https://github.com/SPGoding">@SPGoding</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/876">#876</a></li>
  <li><a href="https://github.com/iridazzle">@iridazzle</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/727">#727</a></li>
  <li><a href="https://github.com/ivanskodje">@ivanskodje</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/891">#891</a></li>
  <li><a href="https://github.com/Eisverygoodletter">@Eisverygoodletter</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/893">#893</a></li>
  <li><a href="https://github.com/robinpokorny">@robinpokorny</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/940">#940</a></li>
  <li><a href="https://github.com/olgarithms">@olgarithms</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/951">#951</a></li>
  <li><a href="https://github.com/manuelhenke">@manuelhenke</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/941">#941</a></li>
  <li><a href="https://github.com/JPrevost">@JPrevost</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/950">#950</a></li>
  <li><a href="https://github.com/koppor">@koppor</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1000">#1000</a></li>
  <li><a href="https://github.com/deseo">@deseo</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1010">#1010</a></li>
  <li><a href="https://github.com/Tom-Brouwer">@Tom-Brouwer</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1040">#1040</a></li>
  <li><a href="https://github.com/simonebortolin">@simonebortolin</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/945">#945</a></li>
  <li><a href="https://github.com/SConaway">@SConaway</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1104">#1104</a></li>
  <li><a href="https://github.com/captn3m0">@captn3m0</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1110">#1110</a></li>
  <li><a href="https://github.com/kevinlin1">@kevinlin1</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1123">#1123</a></li>
  <li><a href="https://github.com/codewithfan">@codewithfan</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1097">#1097</a></li>
  <li><a href="https://github.com/agabrys">@agabrys</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1130">#1130</a></li>
  <li><a href="https://github.com/diablodale">@diablodale</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1068">#1068</a></li>
  <li><a href="https://github.com/m-r-mccormick">@m-r-mccormick</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1142">#1142</a></li>
  <li><a href="https://github.com/fabrik42">@fabrik42</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1153">#1153</a></li>
</ul>

<h2 id="pre-release-v040rc5">Pre-release v0.4.0.rc5</h2>

<p>Hi everyone, we’re so excited to finally release <code class="language-plaintext highlighter-rouge">v0.4.0</code>! For posterity’s sake, we’re going to release <code class="language-plaintext highlighter-rouge">v0.4.0.rc5</code> and then immediately re-release it as <code class="language-plaintext highlighter-rouge">v0.4.0</code>; this should make it more clear what changes were introduced in the lead up to the minor release.</p>

<p>This RC does not introduce any major user-facing features. It adds more customizability for custom SCSS variables (fixing a bug with callout introduction order), <code class="language-plaintext highlighter-rouge">lunr</code> indexing, and loading <code class="language-plaintext highlighter-rouge">mermaid</code> locally. In addition, it fixes bugs introduced in <code class="language-plaintext highlighter-rouge">.rc4</code>: incorrect CSS, inconsistencies with code block backgrounds in dark theme, and the copy code button. It also adds a migration guide for users coming from <code class="language-plaintext highlighter-rouge">v0.3.3</code>.</p>

<h3 id="trying-out-pre-release-v040rc5">Trying out pre-release <code class="language-plaintext highlighter-rouge">v0.4.0.rc5</code></h3>

<p>Similar to the prior release, <code class="language-plaintext highlighter-rouge">v0.4.0.rc5</code> is a <strong>release candidate</strong> for the theme (i.e., a pre-release) with release <code class="language-plaintext highlighter-rouge">v0.4.0</code> following immediately after. While we don’t anticipate many users using this RC, it is still possible to opt-in.</p>

<p>To use this RC explicitly as a remote theme:</p>

<div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.4.0.rc5</span>
</code></pre></div></div>

<p>To use this RC explicitly as a gem-based theme, pin the version in your <code class="language-plaintext highlighter-rouge">Gemfile</code> and re-run <code class="language-plaintext highlighter-rouge">bundle install</code> or <code class="language-plaintext highlighter-rouge">bundle update just-the-docs</code>:</p>

<div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.4.0.rc5"</span>
</code></pre></div></div>

<p>By default, <strong>users will not be upgraded to <code class="language-plaintext highlighter-rouge">0.4.0.rc5</code></strong>. To enforce that explicitly, either:</p>

<ol>
  <li>pin your gem version in your <code class="language-plaintext highlighter-rouge">Gemfile</code>, like so
    <div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.3.3"</span>
</code></pre></div>    </div>
  </li>
  <li>freeze the <code class="language-plaintext highlighter-rouge">remote_theme</code>, like so
    <div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.3.3</span>
</code></pre></div>    </div>
  </li>
</ol>

<h3 id="new-features-5">New Features</h3>

<ul>
  <li>Added: includes for custom <code class="language-plaintext highlighter-rouge">lunr</code> Liquid and JS code by <a href="https://github.com/diablodale">@diablodale</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1068">#1068</a></li>
  <li>Added: new <code class="language-plaintext highlighter-rouge">_sass/custom/setup.scss</code> for variable definition by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1135">#1135</a></li>
  <li>Added: configuration key to load a local version of mermaid by <a href="https://github.com/fabrik42">@fabrik42</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1153">#1153</a></li>
</ul>

<h3 id="bugfixes-and-maintenance">Bugfixes and Maintenance</h3>

<ul>
  <li>Fixed: incorrect <code class="language-plaintext highlighter-rouge">padding</code> property value pair in <code class="language-plaintext highlighter-rouge">search.scss</code> by <a href="https://github.com/kevinlin1">@kevinlin1</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1123">#1123</a></li>
  <li>Fixed: minor spacing and comment nits by <a href="https://github.com/EricFromCanada">@EricFromCanada</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1128">#1128</a></li>
  <li>Fixed: exclude images from being bundled with gem by <a href="https://github.com/m-r-mccormick">@m-r-mccormick</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1142">#1142</a></li>
  <li>Fixed: dark theme code block background, line number colors by <a href="https://github.com/m-r-mccormick">@m-r-mccormick</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1124">#1124</a></li>
  <li>Fixed: copy code button interaction with kramdown line numbers by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1143">#1143</a></li>
</ul>

<h3 id="docs">Docs</h3>

<ul>
  <li>Docs: add a migration guide by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1059">#1059</a></li>
  <li>Docs: update <code class="language-plaintext highlighter-rouge">README</code> demo video by <a href="https://github.com/codewithfan">@codewithfan</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1097">#1097</a></li>
  <li>Docs: update “View Typography Utilities” link by <a href="https://github.com/agabrys">@agabrys</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1130">#1130</a></li>
  <li>Docs: fix broken relative page links by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1106">#1106</a></li>
  <li>Docs: clarify steps to add custom <code class="language-plaintext highlighter-rouge">lunr</code> index code by <a href="https://github.com/diablodale">@diablodale</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1139">#1139</a></li>
  <li>Docs: label new features introduced in <code class="language-plaintext highlighter-rouge">v0.4</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1138">#1138</a></li>
</ul>

<h3 id="new-contributors-10">New Contributors</h3>

<ul>
  <li><a href="https://github.com/kevinlin1">@kevinlin1</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1123">#1123</a></li>
  <li><a href="https://github.com/codewithfan">@codewithfan</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1097">#1097</a></li>
  <li><a href="https://github.com/agabrys">@agabrys</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1130">#1130</a></li>
  <li><a href="https://github.com/diablodale">@diablodale</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1068">#1068</a></li>
  <li><a href="https://github.com/m-r-mccormick">@m-r-mccormick</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1142">#1142</a></li>
  <li><a href="https://github.com/fabrik42">@fabrik42</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1153">#1153</a></li>
</ul>

<h2 id="pre-release-v040rc4">Pre-release v0.4.0.rc4</h2>

<p>Happy new year! We’re celebrating with another pre-release, with features that should help theme users better adapt to changes moving forward. <strong>We aim to re-release this as <code class="language-plaintext highlighter-rouge">v0.4.0</code>, with only few changes</strong>.</p>

<p>Notable new additions include:</p>

<ul>
  <li>modular site components, which split up the site into smaller reusable components; advanced theme users can then remix layouts quickly without duplication</li>
  <li>a “copy code” button to code blocks</li>
  <li>fixing bugs in generated TOCs and navigation from previous prereleases</li>
  <li>various cleanups of CSS and HTML markup</li>
</ul>

<p>The roadmap to <code class="language-plaintext highlighter-rouge">v0.4.0</code> is small. We are only looking to:</p>

<ul>
  <li>finish a migration guide, so users can easily upgrade from <code class="language-plaintext highlighter-rouge">v0.3.3</code> to <code class="language-plaintext highlighter-rouge">v0.4.0</code></li>
  <li>fix one last bug relating to callouts and custom colors</li>
  <li>fix any new bugs introduced by this pre-release</li>
</ul>

<p>Have any questions, thoughts, or concerns? We’d love to hear from you! Please <a href="https://github.com/just-the-docs/just-the-docs/issues">open an issue</a> or <a href="https://github.com/just-the-docs/just-the-docs/discussions">start a discussion</a> and let us know!</p>

<h3 id="trying-out-pre-release-v040rc4">Trying out pre-release <code class="language-plaintext highlighter-rouge">v0.4.0.rc4</code></h3>

<p>Similar to the prior release, <code class="language-plaintext highlighter-rouge">v0.4.0.rc4</code> is a <strong>release candidate</strong> for the theme (i.e., a pre-release) with release <code class="language-plaintext highlighter-rouge">v0.4.0</code> coming soon. We want your help in testing the changes! As of now, the gem on RubyGems and the repository are updated to <code class="language-plaintext highlighter-rouge">v0.4.0.rc4</code>.</p>

<p>To use this RC explicitly as a remote theme:</p>

<div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.4.0.rc4</span>
</code></pre></div></div>

<p>To use this RC explicitly as a gem-based theme, pin the version in your <code class="language-plaintext highlighter-rouge">Gemfile</code> and re-run <code class="language-plaintext highlighter-rouge">bundle install</code> or <code class="language-plaintext highlighter-rouge">bundle update just-the-docs</code>:</p>

<div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.4.0.rc4"</span>
</code></pre></div></div>

<p>By default, <strong>users will not be upgraded to <code class="language-plaintext highlighter-rouge">0.4.0.rc4</code></strong>. To enforce that explicitly, either:</p>

<ol>
  <li>pin your gem version in your <code class="language-plaintext highlighter-rouge">Gemfile</code>, like so
    <div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.3.3"</span>
</code></pre></div>    </div>
  </li>
  <li>freeze the <code class="language-plaintext highlighter-rouge">remote_theme</code>, like so
    <div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.3.3</span>
</code></pre></div>    </div>
  </li>
</ol>

<h3 id="new-features-6">New Features</h3>

<ul>
  <li>Added: support multiple Google Analytics tracking IDs, document UA -&gt; GA4 switch by <a href="https://github.com/MichelleBlanchette">@MichelleBlanchette</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1029">#1029</a></li>
  <li>Added: copy code button to code snippets by <a href="https://github.com/simonebortolin">@simonebortolin</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/945">#945</a></li>
  <li>Added: restore simple configuration of <code class="language-plaintext highlighter-rouge">favicon.ico</code> via <code class="language-plaintext highlighter-rouge">site.static_files</code> by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1095">#1095</a></li>
  <li>Added: modularize site components by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1058">#1058</a></li>
</ul>

<h3 id="bugfixes-and-maintenance-1">Bugfixes and Maintenance</h3>

<ul>
  <li>Fixed: incorrect disambiguation in generated TOCs by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/999">#999</a></li>
  <li>Fixed: duplicated external links in collections by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1001">#1001</a></li>
  <li>Fixed: import order of <code class="language-plaintext highlighter-rouge">custom.scss</code>; puts at end by <a href="https://github.com/deseo">@deseo</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1010">#1010</a></li>
  <li>Fixed: top-level active link styling by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1015">#1015</a></li>
  <li>Fixed: external links for sites with no pages by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1021">#1021</a></li>
  <li>Fixed: duplicate <code class="language-plaintext highlighter-rouge">title</code> if <code class="language-plaintext highlighter-rouge">jekyll-seo-tag</code> not in users’s plugins by <a href="https://github.com/Tom-Brouwer">@Tom-Brouwer</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1040">#1040</a></li>
  <li>Fixed: removes (duplicate) <code class="language-plaintext highlighter-rouge">favicon.html</code>, shifts content to <code class="language-plaintext highlighter-rouge">head_custom.html</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1027">#1027</a></li>
  <li>Fixed: add <code class="language-plaintext highlighter-rouge">reversed</code>, deprecate <code class="language-plaintext highlighter-rouge">desc</code> for nav <code class="language-plaintext highlighter-rouge">child_nav_order</code> by <a href="https://github.com/jmertic">@jmertic</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1061">#1061</a></li>
  <li>Fixed: <code class="language-plaintext highlighter-rouge">child.child_nav_order</code> to <code class="language-plaintext highlighter-rouge">node.child_nav_order</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1065">#1065</a></li>
  <li>Fixed: remove all uses of <code class="language-plaintext highlighter-rouge">/</code> as SASS division by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1074">#1074</a>
    <ul>
      <li>note: this was originally merged as <a href="https://github.com/just-the-docs/just-the-docs/pull/1074">#1074</a> with a bug; it was reverted in <a href="https://github.com/just-the-docs/just-the-docs/pull/1076">#1076</a>, and then reimplemented in <a href="https://github.com/just-the-docs/just-the-docs/pull/1077">#1077</a></li>
    </ul>
  </li>
  <li>Fixed: skip nav collection generation when site has no pages by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1092">#1092</a></li>
  <li>Fixed: standardize SCSS with <code class="language-plaintext highlighter-rouge">declaration-block-no-redundant-longhand-properties</code> by <a href="https://github.com/simonebortolin">@simonebortolin</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1102">#1102</a></li>
  <li>Fixed: incorrect <code class="language-plaintext highlighter-rouge">padding</code> property value pair in <code class="language-plaintext highlighter-rouge">labels.scss</code> by <a href="https://github.com/SConaway">@SConaway</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1104">#1104</a></li>
  <li>Fixed: various bugs with copy code button by <a href="https://github.com/simonebortolin">@simonebortolin</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1096">#1096</a></li>
  <li>Fixed: replace inline styling for <code class="language-plaintext highlighter-rouge">&lt;svg&gt;</code> icons by <a href="https://github.com/captn3m0">@captn3m0</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1110">#1110</a></li>
  <li>Vendor: update <code class="language-plaintext highlighter-rouge">jekyll-anchor-headings</code>, <code class="language-plaintext highlighter-rouge">lunr.js</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1071">#1071</a></li>
</ul>

<h3 id="docs-1">Docs</h3>

<ul>
  <li>Docs: fix typo in changelog links <a href="https://github.com/koppor">@koppor</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1000">#1000</a></li>
  <li>Docs: update homepage (focus: new features, conciseness, deduplication) by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1018">#1018</a></li>
  <li>Docs: update README (focus: new features, conciseness, deduplication) by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1019">#1019</a></li>
  <li>Docs: fix two bugs in “Customization” (custom favicon, new annotation) by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1090">#1090</a></li>
  <li>Docs: Add warning about mandatory <code class="language-plaintext highlighter-rouge">_</code>-prefix for collections by <a href="https://github.com/max06">@max06</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1091">#1091</a></li>
  <li>Docs: remove Google Analytics on main site by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/1113">#1113</a></li>
</ul>

<h3 id="new-contributors-11">New Contributors</h3>

<ul>
  <li><a href="https://github.com/koppor">@koppor</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1000">#1000</a></li>
  <li><a href="https://github.com/deseo">@deseo</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1010">#1010</a></li>
  <li><a href="https://github.com/Tom-Brouwer">@Tom-Brouwer</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1040">#1040</a></li>
  <li><a href="https://github.com/simonebortolin">@simonebortolin</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/945">#945</a></li>
  <li><a href="https://github.com/SConaway">@SConaway</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1104">#1104</a></li>
  <li><a href="https://github.com/captn3m0">@captn3m0</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/1110">#1110</a></li>
</ul>

<p><strong>Full Changelog</strong>: https://github.com/just-the-docs/just-the-docs/compare/v0.4.0.rc3…v0.4.0.rc4</p>

<h2 id="pre-release-v040rc3">Pre-release v0.4.0.rc3</h2>

<p>Hi there! This is (actually) hopefully the last prerelease before <code class="language-plaintext highlighter-rouge">v0.4.0</code>; in particular, if we find that this prerelease is stable, we’ll re-release it as <code class="language-plaintext highlighter-rouge">v0.4.0</code>.</p>

<p>In general, this is a more mature pre-release; there are few new features. However, we’ll highlight <a href="https://github.com/pdmosses">@pdmosses</a>’s work in <a href="https://github.com/just-the-docs/just-the-docs/pull/992">#992</a> to better optimize nav generation for large sites (ex 100+ pages). We don’t expect this to affect most users; however, <strong>it is technically a breaking change</strong>, and we suggest testing your site before upgrading to this prerelease.</p>

<p>We want your feedback! Please <a href="https://github.com/just-the-docs/just-the-docs/issues">open an issue</a> or <a href="https://github.com/just-the-docs/just-the-docs/discussions">start a discussion</a> and let us know!</p>

<p>As soon as we get stable test results from major downstream users, we’ll push out a <code class="language-plaintext highlighter-rouge">v0.4.0</code> ASAP - closing out almost 2 years of backlogged work!</p>

<h3 id="trying-out-pre-release-v040rc3">Trying out pre-release <code class="language-plaintext highlighter-rouge">v0.4.0.rc3</code></h3>

<p>Similar to the prior release, <code class="language-plaintext highlighter-rouge">v0.4.0.rc3</code> is a <strong>release candidate</strong> for the theme (i.e., a pre-release) with release <code class="language-plaintext highlighter-rouge">v0.4.0</code> coming soon. We want your help in testing the changes! As of now, the gem on RubyGems and the repository are updated to <code class="language-plaintext highlighter-rouge">v0.4.0.rc3</code>.</p>

<p>To use this RC explicitly as a remote theme:</p>

<div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.4.0.rc3</span>
</code></pre></div></div>

<p>To use this RC explicitly as a gem-based theme, pin the version in your <code class="language-plaintext highlighter-rouge">Gemfile</code> and re-run <code class="language-plaintext highlighter-rouge">bundle install</code> or <code class="language-plaintext highlighter-rouge">bundle update just-the-docs</code>:</p>

<div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.4.0.rc3"</span>
</code></pre></div></div>

<p>By default, <strong>users will not be upgraded to <code class="language-plaintext highlighter-rouge">0.4.0.rc3</code></strong>. To enforce that explicitly, either:</p>

<ol>
  <li>pin your gem version in your <code class="language-plaintext highlighter-rouge">Gemfile</code>, like so
    <div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.3.3"</span>
</code></pre></div>    </div>
  </li>
  <li>freeze the <code class="language-plaintext highlighter-rouge">remote_theme</code>, like so
    <div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.3.3</span>
</code></pre></div>    </div>
  </li>
</ol>

<h3 id="features">Features</h3>

<p>Broadly, this prerelease is feature-light!</p>

<ul>
  <li>Added: styling for <code class="language-plaintext highlighter-rouge">&lt;blockquote&gt;</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/965">#965</a></li>
  <li>Added: custom include for TOC heading by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/980">#980</a></li>
</ul>

<h3 id="bugfixes-and-experimental-features">Bugfixes and Experimental Features</h3>

<p><em>Note</em>: experimental nav optimization may be unstable. Please give us feedback!</p>

<ul>
  <li>Added: experimental nav optimization for simple cases by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/992">#992</a></li>
  <li>Fixed: spacing issue when search is disabled by <a href="https://github.com/henryiii">@henryiii</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/960">#960</a></li>
  <li>Fixed: active grandchild link class by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/962">#962</a></li>
  <li>Fixed: HTML validation issues (W3C validator) by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/964">#964</a></li>
  <li>Fixed: link styling now uses <code class="language-plaintext highlighter-rouge">text-decoration</code> values by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/967">#967</a></li>
  <li>Fixed: cleaning up Jekyll excludes by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/985">#985</a></li>
  <li>Fixed: docs, narrow styling for code highlighting with line numbers by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/974">#974</a></li>
  <li>Fixed: default syntax highlighting in custom color schemes <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/986">#986</a></li>
</ul>

<p><strong>Full Changelog</strong>: https://github.com/just-the-docs/just-the-docs/compare/v0.4.0.rc2…v0.4.0.rc3</p>

<h2 id="pre-release-v040rc2">Pre-release v0.4.0.rc2</h2>

<p class="warning">This website includes docs for some new features that are not available in <code class="language-plaintext highlighter-rouge">v0.4.0.rc1</code> and <code class="language-plaintext highlighter-rouge">v0.3.3</code>!</p>

<p>Hey there! This is likely the last pre-release before releasing <code class="language-plaintext highlighter-rouge">v0.4.0</code>, which we plan on doing soon (i.e. before the end of the month) - very exciting! Some new additions to highlight:</p>

<ul>
  <li>significant improvement on build time of navigation panel by <a href="https://github.com/pdmosses">@pdmosses</a>
    <ul>
      <li>this is big: for a community member with over 300 pages, we shortened the build time from 3 minutes to 30 seconds!</li>
    </ul>
  </li>
  <li>improved accessibility features led by <a href="https://github.com/JPrevost">@JPrevost</a></li>
  <li>more docs!</li>
</ul>

<p>The intention of this release candidate is to gather even more feedback on a potential <code class="language-plaintext highlighter-rouge">v0.4.0</code>. As it stands, we have not encountered any breaking changes with early adopters of <code class="language-plaintext highlighter-rouge">v0.4.0.rc1</code>. If you encounter any - for either of our pre-releases - please let us know!</p>

<h3 id="trying-out-pre-release-v040rc2">Trying out pre-release <code class="language-plaintext highlighter-rouge">v0.4.0.rc2</code></h3>

<p>Similar to the prior release, <code class="language-plaintext highlighter-rouge">v0.4.0.rc2</code> is a <strong>release candidate</strong> for the theme (i.e., a pre-release) with release <code class="language-plaintext highlighter-rouge">v0.4.0</code> coming soon. We want your help in testing the changes! As of now, the gem on RubyGems and the repository are updated to <code class="language-plaintext highlighter-rouge">v0.4.0.rc2</code>.</p>

<p>To use this RC explicitly as a remote theme:</p>

<div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.4.0.rc2</span>
</code></pre></div></div>

<p>To use this RC explicitly as a gem-based theme, pin the version in your <code class="language-plaintext highlighter-rouge">Gemfile</code> and re-run <code class="language-plaintext highlighter-rouge">bundle install</code> or <code class="language-plaintext highlighter-rouge">bundle update just-the-docs</code>:</p>

<div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.4.0.rc2"</span>
</code></pre></div></div>

<p>By default, <strong>users will not be upgraded to <code class="language-plaintext highlighter-rouge">0.4.0.rc2</code></strong>. To enforce that explicitly, either:</p>

<ol>
  <li>pin your gem version in your <code class="language-plaintext highlighter-rouge">Gemfile</code>, like so
    <div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.3.3"</span>
</code></pre></div>    </div>
  </li>
  <li>freeze the <code class="language-plaintext highlighter-rouge">remote_theme</code>, like so
    <div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.3.3</span>
</code></pre></div>    </div>
  </li>
</ol>

<h3 id="features-1">Features</h3>

<ul>
  <li>Added: accessible titles to nested page nav toggle by <a href="https://github.com/JPrevost">@JPrevost</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/950">#950</a></li>
  <li>Added: better title styling for AsciiDoc examples by <a href="https://github.com/alyssais">@alyssais</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/944">#944</a></li>
  <li>Added: docs for custom search placeholder by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/939">#939</a></li>
  <li>Added: provide ability to skip to main content by <a href="https://github.com/JPrevost">@JPrevost</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/949">#949</a></li>
  <li>Fixed: exclude <code class="language-plaintext highlighter-rouge">vendor/</code> in Jekyll config by <a href="https://github.com/manuelhenke">@manuelhenke</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/941">#941</a></li>
  <li>Fixed: improve build time of navigation panel by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/956">#956</a></li>
</ul>

<h3 id="documentation-and-maintenance">Documentation and Maintenance</h3>

<ul>
  <li>Added: docs load mermaid.js by default by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/935">#935</a></li>
  <li>Fixed: table of contents on search docs by <a href="https://github.com/robinpokorny">@robinpokorny</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/940">#940</a></li>
  <li>Fixed: broken docs link (custom footer) by <a href="https://github.com/olgarithms">@olgarithms</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/951">#951</a></li>
  <li>Fixed: clarify version docs by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/955">#955</a></li>
  <li>Deleted: unused script directory by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/937">#937</a></li>
</ul>

<h3 id="new-contributors-12">New Contributors</h3>

<ul>
  <li><a href="https://github.com/robinpokorny">@robinpokorny</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/940">#940</a></li>
  <li><a href="https://github.com/olgarithms">@olgarithms</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/951">#951</a></li>
  <li><a href="https://github.com/manuelhenke">@manuelhenke</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/941">#941</a></li>
  <li><a href="https://github.com/JPrevost">@JPrevost</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/950">#950</a></li>
</ul>

<h2 id="pre-release-v040rc1">Pre-release v0.4.0.rc1</h2>

<h3 id="were-back">We’re back!</h3>

<p>Hi all! The Just the Docs team is excited to have our first pre-release in over two years! It is jam-packed with features and bugfixes that have been requested by the community since 2020. They include:</p>

<ul>
  <li>The new callouts component</li>
  <li>Allowing pages and collections to coexist on the navigation pane</li>
  <li>New styling: dark syntax highlighting, support for jekyll-asciidoc, word-wrapping instead of overflow for various elements</li>
  <li>More customization: external nav links, custom nav footers, favicon includes, search color and placeholder configuration, mermaid.js support, and nav sorting</li>
  <li>Over 20 bugfixes! Big ones include fixing the <code class="language-plaintext highlighter-rouge">rake</code> command, using <code class="language-plaintext highlighter-rouge">relative_url</code>, and search input color</li>
  <li>More documentation, especially on using custom includes</li>
  <li>Updating core dependencies to stable Ruby versions</li>
  <li>A WIP <a href="https://github.com/just-the-docs/just-the-docs-template">template repository</a> that allows you to setup your own repository using Just the Docs and GitHub Pages with one click - give it a shot! More documentation, etc. is on the way!</li>
</ul>

<p>We want your feedback! Are these changes helpful? Are our docs easy to understand? Should new features like <code class="language-plaintext highlighter-rouge">mermaid</code> be opt-in or opt-out? Please <a href="https://github.com/just-the-docs/just-the-docs/issues">open an issue</a> or <a href="https://github.com/just-the-docs/just-the-docs/discussions">start a discussion</a> and let us know!</p>

<h3 id="trying-out-pre-release-v040rc1">Trying out pre-release <code class="language-plaintext highlighter-rouge">v0.4.0.rc1</code></h3>

<p>Due to the massive scope of these changes, we’re making <code class="language-plaintext highlighter-rouge">v0.4.0.rc1</code> available as a <strong>release candidate</strong> for the theme (i.e., a pre-release) with release <code class="language-plaintext highlighter-rouge">v0.4.0</code> coming soon. We want your help in testing the changes! As of now, the gem on RubyGems and the repository are updated to <code class="language-plaintext highlighter-rouge">v0.4.0.rc1</code>.</p>

<p>To use this RC explicitly as a remote theme:</p>

<div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.4.0.rc1</span>
</code></pre></div></div>

<p>To use this RC explicitly as a gem-based theme, pin the version in your <code class="language-plaintext highlighter-rouge">Gemfile</code> and re-run <code class="language-plaintext highlighter-rouge">bundle install</code> or <code class="language-plaintext highlighter-rouge">bundle update just-the-docs</code>:</p>

<div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.4.0.rc1"</span>
</code></pre></div></div>

<h3 id="staying-on-v033">Staying on <code class="language-plaintext highlighter-rouge">v0.3.3</code></h3>

<p>If you’re not ready to make the switch, that’s alright! If your version of just-the-docs is pinned to <code class="language-plaintext highlighter-rouge">v0.3.3</code> (i.e. by a <code class="language-plaintext highlighter-rouge">Gemfile.lock</code> or in <code class="language-plaintext highlighter-rouge">remote_theme</code>, then there’s nothing you need to do.</p>

<p>If you have not pinned your theme version, you should either:</p>

<ol>
  <li>pin your gem version in your <code class="language-plaintext highlighter-rouge">Gemfile</code>, like so
    <div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">gem</span> <span class="s2">"just-the-docs"</span><span class="p">,</span> <span class="s2">"0.3.3"</span>
</code></pre></div>    </div>
  </li>
  <li>freeze the <code class="language-plaintext highlighter-rouge">remote_theme</code>, like so
    <div class="language-yml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="na">remote_theme</span><span class="pi">:</span> <span class="s">just-the-docs/just-the-docs@v0.3.3</span>
</code></pre></div>    </div>
  </li>
</ol>

<p class="warning">Use of branches for closed PRs (e.g., <a href="https://github.com/just-the-docs/just-the-docs/pull/466">#466</a>, <a href="https://github.com/just-the-docs/just-the-docs/pull/578">#578</a>) is now deprecated, as those branches have been (directly or indirectly) merged, and they may be deleted after the pre-release of <code class="language-plaintext highlighter-rouge">v0.4.0.rc1</code>.</p>

<h3 id="maintenance-1">Maintenance</h3>

<p>Internally, our maintainer team has expanded: <a href="https://github.com/pmarsceill">Patrick Marsceill</a>, the original maintainer, has stepped down from an active role after almost 4 years! We’re very thankful for the work that he’s done to create and maintain one of the most popular Jekyll themes. Please join us in giving him thanks!</p>

<p>The new core team currently consists of <a href="https://github.com/mattxwang">@mattxwang</a>, <a href="https://github.com/pdmosses">@pdmosses</a>, <a href="https://github.com/skullface">@skullface</a>, <a href="https://github.com/dougaitken">@dougaitken</a>, and <a href="https://github.com/max06">@max06</a>. Over the past six months, we’ve been triaging and merging in PRs, as well as contributing our own fixes. We’ll continue to address open issues, merge in PRs from the community, and plan out the future of Just the Docs. If you’d like to contribute, now is a great time!</p>

<h3 id="roadmap">Roadmap</h3>

<p>In the short-term, we’re committed to tidying up everything for a <code class="language-plaintext highlighter-rouge">v0.4.0</code> release. This involves fixing bugs reported from the community in this pre-release, as well as continually merging in minor PRs.</p>

<p>We’re also scoping out medium and long-term projects, and want to keep you in the loop. These include:</p>

<ul>
  <li>upgrading to Jekyll 4, and stopping support for Jekyll 3</li>
  <li>versioned docs - issue <a href="https://github.com/just-the-docs/just-the-docs/issues/728">#728</a></li>
  <li>improved accessibility - issues <a href="https://github.com/just-the-docs/just-the-docs/issues/566">#566</a>, <a href="https://github.com/just-the-docs/just-the-docs/issues/870">#870</a></li>
  <li>internationalization (i18n) - issue <a href="https://github.com/just-the-docs/just-the-docs/issues/59">#59</a></li>
  <li>recursive/multi-level navigation - PR <a href="https://github.com/just-the-docs/just-the-docs/pull/462">#462</a></li>
  <li>toggleable dark mode - issue <a href="https://github.com/just-the-docs/just-the-docs/issues/234">#234</a></li>
</ul>

<p>as well as DX improvements like better regression tests, CI, and tooling. If you’re interested in any of these, please join us <a href="https://github.com/just-the-docs/just-the-docs">on GitHub</a> - any contribution (raising an issue, writing docs, or submitting a PR) is welcome!</p>

<h3 id="features-2">Features</h3>

<ul>
  <li>Added: Combination by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/578">#578</a>
    <ul>
      <li>Added: dark highlighting in <a href="https://github.com/just-the-docs/just-the-docs/pull/463">#463</a></li>
      <li>Added: pages and collections in <a href="https://github.com/just-the-docs/just-the-docs/pull/448">#448</a></li>
      <li>Added: callouts in <a href="https://github.com/just-the-docs/just-the-docs/pull/466">#466</a></li>
      <li>Fixed: breadcrumb behaviour … by <a href="https://github.com/AdityaTiwari2102">@AdityaTiwari2102</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/477">#477</a></li>
      <li>Fixed: prevent rake command corrupting search data in <a href="https://github.com/just-the-docs/just-the-docs/pull/495">#495</a> (also listed below)</li>
      <li>Fixed: nested lists in <a href="https://github.com/just-the-docs/just-the-docs/pull/496">#496</a></li>
      <li>Fixed: set color for search input in <a href="https://github.com/just-the-docs/just-the-docs/pull/498">#498</a> (also listed below)</li>
      <li>Fixed: sites with no child pages (no PR)</li>
      <li>Fixed: TOC/breadcrumbs for multiple collections in <a href="https://github.com/just-the-docs/just-the-docs/pull/494">#494</a></li>
      <li>Added: collection configuration option <code class="language-plaintext highlighter-rouge">nav_fold</code> (no PR)</li>
      <li>Fixed: indentation and color for folded collection navigation (no PR)</li>
      <li>Fixed: scroll navigation to show the link to the current page in <a href="https://github.com/just-the-docs/just-the-docs/pull/639">#639</a></li>
      <li>Fixed: Replace all uses of <code class="language-plaintext highlighter-rouge">absolute_url</code> by <code class="language-plaintext highlighter-rouge">relative_url</code>, by <a href="https://github.com/svrooij">@svrooij</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/544">#544</a></li>
    </ul>
  </li>
  <li>Added: custom favicon <code class="language-plaintext highlighter-rouge">_includes</code> by <a href="https://github.com/burner1024">@burner1024</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/364">#364</a></li>
  <li>Added: set color for search input by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/498">#498</a></li>
  <li>Added: search placeholder configuration by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/613">#613</a></li>
  <li>Added: ‘child_nav_order’ front matter to be able to sort navigation pages in reverse by <a href="https://github.com/jmertic">@jmertic</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/726">#726</a></li>
  <li>Added: <code class="language-plaintext highlighter-rouge">nav_footer_custom</code> include by <a href="https://github.com/nathanjessen">@nathanjessen</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/474">#474</a></li>
  <li>Added: style fixes for jekyll-asciidoc by <a href="https://github.com/alyssais">@alyssais</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/829">#829</a></li>
  <li>Added: mermaid.js support by <a href="https://github.com/nascosto">@nascosto</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/857">#857</a></li>
  <li>Added: support for external navigation links by <a href="https://github.com/SPGoding">@SPGoding</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/876">#876</a></li>
  <li>Added: refactor <code class="language-plaintext highlighter-rouge">mermaid</code> config to use <code class="language-plaintext highlighter-rouge">mermaid_config.js</code> include, only require <code class="language-plaintext highlighter-rouge">mermaid.version</code> in <code class="language-plaintext highlighter-rouge">_config.yml</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/909">#909</a></li>
  <li>Fixed: prepend <code class="language-plaintext highlighter-rouge">site.collections_dir</code> if exists by <a href="https://github.com/alexsegura">@alexsegura</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/519">#519</a></li>
  <li>Fixed: nested task lists (#517) by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/855">#855</a></li>
  <li>Fixed: suppress Liquid processing in CSS comments by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/686">#686</a></li>
  <li>Fixed: prevent rake command from corrupting search data by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/495">#495</a></li>
  <li>Fixed: anchor heading links should be visible on focus by <a href="https://github.com/jacobhq">@jacobhq</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/846">#846</a></li>
  <li>Fixed: add <code class="language-plaintext highlighter-rouge">overflow-x: auto</code> to <code class="language-plaintext highlighter-rouge">figure.highlight</code> by <a href="https://github.com/iridazzle">@iridazzle</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/727">#727</a></li>
  <li>Fixed: add <code class="language-plaintext highlighter-rouge">overflow-wrap: word-break</code> to <code class="language-plaintext highlighter-rouge">body</code> by <a href="https://github.com/iridazzle">@iridazzle</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/889">#889</a></li>
  <li>Fixed: vertical alignment for consecutive labels by <a href="https://github.com/Eisverygoodletter">@Eisverygoodletter</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/893">#893</a></li>
  <li>Fixed: allow links to wrap by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/905">#905</a></li>
  <li>Fixed: nav scroll feature and absolute/relative URLs by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/898">#898</a></li>
</ul>

<h3 id="documentation-10">Documentation</h3>

<ul>
  <li>Added: docs on how to break an <code class="language-plaintext highlighter-rouge">ol</code> by <a href="https://github.com/pdmosses">@pdmosses</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/856">#856</a></li>
  <li>Added: docs for custom includes by <a href="https://github.com/nathanjessen">@nathanjessen</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/806">#806</a></li>
  <li>Added: document caveat about variable dependencies by <a href="https://github.com/waldyrious">@waldyrious</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/555">#555</a></li>
  <li>Added: docs on how to use <code class="language-plaintext highlighter-rouge">custom_head</code> to add a custom favicon by <a href="https://github.com/UnclassedPenguin">@UnclassedPenguin</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/814">#814</a></li>
  <li>Fixed: <code class="language-plaintext highlighter-rouge">ol</code> on <code class="language-plaintext highlighter-rouge">index.md</code> by <a href="https://github.com/pmarsceill">@pmarsceill</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/778">#778</a></li>
  <li>Fixed: image link in Markdown kitchen sink by <a href="https://github.com/JeffGuKang">@JeffGuKang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/221">#221</a></li>
  <li>Fixed: images in Markdown kitchen sink by <a href="https://github.com/dougaitken">@dougaitken</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/782">#782</a></li>
  <li>Fixed: clearer label of link to Jekyll quickstart by <a href="https://github.com/waldyrious">@waldyrious</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/549">#549</a></li>
  <li>Fixed: remove extra spaces in component docs by <a href="https://github.com/MichelleBlanchette">@MichelleBlanchette</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/554">#554</a></li>
  <li>Fixed: double “your” typo in <code class="language-plaintext highlighter-rouge">index.md</code> by <a href="https://github.com/sehilyi">@sehilyi</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/499">#499</a></li>
  <li>Fixed: “you” -&gt; “your” typo in <code class="language-plaintext highlighter-rouge">index.md</code> by <a href="https://github.com/nathanjessen">@nathanjessen</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/473">#473</a></li>
  <li>Fixed: spacing in toc example by <a href="https://github.com/henryiii">@henryiii</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/835">#835</a></li>
  <li>Fixed: typo in <code class="language-plaintext highlighter-rouge">README</code> on <code class="language-plaintext highlighter-rouge">_config.yml</code> by <a href="https://github.com/ivanskodje">@ivanskodje</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/891">#891</a></li>
  <li>Fixed: missing code fence in navigation structure docs by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/906">#906</a></li>
</ul>

<h3 id="maintenance-2">Maintenance</h3>

<ul>
  <li>Added: VScode devcontainer by <a href="https://github.com/max06">@max06</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/783">#783</a></li>
  <li>Added: <code class="language-plaintext highlighter-rouge">webrick</code> to <code class="language-plaintext highlighter-rouge">Gemfile</code> by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/799">#799</a></li>
  <li>Added: ‘This site is powered by Netlify.’ to the footer by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/797">#797</a></li>
  <li>Updated: new repo path by <a href="https://github.com/pmarsceill">@pmarsceill</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/775">#775</a></li>
  <li>Updated: rename <code class="language-plaintext highlighter-rouge">master</code> -&gt; <code class="language-plaintext highlighter-rouge">main</code> by <a href="https://github.com/pmarsceill">@pmarsceill</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/776">#776</a></li>
  <li>Updated: README by <a href="https://github.com/pmarsceill">@pmarsceill</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/777">#777</a></li>
  <li>Updated: Code of Conduct to Contributor Covenant v2.1 by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/790">#790</a></li>
  <li>Updated: CI files, Ruby &amp; Node Versions by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/820">#820</a></li>
  <li>Updated: Stylelint to v14, extend SCSS plugins, remove primer-* configs, resolve issues by <a href="https://github.com/mattxwang">@mattxwang</a> in <a href="https://github.com/just-the-docs/just-the-docs/pull/821">#821</a></li>
</ul>

<h3 id="dependencies">Dependencies</h3>

<ul>
  <li>Upgrade to GitHub-native Dependabot by @dependabot-preview in <a href="https://github.com/just-the-docs/just-the-docs/pull/627">#627</a></li>
  <li>[Security] Bump y18n from 3.2.1 to 3.2.2 by @dependabot-preview in <a href="https://github.com/just-the-docs/just-the-docs/pull/606">#606</a></li>
  <li>[Security] Bump hosted-git-info from 2.7.1 to 2.8.9 by @dependabot-preview in <a href="https://github.com/just-the-docs/just-the-docs/pull/641">#641</a></li>
  <li>[Security] Bump lodash from 4.17.19 to 4.17.21 by @dependabot-preview in <a href="https://github.com/just-the-docs/just-the-docs/pull/640">#640</a></li>
  <li>[Security] Bump ini from 1.3.5 to 1.3.8 by @dependabot-preview in <a href="https://github.com/just-the-docs/just-the-docs/pull/511">#511</a></li>
  <li>Bump path-parse from 1.0.6 to 1.0.7 by @dependabot in <a href="https://github.com/just-the-docs/just-the-docs/pull/699">#699</a></li>
  <li>Bump ajv from 6.10.0 to 6.12.6 by @dependabot in <a href="https://github.com/just-the-docs/just-the-docs/pull/766">#766</a></li>
  <li>Bump prettier from 2.1.2 to 2.5.1 by @dependabot in <a href="https://github.com/just-the-docs/just-the-docs/pull/787">#787</a></li>
  <li>Bump prettier from 2.5.1 to 2.6.2 by @dependabot in <a href="https://github.com/just-the-docs/just-the-docs/pull/809">#809</a></li>
  <li>Bump prettier from 2.6.2 to 2.7.1 by @dependabot in <a href="https://github.com/just-the-docs/just-the-docs/pull/864">#864</a></li>
</ul>

<h3 id="new-contributors-13">New Contributors</h3>

<ul>
  <li><a href="https://github.com/AdityaTiwari2102">@AdityaTiwari2102</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/477">#477</a></li>
  <li><a href="https://github.com/svrooij">@svrooij</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/544">#544</a></li>
  <li><a href="https://github.com/alexsegura">@alexsegura</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/519">#519</a></li>
  <li><a href="https://github.com/burner1024">@burner1024</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/364">#364</a></li>
  <li><a href="https://github.com/JeffGuKang">@JeffGuKang</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/221">#221</a></li>
  <li><a href="https://github.com/dougaitken">@dougaitken</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/782">#782</a></li>
  <li><a href="https://github.com/max06">@max06</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/783">#783</a></li>
  <li><a href="https://github.com/sehilyi">@sehilyi</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/499">#499</a></li>
  <li><a href="https://github.com/nathanjessen">@nathanjessen</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/473">#473</a></li>
  <li><a href="https://github.com/waldyrious">@waldyrious</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/549">#549</a></li>
  <li><a href="https://github.com/MichelleBlanchette">@MichelleBlanchette</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/554">#554</a></li>
  <li><a href="https://github.com/henryiii">@henryiii</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/835">#835</a></li>
  <li><a href="https://github.com/jmertic">@jmertic</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/726">#726</a></li>
  <li><a href="https://github.com/jacobhq">@jacobhq</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/846">#846</a></li>
  <li><a href="https://github.com/UnclassedPenguin">@UnclassedPenguin</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/814">#814</a></li>
  <li><a href="https://github.com/alyssais">@alyssais</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/829">#829</a></li>
  <li><a href="https://github.com/nascosto">@nascosto</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/857">#857</a></li>
  <li><a href="https://github.com/SPGoding">@SPGoding</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/876">#876</a></li>
  <li><a href="https://github.com/iridazzle">@iridazzle</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/727">#727</a></li>
  <li><a href="https://github.com/ivanskodje">@ivanskodje</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/891">#891</a></li>
  <li><a href="https://github.com/Eisverygoodletter">@Eisverygoodletter</a> made their first contribution in <a href="https://github.com/just-the-docs/just-the-docs/pull/893">#893</a></li>
</ul>

<p><strong>Full Changelog</strong>: https://github.com/just-the-docs/just-the-docs/compare/v0.3.3…v0.4.0.rc1</p>

<h2 id="v033">v0.3.3</h2>

<h3 id="-features">🚀 Features</h3>

<ul>
  <li>Add custom header and footer include files @CodeSandwich (#334)</li>
</ul>

<h3 id="-bug-fixes">🐛 Bug Fixes</h3>

<ul>
  <li>Limit the effect of <code class="language-plaintext highlighter-rouge">nav_exclude</code> to the main navigation @pdmosses (#443)</li>
  <li>Update normalize.scss @pdmosses (#444)</li>
  <li>Update code.scss @pdmosses (#445)</li>
  <li>Fix list alignment @pdmosses (#446)</li>
</ul>

<h3 id="-maintenance">🧰 Maintenance</h3>

<ul>
  <li>Bump stylelint-config-primer from 9.0.0 to 9.2.1 @dependabot-preview (#451)</li>
  <li>Bump stylelint from 13.6.1 to 13.7.2 @dependabot-preview (#440)</li>
  <li>Bump @primer/css from 15.1.0 to 15.2.0 @dependabot-preview (#436)</li>
  <li>Bump prettier from 2.1.1 to 2.1.2 @dependabot-preview (#429)</li>
</ul>

<h2 id="v032">v0.3.2</h2>

<h3 id="changes">Changes</h3>

<ul>
  <li>Safe page sorting @pdmosses (#411)</li>
  <li>v0.3.2 @pmarsceill (#388)</li>
</ul>

<h3 id="-features-1">🚀 Features</h3>

<ul>
  <li>make font-sizes sass variables so they can be changed @pdebruic (#361)</li>
  <li>run the site locally inside docker container @fogfish (#398)</li>
  <li>Feature/doc collections @SgtSilvio (#379)</li>
  <li>Adjust dl layout @pdmosses (#401)</li>
</ul>

<h3 id="-bug-fixes-1">🐛 Bug Fixes</h3>

<ul>
  <li>Add site.gh_edit_source to “Edit this page on GitHub” link @mrfleap (#418)</li>
  <li>Inhibit text-transform for code in h4 @pdmosses (#404)</li>
  <li>Fix native font stack precedence issue on Windows systems. @hvianna (#331)</li>
  <li>Support for the linenos option on highlighted code @pdmosses (#375)</li>
  <li>Update anchor_headings.html @pdmosses (#399)</li>
  <li>Fix https @marksie1988 (#359)</li>
</ul>

<h3 id="-maintenance-1">🧰 Maintenance</h3>

<ul>
  <li>Bump prettier from 2.0.5 to 2.1.1 @dependabot-preview (#427)</li>
  <li>Bump prettier from 2.0.5 to 2.1.1 @dependabot-preview (#419)</li>
  <li>[Security] Bump lodash from 4.17.15 to 4.17.19 @dependabot-preview (#389)</li>
  <li>Bump @primer/css from 14.4.0 to 15.1.0 @dependabot-preview (#402)</li>
  <li>Bump lodash from 4.17.15 to 4.17.19 @dependabot (#384)</li>
  <li>Bump @primer/css from 14.4.0 to 15.0.0 @dependabot-preview (#371)</li>
</ul>

<h2 id="v031">v0.3.1</h2>

<h3 id="changes-1">Changes</h3>

<h3 id="-bug-fixes-2">🐛 Bug Fixes</h3>

<ul>
  <li>Improve accessibility by adding label to Anchor links. @mscoutermarsh (#376)</li>
</ul>

<h3 id="-maintenance-2">🧰 Maintenance</h3>

<ul>
  <li>Remove collapsible TOC on nav doc @pmarsceill (#368)</li>
  <li>Pdmosses collapsible toc @pmarsceill (#367)</li>
</ul>

<h2 id="v030">v0.3.0</h2>

<h3 id="changes-2">Changes</h3>

<ul>
  <li>v0.2.9 @pmarsceill (#306)</li>
</ul>

<h3 id="-features-2">🚀 Features</h3>

<ul>
  <li>Add print styles @pmarsceill (#362)</li>
  <li>Navigation improvements and search sections @SgtSilvio (#352)</li>
</ul>

<h3 id="-bug-fixes-3">🐛 Bug Fixes</h3>

<ul>
  <li>Remove constraint with jekyll 4.1.0 @PierrickMartos (#348)</li>
</ul>

<h3 id="-maintenance-3">🧰 Maintenance</h3>

<ul>
  <li>Bump version numbers @pmarsceill (#360)</li>
  <li>Bump stylelint from 13.3.3 to 13.6.1 @dependabot-preview (#343)</li>
  <li>Bump stylelint-config-prettier from 8.0.1 to 8.0.2 @dependabot-preview (#349)</li>
</ul>

<h2 id="v029">v0.2.9</h2>

<h3 id="bug-fixes">Bug fixes</h3>
<ul>
  <li>Horizontal Alignment #103 @pmarsceill</li>
  <li>Code snippet in headers do not inherit font size #140 @pmarsceill</li>
  <li>Fix duplicated title and description tags #294 @iefserge</li>
  <li>Update nav.html for handling nav_exclude #282 @blawqchain</li>
  <li>Fix duplicate entries in nav.html and default.html #239 @KasparEtter</li>
  <li>Don’t show pages with no title (e.g. redirects in nav) https://github.com/pmarsceill/just-the-docs/pull/295/commits/672de29f2e332a9350af7237e4fb6693c848989e @SgtSilvio</li>
  <li>[SEARCH RAKE] Fix search generator #319 @RoiArthurB</li>
</ul>

<h3 id="enhancements">Enhancements</h3>
<ul>
  <li>Improvement/custom themes #186 @SgtSilvio</li>
  <li>feat: adds “edit this page” and “page last modified” to footer #217 @malsf21</li>
  <li>feat: adds option to open aux links in new tab #229 @malsf21</li>
  <li>Default nav order #236 @pdmosses</li>
  <li>Enable IP anonymization in Google Analytics (GDPR) #250 @r-brown</li>
</ul>

<p>closes #240 #308 #266 #140 #103</p>

<h2 id="v028">v0.2.8</h2>

<h3 id="bugfixes-15">Bugfixes</h3>
<ul>
  <li>bugfix in search.rake #218 @tiaitsch85</li>
</ul>

<h3 id="dependency-and-security-updates">Dependency and security updates:</h3>

<ul>
  <li>Update jekyll requirement from ~&gt; 3.8.5 to &gt;= 3.8.5, &lt; 4.1.0 #197 @dependabot-preview</li>
  <li>Update rake requirement from ~&gt; 12.3.1 to &gt;= 12.3.1, &lt; 13.1.0 #227 @dependabot-preview</li>
  <li>Bump stylelint-config-primer from 8.0.0 to 9.0.0 #247 @dependabot-preview</li>
  <li>Update bundler requirement from ~&gt; 2.0.1 to ~&gt; 2.1.4 #268 @dependabot-preview</li>
  <li>Bump @primer/css from 12.7.0 to 14.3.0 #296 @dependabot-preview</li>
</ul>

<h3 id="operations">Operations</h3>

<ul>
  <li>Update CI to test multiple versions of Jekyll</li>
  <li>Update CI to check the rake command that builds the search file</li>
</ul>

<p>fixes #291 #256 #293 #177</p>

<h2 id="v027">v0.2.7</h2>

<h3 id="bugs-fixed">Bugs fixed</h3>
<ul>
  <li>Anchor headings are now displayed on hover, not only on heading hover</li>
  <li>Deduplicated anchor heading svg</li>
  <li>If last page of <code class="language-plaintext highlighter-rouge">site.html_pages</code> was excluded from search, search json breaks</li>
  <li>Config variable should be <code class="language-plaintext highlighter-rouge">blanklines</code> not <code class="language-plaintext highlighter-rouge">blank_lines</code> for html compression</li>
  <li><code class="language-plaintext highlighter-rouge">list-style-none</code> does not hide bullets on <code class="language-plaintext highlighter-rouge">ul</code></li>
</ul>

<h3 id="enhancements-1">Enhancements</h3>
<ul>
  <li>Summary for child pages appears in generated TOC</li>
  <li>Site logo configuration supported replacing title text with image</li>
  <li>Allow custom CSS overrides (new scss partial at the end of the cascade) separate from variable overrides.</li>
  <li>Configuration around search strings added to allow search for hyphenated words</li>
</ul>

<h3 id="maintenance-3">Maintenance</h3>
<ul>
  <li>Update docs to suggest using index.md as section page filename</li>
  <li>Bump @primer/css from 12.6.0 to 12.7.0</li>
  <li>Bump mixin-deep from 1.3.1 to 1.3.2</li>
  <li>Bump stylelint-config-primer from 7.0.1 to 8.0.0</li>
</ul>

<h3 id="pr-included">PR included</h3>
<ul>
  <li>#98 by @stefanoborini Introduces the possibility for a summary in the table of contents</li>
  <li>#141 by @ghabs Fix trailing comma bug in search-data.json</li>
  <li>#153 by @jacobherrington Change button copy on theme preview</li>
  <li>#181 by @m3nu Recommend using index.md as parent page for sections</li>
  <li>#183 by @SgtSilvio Improve heading anchors</li>
  <li>#187 by @SgtSilvio Improvement/site logo</li>
  <li>#200 Bump mixin-deep from 1.3.1 to 1.3.2</li>
  <li>#203 by @pdmosses Search config</li>
  <li>#205 by @pdmosses Fix blank_lines var to blanklines in config.yml</li>
  <li>#206 by @iamcarrico Allow for custom overrides by the user</li>
  <li>#208 Bump @primer/css from 12.6.0 to 12.7.0</li>
  <li>#213 Bump mixin-deep from 1.3.1 to 1.3.2</li>
  <li>#214 Bump stylelint-config-primer from 7.0.1 to 8.0.0</li>
  <li>#215 Bump @primer/css from 12.6.0 to 12.7.0</li>
</ul>

<h2 id="v026">v0.2.6</h2>

<h3 id="bugs-fixed-1">Bugs fixed</h3>
<ul>
  <li>Google Analytics tag has been updated #162</li>
  <li>~BaseURL has been modified #109~ Reverted – seems the existing implementation worked</li>
  <li>Titles can now wrap fixes #106</li>
</ul>

<h3 id="enhancements-2">Enhancements</h3>
<ul>
  <li>Search now displays content preview #135</li>
  <li>Custom footer content added #179</li>
  <li>Now using GitHub Actions for CI #170</li>
</ul>

<h3 id="maintenance-4">Maintenance</h3>
<ul>
  <li>lunrjs upgraded #135</li>
  <li>Nav generation is optimized #159</li>
  <li>Stylelint upgrade #143</li>
  <li>Stylelint config primer upgrade #149</li>
  <li>Lodash upgrade #160</li>
</ul>

<h3 id="pr-included-1">PR included</h3>
<p>~#109 by @daviddarnes - Fix baseurl link~ Reverted
#135 by @SgtSilvio - Upgrades lunr.js, improves search UI, adds heading anchors
#152 by @yavorg - Improves syntax highlighting for js readablity
#159 by @julienduchesne - Optimizes nav generation
#162 by @nergmada - Modifies the google analytics code to match the new tags used by GA</p>

<h2 id="v025">v0.2.5</h2>

<h3 id="bugs-fixed-2">Bugs fixed</h3>

<ul>
  <li>Duplicate title tag when Jekyll SEO Plugin gem is used #125 #126</li>
</ul>

<h3 id="enhancements-3">Enhancements</h3>

<ul>
  <li>Favicon support added #118</li>
</ul>

<h3 id="maintenance-5">Maintenance</h3>
<ul>
  <li>Bump stylelint-config-primer from 6.0.0 to 7.0.0  #123</li>
  <li>Bump @primer/css from 12.2.3 to 12.3.1 #129</li>
  <li>Add workflow to publish to GPR</li>
  <li>Fix workflow to publish to Ruby Gems</li>
</ul>

<h2 id="v024">v0.2.4</h2>

<h3 id="bugs">Bugs</h3>

<ul>
  <li>#102 Remove unnecessary console.log() @JoeNyland</li>
  <li>#97 Import custom Sass variable overrides before default variables are defined @montchr and @ptvandi</li>
</ul>

<h3 id="additions">Additions</h3>
<ul>
  <li>#117 Add links to docs for setting up GH pages locally @gnarea</li>
  <li>#95 Add SEO and ‘lang’ param for <code class="language-plaintext highlighter-rouge">_config</code> @gebeto</li>
</ul>

<h2 id="v023">v0.2.3</h2>

<h3 id="enhancements-4">Enhancements</h3>
<ul>
  <li>Adds ability to use Google Analytics tracking by @pmarsceill</li>
</ul>

<h3 id="bug-fixes-1">Bug fixes</h3>
<ul>
  <li>Fixes 404 error for “/assets/js//search-data.json” by @stephenedmondson</li>
  <li>Fixes #80 Single quotes in the string were unescaped and ruby attempted variable substitution of amp within it (which failed) by @novelistparty</li>
  <li>Fixes bug that would only show 2 or more search results (not one) by @ilivewithian</li>
  <li>Fixes a typo on the layout example by @woernfl</li>
  <li>Fixes #78 Page scroll position too far down on load by @pmarsceill</li>
  <li>Fixds ability to nest ul in ol without breaking style or counters</li>
</ul>

<h3 id="dependency-updates">Dependency updates</h3>
<ul>
  <li>Bumps stylelint dependency from 9.9.0 to 9.10.1</li>
</ul>

<h2 id="v022">v0.2.2</h2>

<ul>
  <li>Bumps stylelint-config-primer to 3.0.1 #44</li>
  <li>Bumps bundler req to 2.0.1 #61</li>
  <li>Adds custom 404 page</li>
  <li>Excludes package-lock.json from jekyll build #47</li>
  <li>Fixes keyboard scrolling / focus #48</li>
  <li>Adds ARIA roles to navigation elements</li>
  <li>Adds support for optional page description metadata (if present in yaml front matter)</li>
  <li>Addresses some issues with search in #46</li>
  <li>Option to hide TOC on parent pages if turned off in page’s YAML front matter #30</li>
  <li>Option to suppress an item from being indexed by search if present in page’s YAML front matter #32</li>
</ul>

<h2 id="v021">v0.2.1</h2>

<p>This update fixes security vulnerabilities in the lodash sub-dependency and bumps other dev dependencies to their latest version.</p>

<h2 id="v020">v0.2.0</h2>

<p>Adds:</p>
<ul>
  <li>Dark mode via <code class="language-plaintext highlighter-rouge">color_scheme</code> parameter</li>
  <li>Ability to exclude a page from the main nav with <code class="language-plaintext highlighter-rouge">nav_exclude</code> parameter closes #21</li>
  <li>Ability for create children of children pages (3 nav levels) closes #25</li>
</ul>

<p>Changes:</p>
<ul>
  <li>Permalink structure for tiered navigation has been updated</li>
  <li>Some colors have been updated for consistency / accessibility</li>
</ul>

<h2 id="v016">v0.1.6</h2>

<h3 id="added">Added</h3>

<ul>
  <li>Support for task list styles #19</li>
  <li>Configuration docs</li>
  <li>Configuration option to enable / disable search</li>
  <li>Normalize.scss dependency pulled into project #16 #</li>
</ul>

<h3 id="fixed">Fixed</h3>

<ul>
  <li>Layout bug in navigation #17</li>
</ul>

<h2 id="v015">v0.1.5</h2>

<p>Major changes:</p>

<ul>
  <li>Fixed bug where the rake task would fail when the assets/js directory didn’t exist</li>
</ul>

<h2 id="v014">v0.1.4</h2>

<p>Major changes:</p>
<ul>
  <li>Adds Rake as a runtime dependency</li>
  <li>Definition list styled</li>
  <li>Sidebar and support cleaned up for smaller screen support</li>
  <li>Updated some stale docs</li>
</ul>

<h2 id="v013">v0.1.3</h2>

<p>Major changes:</p>
<ul>
  <li>Fix path problems, typos, and general clean-up for OSS.</li>
</ul>

<h2 id="v012">v0.1.2</h2>

<p>Fix paths when deployed to gh-pages</p>

<h2 id="v011">v0.1.1</h2>

<p>Major updates:</p>
<ul>
  <li>Adds search to mobile nav</li>
  <li>Pulls footer to bottom of the page on mobile (not hidden in nav)</li>
</ul>

<p>Minor updates:</p>
<ul>
  <li>Cleans up h1 typography spacing</li>
</ul>


</div>
