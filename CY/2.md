# BFC
**什么是BFC**  
BFC 全称为 块格式化上下文 (Block Formatting Context) 。
单从全称来看我们似乎并不能得到什么特别有用的信息，所以我去百度了一下  
让我们看下官方如何解释：
>一个块格式化上下文（block formatting context） 是Web页面的可视化CSS渲染出的一部分。它是块级盒布局出现的区域，也是浮动层元素进行交互的区域。
一个块格式化上下文由以下之一创建：

> * 根元素或其它包含它的元素
> * 浮动元素 (元素的 float 不是 none)
> * 绝对定位元素 (元素具有 position 为 absolute 或 fixed)
> * 内联块 (元素具有 display: inline-block)
> * 表格单元格 (元素具有 display: table-cell，HTML表格单元格默认属性)
> * 表格标题 (元素具有 display: table-caption, HTML表格标题默认属性)
> * 具有overflow 且值不是 visible 的块元素，
> * display: flow-root
> * column-span: all 应当总是会创建一个新的格式化上下文，即便具有 column-span: all 的元素并不被包裹在一个多列容器中。
> * 一个块格式化上下文包括创建它的元素内部所有内容，除了被包含于创建新的块级格式化上下文的后代元素内的元素。  

>块格式化上下文对于定位 (参见 float) 与清除浮动 (参见 clear) 很重要。定位和清除浮动的样式规则只适用于处于同一块格式化上下文内的元素。浮动不会影响其它块格式化上下文中元素的布局，并且清除浮动只能清除同一块格式化上下文中在它前面的元素的浮动。  

所以现在来看我之前的总结并不完美，除了我说的方法还有其他方法能够制造出BFC格式。  
对于这个文档其实看不是很懂，所以我大致做个解读，BFC的功能大致分为两个：  
1.使BFC内部浮动元素不会乱跑  
2.和浮动元素产生边界  
还是上代码说吧  
```html
<div class="out">
 <div class="in"></div>
</div>
```
```css
.out{
    border:10px solid red;
    min-height:20px;
}
.in{
    background:grey;
    height:100px;
}
```
 效果是这样的：  

![效果](https://upload-images.jianshu.io/upload_images/6874766-6d653a57e10b289d.png?imageMogr2/auto-orient/strip|imageView2/2/w/634/format/webp)  

在正常的文档流中，块级元素是按照从下自上，内联元素从左到右顺序排列的。但是如果我的给里面的元素一个float或者说是绝对定位，它就会脱离普通的文档流。
效果就变成这样子了：
![效果](https://upload-images.jianshu.io/upload_images/6874766-b1004d68354da7a6.png?imageMogr2/auto-orient/strip|imageView2/2/w/640/format/webp)  
此时我们还想让外层元素包裹住内层元素元素应该如何去做？
就是让外层元素产生一个BFC
![效果](https://upload-images.jianshu.io/upload_images/6874766-8e20e1906fb635b5.png?imageMogr2/auto-orient/strip|imageView2/2/w/644/format/webp) 
这就是BFC第一个作用了，虽然跟第一篇的内容有点相似，但是请让我水一水。

那么和浮动元素产生边界
是怎么样的
先上一个代码
```html
<div class="left"></div>
<div class="right"></div>
```
```css
div{
    border:3px solid red;
    height:100px;
}
.left{
  min-width:200px;
  margin-right:20px;
  float:left;
}
.right{
  border-color:blue;
  display:flow-root;
}
```
![效果](https://upload-images.jianshu.io/upload_images/6874766-217d6deeffa5d5d3.png?imageMogr2/auto-orient/strip|imageView2/2/w/589/format/webp) 
如果你想要左右元素有margin,除了BFC以外就只能margin=width_of_right+margin_initial(就是只一开始你想要他们两之间的距离)
所以到这里，如果平时在写前端时候你的布局崩了，8成是你的float乱用记得构造BFC。

