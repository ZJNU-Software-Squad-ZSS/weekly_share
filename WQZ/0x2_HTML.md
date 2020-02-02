## HTML基础

**列表**

- 无序列表

  无序列表是一个项目的列表，此列项目<u>使用粗体圆点（典型的小黑圆圈）进行标记</u>。

  无序列表始于 <ul> 标签。每个列表项始于 <li>。

  ```
  <ul>
  <li>Coffee</li>
  <li>Milk</li>
  </ul>
  ```

- 有序列表

  同样，有序列表也是一列项目，列表项目<u>使用数字进行标记</u>。

  有序列表始于 <ol> 标签。每个列表项始于 <li> 标签。

  ```
  <ol>
  <li>Coffee<li>
  <li>Milk<li>
  </ol>
  ```

- 自定义列表

  自定义列表不仅仅是一列项目，而是项目及其注释的组合。

  自定义列表以 <dl> 标签开始。每个自定义列表<u>项</u>以 <dt> 开始。每个自定义列表项的<u>定义</u>以 <dd> 开始。

  ```
  <dl>
  <dt>Coffee</dt>
  <dd>Black hot drink</dd>
  <dt>Milk</dt>
  <dd>White cold drink</dd>
  </dl>
  ```

- 不同类型的无序列表

  ```
  <h4>Disc 项目符号列表：</h4>
  <ul type="disc">
   <li>苹果</li>
   <li>香蕉</li>
   <li>柠檬</li>
   <li>桔子</li>
  </ul>  
  
  <h4>Circle 项目符号列表：</h4>
  <ul type="circle">
   <li>苹果</li>
   <li>香蕉</li>
   <li>柠檬</li>
   <li>桔子</li>
  </ul>  
  
  <h4>Square 项目符号列表：</h4>
  <ul type="square">
   <li>苹果</li>
   <li>香蕉</li>
   <li>柠檬</li>
   <li>桔子</li>
  </ul>  
  ```

- 不同类型的有序列表

  ```
  <h4>数字列表：</h4>
  <ol>
   <li>苹果</li>
   <li>香蕉</li>
   <li>柠檬</li>
   <li>桔子</li>
  </ol>  
  
  <h4>字母列表：</h4>
  <ol type="A">
   <li>苹果</li>
   <li>香蕉</li>
   <li>柠檬</li>
   <li>桔子</li>
  </ol>  
  
  <h4>小写字母列表：</h4>
  <ol type="a">
   <li>苹果</li>
   <li>香蕉</li>
   <li>柠檬</li>
   <li>桔子</li>
  </ol>  
  
  <h4>罗马字母列表：</h4>
  <ol type="I">
   <li>苹果</li>
   <li>香蕉</li>
   <li>柠檬</li>
   <li>桔子</li>
  </ol>  
  
  <h4>小写罗马字母列表：</h4>
  <ol type="i">
   <li>苹果</li>
   <li>香蕉</li>
   <li>柠檬</li>
   <li>桔子</li>
  </ol>  
  ```

- 嵌套列表

  ```
  <h4>一个嵌套列表：</h4>
  <ul>
    <li>咖啡</li>
    <li>茶
      <ul>
      <li>红茶</li>
      <li>绿茶
        <ul>
        <li>中国茶</li>
        <li>非洲茶</li>
        </ul>
      </li>
      </ul>
    </li>
    <li>牛奶</li>
  </ul>
  ```

  

**块**

- HTML<div>元素

  ```
  <div>元素是块级元素，它是可用于组合其他HTML元素的容器
  <div>元素没有特定的含义。除此之外，由于它属于块级元素，浏览器会在其前后显示折行。
  如果与CSS一同使用，<div>元素可用于对大的内容块设置样式属性。
  <div>元素的另一个常见的用途是文档布局。它取代了使用表格定义布局的老式方法。使用 <table> 元素进行文档布局不是表格的正确用法。<table> 元素的作用是显示表格化的数据。
  ```

- HTML<span>元素

  ```
  HTML <span> 元素是内联元素，可用作文本的容器。
  <span> 元素也没有特定的含义。
  当与 CSS 一同使用时，<span> 元素可用于为部分文本设置样式属性。
  ```

  

类

- 对HTML进行分类（设置类），使我们能够为元素的类定义CSS样式

  为相同的类设置相同的样式，或者为不同的类设置不同的样式

  ```
  <!DOCTYPE html>
  <html>
  <head>
  <style>
  .cities {
      background-color:black;
      color:white;
      margin:20px;
      padding:20px;
  } 
  </style>
  </head>
  
  <body>
  
  <div class="cities">
  <h2>London</h2>
  <p>
  London is the capital city of England. 
  It is the most populous city in the United Kingdom, 
  with a metropolitan area of over 13 million inhabitants.
  </p>
  </div> 
  
  </body>
  </html>
  ```

- 分类块级元素

  HTML<div>元素是块级元素。它能够用作其他HTML元素的容器。

  设置<div>元素的类，使我们能够为相同的<div>元素设置相同的类

  ```
  <!DOCTYPE html>
  <html>
  <head>
  <style>
  .cities {
      background-color:black;
      color:white;
      margin:20px;
      padding:20px;
  } 
  </style>
  </head>
  
  <body>
  
  <div class="cities">
  <h2>London</h2>
  <p>London is the capital city of England. 
  It is the most populous city in the United Kingdom, 
  with a metropolitan area of over 13 million inhabitants.</p>
  </div>
  
  <div class="cities">
  <h2>Paris</h2>
  <p>Paris is the capital and most populous city of France.</p>
  </div>
  
  <div class="cities">
  <h2>Tokyo</h2>
  <p>Tokyo is the capital of Japan, the center of the Greater Tokyo Area,
  and the most populous metropolitan area in the world.</p>
  </div>
  
  </body>
  </html>
  ```

- 分类行内元素

  HTML<span>元素是行内元素，能够用作文本的容器。

  设置<span>元素的类，能够为相同的<span>元素设置相同的样式

  ```
  <html>
  <head>
  <style>
    span.red{color:red;}
  </style>
  </head>
  <body>
  
  <h1>My<span class="red">Important</span>Heading</h1>
  
  </body>
  </html>
  ```

  

布局

- 使用<div>元素的HTML布局

  <div>元素通常用作布局工具，因为能够轻松地通过CSS对其进行定位

- ```
  <body>
  
  <div id="header">
  <h1>City Gallery</h1>
  </div>
  
  <div id="nav">
  London<br>
  Paris<br>
  Tokyo<br>
  </div>
  
  <div id="section">
  <h1>London</h1>
  <p>
  London is the capital city of England. It is the most populous city in the United Kingdom,
  with a metropolitan area of over 13 million inhabitants.
  </p>
  <p>
  Standing on the River Thames, London has been a major settlement for two millennia,
  its history going back to its founding by the Romans, who named it Londinium.
  </p>
  </div>
  
  <div id="footer">
  Copyright W3School.com.cn
  </div>
  
  </body>
  ```

  CSS：

  ```
  <style>
  #header{
      background-color:black;
      color:white;
      text-align:center;
      padding:5px;
  }
  
  #nav{
     line-height:30px;
     background-color:#eeeeee;
     height:300px;
     width:100px;
     float:left;
     padding:5px;
  }
  #section{
     width:350px;
     float:left;
     padding:10px;
  }
  
  #footer{
    background-color:black;
    color:white;
    clear:both;
    text-align:center;
    padding:5px;
  }
  </style>
  ```

  ##### HTML5 语义元素

  | header  | 定义文档或节的页眉             |
  | ------- | ------------------------------ |
  | nav     | 定义导航链接的容器             |
  | section | 定义文档中的节                 |
  | article | 定义独立的自包含文章           |
  | aside   | 定义内容之外的内容（比如侧栏） |
  | footer  | 定义文档或节的页脚             |
  | details | 定义额外的细节                 |
  | summary | 定义 details 元素的标题        |

- ```
  <body>
  
  <header>
  <h1>City Gallery</h1>
  </header>
  
  <nav>
  London<br>
  Paris<br>
  Tokyo<br>
  </nav>
  
  <section>
  <h1>London</h1>
  <p>
  London is the capital city of England. It is the most populous city in the United Kingdom,
  with a metropolitan area of over 13 million inhabitants.
  </p>
  <p>
  Standing on the River Thames, London has been a major settlement for two millennia,
  its history going back to its founding by the Romans, who named it Londinium.
  </p>
  </section>
  
  <footer>
  Copyright
  </footer>
  
  </body>
  ```

  CSS

  ```
  <style>
  header{
     background-color:black;
     color:white;
     text-align:center;
     padding:5px;
  }
  
  nav{
     line-height:30px;
     background-color:#eeeeee;
     height:300px;
     width:100px;
     float:left;
     padding:5px;
  }
  
  section{
     width:350px;
     float:left;
     padding:10px;
  }
  
  footer{
     background-color:black;
     color:white;
     clear:both;
  }
  ```

- 使用表格的HTML布局

  ```
  <table>元素不是作为布局工具而设计的.
  <table>元素的作用是显示表格化的数据。
  使用 <table> 元素能够取得布局效果，因为能够通过 CSS 设置表格元素的样式：
  ```
  
  ```
  <body>
  
  <table class="lamp">
  <tr>
    <th>
      <img src=" " alt=" " height:32px ; width:32px>
    </th>
    <td>
      The table element was not designed to be a layout tool.
    </td>
  </tr>
  </table>
  </body>
  ```
  
  CSS
  
  ```
  <style>
  table.lamp{
      width:100%;
      border:1px solid #d4d4d4;
  }
  table.lamp th,td{
      padding:10px;
  }
  table.lamp td{
      width:40px;
  }
  </style>
  
  ```
  
  

响应式设计

- ```
  什么是响应式 Web 设计？
  RWD 指的是响应式 Web 设计（Responsive Web Design）
  RWD 能够以可变尺寸传递网页
  RWD 对于平板和移动设备是必需的
  ```

  

框架

- 通过使用框架，你可以在同一个浏览器窗口中显示不止一个页面。每份HTML文档称为一个框架，并且每个框架都独立于其他的框架。 

   使用框架的坏处：

  - 开发人员必须同时跟踪更多的HTML文档
  - 很难打印整张页面

- 框架结构标签（<frameset>）
  - 框架结构标签（<frameset>）定义如何将窗口分割为框架
  - 每个 frameset 定义了一系列行*或*列
  - rows/columns 的值规定了每行或每列占据屏幕的面积

-  框架标签（Frame）
  Frame 标签定义了放置在每个框架中的 HTML 文档。
  在下面的这个例子中，我们设置了一个两列的框架集。第一列被设置为占据浏览器窗口的 25%。第二列被设置为占据浏览器窗口的 75%。HTML 文档 "frame_a.htm" 被置于第一个列中，而 HTML 文档 "frame_b.htm" 被置于第二个列中：
  
  ```
  <frameset cols="25%,75%">
     <frame src="网页链接">
     <frame src=" ">
  </frameset>
  ```
  
  - 基本的注意事项 - 有用的提示：
    假如一个框架有可见边框，用户可以拖动边框来改变它的大小。为了避免这种情况发生，可以在 <frame> 标签中加入：noresize="noresize"。
    为不支持框架的浏览器添加 <noframes> 标签。

- 混合框架结构

  有行有列

  ```
  <html>
  <frameset rows="50% ,50%">
  <frame src="网页链接 ">
  <frameset cols="25%,75%">
  <frame src="网页链接 ">
  <frame src="网页链接 ">
  </frameset>
  </frameset>
  </html>
  ```

- 导航框架

  ```
  <html>
  <frameset cols="120,*">
     <frame src=" .html">
     <frame src=" .html" name="showframe">
  </frameset>
  </html>
  ```

  具体的

  ```
  在5.html里写入
  <html>
  <framesetcols="30%,70%">
  <frame src="4.html" />
  <framesrc="5.html" name="show"/>
  </html>
  
  在4.html里写入
  <html>
  <p>  <ahref="1.html" target="show">A</a>     </p>
  <p>  <a href="2.html" target="show">B</a>    </p>
  <p>  <a href="3.html" target="show">C</a>     </p>
  </html>
  ```

  