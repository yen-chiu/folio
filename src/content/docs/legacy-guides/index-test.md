---
title: Markdown 示例大全
slug: legacy-guides/index-test
legacySource: docs/Usage Guidelines/index-test.md
legacyUrl: /docs/Usage Guidelines/index-test/
sidebar:
  order: 99
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

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

<p>文本可以是<strong>粗体</strong>、<em>斜体</em> 或<del>删除线</del>。</p>

<p><a href="/WendellManual/">链接到另一个页面</a>。</p>

<p>段落之间应该有空格。</p>

<p>段落之间应该有空格。我们建议包含 README 或包含有关恁的项目的信息的文件。</p>

<h1 id="标题-1">标题 1</h1>

<p>这是标题后面的普通段落。GitHub 是一个用于版本控制和协作的代码托管平台。它允许恁和其他人从任何地方共同完成项目。</p>

<h2 id="标题-2">标题 2</h2>

<blockquote>
  <p>这是标题后面的块引用。</p>

  <p>当某件事足够重要时，即使胜算不大，恁也会去做。</p>
</blockquote>

<h3 id="标题-3">标题 3</h3>

<div class="language-js highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1">// Javascript code with syntax highlighting.</span>
<span class="kd">var</span> <span class="nx">fun</span> <span class="o">=</span> <span class="kd">function</span> <span class="nf">lang</span><span class="p">(</span><span class="nx">l</span><span class="p">)</span> <span class="p">{</span>
  <span class="nx">dateformat</span><span class="p">.</span><span class="nx">i18n</span> <span class="o">=</span> <span class="nf">require</span><span class="p">(</span><span class="dl">'</span><span class="s1">./lang/</span><span class="dl">'</span> <span class="o">+</span> <span class="nx">l</span><span class="p">)</span>
  <span class="k">return</span> <span class="kc">true</span><span class="p">;</span>
<span class="p">}</span>
</code></pre></div></div>

<div class="language-ruby highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Ruby code with syntax highlighting</span>
<span class="no">GitHubPages</span><span class="o">::</span><span class="no">Dependencies</span><span class="p">.</span><span class="nf">gems</span><span class="p">.</span><span class="nf">each</span> <span class="k">do</span> <span class="o">|</span><span class="n">gem</span><span class="p">,</span> <span class="n">version</span><span class="o">|</span>
  <span class="n">s</span><span class="p">.</span><span class="nf">add_dependency</span><span class="p">(</span><span class="n">gem</span><span class="p">,</span> <span class="s2">"= </span><span class="si">#{</span><span class="n">version</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
<span class="k">end</span>
</code></pre></div></div>

<h4 id="标题-4-代码未转换">标题 4 <code class="language-plaintext highlighter-rouge">代码未转换</code></h4>

<ul>
  <li>这是一个标题后面的无序列表。</li>
  <li>这是一个标题后面的无序列表。</li>
  <li>这是一个标题后面的无序列表。</li>
</ul>

<h5 id="标题-5">标题 5</h5>

<ol>
  <li>这是一个标题后面的有序列表。</li>
  <li>这是一个标题后面的有序列表。</li>
  <li>这是一个标题后面的有序列表。</li>
</ol>

<h6 id="标题-6">标题 6</h6>

<p><a href=".">这是一个非常长的链接，它会换行，因此即使它位于行首</a> 也不会溢出。</p>

<ul>
  <li><a href=".">这是一个非常长的链接，它会换行，因此在列表中第一个项目 </a> 中使用时不会溢出行。</li>
</ul>

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

<h3 id="下方有一条水平线">下方有一条水平线。</h3>

<hr />

<h3 id="这是一个无序列表">这是一个无序列表:</h3>

<ul>
  <li>项目 foo</li>
  <li>项目 bar</li>
  <li>项目 baz</li>
  <li>项目 zip</li>
</ul>

<h3 id="有序列表">有序列表:</h3>

<ol>
  <li>项目一</li>
  <li>项目二</li>
  <li>项目三</li>
  <li>项目四</li>
</ol>

<h3 id="有序列表继续">有序列表，继续:</h3>

<ol>
  <li>项目一</li>
  <li>项目二</li>
</ol>

<p>一些文本</p>

<ol style="counter-reset:none">
  <li>项目三</li>
  <li>项目四</li>
</ol>

<h3 id="有序列表从-42-开始">有序列表从 42 开始:</h3>

<ol style="counter-reset:step-counter 41">
  <li>项目 42</li>
  <li>项目 43</li>
  <li>项目 44</li>
</ol>

<h3 id="嵌套列表">嵌套列表:</h3>
<ul>
  <li>level 1 item
    <ul>
      <li>level 2 item</li>
      <li>level 2 item
        <ul>
          <li>level 3 item</li>
          <li>level 3 item</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>level 1 item
    <ul>
      <li>level 2 item</li>
      <li>level 2 item</li>
      <li>level 2 item</li>
    </ul>
  </li>
  <li>level 1 item
    <ul>
      <li>level 2 item</li>
      <li>level 2 item</li>
    </ul>
  </li>
  <li>level 1 item</li>
</ul>

<h3 id="将-ol-嵌套在-ul-中">将 ol 嵌套在 ul 中</h3>

<ul class="task-list">
  <li>level 1 item (ul)
    <ol>
      <li>level 2 item (ol)</li>
      <li>level 2 item (ol)
        <ul>
          <li>level 3 item (ul)</li>
          <li>level 3 item (ul)</li>
        </ul>
      </li>
    </ol>
  </li>
  <li>level 1 item (ul)
    <ol>
      <li>level 2 item (ol)</li>
      <li>level 2 item (ol)
        <ul>
          <li>level 3 item (ul)</li>
          <li>level 3 item (ul)</li>
        </ul>
      </li>
      <li>level 4 item (ol)</li>
      <li>level 4 item (ol)
        <ul>
          <li>level 3 item (ul)</li>
          <li>level 3 item (ul)</li>
        </ul>
      </li>
    </ol>
  </li>
  <li>level 1 item (ul)
    <h3 id="任务列表">任务列表</h3>
  </li>
  <li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled="disabled" />恁好，这是一个待办事项</li>
  <li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled="disabled" />恁好，这是另一个待办事项</li>
  <li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled="disabled" checked="checked" />再见，这个事项已完成</li>
</ul>

<h3 id="嵌套任务列表">嵌套任务列表</h3>

<ul class="task-list">
  <li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled="disabled" />一级项目（任务）
    <ul class="task-list">
      <li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled="disabled" />二级项目（任务）</li>
      <li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled="disabled" />二级项目（任务）</li>
    </ul>
  </li>
  <li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled="disabled" />一级项目（任务）</li>
  <li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled="disabled" />一级项目（任务）</li>
</ul>

<h3 id="在任务列表中嵌套无序列表">在任务列表中嵌套无序列表</h3>

<ul class="task-list">
  <li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled="disabled" />一级项目（任务）
    <ul>
      <li>二级项目（无序列表）</li>
      <li>二级项目（无序列表）</li>
    </ul>
  </li>
  <li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled="disabled" />一级项目（任务）</li>
  <li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled="disabled" />一级项目（任务）</li>
</ul>

<h3 id="在无序列表中嵌套任务列表">在无序列表中嵌套任务列表</h3>

<ul>
  <li>一级项目（无序列表）
    <ul class="task-list">
      <li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled="disabled" />二级项目（任务）</li>
      <li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled="disabled" />二级项目（任务）</li>
    </ul>
  </li>
  <li>一级项目（无序列表）</li>
  <li>一级项目（无序列表）</li>
</ul>

<h3 id="小图片">小图片</h3>

<!-- ![](../../assets/images/small-image.jpg) -->
<p><img src="https://raw.githubusercontent.com/yen-chiu/WendellManual/master/assets/images/small-image.jpg" alt="" /></p>

<h3 id="大图片">大图片</h3>
<p><img src="https://raw.githubusercontent.com/yen-chiu/WendellManual/master/assets/images/large-image.jpg" alt="" />
<!-- ![](../../assets/images/large-image.jpg) --></p>

<p>“<a href="https://www.flickr.com/photos/97810305@N08/9401451269">弗罗茨瓦夫大学图书馆数字化稀有档案文本</a>” by <a href="https://www.flickr.com/photos/97810305@N08">j_cadmus</a> is marked with <a href="https://creativecommons.org/licenses/by/2.0/?ref=openverse">CC BY 2.0</a>.</p>

<h3 id="标签">标签</h3>

<p class="label">我是一个标签</p>

<p class="label label-blue">蓝色</p>
<p class="label label-green">绿色</p>
<p class="label label-purple">紫色</p>
<p class="label label-yellow">黄色</p>
<p class="label label-red">红色</p>

<p class="label"><strong>粗体</strong></p>
<p class="label"><em>斜体</em></p>
<p class="label"><strong><em>粗体 + 斜体</em></strong></p>

<h3 id="定义列表可以使用-html-语法">定义列表可以使用 HTML 语法。</h3>

<dl>
<dt>名字</dt>
<dd>哥斯拉</dd>
<dt>出生</dt>
<dd>1952</dd>
<dt>出生地</dt>
<dd>日本</dd>
<dt>颜色</dt>
<dd>绿色</dd>
</dl>

<h4 id="多个描述术语和值">多个描述术语和值</h4>

<dl>
  <dt>术语</dt>
  <dd>术语的简短描述</dd>
  <dt>较长的术语</dt>
  <dd>较长的术语描述，
可能不止一行</dd>
  <dt>术语</dt>
  <dd>术语的第一个描述，
可能不止一行</dd>
  <dd>
    <p>术语的第二个描述，
可能不止一行</p>
  </dd>
  <dt>术语1</dt>
  <dt>术语2</dt>
  <dd>术语1和术语2的单一描述，
可能不止一行</dd>
  <dt>术语1</dt>
  <dt>术语2</dt>
  <dd>术语1和术语2的第一个描述，
可能不止一行</dd>
  <dd>
    <p>术语1和术语2的第二个描述，
可能不止一行</p>
  </dd>
</dl>

<h3 id="更多代码">更多代码</h3>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="k">def</span> <span class="nf">dump_args</span><span class="p">(</span><span class="n">func</span><span class="p">):</span>
    <span class="sh">"</span><span class="s">This decorator dumps out the arguments passed to a function before calling it</span><span class="sh">"</span>
    <span class="n">argnames</span> <span class="o">=</span> <span class="n">func</span><span class="p">.</span><span class="n">func_code</span><span class="p">.</span><span class="n">co_varnames</span><span class="p">[:</span><span class="n">func</span><span class="p">.</span><span class="n">func_code</span><span class="p">.</span><span class="n">co_argcount</span><span class="p">]</span>
    <span class="n">fname</span> <span class="o">=</span> <span class="n">func</span><span class="p">.</span><span class="n">func_name</span>
    <span class="k">def</span> <span class="nf">echo_func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span><span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
        <span class="k">print</span> <span class="n">fname</span><span class="p">,</span> <span class="sh">"</span><span class="s">:</span><span class="sh">"</span><span class="p">,</span> <span class="sh">'</span><span class="s">, </span><span class="sh">'</span><span class="p">.</span><span class="nf">join</span><span class="p">(</span>
            <span class="sh">'</span><span class="s">%s=%r</span><span class="sh">'</span> <span class="o">%</span> <span class="n">entry</span>
            <span class="k">for</span> <span class="n">entry</span> <span class="ow">in</span> <span class="nf">zip</span><span class="p">(</span><span class="n">argnames</span><span class="p">,</span><span class="n">args</span><span class="p">)</span> <span class="o">+</span> <span class="n">kwargs</span><span class="p">.</span><span class="nf">items</span><span class="p">())</span>
        <span class="k">return</span> <span class="nf">func</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">echo_func</span>

<span class="nd">@dump_args</span>
<span class="k">def</span> <span class="nf">f1</span><span class="p">(</span><span class="n">a</span><span class="p">,</span><span class="n">b</span><span class="p">,</span><span class="n">c</span><span class="p">):</span>
    <span class="k">print</span> <span class="n">a</span> <span class="o">+</span> <span class="n">b</span> <span class="o">+</span> <span class="n">c</span>

<span class="nf">f1</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">precondition</span><span class="p">(</span><span class="n">precondition</span><span class="p">,</span> <span class="n">use_conditions</span><span class="o">=</span><span class="n">DEFAULT_ON</span><span class="p">):</span>
    <span class="k">return</span> <span class="nf">conditions</span><span class="p">(</span><span class="n">precondition</span><span class="p">,</span> <span class="bp">None</span><span class="p">,</span> <span class="n">use_conditions</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">postcondition</span><span class="p">(</span><span class="n">postcondition</span><span class="p">,</span> <span class="n">use_conditions</span><span class="o">=</span><span class="n">DEFAULT_ON</span><span class="p">):</span>
    <span class="k">return</span> <span class="nf">conditions</span><span class="p">(</span><span class="bp">None</span><span class="p">,</span> <span class="n">postcondition</span><span class="p">,</span> <span class="n">use_conditions</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">conditions</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="n">__slots__</span> <span class="o">=</span> <span class="p">(</span><span class="sh">'</span><span class="s">__precondition</span><span class="sh">'</span><span class="p">,</span> <span class="sh">'</span><span class="s">__postcondition</span><span class="sh">'</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">pre</span><span class="p">,</span> <span class="n">post</span><span class="p">,</span> <span class="n">use_conditions</span><span class="o">=</span><span class="n">DEFAULT_ON</span><span class="p">):</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">use_conditions</span><span class="p">:</span>
            <span class="n">pre</span><span class="p">,</span> <span class="n">post</span> <span class="o">=</span> <span class="bp">None</span><span class="p">,</span> <span class="bp">None</span>

        <span class="n">self</span><span class="p">.</span><span class="n">__precondition</span>  <span class="o">=</span> <span class="n">pre</span>
        <span class="n">self</span><span class="p">.</span><span class="n">__postcondition</span> <span class="o">=</span> <span class="n">post</span>
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>长的单行代码块不应换行。如果它们太长，则应水平滚动。这行代码应该足够长以演示这一点。
</code></pre></div></div>

<h3 id="mermaid-图表">Mermaid 图表</h3>

<p>以下代码仅在 <code class="language-plaintext highlighter-rouge">_config.yml</code> 中提供 <code class="language-plaintext highlighter-rouge">mermaid</code> 键时显示为图表。</p>

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

<h3 id="折叠部分">折叠部分</h3>

<p>以下使用 <a href="https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-collapsed-sections"><code class="language-plaintext highlighter-rouge">&lt;details&gt;</code></a> 标签创建一个折叠部分。</p>

<details>
  <summary>购物清单（点击我！）</summary>

  <p>这是 <code class="language-plaintext highlighter-rouge">&lt;details&gt;</code> 下拉菜单中的内容。</p>

  <ul class="task-list">
    <li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled="disabled" />苹果</li>
    <li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled="disabled" />橙子</li>
    <li class="task-list-item"><input type="checkbox" class="task-list-item-checkbox" disabled="disabled" />牛奶</li>
  </ul>

</details>
<p>```</p>


</div>
