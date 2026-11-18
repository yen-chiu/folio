---
title: 布局
slug: legacy-guides/layout/layout
legacySource: docs/Usage Guidelines/layout/layout.md
legacyUrl: /docs/Usage Guidelines/layout/layout/
sidebar:
  order: 4.5
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 id="布局layout">布局（Layout）</h1>

<p class="fs-6 fw-300">恁可以在页面的 <a href="https://jekyllrb.com/docs/front-matter/">front matter</a> 中指定布局。Just the Docs 提供了一个带有侧边栏的 <code class="language-plaintext highlighter-rouge">default</code> 布局（主题文档中几乎所有页面都使用该布局），以及一个省略侧边栏的 <code class="language-plaintext highlighter-rouge">minimal</code> 布局。</p>

<h2 id="布局的概念">布局的概念</h2>

<p>请参阅 <a href="https://jekyllrb.com/docs/layouts/">Jekyll 的布局文档页面</a> 了解布局的基本概念以及如何指定它们。</p>

<p>恁可以使用 <a href="https://jekyllrb.com/docs/configuration/front-matter-defaults/">Jekyll 的 front matter 默认值</a> 来为多个页面指定相同的布局。</p>

<h2 id="default-布局"><code class="language-plaintext highlighter-rouge">default</code> 布局</h2>

<p>此页面使用的是 <code class="language-plaintext highlighter-rouge">default</code> 布局。本网站通过 <a href="https://jekyllrb.com/docs/configuration/front-matter-defaults/">front matter 默认值</a> 配置为 <code class="language-plaintext highlighter-rouge">docs</code> 目录下的所有页面设置 <code class="language-plaintext highlighter-rouge">layout: default</code>。</p>

<p>Just the Docs 的默认布局是 <em>响应式布局</em>: 在中宽及以上宽度的显示屏上，会显示一个包含导航面板的侧边栏；在较窄的显示屏上，侧边栏会自动隐藏在一个按钮下。</p>

<p>除了顶级页面以外，所有页面都会自动显示所谓的 <em>breadcrumbs</em>（导航路径）: 链接到它们的父页面以及更高层级的祖先页面。这些 breadcrumbs 显示在页面主要内容的上方。</p>

<p>通常，每个有子页面的页面会在其主要内容下方显示一个指向子页面的链接列表（可以通过在 front matter 中设置 <code class="language-plaintext highlighter-rouge">has_toc: false</code> 来隐藏此功能）。这个链接列表作为一个 <em>目录表</em>（table of contents）显示在页面中。</p>

<h2 id="minimal-布局"><code class="language-plaintext highlighter-rouge">minimal</code> 布局</h2>

<p>本页面的一个子页面和孙页面使用了 <code class="language-plaintext highlighter-rouge">minimal</code> 布局。该布局与 <code class="language-plaintext highlighter-rouge">default</code> 布局的区别在于省略了侧边栏以及导航面板。要在使用 <code class="language-plaintext highlighter-rouge">minimal</code> 布局的页面之间导航，恁可以使用 breadcrumbs 和目录表。</p>

<h2 id="有选择地隐藏或显示侧边栏">有选择地隐藏或显示侧边栏</h2>

<p>可以使用 <a href="https://jekyllrb.com/docs/configuration/front-matter-defaults/">Jekyll 的 front matter 默认值</a> 来为多个页面应用 <code class="language-plaintext highlighter-rouge">minimal</code> 布局。此外，还有一些变量可以控制页面的布局。在 <code class="language-plaintext highlighter-rouge">_config.yml</code> 中，可以通过设置 <code class="language-plaintext highlighter-rouge">nav_enabled: false</code> 来禁用整个站点的侧边栏导航面板。然后可以通过为页面的 front matter 变量分配 <code class="language-plaintext highlighter-rouge">nav_enabled: true</code> 来选择性地在特定页面启用侧边栏。例如，可以在主页上启用侧边栏导航，而其他所有页面禁用它。</p>

<div class="language-yaml highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nn">---</span>
<span class="na">layout</span><span class="pi">:</span> <span class="s">default</span>
<span class="na">title</span><span class="pi">:</span> <span class="s">Home</span>
<span class="na">nav_enabled</span><span class="pi">:</span> <span class="kc">true</span>
<span class="nn">---</span>
</code></pre></div></div>

<h2 id="其他布局">其他布局</h2>

<p>Just the Docs 还提供其他布局: <code class="language-plaintext highlighter-rouge">about</code>、<code class="language-plaintext highlighter-rouge">home</code>、<code class="language-plaintext highlighter-rouge">page</code> 和 <code class="language-plaintext highlighter-rouge">post</code>。目前，它们都基于 <code class="language-plaintext highlighter-rouge">default</code> 布局。有关如何自定义它们，请参阅 <a href="https://jekyllrb.com/docs/layouts/#inheritance">Jekyll 的继承文档</a>。</p>



</div>
