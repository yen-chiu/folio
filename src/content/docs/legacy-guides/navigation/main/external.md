---
title: 外部链接
slug: legacy-guides/navigation/main/external
legacySource: docs/Usage Guidelines/navigation/main/external.md
legacyUrl: /docs/Usage Guidelines/navigation/main/external/
sidebar:
  order: 6
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 id="external-links">External Links</h1>

<p>To add external links to the navigation, add them to the <code class="language-plaintext highlighter-rouge">nav_external_links</code> <a href="/WendellManual/docs/Usage%20Guidelines/configuration/">configuration</a> option in your site’s <code class="language-plaintext highlighter-rouge">_config.yml</code> file.
External links will appear in the navigation after the links to ordinary pages, but before any collections.</p>

<h2 class="text-delta" id="example-external-links">Example: external links</h2>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># External navigation links</span>
<span class="na">nav_external_links</span><span class="pi">:</span>
  <span class="pi">-</span> <span class="na">title</span><span class="pi">:</span> <span class="s">Just the Docs on GitHub</span>
    <span class="na">url</span><span class="pi">:</span> <span class="s">https://github.com/just-the-docs/just-the-docs</span>
    <span class="na">hide_icon</span><span class="pi">:</span> <span class="kc">false</span> <span class="c1"># set to true to hide the external link icon - defaults to false</span>
    <span class="na">opens_in_new_tab</span><span class="pi">:</span> <span class="kc">false</span> <span class="c1"># set to true to open this link in a new tab - defaults to false</span>
</code></pre></div></div>

<h2 id="opening-external-links-in-a-new-tab">Opening external links in a new tab</h2>

<p>The external links are decorated by an icon, which distinguishes them from internal links.
You can suppress the icon by setting <code class="language-plaintext highlighter-rouge">hide_icon: true</code>.</p>

<p>By default, external links are not opened in a new tab. However, this can be enabled by:</p>

<ol>
  <li>setting <code class="language-plaintext highlighter-rouge">opens_in_new_tab: true</code> in the link’s configuration object</li>
  <li>setting the configuration option <code class="language-plaintext highlighter-rouge">nav_external_links_new_tab: true</code> in <code class="language-plaintext highlighter-rouge">_config.yml</code></li>
</ol>

<p>When they conflict, <code class="language-plaintext highlighter-rouge">opens_in_new_tab</code> takes precedence.</p>


</div>
