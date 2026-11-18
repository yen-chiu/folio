---
title: 表格
slug: legacy-guides/ui-components/tables
legacySource: docs/Usage Guidelines/ui-components/tables.md
legacyUrl: /docs/Usage Guidelines/ui-components/tables/
sidebar:
  order: 4
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 id="tables">Tables</h1>

<p>Tables are responsive by default, allowing wide tables to have a horizontal scroll to access columns outside of the normal viewport.</p>

<div class="code-example">

  <table>
    <thead>
      <tr>
        <th style="text-align: left">head1</th>
        <th style="text-align: left">head two</th>
        <th style="text-align: left">three</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="text-align: left">ok</td>
        <td style="text-align: left">good swedish fish</td>
        <td style="text-align: left">nice</td>
      </tr>
      <tr>
        <td style="text-align: left">out of stock</td>
        <td style="text-align: left">good and plenty</td>
        <td style="text-align: left">nice</td>
      </tr>
      <tr>
        <td style="text-align: left">ok</td>
        <td style="text-align: left">good <code class="language-plaintext highlighter-rouge">oreos</code></td>
        <td style="text-align: left">hmm</td>
      </tr>
      <tr>
        <td style="text-align: left">ok</td>
        <td style="text-align: left">good <code class="language-plaintext highlighter-rouge">zoute</code> drop</td>
        <td style="text-align: left">yumm</td>
      </tr>
    </tbody>
  </table>

</div>
<div class="language-markdown highlighter-rouge"><div class="highlight"><pre class="highlight"><code>| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good <span class="sb">`oreos`</span>      | hmm   |
| ok           | good <span class="sb">`zoute`</span> drop | yumm  |
</code></pre></div></div>


</div>
