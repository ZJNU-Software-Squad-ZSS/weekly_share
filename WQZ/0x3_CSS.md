## CSS

developer.mozilla.org/en-US(中文zh-CN)/docs/web/CSS



字体

www.cssfontstack.com

fonts.google.com

thetype.com

字谈字畅

快捷键

lorem乱数假文

li*5 5列

link css

.box

body代表整个页面

如果在自己块里没有定义的属性会沿袭body里的属性



```
   font-family: Verdana, Geneva, Tahoma, sans-serif;
   font-style: italic;
   font-weight: normal;
   font-size: 16px;
   text-decoration: underline;
   color: blue;
   text-align: center;
   text-transform: capitalize;
   text-shadow: -1px 1px #aaa,
   0px 4px 1px rgba(0,0,0,0.5),
   4px 4px 5px rgba(0,0,0,0.7),
   0px 0px 7px rgba(0,0,0,0.4);
   line-height: 1.5;
   letter-spacing: 2px;
   word-spacing: 4px; 
```



```
list-style-type: square;
list-style-image: url("check.jpg");
list-style-position: inside;
```



```
 a[href*="http"] 选中 <a> 元素，但是只会选中那些拥有 href 属性，且属性的值包含 "http" 的 <a>的元素。
 在链接上设置 padding-right ，为背景图片留出空间，所以我们不会和文本重叠。
Link (没有访问过的): 这是链接的默认状态，当它没有处在其他状态的时候，它可以使用:link 伪类来应用样式。
Visited: 这个链接已经被访问过了(存在于浏览器的历史纪录), 它可以使用 :visited 伪类来应用样式。
Hover: 当用户的鼠标光标刚好停留在这个链接，它可以使用 :hover 伪类来应用样式。
Focus: 一个链接当它被选中的时候 (比如通过键盘的 Tab  移动到这个链接的时候，或者使用编程的方法来选中这个链接 HTMLElement.focus()) 它可以使用 :focus 伪类来应用样式。
Active: 一个链接当它被激活的时候 (比如被点击的时候)，它可以使用 :active 伪类来应用样式。
```

```
a:link{
    color: black;
    outline: none;
    text-decoration: none;
}

a:hover{
    border-bottom: 0.5px solid black;
    color: orange;
}

a:active{
    
    color:rgb(194, 206, 151);
    background-color: yellow;
}

a:visited{
    color: palegreen;
}

a[href*=".com"]{
    background: url("check.jpg") no-repeat 100% 0;
    padding-right: 19px;
}
```

选择器

选择在<aside>里的<ul>里的<li>而不是其他地方的<li>

```
aside ul li{
    line-height: 1.6;
    list-style: circle;
}
```



```
div:nth-of-type(1) {
  width: 48%;
}

div:nth-of-type(2) {
  width: 48%;
}
```

奇，偶数，指定数样式

1.简单数字序号写法

```
:nth-child(number)
```

直接匹配第number个元素。参数number必须为大于0的整数。

例子：

```
li:nth-child(3){background:orange;}/把第3个LI的背景设为橙色/
```

2.倍数

```
:nth-chile(an)
```

匹配所有倍数为a的元素。其中参数an中的字母n不可缺省，它是倍数写法的标志，如3n、5n。

例子：

```
li:nth-child(3n){background:orange;}/把第3、第6、第9、…、所有3的倍数的LI的背景设为橙色/
```

3.奇偶匹配

```
:nth-child(odd) 与 :nth-child(even)
```

分别匹配序号为奇数与偶数的元素。奇数(odd)与(2n+1)结果一样；偶数(even)与(2n+0)及(2n)结果一样。

表格奇偶数行定义样式就可以写成

```
.table > tr:nth-child(even) > td {} //（偶数行）

.table > tr:nth-child(odd) > td {background-color: #ccc;} //（奇数行）
```

link用于菜单按钮

```
<ul>
    <li><a href="#">Home</a></li>
    <li><a href="#">Finding us</a></li>
    <li><a href="#">Courses</a></li>
    <li><a href="#">Staff</a></li>
    <li><a href="#">Media</a></li>
    <li><a href="#">Prospectus</a></li>
</ul>
```

```
.list{
    font-size: large;
    color: #a66;
}
.list ul {
    padding: 0;
    width: 100%;
    list-style-type: none;
  }



.list a {
    outline: none;
    text-decoration: none;
    text-align: center;
    line-height: 2;
    

  }
  
.list  li:last-child a {
    margin-right: 0;
  }
.list a{
   width: 160px;
   display: block;
   margin-top:4px ;
}
.list  a:link, a:visited, a:focus {
    border: #a66 1px solid;
    padding: 20px;
    color: #a66;
  }
  
.list  a:hover {     
    background: orange;
  }
  
.list  a:active {
    background: red;
    color: white;
  }

```

要**将列表前面的标点**去掉：

```
ul{
   list-style-type:none;
}
```

要设置a的框的宽和高：要先将它设置成display：block，才能定义宽高

```
a{
   display:block;
   width:160px;
}
```

不能设置height和width在inline元素中，要用disply：block后才能设置

常见的inline元素

<a> <img> <map> <br> <em> <botton>  <span>  <strong> <small>



```
body{
    width: 500px;
    margin:auto;
}

h1{
    text-align: center;
}

p{
    background: rgba(255, 84, 104, 0.3);
    border: 2px solid rgb(255, 84, 104);
    padding: 10px;
    margin: 10px;
}
```



### flex-box弹性盒子

每一个大小相同

```
display:flex
flex-direction:column;
flex-wrap:wrap;
flex:200px;
article{
   flex:1 ;
}

article:nth-of-type(3){
   flex:2;
}

```

[`align-items`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/align-items)控制 flex 项在交叉轴上的位置。

```
align-items: center;  一般用这个
align-items: flex-end;
align-items: flex-start;
```

[`justify-content`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/justify-content) 控制 flex 项在主轴上的位置

```
justify-content: center;
justify-content: flex-end;
justify-content: flex-start;
justify-content: space-between;
justify-content: space-around;  一般用这个
justify-content: space-evenly;
```

#### flex项排序

- 所有 flex 项默认的 [`order`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/order) 值是 0。

- order 值大的 flex 项比 order 值小的在显示顺序中更靠后。

- 相同 order 值的 flex 项按源顺序显示。所以假如你有四个元素，其 order 值分别是2，1，1和0，那么它们的显示顺序就分别是第四，第二，第三，和第一。

- 第三个元素显示在第二个后面是因为它们的 order 值一样，且第三个元素在源顺序中排在第二个后面。

  ```
  button：first-child{
      order:1;
  }
  ```

  

#### flex嵌套



#### box-sizing

```
box-sizing:content-box;
box-sizing:border-box;
```
使用content-box：会超出父框范围 

其设置的width与height只会应用到这个元素的内容区。如果这个元素有任何的 [`border`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/border) 或 [`padding`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/padding) ，绘制到屏幕上时的盒子宽度和高度会加上设置的边框和内边距值。这意味着当你调整一个元素的宽度和高度时需要时刻注意到这个元素的边框和内边距。当我们实现响应式布局时，这个特点尤其烦人。

```
box-sizing: content-box;
width: 100%;
border: solid #5B6DCD 10px;
padding: 5px;
```
使用border-box 在父框里面

`border-box` 告诉浏览器：你想要设置的边框和内边距的值是包含在width内的。也就是说，如果你将一个元素的width设为100px，那么这100px会包含它的border和padding，内容区的实际宽度是width减去(border + padding)的值。大多数情况下，这使得我们更容易地设定一个元素的宽高

```
box-sizing: border-box;
width: 100%;
border: solid #5B6DCD 10px;
padding: 5px;
```



### Grid Layout网格布局

## What is a grid?

A grid is an intersecting set of horizontal and vertical lines – one set defining columns, and the other, rows. Elements can be placed onto the grid, within these column and row lines. 

## The Grid container

We create a *grid container* by declaring `display: grid` or `display: inline-grid` on an element. As soon as we do this, all *direct children* of that element become *grid items*.

```
.wrapper{
   display:grid;
}
```

## Grid Tracks

We define rows and columns on our grid with the [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-columns) and [`grid-template-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-rows) properties. These define grid tracks. A *grid track* is the space between any two lines on the grid. 

#### grid-template-columns(定义格子的宽)

```
grid-template-columns:60px 60px;
grid-template-columns:1fr 60px;
grid-template-columns:1fr 2fr;
grid-template-columns:8ch auto;
```

#### grid-template-rows(定义格子的高度)

```
grid-template-rows:auto;
grid-template-rows:40px 4em 40px;
grid-template-rows:1fr 2fr 1fr;
```

#### fr单位(就是一个比例单位和flex：1有点像)

在下一个示例中，我们创建一个定义，先定义一个`2fr`轨迹，然后定义两个`1fr`轨迹。可用空间分为四个。第一部分分为两部分，第二部分分别为一部分。

```
.wrapper{
   display:grid;
   grid-template-columns:2fr 1fr 1fr;
}
```

在最后一个示例中，我们将绝对大小的轨道与分数单位混合在一起。第一轨道为500像素，因此固定宽度会从可用空间中扣除。剩余空间分为三个部分，并与两个柔性轨道成比例分配。

```
.wrapper{
   display:grid;
   grid-template-columns:500px 1fr 2fr;
}
```

#### repeat() 

具有多个轨道的大型网格可以使用该  `repeat()`符号来重复轨道列表的全部或一部分。

```css
.wrapper {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}
```

也可以写成：

```
.wrapper{
  display:grid;
  grid-template-columns:repeat(3,1fr);
}
```

重复符号可<u>用于部分曲目列表</u>。在下一个示例中，我创建了一个带有初始20像素轨道，然后是6个`1fr`轨道的重复部分，最后是20像素轨道的网格。

```
.wrapper{
   display:grid;
   grid-template-columns:20px repeat(6,1fr) 20px;
}
```

重复表示法获取曲目列表，并使用它来创建曲目的重复模式。在下一个示例中，我的网格将包含10个轨道，一个`1fr`轨道，然后是一个`2fr`轨道。此模式将重复五次.

```
.wrapper{
   display:grid;
   grid-template-columns:repeat(5,1fr,2fr);
}
```

#### 隐式和显式网格

在创建示例网格时，我们使用[`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-columns)属性专门定义了列轨迹，但是网格也自行创建了行。这些行是隐式网格的一部分。显式网格由用[`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-columns)或定义的任何行和列组成[`grid-template-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-rows)。

您还可以使用[`grid-auto-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-auto-rows)和[`grid-auto-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-auto-columns)属性为<u>在隐式网格中创建的轨道定义设置大小</u>。

在下面的示例中，我们用于`grid-auto-rows`确保在隐式网格中创建的轨道的高度为200像素。

```
.wrapper {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-auto-rows: 200px;
}
```

#### 网格大小和minmax()

在设置显式网格或定义自动创建的行或列的大小时，我们可能希望为轨道提供最小尺寸，但还要确保它们可以扩展以适合所添加的任何内容。例如，我可能希望行的折叠长度永远不会小于100像素，但是如果我的内容延伸到300像素的高度，那么我希望行延伸到该高度。

Grid具有此[`minmax()`](https://developer.mozilla.org/en-US/docs/Web/CSS/minmax)功能的解决方案。

下面示例中：这意味着自动创建的行的最小高度为100像素，最大为`auto`。使用`auto`表示大小将查看内容大小，并会拉伸以为该行中单元格中最高的项目提供空间。

```
.wrapper{
   display:grid;
   grid-template-columns:repeat(3,1fr);
   grid-auto-rows:minmax(100px,auto);
}
```

### 根据行定位项目

我们将在后面的文章中详细探讨基于行的放置。以下示例演示了一种简单的方法。放置物品时，我们将目标对准线而不是轨道。

在下面的例子里，我把我们的三列的铁路网前两项，使用[`grid-column-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-column-start)，[`grid-column-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-column-end)，[`grid-row-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-row-start)和[`grid-row-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-row-end)属性。从左到右工作，第一项放置在列线1的上方，并跨越到列线4，在我们的情况下，列线是网格上最右边的线。它从第1行开始，到第3行结束，因此跨越两个行磁道。

第二项从网格列第1行开始，跨越一条轨道。这是默认设置，因此不需要指定结束行。它还跨越了从第3行到第5行的两个行轨迹。其他项将自己放置在网格上的空白区域中

```html
<div class="wrapper">
  <div class="box1">One</div>
  <div class="box2">Two</div>
  <div class="box3">Three</div>
  <div class="box4">Four</div>
  <div class="box5">Five</div>
</div>
```

```css
.wrapper { 
  display: grid; 
  grid-template-columns: repeat(3, 1fr); 
  grid-auto-rows: 100px; 
} 

.box1 { 
  grid-column-start: 1; 
  grid-column-end: 4; 
  grid-row-start: 1; 
  grid-row-end: 3; 
}

.box2 { 
  grid-column-start: 1; 
  grid-row-start: 3; 
  grid-row-end: 5; 
}
```

#### gap 间距

在列之间创建了10像素的间距，在行之间创建了10像素的间距。[`column-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/column-gap)[`row-gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/row-gap)[`gap`](https://developer.mozilla.org/en-US/docs/Web/CSS/gap)`1em`

```
.wrapper{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    column-gap:10px;
    row-gap:1em;
}
```



### float浮动



#### 首字母下沉

#### 多列浮动布局

```
body{
    width: 90%;
    max-width: 900px;
    margin: 0 auto;
}

div:nth-of-type(1){
    width: 48%;
    float: left;
}

div:nth-of-type(2){
    width: 48%;
    float: right;
}
```

你会注意到，我们所有列使用宽度百分比——这是一个很好的策略，因为它创建一个流式布局（**liquid layout**），一种调整为不同的屏幕尺寸，并在较小的屏幕尺寸下保持相同的列宽度比例。请尝试调整浏览器窗口的宽度，以便自己查看。这是响应式网页设计的一个有价值的工具，我们将在以后的模块中讨论。

#### 三列布局

```
body{
    width: 90%;
    max-width: 900px;
    margin: 0 auto;
}

div:nth-of-type(1){
    width: 36%;
    float: left;
}

div:nth-of-type(2){
    width: 30%;
    float: left;
    margin-left: 4%;
}

div:nth-of-type(3){
    width: 26%;
    float: right;
}
```

三列加起来的width最好不要到100% 留一点分给列间距

尝试改变第二列的 [`float`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/float)值为 `right` ，你会看到现在的视觉顺序是这样的：



<label>and <input>

```
<div class="preference">
    <label for="cheese">Do you like cheese?</label>
    <input type="checkbox" name="cheese" id="cheese">
</div>
```

将一个 `<label>` 和一个<input>元素放在一起会有以下几点好处：

- 标签文本不仅与其相应的文本输入在视觉上相关联; 它也以编程方式与它相关联。 这意味着，当用户点击到表单输入时，屏幕阅读器可以读出标签，使在使用辅助技术的用户更容易理解应输入哪些数据.
- 你可以单击关联的标签来聚焦或者激活 input，以及 input 本身。这种增加的命中区域为激活 input 提供了方便，包括那些使用触摸屏设备的。

想要将一个 `<label>` 和一个 `<input>` 元素匹配在一起，你需要给 `<input>` 一个 `id` 属性。而 `<label>` 需要一个 `for` 属性，其值和 input 的 `id` 一样。



#### cursor

**cursor** [CSS](https://developer.mozilla.org/zh-CN/docs/Web/CSS)属性定义鼠标指针悬浮在元素上方显示的鼠标光标。

```
cursor:help;
cursor:wait;
cursor:crosshair;
cursor:not-allowed;
cursor:zoom-in;
```



#### transition

可以为一个元素在不同状态之间切换的时候定义不同的过渡效果。



#### 多列布局

带有 `.container` 的 <div>将成为我们 multicol 的容器。 通过这两个属性开启 multicol [`column-count`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/column-count) 或者 [`column-width`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/column-width)。

**column-count** CSS属性，描述元素的列数。

```
.container{
   column-count:3;
}
```

**column-width** CSS属性建议一个最佳列宽。 列宽是在添加另一列之前列将成为最大宽度。

浏览器将**按照你指定的宽度尽可能多的创建列**；任何剩余的空间之后会被现有的列平分。 这意味着你可能无法期望得到你指定宽度，除非容器的宽度刚好可以被你指定的宽度除尽。

```
.container{
    column-width:200px;
}
```

Multicol 创建的列无法单独的设定样式。 不存在让单独某一列比其他列更大的方法，同样无法为某一特定的列设置独特的背景色、文本颜色。你有两个机会改变列的样式：

- 使用 [`column-gap`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/column-gap) 改变列间间隙。
- 用 [`column-rule`](https://developer.mozilla.org/zh-CN/docs/Web/CSS/column-rule) 在列间加入一条分割线

```
.container {
  column-count: 3;
  column-gap: 20px;
  column-rule: 4px dotted rgb(79, 185, 227);
}
```

多页媒体中的内容拆分、折断

```
  break-inside: avoid;
  page-break-inside: avoid;
```



### 响应式布局

#### 媒体查询

该**CSS媒体查询**为您提供了一种方式，**只有当浏览器和设备环境匹配您指定**，例如规则“视口宽度大于480个像素”**应用CSS**。**媒体查询是自适应网页设计的关键部分，因为它允许您根据视口的大小来创建不同的布局**，但是它们也可以用于检测有关您的网站所运行的环境的其他信息，例如用户正在使用触摸屏而不是鼠标。

最简单的媒体查询语法如下所示：

```
@media media-type和（media-feature-rule）{
  / * CSS规则转到此处* /
}
```

它包括：

- 一种媒体类型，它告诉浏览器此代码用于哪种媒体（例如，打印或屏幕）。

- 必须应用媒体表达式，这是必须通过的规则或测试，才能应用所包含的CSS。

- 如果测试通过且媒体类型正确，则将应用一组CSS规则。

  

### 媒体类型

您可以指定的媒体类型可能是：

- `all`
- `print`
- `screen`
- `speech`

```
@media print{
   body{
      font-size:12pt;
   }
}
```

### 媒体功能规则

指定类型后，您可以使用规则定位媒体功能。

#### 宽度和高度

为了创建响应式设计（并且广泛支持浏览器），我们最常检测到的功能是视口宽度，如果视口大于或小于某个宽度（或确切的宽度），我们可以使用CSS `min-width`，`max-width`以及`width`媒体功能。

```
@media screen and(width:600px){
   body{
     color:red;
   }
}
```

```
@media screen and (max-width:400px){
    body{
       color:blue;
    }
}
```

实际上，对于响应式设计，使用最小值或最大值要有用得多，因此您很少看到`width`或`height`单独使用。

#### 取向

一种受支持的媒体功能是`orientation`，它使我们能够测试纵向或横向模式。要在设备横向放置时更改正文文本颜色，请使用以下媒体查询。

```
@media(orientation:landscape){
    body{
       color:rebeccapurple;
    }
}
```

标准的桌面视图具有横向，并且在纵向模式下在手机或平板电脑上查看时，在该方向上正常工作的设计可能无法正常工作。方向测试可以帮助您创建针对纵向模式下的设备优化的布局。

#### 指点设备的使用

作为4级规范的一部分，`hover`引入了媒体功能。此功能意味着您可以测试用户是否具有将鼠标悬停在某个元素上的能力，这实际上意味着他们正在使用某种定点设备。触摸屏和键盘导航不会悬停。

```
@media(hover:hover){
   body{
      color:rebeccapurple;
   }
}
```

如果我们知道用户无法悬停，则默认情况下我们可以显示一些交互式功能。对于可以悬停的用户，当链接悬停时，我们可能选择使其可用。

`pointer`媒体功能也在第4级中。这需要三个可能的值`none`，`fine`和`coarse`。一个`fine`指针是像一个鼠标或触控板。它使用户可以精确地瞄准小区域。一个`coarse`指针是在触摸屏上手指。该值`none`表示用户没有定点设备。也许他们仅使用键盘或语音命令进行导航。

使用`pointer`可以帮助您设计更好的界面，以响应用户与屏幕的交互类型。例如，如果您知道用户正在通过触摸屏与设备进行交互，则可以创建较大的点击区域。

### 媒体查询中的“与”逻辑

要组合媒体功能，可以使用`and`与`and`上面用于组合媒体类型和功能的方法几乎相同的方法。例如，我们可能要测试`min-width`和`orientation`。仅当视口至少为400像素宽且设备处于横向模式时，主体文本才会为蓝色。

```
@media screen and(max-width:400px) and (orientation:landscape){
   body{
      color:blue;
   }
}
```

### 媒体查询中的“或”逻辑

如果您有一组查询，其中任何一个都可以匹配，则可以**用逗号分隔**这些查询。在下面的示例中，如果视口至少为400像素宽或设备处于横向，则文本将为蓝色。如果以上任何一项为真，则查询匹配。

```
@media screen and (min-width: 400px), screen and (orientation: landscape) {
    body {
        color: blue;
    }
}
```

### 媒体查询中的“非”逻辑

您可以使用`not`运算符来否定整个媒体查询。这颠倒了整个媒体查询的含义。因此，在下一个示例中，如果方向是纵向，则文本将仅是蓝色。

## 如何选择断点

在响应式设计的早期，许多设计师会尝试针对非常特定的屏幕尺寸。发布了流行的手机和平板电脑的屏幕尺寸列表，以便可以创建与这些视口完全匹配的设计。

现在，设备太多了，尺寸繁多，无法实现。这意味着，不是针对所有设计指定特定的大小，而是一种更好的方法是将设计更改为内容以某种方式开始破裂的大小。可能行的长度变得太长，或者装箱的侧边栏被压扁并且难以阅读。这就是您要使用媒体查询将设计更改为可用空间更好的地方。这种方法意味着所用设备的确切尺寸无关紧要，可以满足每个范围的要求。引入媒体查询的点称为**断点**。