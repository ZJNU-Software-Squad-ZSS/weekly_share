# 1x0_Boostrap
久等了（指每周分享
然而上星期已经把主要的难点攻克下来了。因此这星期花了大量时间来写技术文档，所以并没有什么爬坑干货
但在这星期的前几天为了给网页排个版而稍稍看了下Boostrap的内容，在这里做个皮毛上的记录

## Boostrap简介
Bootstrap4 目前是 Bootstrap 的最新版本，是一套用于 HTML、CSS 和 JS 开发的开源工具集。
利用提供的 Sass 变量和大量 mixin、响应式栅格系统、可扩展的预制组件、基于 jQuery 的强大的插件系统，能够快速为你的想法开发出原型或者构建整个 app 。
###### 要点提取
1、Boostrap开源
2、最新版本为Boostrap4（boostrap3和4语法差距较大
3、用于html、css、js，使用时需要引入boostrap.css和boostrap.js
4、基于jQuery 使用时也要引入jquery.js(先引入这个
5、模板示例
```html
<!--Bootstrap 要求使用 HTML5 文件类型，所以需要添加 HTML5 doctype 声明。-->
<!DOCTYPE html>
<html>
   <head>
      <title>Bootstrap 模板</title>
      <!--一下设置是为了对移动设备友好
        width=device-width 表示宽度是设备屏幕的宽度。
        initial-scale=1 表示初始的缩放比例。
        shrink-to-fit=no 自动适应手机屏幕的宽度。-->
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <!-- 引入 Bootstrap -->
      <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
 
   </head>
   <body>
      <h1>Hello, world!</h1>
 
      <!-- jQuery (Bootstrap 的 JavaScript 插件需要引入 jQuery) -->
      <script src="https://code.jquery.com/jquery.js"></script>
      <!-- 包括所有已编译的插件 -->
      <script src="js/bootstrap.min.js"></script>
   </body>
</html>
```
## 开始构造Boostrap
Boostrap需要用一个container类的div来包容所有网页内容
之后所有的内容都写在该div中
```html
<div class="container">
</div>//这个container将对网页两边留一部分白
<div class="container-fluid">
</div>将占满所有宽度
```
#### Boostrap网格系统
###### Boostrap提供一套网格系统来分配同一排的不同列所占宽度的大小
将一行划分成12个单位宽度，不同的列可以占不同的单位宽度
示例：
```html
<div class="row">
      <div class="col-3">
      </div>
      <div class="col-9">
   	  </div>
  </div>
```
像这样将产生两个列，在任何时候他们的宽度比都是1:2
.col-sm-   将设置屏幕宽度大于等于576px时的单位宽度
.col-md-   将设置屏幕宽度大于等于768px时的单位宽度
.col-lg-   将设置屏幕宽度大于等于992px时的单位宽度
.col-xl-   将设置屏幕宽度大于等于1200px时的单位宽度
当屏幕宽度小于列所定义的最小生效宽度时，将会自动占用一行的空间
###### 列偏移
通过设置`offset-*-*`类可以使某一个列向右偏移
如`offset-sm-3` 该div列在屏幕宽度大于等于576px时向右梛3列。
###### 小结
通过使用以上类，可以快速开发出一个能针对不同设备而打开不同排版的网页。

## Boostrap文字排版
###### display
`<h1 class="display-1">Display 2</h1>`
类display-1~4可以用在html的标题标签中，产生更大更粗的样式
###### small
`<h2>h2 标题 <small>副标题</small></h2>`
类small可以用在html的标题标签中，产生相比较小较细的样式
###### mark
`<p>使用 mark 元素来 <mark>高亮</mark> 文本。</p>`
类mark里的文字将添加黄色背景，产生高亮效果
###### abbr
`<p>The <abbr title="World Health Organization">WHO</abbr> was founded in 1948.</p>`
类abbr里的文字将添加下划线，当鼠标移至上面时，将显示title里的字符串
###### blockquote
```html
<blockquote class="blockquote">
    <p>For 50 years, WWF has been protecting the future of nature.</p>
    <footer class="blockquote-footer">From WWF's website</footer>
  </blockquote>
```
在For 50 yeats.......之后，将添加一个From WWF's website的引用样式
###### dl
```html
<dl>
    <dt>Coffee</dt>
    <dd>- black hot drink</dd>
    <dt>Milk</dt>
    <dd>- white cold drink</dd>
  </dl>  
```
样式如下：
**coffee**
- black hot drink
**Milk**
- white cold drink
###### code
`<code></code>`行内代码
###### kbd
`<kbd>ctrl + p</kbd>`行内 按键提示
###### pre
```html
<pre>
</pre>
```
多行代码
###### 更多文字排版见教程