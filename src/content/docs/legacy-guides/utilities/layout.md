---
title: 布局
slug: legacy-guides/utilities/layout
legacySource: docs/Usage Guidelines/utilities/layout.md
legacyUrl: /docs/Usage Guidelines/utilities/layout/
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 class="no_toc" id="布局实用程序">布局实用程序</h1>

<h2 class="no_toc text-delta" id="目录">目录</h2>

<ol id="markdown-toc">
  <li><a href="#spacing" id="markdown-toc-spacing">spacing</a></li>
  <li><a href="#horizontal-alignment" id="markdown-toc-horizontal-alignment">Horizontal Alignment</a></li>
  <li><a href="#vertical-alignment" id="markdown-toc-vertical-alignment">Vertical Alignment</a></li>
  <li><a href="#display" id="markdown-toc-display">Display</a></li>
</ol>

<hr />

<h2 id="spacing">spacing</h2>

<p>这些间隔符可用于响应式实用程序类的边距和填充。将这些前缀与屏幕尺寸和间距比例相结合，即可响应式地使用它们。
| Classname prefix | Related CSS Property          |
|:—————–|:——————————|
| <code class="language-plaintext highlighter-rouge">.m-</code>            | <code class="language-plaintext highlighter-rouge">margin</code>                      |
| <code class="language-plaintext highlighter-rouge">.mx-</code>           | <code class="language-plaintext highlighter-rouge">margin-left</code>, <code class="language-plaintext highlighter-rouge">margin-right</code> |
| <code class="language-plaintext highlighter-rouge">.my-</code>           | <code class="language-plaintext highlighter-rouge">margin top</code>, <code class="language-plaintext highlighter-rouge">margin bottom</code> |
| <code class="language-plaintext highlighter-rouge">.mt-</code>           | <code class="language-plaintext highlighter-rouge">margin-top</code>                  |
| <code class="language-plaintext highlighter-rouge">.mr-</code>           | <code class="language-plaintext highlighter-rouge">margin-right</code>                |
| <code class="language-plaintext highlighter-rouge">.mb-</code>           | <code class="language-plaintext highlighter-rouge">margin-bottom</code>               |
| <code class="language-plaintext highlighter-rouge">.ml-</code>           | <code class="language-plaintext highlighter-rouge">margin-left</code>                 |</p>

<table>
  <thead>
    <tr>
      <th style="text-align: left">Classname prefix</th>
      <th style="text-align: left">Related CSS Property</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.p-</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">padding</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.px-</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">padding-left</code>, <code class="language-plaintext highlighter-rouge">padding-right</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.py-</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">padding top</code>, <code class="language-plaintext highlighter-rouge">padding bottom</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.pt-</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">padding-top</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.pr-</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">padding-right</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.pb-</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">padding-bottom</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.pl-</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">padding-left</code></td>
    </tr>
  </tbody>
</table>

<p>Spacing values are based on a <code class="language-plaintext highlighter-rouge">1rem = 16px</code> spacing scale, broken down into these units:</p>

<table>
  <thead>
    <tr>
      <th style="text-align: left">Spacer/suffix</th>
      <th style="text-align: left">Size in rems</th>
      <th style="text-align: left">Rem converted to px</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">1</code></td>
      <td style="text-align: left">0.25rem</td>
      <td style="text-align: left">4px</td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">2</code></td>
      <td style="text-align: left">0.5rem</td>
      <td style="text-align: left">8px</td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">3</code></td>
      <td style="text-align: left">0.75rem</td>
      <td style="text-align: left">12px</td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">4</code></td>
      <td style="text-align: left">1rem</td>
      <td style="text-align: left">16px</td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">5</code></td>
      <td style="text-align: left">1.5rem</td>
      <td style="text-align: left">24px</td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">6</code></td>
      <td style="text-align: left">2rem</td>
      <td style="text-align: left">32px</td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">7</code></td>
      <td style="text-align: left">2.5rem</td>
      <td style="text-align: left">40px</td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">8</code></td>
      <td style="text-align: left">3rem</td>
      <td style="text-align: left">48px</td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">auto</code></td>
      <td style="text-align: left">auto</td>
      <td style="text-align: left">auto</td>
    </tr>
  </tbody>
</table>

<p>Use <code class="language-plaintext highlighter-rouge">mx-auto</code> to horizontally center elements.</p>

<h3 class="no_toc text-delta" id="applying-spacing-utilities-with--">Applying Spacing Utilities with <code class="language-plaintext highlighter-rouge">{: }</code></h3>

<p>In Markdown, use the <code class="language-plaintext highlighter-rouge">{: }</code> wrapper to apply custom classes:</p>

<div class="language-markdown highlighter-rouge"><div class="highlight"><pre class="highlight"><code>This paragraph will have a margin bottom of 1rem/16px on large screens.
{: .mb-lg-4 }

This paragraph will have 2rem/32px of padding on the right and left at all screen sizes.
{: .px-6 }
</code></pre></div></div>

<h2 id="horizontal-alignment">Horizontal Alignment</h2>

<table>
  <thead>
    <tr>
      <th style="text-align: left">CSS Class</th>
      <th style="text-align: left">Applied CSS Declaration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.float-left</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">float: left</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.float-right</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">float: right</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.flex-justify-start</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">justify-content: flex-start</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.flex-justify-end</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">justify-content: flex-end</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.flex-justify-between</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">justify-content: space-between</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.flex-justify-around</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">justify-content: space-around</code></td>
    </tr>
  </tbody>
</table>

<p><em>Note: any of the <code class="language-plaintext highlighter-rouge">flex-</code> classes must be used on a parent element that has <code class="language-plaintext highlighter-rouge">d-flex</code> applied to it.</em></p>

<h2 id="vertical-alignment">Vertical Alignment</h2>

<table>
  <thead>
    <tr>
      <th style="text-align: left">CSS Class</th>
      <th style="text-align: left">Applied CSS Declaration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.v-align-baseline</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">vertical-align: baseline</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.v-align-bottom</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">vertical-align: bottom</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.v-align-middle</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">vertical-align: middle</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.v-align-text-bottom</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">vertical-align: text-bottom</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.v-align-text-top</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">vertical-align: text-top</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.v-align-top</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">vertical-align: top</code></td>
    </tr>
  </tbody>
</table>

<h2 id="display">Display</h2>

<p>Display classes aid in adapting the layout of the elements on a page:</p>

<table>
  <thead>
    <tr>
      <th style="text-align: left">CSS Class</th>
      <th style="text-align: left">Applied CSS Declaration</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.d-block</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">display: block</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.d-flex</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">display: flex</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.d-inline</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">display: inline</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.d-inline-block</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">display: inline-block</code></td>
    </tr>
    <tr>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">.d-none</code></td>
      <td style="text-align: left"><code class="language-plaintext highlighter-rouge">display: none</code></td>
    </tr>
  </tbody>
</table>

<p>Use these classes in conjunction with the responsive modifiers.</p>

<h3 class="no_toc text-delta" id="applying-display-utilities-with--">Applying Display Utilities with <code class="language-plaintext highlighter-rouge">{: }</code></h3>

<p>In Markdown, use the <code class="language-plaintext highlighter-rouge">{: }</code> wrapper to apply custom classes:</p>

<div class="language-markdown highlighter-rouge"><div class="highlight"><pre class="highlight"><code>This button will be hidden until medium screen sizes:

<span class="p">[</span><span class="nv"> A button </span><span class="p">](</span><span class="sx">#url</span><span class="p">)</span>
{: .d-none .d-md-inline-block }

These headings will be <span class="sb">`inline-block`</span>:

<span class="gu">### heading 3</span>
{: .d-inline-block }

<span class="gu">### heading 3</span>
{: .d-inline-block }
</code></pre></div></div>


</div>
