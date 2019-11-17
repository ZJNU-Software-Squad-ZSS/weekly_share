## web开发技术


基础知识点

#### HTML

**1.标题**  

```
<h1>This is a heading</h1>
<h2>This is a heading</h2>
<h3>This is a heading</h3>
```

**2.段落**

```
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
```

   段落里换行<br/>

```
<p>This is<br />a para<br />graph with line breaks</p>
```

**3.链接**

```
<a href="http://www.w3school.com.cn">This is a link</a>
```

   href后面引号里时跳转的链接，this is a link 是网页里显示的文字

**4.图像**

```
<img src="w3school.jpg" width="104" height="142" />
```

- **替换文本属性（Alt）**

​    在浏览器无法载入图像时，替换文本属性告诉读者她们失去的信息

```
<img src="boat.gif" alt="Big Boat">
```

- **背景图片**

   background=“URL”

```
<html>

<body background="/i/eg_background.jpg">

<h3>图像背景</h3>

<p>gif 和 jpg 文件均可用作 HTML 背景。</p>

<p>如果图像小于页面，图像会进行重复。</p>

</body>
</html>
```

- **图片排版**

   align="bottom"

   align="middle"

   align="top"

```
<html>

<body>

<h2>未设置对齐方式的图像：</h2>

<p>图像 <img src ="/i/eg_cute.gif"> 在文本中</p>

<h2>已设置对齐方式的图像：</h2>

<p>图像 <img src="/i/eg_cute.gif" align="bottom"> 在文本中</p>

<p>图像 <img src ="/i/eg_cute.gif" align="middle"> 在文本中</p>

<p>图像 <img src ="/i/eg_cute.gif" align="top"> 在文本中</p>

<p>请注意，bottom 对齐方式是默认的对齐方式。</p>

</body>
</html>
```

- **调整图像尺寸**

   width="500"  height="50"

```
<html>

<body>

<img src="/i/eg_mouse.jpg" width="50" height="50">

<br />

<img src="/i/eg_mouse.jpg" width="100" height="100">

<br />

<img src="/i/eg_mouse.jpg" width="200" height="200">

<p>通过改变 img 标签的 "height" 和 "width" 属性的值，您可以放大或缩小图像。</p>

</body>
</html>
```

- **浮动图像：将图篇放置文本左侧或右侧**

  align="left"

  align="right"

```
<html>
<body>
<p>
<img src="/i/eg_cute.gif" align="left">
带有图像的一个段落。图像的 align 属性设置为 "left"。图像将浮动到文本的左侧。
</p>

<p>
<img src="/i/eg_cute.gif" align="right">
带有图像的一个段落。图像的 align 属性设置为 "right"。图像将浮动到文本的右侧。
</p>
</body>
</html>
```

- **制作图像链接**

```
<a href="url"><img src="rRl"></a>
```

```
<html>

<body>
<p>
您也可以把图像作为链接来使用：
<a href="/example/html/lastpage.html">
<img border="0" src="/i/eg_buttonnext.gif" />
</a>
</p>

</body>
</html>
```

  border表示边框

- **创建图像映射**：

   本例显示如何创建带有可供点击区域的图像地图。其中的每个区域都是一个超级链接。

```
<html>
<body>
<p>请点击图片上的星球，把它们放大</p>
<img src="/i/eg_planets.jpg" border="0" usemap="#planetmap" alt="Planets" />

<map name="planetmap" id="planetmap">

<area
shape="circle"
coords="180,139,14"
href="/example/html/venus.html"
target="_blank"
alt="Venus" />

<area
shape="circle"
coords="129,161,10"
href ="/example/html/mercur.html"
target ="_blank"
alt="Mercury" />

<area
shape="rect"
coords="0,0,110,260"
href ="/example/html/sun.html"
target ="_blank"
alt="Sun" />

</map>

<p><b>注释：</b>img 元素中的 "usemap" 属性引用 map 元素中的 "id" 或 "name" 属性（根据浏览器），所以我们同时向 map 元素添加了 "id" 和 "name" 属性。</p>

</body>
</html>

```

```
<map>  定义图像地图 
<area> 定义图像地图中的可点击区域
1.img里加入 usemap="#name"
2.定义map <map name="name">
3.定义area <area shape=" " coords=" " href=" " target=" ">
格式：
<img  src="" usemap="#xyz"  />
<map name="xyz">
<area  shape="" coords="" href="" target="" />
</map>
```

图像映射可以理解为图片加载图片，通过<img/>后添加<map>和<area>设置。

area元素的属性：

(1)shape：必须的属性，用于描述区域的形状，rect\poly\circle\default 可选, 矩形\多边形\圆形，default指的是还没有被定义的区域。

(2)coords：

<!--"rect"表示该区域是矩形，"0,0,100,100"表示左上角的坐标和右下角的坐标，左上角“0,0”-->

<!--"circle"表示该区域为圆形，"10,10,5"表示圆心坐标和半径-->

<!--"poly"表示多边形，"0,0,100,100,234,234,123,123,245,245"表示所有顶点的坐标-->

(4)target：

html target属性，一般是在a标签中使用

Target 属性，可以定义**被链接的文档在何处显示**。

1.   target="_blank"  在浏览器新窗口打开文档
2.  target="_parent" 这个目标使得文档载入父窗口或者包含来超链接引用的框架的框架集。如果这个引用是在窗口或者在顶级框架中，那么它与目标 _self 等效。
3.  target="_self" 这个目标的值对所有没有指定目标的 <a> 标签是默认目标，它使得目标文档载入并显示在相同的框架或者窗口中作为源文档。这个目标是多余且不必要的，除非和文档标题 <base> 标签中的 target 属性一起使用。
4.  target="_top" 这个目标使得文档载入包含这个超链接的窗口，用 _top 目标将会清除所有被包含的框架并将文档载入整个浏览器窗口。

**5.水平线**

```
<p>This is a paragraph</p>
<hr />
<p>This is a paragraph</p>
<hr />
<p>This is a paragraph</p>
```

**6.注释**

```
<!-- This is a comment -->
```

**7.样式**

- **背景颜色 <background-color>**

```
<html>

<body style="background-color:yellow">
<h2 style="background-color:red">This is a heading</h2>
<p style="background-color:green">This is a paragraph.</p>
</body>

</html>
```

- **字体、颜色和尺寸：font-family、color 以及 font-size 属性分别定义元素中文本的字体系列、颜色和字体尺寸**

```
<html>

<body>
<h1 style="font-family:verdana">A heading</h1>
<p style="font-family:arial;color:red;font-size:20px;">A paragraph.</p>
</body>

</html>
```

- **文本对齐：text-align**

```
<html>

<body>
<h1 style="text-align:center">This is a heading</h1>
<p>The heading above is aligned to the center of this page.</p>
</body>

</html>
```

**8.格式化**

| 标签     | 描述           |
| :------- | :------------- |
| <b>      | 定义粗体文本。 |
| <big>    | 定义大号字。   |
| <em>     | 定义着重文字。 |
| <i>      | 定义斜体字。   |
| <small>  | 定义小号字。   |
| <strong> | 定义加重语气。 |
| <sub>    | 定义下标字。   |
| <sup>    | 定义上标字。   |
| <ins>    | 定义插入字。   |
| <del>    | 定义删除字。   |

```
<html>

<body>

<b>This text is bold</b>

<br />

<strong>This text is strong</strong>

<br />

<big>This text is big</big>

<br />

<em>This text is emphasized</em>

<br />

<i>This text is italic</i>

<br />

<small>This text is small</small>

<br />

This text contains
<sub>subscript</sub>

<br />

This text contains
<sup>superscript</sup>

</body>
</html>
```

- 文字方向

  <bdo dir="rtl"> 从右向左输出

```
<html>

<body>

<p>
如果您的浏览器支持 bi-directional override (bdo)，下一行会从右向左输出 (rtl)；
</p>

<bdo dir="rtl">
Here is some Hebrew text
</bdo>

</body>
</html>
```

- 块引用

  ```
  <blockquote>
      长引用
  </blockquote>
  
  <q>
      短引用
  </q>
  ```

  ```
  <html>
  
  <body>
  
  这是长的引用：
  <blockquote>
  这是长的引用。这是长的引用。这是长的引用。这是长的引用。这是长的引用。这是长的引用。这是长的引用。这是长的引用。这是长的引用。这是长的引用。这是长的引用。
  </blockquote>
  
  这是短的引用：
  <q>
  这是短的引用。
  </q>
  
  <p>
  使用 blockquote 元素的话，浏览器会插入换行和外边距，而 q 元素不会有任何特殊的呈现。
  </p>
  
  </body>
  </html>
  ```

  使用 blockquote 元素的话，浏览器会插入换行和外边距

- 删除字和插入字效果

  ```
  <html>
  
  <body>
  
  <p>一打有 <del>二十</del> <ins>十二</ins> 件。</p>
  
  <p>大多数浏览器会改写为删除文本和下划线文本。</p>
  
  <p>一些老式的浏览器会把删除文本和下划线文本显示为普通文本。</p>
  
  </body>
  </html>
  ```

- 地址

  ```
  <!DOCTYPE html>
  <html>
  <body>
  
  <address>
  written by <a href=“mailto:webmaster@example.com”>Donald Duck</a>.<br>
  visit us at:<br>
  example.com<br>
  box 564m,Disneyland<br>
  USA
  </adress>
  
  </body>
  </html>
  ```

- 预格式文本

  预格式文本，它保留了空格和换行。

  ```
  <html>
  
  <body>
  
  <pre>
  这是
  预格式文本。
  它保留了      空格
  和换行。
  </pre>
  
  <p>pre 标签很适合显示计算机代码：</p>
  
  <pre>
  for i = 1 to 10
       print i
  next i
  </pre>
  
  </body>
  </html>
  ```

  

- “计算机输出”标签

  这些标签常用于显示计算机/编程代码。

  ```
  <html>
  
  <body>
  
  <code>Computer code</code>
  <br />
  <kbd>Keyboard input</kbd>
  <br />
  <tt>Teletype text</tt>
  <br />
  <samp>Sample text</samp>
  <br />
  <var>Computer variable</var>
  <br />
  
  <p>
  <b>注释：</b>这些标签常用于显示计算机/编程代码。
  </p>
  
  </body>
  </html>
  ```

  | 标签   | 描述                 |
  | :----- | :------------------- |
  | <code> | 定义计算机代码。     |
  | <kbd>  | 定义键盘码。         |
  | <samp> | 定义计算机代码样本。 |
  | <tt>   | 定义打字机代码。     |
  | <var>  | 定义变量。           |
  | <pre>  | 定义预格式文本。     |

- 缩写和首字母缩写

  ```
  <html>
  
  <body>
  
  <abbr title="etcetera">etc.</abbr>
  <br />
  <acronym title="world wide web">WWW</acronym> 
  
  <p>在某些浏览器中，当您把鼠标移至缩略词语上时，title 可用于展示表达的完整版本。</p>
  
  <p>仅对于 IE 5 中的 acronym 元素有效。</p>
  
  <p>对于 Netscape 6.2 中的 abbr 和 acronym 元素都有效。</p>
  
  </body>
  </html>
  ```

  | 标签         | 描述               |
  | :----------- | :----------------- |
  | <abbr>       | 定义缩写。         |
  | <acronym>    | 定义首字母缩写。   |
  | <address>    | 定义地址。         |
  | <bdo>        | 定义文字方向。     |
  | <blockquote> | 定义长的引用。     |
  | <q>          | 定义短的引用语。   |
  | <cite>       | 定义引用、引证。   |
  | <dfn>        | 定义一个定义项目。 |

**9.CSS**

- HTML中的样式

    使用添加到 <head> 部分的样式信息对 HTML 进行格式化。

  ```
  <html>
  
  <head>
  <style type="text/css">
  h1 {color: red}
  p {color: blue}
  </style>
  </head>
  
  <body>
  <h1>header 1</h1>
  <p>A paragraph.</p>
  </body>
  
  </html>
  ```

- 创建没有下划线的链接

  style="text-decoration:none"

  ```
  <html>
  <head>
  <meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
  <meta http-equiv="Content-Language" content="zh-cn" />
  </head>
  
  <body>
  
  <a href="/example/html/lastpage.html" style="text-decoration:none">
  这是一个链接！
  </a>
  
  </body>
  </html>
  ```

**10.链接**

- 创建超级链接

  ```
  <html>
  
  <body>
  
  <p>
  <a href="/index.html">本文本</a> 是一个指向本网站中的一个页面的链接。</p>
  
  <p><a href="http://www.microsoft.com/">本文本</a> 是一个指向万维网上的页面的链接。</p>
  
  </body>
  </html>
  ```

  1. 通过使用 href 属性 - 创建指向另一个文档的链接
  2. 通过使用 name 属性 - 创建文档内的书签
  3. 使用 Target 属性，你可以定义被链接的文档在何处显示

- HTML链接中的name属性

  name 属性规定锚（anchor）的名称。 

  您可以使用 name 属性创建 HTML 页面中的书签。

  书签不会以任何特殊方式显示，它对读者是不可见的。

  当使用命名锚（named anchors）时，我们可以创建直接跳至该命名锚（比如页面中某个小节）的链接，这样使用者就无需不停地滚动页面来寻找他们需要的信息了。

  **命名锚的语法：**

  ```
  <a name="label">锚（显示在页面上的文本）</a>
  ```

  **提示：**锚的名称可以是任何你喜欢的名字。

  **提示：**您可以使用 id 属性来替代 name 属性，命名锚同样有效。

  **实例**

  首先，我们在 HTML 文档中对锚进行命名（创建一个书签）：

  ```
  <a name="tips">基本的注意事项 - 有用的提示</a>
  ```

  然后，我们在同一个文档中创建指向该锚的链接：

  ```
  <a href="#tips">有用的提示</a>
  ```

  您也可以在其他页面中创建指向该锚的链接：

  ```
  <a href="http://www.w3school.com.cn/html/html_links.asp#tips">有用的提示</a>
  ```

  在上面的代码中，我们将 # 符号和锚名称添加到 URL 的末端，就可以直接链接到 tips 这个命名锚了。

- 在新的浏览器窗口打开链接

  使用target="_blank"

  ```
  <html>
  
  <body>
  
  <a href="http://www.w3school.com.cn/" target="_blank">Visit W3School!</a>
  
  <p>如果把链接的 target 属性设置为 "_blank"，该链接会在新窗口中打开。</p>
  
  </body>
  
  </html>
  
  ```

- 跳出框架

  ```
  <html>
  
  <body>
  
  <p>被锁在框架中了？</p>
  <a href="/index.html" targe="_top">请点击这里 </a>
  
  </body>
  </html>
  ```


- 创建电子邮件链接

  href="mailto：电子邮件地址”可以创建电子邮件链接

  基本语法：

  ```
  <a href="mailto:841422538@qq.com">Email</a>
  ```

  现在，如果用户单击此链接，它就能自动打开当前计算机系统中默认的电子邮件客户端软件，例如OutLook Express以及Foxmail等。

  注：使用此方法发送电子邮件有一个问题，如果用户的计算机上没有安装电子邮件客户端，则无法发送电子邮件。

  指定主题:subject

  ```
  <a href="mailto:841422538@qq.com?subject=hello%20again"></a>
  ```

  抄送cc：顾名思义就是把你所要发送的邮件复制一份，同时在发给别的人，但会注明“抄送”字样，用来提示对方，他不是主送人，不用答复、批复。

  注意：我们应该使用 %20 来替换单词之间的空格字符，这样在浏览器上才可以正确地显示文本。

**11.表格**

- **table常用标签：**
  1、table标签：声明一个表格
  2、tr标签：定义表格中的一行
  3、td和th标签：定义一行中的一个单元格，td代表普通单元格，th表示表头单元格
  **table常用属性：** 
  1、border 定义表格的边框
  2、cellpadding 定义单元格内内容与边框的距离
  3、cellspacing 定义单元格与单元格之间的距离
  4、align 设置单元格中内容的水平对齐方式,设置值有：left | center | right
  5、valign 设置单元格中内容的垂直对齐方式 top | middle | bottom
  6、colspan 设置单元格水平合并
  7、rowspan 设置单元格垂直合并

  ```
  <table border="1">
  <tr>
  <td>100<td>
  <td>200<td>
  </tr>
  </table>
  ```

- 表格的表头

  表头使用<th>标签定义

  ```
  <table border="1">
  
  <tr>
  <th>Heading<th>
  <th>Heading2<th>
  </tr>
  
  <tr>
  <td>sun</td>
  <td>light</td>
  </tr>
  
  </table>
  ```

- 表格中的空单元格

  空格占位符：&nbsp

  ```
  <td>&nbsp</td>
  ```


- 带有标题的表格

  <caption>标题</caption>

  ```
  <table border="6">
  <caption>我的标题</caption>
  <tr>
    <td>100</td>
    <td>200</td>
    <td>300</td>
  </tr>
  <tr>
    <td>400</td>
    <td>500</td>
    <td>600</td>
  </tr>
  </table>
  ```

- 跨行或跨列的表格单元格

  <th colspan="2">电话</th> 横跨两列的单元格

  <th rowspan="2">电话</th>横跨两行的单元格

  ```
  <h4>横跨两列的单元格：</h4>
  <table border="1">
  <tr>
    <th>姓名</th>
    <th colspan="2">电话</th>
  </tr>
  <tr>
    <td>Bill Gates</td>
    <td>555 77 854</td>
    <td>555 77 855</td>
  </tr>
  </table>
  
  <h4>横跨两行的单元格：</h4>
  <table border="1">
  <tr>
    <th>姓名</th>
    <td>Bill Gates</td>
  </tr>
  <tr>
    <th rowspan="2">电话</th>
    <td>555 77 854</td>
  </tr>
  <tr>
    <td>555 77 855</td>
  </tr>
  </table>
  ```

- 表格内的标签

  ```
  <table border="1">
  <tr>
   <td>
    <p>这是一个段落</p>
    <p>这是另一个段落</p>
   </td>
   <td>这个单元包含一个表格：
     <table border="1">
     <tr>
       <td>A<td>
       <td>B<td>
     </tr>
     <tr>
       <td>C</td>
       <td>D</td>
     </tr>
     <table>
   </td>
  </tr>
  ```

- 单元格边距

  使用 Cell padding 来创建单元格内容与其边框之间的空白

  ```
  <table border="1" cellpadding="10">
  <tr>
    <td>First</td>
    <td>Row</td>
  </tr>   
  <tr>
    <td>Second</td>
    <td>Row</td>
  </tr>
  </table>
  ```

  

- 单元格间距

  使用 Cell spacing 增加单元格之间的距离。

  ```
  <table border="1" cellspacing="10">
  <tr>
    <td>First</td>
    <td>Row</td>
  </tr>   
  <tr>
    <td>Second</td>
    <td>Row</td>
  </tr>
  </table>
  ```

  

- 向表格添加背景颜色或背景图像

  ```
  背景颜色
  <table border="1" bgcolor="red">
  <tr>
    <td>First</td>
    <td>Row</td>
  </tr>   
  <tr>
    <td>Second</td>
    <td>Row</td>
  </tr>
  </table>
  
  背景图像
  <table bordre="1" background="/i/eg_bg_07.gif">
  <tr>
    <td>First</td>
    <td>Row</td>
  </tr>   
  <tr>
    <td>Second</td>
    <td>Row</td>
  </tr>
  </table>
  ```

- 单元格排列

  使用 "align" 属性排列单元格内容,以便创建一个美观的表格。

  ```
  <th align="left">消费项目....</th>
  <th align="right">一月</th>
  ```

  

​     