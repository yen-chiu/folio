---
title: 首页
slug: legacy-guides/original-home
legacySource: index.md
legacyUrl: /
sidebar:
  order: 1
banner:
  content: 历史参考：本页记录旧 Jekyll / Just the Docs 的用法，示例按迁移时的内容保留。Folio 的使用方法请看「从这里开始」。
---

<div class="legacy-content">

<h1 class="fs-9" id="专注于高质量文档编写">专注于高质量文档编写</h1>

<p class="fs-6 fw-300">-… ..- - -….- …. . -….- .- .-.. .-. . .- -.. -.– -….- …. .- … -….- …. .. … -….- .-. — … .</p>

<p><a href="#开始" class="btn btn-primary fs-5 mb-4 mb-md-0 mr-2">立即开始</a>
<a href="https://github.com/yen-chiu/WendellManual" class="btn fs-5 mb-4 mb-md-0">在 GitHub 上查看</a></p>

<hr />

<blockquote class="warning">
  <p><strong>提示:</strong> 请参阅 <a href="/WendellManual/CHANGELOG/">更新日志</a> 了解最新发布、功能更新和错误修复。</p>
</blockquote>

<p>通过使用 <a href="https://daringfireball.net/projects/markdown/">Markdown</a>、<a href="https://github.com/Shopify/liquid/wiki">Liquid</a> 模板语言和 HTML 编写源文件，构建的专业级文档平台。<sup id="fnref:1"><a href="#fn:1" class="footnote" rel="footnote" role="doc-noteref">1</a></sup></p>

<hr />

<h2 id="开始">开始</h2>
<h3 id="关于项目">关于项目</h3>

<p>WendellManual 是一份指南，由 © 2023-2026 创建，旨在帮助用户快速上手。</p>

<h4 id="特别感谢-just-the-docs-的贡献者">特别感谢 Just the Docs 的贡献者</h4>
<ul class="list-style-none">

  <li class="d-inline-block mr-1">
    <a href="https://github.com/pmarsceill">
      <img src="https://avatars.githubusercontent.com/u/896475?v=4" width="32" height="32" alt="pmarsceill" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/mattxwang">
      <img src="https://avatars.githubusercontent.com/u/14893287?v=4" width="32" height="32" alt="mattxwang" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/yen-chiu">
      <img src="https://avatars.githubusercontent.com/u/105543343?v=4" width="32" height="32" alt="yen-chiu" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/pdmosses">
      <img src="https://avatars.githubusercontent.com/u/18308236?v=4" width="32" height="32" alt="pdmosses" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/SgtSilvio">
      <img src="https://avatars.githubusercontent.com/u/28134127?v=4" width="32" height="32" alt="SgtSilvio" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/apps/dependabot">
      <img src="https://avatars.githubusercontent.com/in/29110?v=4" width="32" height="32" alt="dependabot[bot]" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/apps/dependabot-preview">
      <img src="https://avatars.githubusercontent.com/in/2141?v=4" width="32" height="32" alt="dependabot-preview[bot]" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/dependabot-support">
      <img src="https://avatars.githubusercontent.com/u/112581971?v=4" width="32" height="32" alt="dependabot-support" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/max06">
      <img src="https://avatars.githubusercontent.com/u/7556827?v=4" width="32" height="32" alt="max06" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/EricFromCanada">
      <img src="https://avatars.githubusercontent.com/u/3324775?v=4" width="32" height="32" alt="EricFromCanada" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/stefanoborini">
      <img src="https://avatars.githubusercontent.com/u/132967?v=4" width="32" height="32" alt="stefanoborini" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/daviddarnes">
      <img src="https://avatars.githubusercontent.com/u/1177460?v=4" width="32" height="32" alt="daviddarnes" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/hvianna">
      <img src="https://avatars.githubusercontent.com/u/1033735?v=4" width="32" height="32" alt="hvianna" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/gebeto">
      <img src="https://avatars.githubusercontent.com/u/13422799?v=4" width="32" height="32" alt="gebeto" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/dougaitken">
      <img src="https://avatars.githubusercontent.com/u/52214?v=4" width="32" height="32" alt="dougaitken" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/r-brown">
      <img src="https://avatars.githubusercontent.com/u/1361258?v=4" width="32" height="32" alt="r-brown" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/CodeSandwich">
      <img src="https://avatars.githubusercontent.com/u/26183680?v=4" width="32" height="32" alt="CodeSandwich" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/waldyrious">
      <img src="https://avatars.githubusercontent.com/u/478237?v=4" width="32" height="32" alt="waldyrious" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/simonebortolin">
      <img src="https://avatars.githubusercontent.com/u/26844016?v=4" width="32" height="32" alt="simonebortolin" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/pdebruic">
      <img src="https://avatars.githubusercontent.com/u/67050?v=4" width="32" height="32" alt="pdebruic" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/plancomps-admin">
      <img src="https://avatars.githubusercontent.com/u/62553846?v=4" width="32" height="32" alt="plancomps-admin" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/nathanjessen">
      <img src="https://avatars.githubusercontent.com/u/1830690?v=4" width="32" height="32" alt="nathanjessen" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/burner1024">
      <img src="https://avatars.githubusercontent.com/u/1279852?v=4" width="32" height="32" alt="burner1024" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/flyx">
      <img src="https://avatars.githubusercontent.com/u/791710?v=4" width="32" height="32" alt="flyx" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/rmoff">
      <img src="https://avatars.githubusercontent.com/u/3671582?v=4" width="32" height="32" alt="rmoff" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/phillipcutter">
      <img src="https://avatars.githubusercontent.com/u/5022578?v=4" width="32" height="32" alt="phillipcutter" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/MichelleBlanchette">
      <img src="https://avatars.githubusercontent.com/u/33374343?v=4" width="32" height="32" alt="MichelleBlanchette" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/iridazzle">
      <img src="https://avatars.githubusercontent.com/u/63270221?v=4" width="32" height="32" alt="iridazzle" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/m-r-mccormick">
      <img src="https://avatars.githubusercontent.com/u/100036696?v=4" width="32" height="32" alt="m-r-mccormick" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/kevinlin1">
      <img src="https://avatars.githubusercontent.com/u/1915715?v=4" width="32" height="32" alt="kevinlin1" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/KasparEtter">
      <img src="https://avatars.githubusercontent.com/u/16501371?v=4" width="32" height="32" alt="KasparEtter" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/Zarthus">
      <img src="https://avatars.githubusercontent.com/u/3660408?v=4" width="32" height="32" alt="Zarthus" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/jmertic">
      <img src="https://avatars.githubusercontent.com/u/296737?v=4" width="32" height="32" alt="jmertic" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/JPrevost">
      <img src="https://avatars.githubusercontent.com/u/1386650?v=4" width="32" height="32" alt="JPrevost" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/JeffGuKang">
      <img src="https://avatars.githubusercontent.com/u/216363?v=4" width="32" height="32" alt="JeffGuKang" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/iamcarrico">
      <img src="https://avatars.githubusercontent.com/u/1394978?v=4" width="32" height="32" alt="iamcarrico" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/henryiii">
      <img src="https://avatars.githubusercontent.com/u/4616906?v=4" width="32" height="32" alt="henryiii" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/diablodale">
      <img src="https://avatars.githubusercontent.com/u/679350?v=4" width="32" height="32" alt="diablodale" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/alyssais">
      <img src="https://avatars.githubusercontent.com/u/2768870?v=4" width="32" height="32" alt="alyssais" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/stefanintech">
      <img src="https://avatars.githubusercontent.com/u/85418632?v=4" width="32" height="32" alt="stefanintech" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/iefserge">
      <img src="https://avatars.githubusercontent.com/u/6034700?v=4" width="32" height="32" alt="iefserge" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/sehilyi">
      <img src="https://avatars.githubusercontent.com/u/9922882?v=4" width="32" height="32" alt="sehilyi" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/blawqchain">
      <img src="https://avatars.githubusercontent.com/u/20367776?v=4" width="32" height="32" alt="blawqchain" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/SPGoding">
      <img src="https://avatars.githubusercontent.com/u/15277496?v=4" width="32" height="32" alt="SPGoding" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/kcromanpl">
      <img src="https://avatars.githubusercontent.com/u/77137658?v=4" width="32" height="32" alt="kcromanpl" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/robinpokorny">
      <img src="https://avatars.githubusercontent.com/u/68341?v=4" width="32" height="32" alt="robinpokorny" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/ilivewithian">
      <img src="https://avatars.githubusercontent.com/u/422605?v=4" width="32" height="32" alt="ilivewithian" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/PierrickMartos">
      <img src="https://avatars.githubusercontent.com/u/1785711?v=4" width="32" height="32" alt="PierrickMartos" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/koppor">
      <img src="https://avatars.githubusercontent.com/u/1366654?v=4" width="32" height="32" alt="koppor" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/olgarithms">
      <img src="https://avatars.githubusercontent.com/u/9518805?v=4" width="32" height="32" alt="olgarithms" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/captn3m0">
      <img src="https://avatars.githubusercontent.com/u/584253?v=4" width="32" height="32" alt="captn3m0" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/mitchnemirov">
      <img src="https://avatars.githubusercontent.com/u/7938872?v=4" width="32" height="32" alt="mitchnemirov" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/mscoutermarsh">
      <img src="https://avatars.githubusercontent.com/u/155044?v=4" width="32" height="32" alt="mscoutermarsh" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/stephenedmondson">
      <img src="https://avatars.githubusercontent.com/u/3026795?v=4" width="32" height="32" alt="stephenedmondson" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/SConaway">
      <img src="https://avatars.githubusercontent.com/u/20807660?v=4" width="32" height="32" alt="SConaway" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/marksie1988">
      <img src="https://avatars.githubusercontent.com/u/159166?v=4" width="32" height="32" alt="marksie1988" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/thapasusheel">
      <img src="https://avatars.githubusercontent.com/u/148353363?v=4" width="32" height="32" alt="thapasusheel" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/Tom-Brouwer">
      <img src="https://avatars.githubusercontent.com/u/23358319?v=4" width="32" height="32" alt="Tom-Brouwer" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/UnclassedPenguin">
      <img src="https://avatars.githubusercontent.com/u/7208221?v=4" width="32" height="32" alt="UnclassedPenguin" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/sigv">
      <img src="https://avatars.githubusercontent.com/u/1391569?v=4" width="32" height="32" alt="sigv" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/yavorg">
      <img src="https://avatars.githubusercontent.com/u/1086030?v=4" width="32" height="32" alt="yavorg" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/deseo">
      <img src="https://avatars.githubusercontent.com/u/5795440?v=4" width="32" height="32" alt="deseo" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/jacobherrington">
      <img src="https://avatars.githubusercontent.com/u/11466782?v=4" width="32" height="32" alt="jacobherrington" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/nascosto">
      <img src="https://avatars.githubusercontent.com/u/2653283?v=4" width="32" height="32" alt="nascosto" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/omahs">
      <img src="https://avatars.githubusercontent.com/u/73983677?v=4" width="32" height="32" alt="omahs" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/tiaitsch85">
      <img src="https://avatars.githubusercontent.com/u/2466354?v=4" width="32" height="32" alt="tiaitsch85" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/agabrys">
      <img src="https://avatars.githubusercontent.com/u/10604335?v=4" width="32" height="32" alt="agabrys" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/nergmada">
      <img src="https://avatars.githubusercontent.com/u/5811572?v=4" width="32" height="32" alt="nergmada" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/alexsegura">
      <img src="https://avatars.githubusercontent.com/u/1162230?v=4" width="32" height="32" alt="alexsegura" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/RoiArthurB">
      <img src="https://avatars.githubusercontent.com/u/16764085?v=4" width="32" height="32" alt="RoiArthurB" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/ghabs">
      <img src="https://avatars.githubusercontent.com/u/3542567?v=4" width="32" height="32" alt="ghabs" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/folbert">
      <img src="https://avatars.githubusercontent.com/u/214164?v=4" width="32" height="32" alt="folbert" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/bobvandevijver">
      <img src="https://avatars.githubusercontent.com/u/1835343?v=4" width="32" height="32" alt="bobvandevijver" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/bmann">
      <img src="https://avatars.githubusercontent.com/u/280420?v=4" width="32" height="32" alt="bmann" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/blaylockbk">
      <img src="https://avatars.githubusercontent.com/u/6249613?v=4" width="32" height="32" alt="blaylockbk" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/CarbonNeuron">
      <img src="https://avatars.githubusercontent.com/u/16768821?v=4" width="32" height="32" alt="CarbonNeuron" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/fabrik42">
      <img src="https://avatars.githubusercontent.com/u/223822?v=4" width="32" height="32" alt="fabrik42" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/Dima-369">
      <img src="https://avatars.githubusercontent.com/u/15002298?v=4" width="32" height="32" alt="Dima-369" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/fogfish">
      <img src="https://avatars.githubusercontent.com/u/716093?v=4" width="32" height="32" alt="fogfish" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/Eisverygoodletter">
      <img src="https://avatars.githubusercontent.com/u/76079042?v=4" width="32" height="32" alt="Eisverygoodletter" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/woernfl">
      <img src="https://avatars.githubusercontent.com/u/28304331?v=4" width="32" height="32" alt="woernfl" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/flut1">
      <img src="https://avatars.githubusercontent.com/u/1841618?v=4" width="32" height="32" alt="flut1" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/gnarea">
      <img src="https://avatars.githubusercontent.com/u/369863?v=4" width="32" height="32" alt="gnarea" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/ivanskodje">
      <img src="https://avatars.githubusercontent.com/u/6776092?v=4" width="32" height="32" alt="ivanskodje" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/jacobhq">
      <img src="https://avatars.githubusercontent.com/u/29145479?v=4" width="32" height="32" alt="jacobhq" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/jakebresnehan">
      <img src="https://avatars.githubusercontent.com/u/227719?v=4" width="32" height="32" alt="jakebresnehan" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/joesb">
      <img src="https://avatars.githubusercontent.com/u/518081?v=4" width="32" height="32" alt="joesb" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/JoeNyland">
      <img src="https://avatars.githubusercontent.com/u/7666402?v=4" width="32" height="32" alt="JoeNyland" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/joelhawksley">
      <img src="https://avatars.githubusercontent.com/u/1940294?v=4" width="32" height="32" alt="joelhawksley" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/novelistparty">
      <img src="https://avatars.githubusercontent.com/u/1569364?v=4" width="32" height="32" alt="novelistparty" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/m3nu">
      <img src="https://avatars.githubusercontent.com/u/3916435?v=4" width="32" height="32" alt="m3nu" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/manuelhenke">
      <img src="https://avatars.githubusercontent.com/u/47060836?v=4" width="32" height="32" alt="manuelhenke" />
    </a>
  </li>

  <li class="d-inline-block mr-1">
    <a href="https://github.com/flanakin">
      <img src="https://avatars.githubusercontent.com/u/399533?v=4" width="32" height="32" alt="flanakin" />
    </a>
  </li>

</ul>

<hr />

<hr />

<h3 id="相关链接">相关链接</h3>
<ul>
  <li><a href="https://jekyllrb.com">Jekyll 官方文档</a></li>
  <li><a href="https://daringfireball.net/projects/markdown/">Markdown 指南</a></li>
  <li><a href="https://github.com/Shopify/liquid/wiki">Liquid 模板语言</a></li>
  <li><a href="https://jekyllrb.com/docs/front-matter/">Front Matter 说明</a></li>
  <li><a href="https://jekyllrb.com/docs/configuration/">Jekyll 配置指南</a></li>
  <li><a href="https://pages.github.com/">GitHub Pages 教程</a></li>
  <li><a href="https://github.blog/changelog/2022-07-27-github-pages-custom-github-actions-workflows-beta/">GitHub Actions 工作流</a></li>
</ul>

<div class="footnotes" role="doc-endnotes">
  <ol>
    <li id="fn:1">
      <p>本页面的 <a href="https://github.com/yen-chiu/WendellManual/blob/master/index.md">源文件</a> 使用了 Markdown、Liquid 和 HTML。 <a href="#fnref:1" class="reversefootnote" role="doc-backlink">&#8617;</a></p>
    </li>
  </ol>
</div>


</div>
