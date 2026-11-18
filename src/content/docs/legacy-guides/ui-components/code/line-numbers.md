---
title: 行号
slug: legacy-guides/ui-components/code/line-numbers
legacySource: docs/Usage Guidelines/ui-components/code/line-numbers.md
legacyUrl: /docs/Usage Guidelines/ui-components/code/line-numbers/
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 id="code-snippets-with-line-numbers">Code Snippets with Line Numbers</h1>

<p class="warning">In prior versions of the docs, we provided “workarounds” to rendering issues arising from code snippets with line numbers. While these seemed to resolve visual layout issues, they did not resolve core issues with Jekyll generating invalid HTML. See <a href="#detailed-error-explanation">the detailed explanation</a> for more information.</p>

<p>The default settings for HTML compression are incompatible with the HTML
produced by Jekyll for line numbers from highlighted code
– both when using Kramdown code fences and when using Liquid highlight tags.</p>

<p>To avoid non-conforming HTML and unsatisfactory layout, HTML compression
can be turned off by using the following configuration option:</p>

<figure class="highlight"><pre><code class="language-yaml" data-lang="yaml"><span class="na">compress_html</span><span class="pi">:</span>
  <span class="na">ignore</span><span class="pi">:</span>
    <span class="na">envs</span><span class="pi">:</span> <span class="s">all</span></code></pre></figure>

<p>When using Kramdown code fences, line numbers are turned on globally by the
following configuration option:</p>

<figure class="highlight"><pre><code class="language-yaml" data-lang="yaml"><span class="na">kramdown</span><span class="pi">:</span>
  <span class="na">syntax_highlighter_opts</span><span class="pi">:</span>
    <span class="na">block</span><span class="pi">:</span>
      <span class="na">line_numbers</span><span class="pi">:</span> <span class="kc">true</span></code></pre></figure>

<p>Line numbers can then be suppressed locally using Liquid tags (<em>without</em> the
<code class="language-plaintext highlighter-rouge">linenos</code> option) instead of fences:</p>

<figure class="highlight"><pre><code class="language-yaml" data-lang="yaml"><span class="pi">{</span><span class="err">%</span> <span class="nv">highlight some_language %</span><span class="pi">}</span>
<span class="s">Some code</span>
<span class="pi">{</span><span class="err">%</span> <span class="nv">endhighlight %</span><span class="pi">}</span></code></pre></figure>

<h2 id="detailed-error-explanation">Detailed Error Explanation</h2>

<p>Consider this following code snippet, intended to highlight a simple Ruby program:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>{% highlight ruby linenos %}
def foo
  puts 'foo'
end
{% endhighlight %}
</code></pre></div></div>

<p>If this is directly placed within a file processed by Jekyll (via Just the Docs, with HTML compression enabled), the following markup will be generated:</p>

<div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nt">&lt;figure</span> <span class="na">class=</span><span class="s">"highlight"</span><span class="nt">&gt;</span>&gt;<span class="nt">&lt;code</span> <span class="na">class=</span><span class="s">"language-ruby"</span> <span class="na">data-lang=</span><span class="s">"ruby"</span><span class="nt">&gt;&lt;div</span> <span class="na">class=</span><span class="s">"table-wrapper"</span><span class="nt">&gt;&lt;table</span> <span class="na">class=</span><span class="s">"rouge-table"</span><span class="nt">&gt;&lt;tbody&gt;&lt;tr&gt;&lt;td</span> <span class="na">class=</span><span class="s">"gutter gl"</span><span class="nt">&gt;&lt;pre</span> <span class="na">class=</span><span class="s">"lineno"</span><span class="nt">&gt;</span>1
2
3
<span class="nt">&lt;/pre&gt;&lt;td</span> <span class="na">class=</span><span class="s">"code"</span><span class="nt">&gt;&lt;pre&gt;&lt;span</span> <span class="na">class=</span><span class="s">"k"</span><span class="nt">&gt;</span>def<span class="nt">&lt;/span&gt;</span> <span class="nt">&lt;span</span> <span class="na">class=</span><span class="s">"nf"</span><span class="nt">&gt;</span>foo<span class="nt">&lt;/span&gt;</span>
  <span class="nt">&lt;span</span> <span class="na">class=</span><span class="s">"nb"</span><span class="nt">&gt;</span>puts<span class="nt">&lt;/span&gt;</span> <span class="nt">&lt;span</span> <span class="na">class=</span><span class="s">"s1"</span><span class="nt">&gt;</span>'foo'<span class="nt">&lt;/span&gt;</span>
<span class="nt">&lt;span</span> <span class="na">class=</span><span class="s">"k"</span><span class="nt">&gt;</span>end<span class="nt">&lt;/span&gt;</span>
<span class="nt">&lt;/pre&gt;&lt;/figure&gt;</span>
</code></pre></div></div>

<p>This HTML is invalid; in particular, there are two issues:</p>

<ol>
  <li>there are many missing closing tags, and a superfluous <code class="language-plaintext highlighter-rouge">&gt;</code>, which produce visually garbled output</li>
  <li>a <code class="language-plaintext highlighter-rouge">&lt;table&gt;</code> is placed within a <code class="language-plaintext highlighter-rouge">&lt;code&gt;</code> element, which is syntactically invalid HTML (but is often allowed by browsers)</li>
</ol>

<p>To emphasize this first difference, here is the same markup output, indented by tag:</p>

<div class="language-html highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nt">&lt;figure</span> <span class="na">class=</span><span class="s">"highlight"</span><span class="nt">&gt;</span>
  &gt;
  <span class="nt">&lt;code</span> <span class="na">class=</span><span class="s">"language-ruby"</span> <span class="na">data-lang=</span><span class="s">"ruby"</span><span class="nt">&gt;</span>
    <span class="nt">&lt;div</span> <span class="na">class=</span><span class="s">"table-wrapper"</span><span class="nt">&gt;</span>
      <span class="nt">&lt;table</span> <span class="na">class=</span><span class="s">"rouge-table"</span><span class="nt">&gt;</span>
        <span class="nt">&lt;tbody&gt;</span>
          <span class="nt">&lt;tr&gt;</span>
            <span class="nt">&lt;td</span> <span class="na">class=</span><span class="s">"gutter gl"</span><span class="nt">&gt;</span>
              <span class="nt">&lt;pre</span> <span class="na">class=</span><span class="s">"lineno"</span><span class="nt">&gt;</span>
1
2
3
              <span class="nt">&lt;/pre&gt;</span>
              <span class="nt">&lt;td</span> <span class="na">class=</span><span class="s">"code"</span><span class="nt">&gt;</span>
                <span class="nt">&lt;pre&gt;</span>
<span class="nt">&lt;span</span> <span class="na">class=</span><span class="s">"k"</span><span class="nt">&gt;</span>def<span class="nt">&lt;/span&gt;</span>
<span class="nt">&lt;span</span> <span class="na">class=</span><span class="s">"nf"</span><span class="nt">&gt;</span>foo<span class="nt">&lt;/span&gt;</span>
<span class="nt">&lt;span</span> <span class="na">class=</span><span class="s">"nb"</span><span class="nt">&gt;</span>puts<span class="nt">&lt;/span&gt;</span>
<span class="nt">&lt;span</span> <span class="na">class=</span><span class="s">"s1"</span><span class="nt">&gt;</span>'foo'<span class="nt">&lt;/span&gt;</span>
<span class="nt">&lt;span</span> <span class="na">class=</span><span class="s">"k"</span><span class="nt">&gt;</span>end<span class="nt">&lt;/span&gt;</span>
                <span class="nt">&lt;/pre&gt;</span>
<span class="nt">&lt;/figure&gt;</span>
</code></pre></div></div>

<p>In order, there are missing <code class="language-plaintext highlighter-rouge">&lt;/td&gt;</code>, <code class="language-plaintext highlighter-rouge">&lt;/td&gt;</code>, <code class="language-plaintext highlighter-rouge">&lt;/tr&gt;</code>, <code class="language-plaintext highlighter-rouge">&lt;/tbody&gt;</code>, <code class="language-plaintext highlighter-rouge">&lt;/table&gt;</code>, <code class="language-plaintext highlighter-rouge">&lt;/div&gt;</code>, and <code class="language-plaintext highlighter-rouge">&lt;/code&gt;</code> tags. As a result, the following elements of the page - including the site footer - become visually garbled as browsers attempt to recover gracefully.</p>

<p>Prior workarounds we suggested (such as <a href="https://github.com/penibelst/jekyll-compress-html/issues/71#issuecomment-188144901">Dmitry Hrabrov’s in <code class="language-plaintext highlighter-rouge">jekyll-compress-html</code>#71</a>) resolve the missing tag problem. However, they still place a <code class="language-plaintext highlighter-rouge">&lt;table&gt;</code> within a <code class="language-plaintext highlighter-rouge">&lt;code&gt;</code> element. The HTML spec normatively states that <code class="language-plaintext highlighter-rouge">&lt;code&gt;</code> elements should only contain “<a href="https://html.spec.whatwg.org/multipage/dom.html#phrasing-content-2">phrasing content</a>”, which does not include <code class="language-plaintext highlighter-rouge">&lt;table&gt;</code> (<a href="https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-code-element">spec ref</a>). To avoid incorrectly rendered HTML, the previously-suggested workaround using the current version of <code class="language-plaintext highlighter-rouge">_includes/fix_linenos.html</code> should <em>not</em> be used!</p>


</div>
