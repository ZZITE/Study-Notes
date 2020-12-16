## 关于XML
###  前言
由于项目原因需要在megento模版基础上做二次开发, 查看源码后发现文件结构基本通过XML构建(虽然由于历史原因XML已经几乎淡出web开发, 以至于在我学习前端的路上几乎是只听过没见过...),既然接触到了还是花点时间在这里补下XML的知识。

### 关于XML (可扩展标记语言)
  提到XML,这里首先要了解下它的父集SGML(标准通用标记语言), 它是一种定义标记语言的元语言, 是一种非常复杂的文档的结构, 其古老程度早在万维网之前。功能强大的同时却太过复杂(Sounds great, maybe later) :) 

  在SGML的基础上,诞生了HTML(超文本标记语言)。最初的HTML只是SGML的一个应用, 它的优点是比较适合web 页面的开发, 快速而简单。需要注意的是如今的HTML跟最初的HTML已大不相同,它包含了当初的HTML/XHTML/DOM等许多标准, 直至今日HTML5.0已经不再基于SGML, 它是W3C制定的一套HTML的全新标准, 也正是因为它不基于SGML, 我们也不再需要在HTML的开头对DTD进行引用。HTML的发展是一个不断修复历史问题, 规范标准, 强大自身可用性的过程。也是前端领域上不断变化创新的生命力的一个缩影。

  而XML(可扩展标记语言)作为SGML的子集,它简化了SGML,并且期望取代SGML。其结合了SGML,HTML的优点,去除复杂部分, 保持轻巧并可在web上良好工作。在最初的时候, XML一度被认为是取代HTML未来的存在, 这也是XHTML(可扩展超文本标记语言)诞生的原因。继承XML的特点, 严谨,整齐,更好的语义化,这些都是XHTML带来的好处。XHTML希望大家都以一个标准去构建完美的网页格式, 更良好的书写, 更严谨的执行。可以说如果每个前端工程师都能按照这样的标准去构建网页, 对于互联网的发展是有不少好处的。然而XHTML最终还是倒在了XHTML2.0的标准上。快速发展出的更加易用的HTML5标准,以及浏览器的宽容支持, 最终使得XHTML成了昙花一现的美好愿景。

  XML风格的XHTML失败了, 那么XML呢。首先需要认识XML被创造的初衷。XML 被设计用来传输和存储数据，其焦点是数据的内容, 而HTML 被设计用来显示数据，其焦点是数据的外观。HTML 旨在显示信息，而 XML 旨在传输信息。纯文本保存结构化数据，是XML最大的优点。(尽管在数据传输这块XML大多也已经被JSON取代...)看起来XML的存在似乎没有什么不可替代性(尴尬尴尬),但是！作为一个强大而通用的工具...好吧我就是单纯因为要用到所以才来学习的, 摔!)

  ### XML基础

  先看一个简单的XML
  ```
  <?xml version="1.0" encoding="UTF-8"?>
  <note>
  <to>world</to>
  <from>me</from>
  <heading>Hellow</heading>
  <body>world</body>
  </note>
  ```

  跟HTML相比, 可以第一眼看出的是`<to>` `<from>`这样的标签。在HTML中我们使用到的标签都是定义好的, 使用如上不存在的标签就会发生错误。但在XML中, 不存在预定义的标签。XML允许文档的创作者定义自己的标签和文档结构。

第一行是 XML 声明。它定义 XML 的版本（1.0）和所使用的编码（UTF-8 : 万国码, 可显示各种语言）。声明是可选的, 如存在则必须放在第一行。后面的内容如同一张便签, 标签 `<note>` 体现了XML出色的自我描述性, 同时作为XML 必须具备的根元素, 是其它元素的父元素。XML在结构上同HTML相似都是以树形的结构形式。

与HTML不同的除了必须存在根节点外, XML的标签必须被正确的闭合,如 `</br>` 同时XML对大小写敏感, 必须使用相同的大小写来打开闭合标签。XML标签必须被正确的嵌套如 `<p><i></i></p>`。XML中的空格会被正确的保留而不是像HTML那样合并为一个。

另外, 在XML中还存在一些实体引用。如 `<` 这样的符号如果出现在文本中解析器会把它当成新元素的开始而发生错误。为了避免这样的错误XML中使用实体引用 `
&lt;` 来代替。像这样的实体引用在XML中一共有5个：

<table>
<tbody>
<tr>
<td>&amp;lt;</td>
<td>&lt;</td>
<td>less than</td>
</tr>
<tr>
<td>&amp;gt;</td>
<td>&gt;</td>
<td>greater than</td>
</tr>
<tr>
<td>&amp;amp;</td>
<td>&amp;</td>
<td>ampersand </td>
</tr>
<tr>
<td>&amp;apos;</td>
<td>'</td>
<td>apostrophe</td>
</tr>
<tr>
<td>&amp;quot;</td>
<td>"</td>
<td>quotation mark</td>
</tr>
</tbody>
</table>

XML中的标签包含标签中的内容都属于XML的元素, XML元素遵循一定的命名规范

* 名称可以包含字母、数字以及其他的字符
* 名称不能以数字或者标点符号开始
* 名称不能以字母 xml（或者 XML、Xml 等等）开始
* 名称不能包含空格

可使用任何名称，没有保留的字词。使用下划线和简短的描述性单词命名如 `<first_name>、<last_name>` 较为规范。

XML中的属性用于提供有关元素的额外信息。他们必须使用双引号包括。实际上很多时候属性和元素做到的是同一件事,他们都被用提供一样信息。而区别使用属性还是元素的判别在于是否提供了数据相关的信息。同时，属性难以阅读和维护，不易扩展，例如:
```
<note day="10" month="01" year="2008"
to="Tove" from="Jani" heading="Reminder"
body="Don't forget me this weekend!">
</note>
<!-- bad -->
```
所以建议在提供数据信息上多使用元素，而仅用属性来提供与数据无关的信息。

XML可以引用一套规范来验证XML语法的正确性，如引入 `DTD` 标准来验证，语法错误就会曝出程序不再运行。

XML在浏览器上会被直接解析为源码形式而不像HTML一样具有一定的样式，这是因为XML的元素标签都由创建者自主定义，浏览器无法像对HTML中的 `<table> <p>` 一样应用样式。可以通过外部引用CSS样式表的方式来设置样式但这并不是常用方法，XML通常通过XSLT来将其转化为HTML从而更好的展示。

### XML javascript

<strong>XMLHttpRequest对象</strong>作为AJAX技术的核心具有非凡的意义。它用于与后台间的数据交互，其不需要重载页面即可完成数据交互通讯的特点也使得AJAX在前端大放异彩。使用JS新建一个XMLHttpRequest对象：
```
xmlhttp=new XMLHttpRequest();
```
XML和HTML一样具有DOM结构，定义了访问和操作 XML 文档的标准方法。所有元素可以通过 DOM 树来访问。可以修改或删除它们的内容，并创建新的元素。元素，它们的文本，以及它们的属性，都被认为是节点。

使用XML、HTML、JS构建一个小DEMO：

```
<!--XML-->
<CD>
<TITLE>Empire Burlesque</TITLE>
<ARTIST>Bob Dylan</ARTIST>
<COUNTRY>USA</COUNTRY>
<COMPANY>Columbia</COMPANY>
<PRICE>10.90</PRICE>
<YEAR>1985</YEAR>
</CD>
```
```
<!--HTML-->
<!DOCTYPE html>
<html>
<head>
</head>
<body onload="displayCD()">
<div id='showCD'></div>
</body>
</html>
```
```
<script>
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
xmlhttp.open("GET","cd_catalog.xml",false);
xmlhttp.send();
xmlDoc=xmlhttp.responseXML; 

x=xmlDoc.getElementsByTagName("CD");
i=0;

function displayCD()
{
artist=(x[i].getElementsByTagName("ARTIST")[0].childNodes[0].nodeValue);
title=(x[i].getElementsByTagName("TITLE")[0].childNodes[0].nodeValue);
year=(x[i].getElementsByTagName("YEAR")[0].childNodes[0].nodeValue);
txt="Artist: " + artist + "<br>Title: " + title + "<br>Year: "+ year;
document.getElementById("showCD").innerHTML=txt;
}
</script>
```
上面的程序通过XMLHttpRequest获取XML中的数据经过JS处理后再渲染到HTML中。

### More

<strong>命名空间。</strong>在使用XML过程中可能会碰到命名冲突的问题，给XML设定命名空间可以有效的避免,同时这样做也可以在使用XSLT转化XML时，命名空间也能很好的指定需要转化的部分。命名空间的声明语法如下
```
xmlns:前缀="URI"。
```
分别给予命名空间：
```
<root xmlns:h="http://xxx/1"
xmlns:f="http://xxx/2">

<h:table>
<h:tr>
<h:td>Apples</h:td>
<h:td>Bananas</h:td>
</h:tr>
</h:table>

<f:table>
<f:name>African Coffee Table</f:name>
<f:width>80</f:width>
<f:length>120</f:length>
</f:table>

</root>
```
其中命名空间中的URI并不会被解析，它的作用仅仅只是给予一个唯一的名称标标识。

使用默认的命名空间可以省去在每个标签都写上前缀的麻烦：
```
xmlns="namespaceURI"
```
ex:
```
<table xmlns="http://xxx/3">
<tr>
<td>Apples</td>
<td>Bananas</td>
</tr>
</table>
```

<strong>CDATA</strong> 在XML中只有在CDATA中的文本会被解析器忽略，语法如下：
```
<script>
<![CDATA[
function matchwo(a,b)
{
if (a < b && a < 0) then
{
return 1;
}
else
{
return 0;
}
}
]]>
</script>
```
其中在CDATA部分中不能包含 `']]>'` 也不可再嵌套CDATA内容 


### 总结

* XML 可用于交换、共享和存储数据。

* XML 文档形成 树状结构，在"根"和"叶子"的分支机构开始的。

* XML 有非常简单的 语法规则。带有正确语法的 XML 是"形式良好"的。有效的 XML 是针对 DTD 进行验证的。

* XSLT 用于把 XML 转换为其他格式，比如 HTML。

* 所有现代的浏览器有一个内建的 XML 解析器，可读取和操作 XML。

* DOM（Document Object Model）定义了一个访问 XML 的标准方式。

* XMLHttpRequest 对象提供了一个网页加载后与服务器进行通信的方式。

* XML 命名空间提供了一种避免元素命名冲突的方法。

* CDATA 区域内的文本会被解析器忽略。