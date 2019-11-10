# CSS浏览器兼容性问题及解决方案小记

本文的解决方向主要为四个大的方向，细节问题暂不记录,欢迎补充纠正。

### 为什么会有浏览器兼容问题

------

 还不是因为浏览器厂商太多了！ 

这是世界市场权威调查机构NetMarketShare公布的2018年10月各浏览器市场占有率 ，chrome的占有率高达66.43%，这对兼容性问题而言是个好消息。

![图表](https://image-static.segmentfault.com/178/226/1782269537-5c6a3e8d7d18d_articlex)

 而根据百度流量研究院提供的2018年11月至2019年1月的数据可以看出，IE系仍然占有很大比重，任重而道远啊~ 

![图表](https://image-static.segmentfault.com/331/538/3315384136-5c6a3e8d9aea4_articlex)

兼容性带来了默认样式、支持属性等方面的各种差异，使得网页在不同浏览器上的显示效果大打折扣，所以，下面介绍四种解决方向。

### 1.浏览器CSS样式初始化

------

 不同的浏览器默认的样式不尽相同，所以开发时的第一件事可能就是把它们统一。 举两个差异的栗子：

1.页边距

　　　　IE默认为10px，通过body的`margin`属性设置
　　　　FF默认为8px，通过body的`padding`属性设置

2.段间距

　　　　IE默认为19px，通过p的`margin-top`属性设置
　　　　FF默认为1.12em，通过p的`margin-bottom`属性设

所以，平时css开始时经常会有：

```css
*{
    margin: 0;
    padding: 0;
    ...
}
```

但是平时经验有限，所以，如果你也像我一样不知道该初始化什么的话， Normalize.css 这个库可以作为一个样板， github star数量接近4万 。

 通过CSS样式初始化，能解决不少常规的兼容性问题，接下来再看看浏览器的私有属性。

### 2. 浏览器私有属性

------

 通常，有W3C组织成员提出一个新属性，比如说圆角border-radius，大家都觉得好，但W3C制定标准，要走很复杂的程序，审查等。而浏览器商市场推广时间紧，如果一个属性已经够成熟了，就会在浏览器中加入支持。 

 浏览器厂商通常都是在属性名称前添加厂商的私有前缀，来测试这些尚未成为标准的特性。因此，可以借助私有前缀，来解决浏览器对CSS3的兼容性问题。 

 不同的内核都有各自的私有前缀，三大主流内核的私有前缀见表 。

| 内核    | 前缀     |           主要浏览器           |
| ------- | -------- | :----------------------------: |
| Trident | -ms-     |       Internet Explorer        |
| Gecko   | -moz-    |            Firefox             |
| Webkit  | -webkit- | Chrome、Opera、Safari、Android |

例：（border-radius圆桌角属性）

```
round {
    -ms-border-radius: 10px;      /* Miscrosoft (Internet Explorer) */
    -moz-border-radius: 10px;    /* Mozilla(如Firefox) */
    -webkit-border-radius: 10px;  /* Webkit(如Chrome 、Opera、Safari) */
    border-radius: 10px;          /* W3C */
}
```

使用私有前缀时，如果私有特性和最后的标准特性不一致，就会出现兼容问题。因此，需要把浏览器的私有属性写在前面，把标准属性写在最后面，来确保在特性被完全支持时，能得到正确的效果。

列出每一种私有前缀是最理想的做法，但实际开发中，很少有人这样做。最好的作法是，在编写规则之前，检查哪些浏览器支持该特性，仅列出不支持该特性的私有前缀。

### 3. CSS hack

------

有时我们需要针对不同的浏览器或不同版本写特定的CSS样式，这种针对不同的浏览器/不同版本写相应的CSS code的过程，叫做CSS hack 。

CSS hack的写法大致归纳为3种：条件hack、属性级hack、选择符级hack。 

#### 条件hack

语法：

```
<!--[if <keywords>? IE <version>?]>
    代码块，可以是html，css，js
<![endif]-->
```

取值及举例：

```
只在IE下生效

<!--[if IE]>

这段文字只在IE浏览器显示

<![endif]-->

只在IE6下生效

<!--[if IE 6]>

这段文字只在IE6浏览器显示

<![endif]-->

只在IE6以上版本生效

<!--[if gte IE 6]>

这段文字只在IE6以上(包括)版本IE浏览器显示

<![endif]-->

只在IE8上不生效

<!--[if ! IE 8]>

这段文字在非IE8浏览器显示

<![endif]-->

非IE浏览器生效

<!--[if !IE]>

这段文字只在非IE浏览器显示

<![endif]-->
```

#### 属性hack 

属性前缀法是在CSS样式属性名前加上一些只有特定浏览器才能识别的hack前缀，以达到预期的页面展现效果。 

语法：          

```html
selector{<hack>?property:value<hack>?;}
```

取值：

在标准模式中

“-″减号是IE6专有的hack

- “-″减号是IE6专有的hack
- “\9″ IE6/IE7/IE8/IE9/IE10都生效
- “\0″ IE8/IE9/IE10都生效，是IE8/9/10的hack
- “\9\0″ 只对IE9/IE10生效，是IE9/10的hack

举例：

```html
.test {
  color: #090\9; /* For IE8+ */
  *color: #f00;  /* For IE7 and earlier */
  _color: #ff0;  /* For IE6 and earlier */
}
```

#### 选择符级hack

选择符级hack是针对一些页面表现不一致或者需要特殊对待的浏览器，在CSS选择器前加上一些只有某些特定浏览器才能识别的前缀进行hack。 

语法：          

```html
<hack> selector{ sRules }
```

取值：

常见的选择符级hack有

```html
*html *前缀只对IE6生效
*+html *+前缀只对IE7生效
@media screen\9{...}只对IE6/7生效
@media \0screen {body { background: red; }}只对IE8有效
@media \0screen\,screen\9{body { background: blue; }}只对IE6/7/8有效
@media screen\0 {body { background: green; }} 只对IE8/9/10有效
@media screen and (min-width:0\0) {body { background: gray; }} 只对IE9/10有效
@media screen and (-ms-high-contrast: active), (-ms-high-contrast: none) {body { background: orange; }} 只对IE10有效
```

举例：

```
* html .test { color: #090; }       /* For IE6 and earlier */
* + html .test { color: #ff0; }     /* For IE7 */
```

 不过花大力气解决这些兼容性问题，  并不能给我们技术上带来什么大的提升，无非是给各个浏览器厂商填坑罢了，随着时间的流逝，这些技术的价值也会越来越小，怎么花最小的力气解决css兼容性问题，让我们把更多的时间留给美好的生活，才是关键，好在有一些自动化插件可以帮我们从繁重的兼容性处理中解脱处理。 

### 4. 自动化插件

------

Autoprefixer是一款自动管理浏览器前缀的插件，它可以解析CSS文件并且添加浏览器前缀到CSS内容里，使用Can I Use（caniuse网站）的数据来决定哪些前缀是需要的。

把Autoprefixe添加到资源构建工具（例如Grunt）后，可以完全忘记有关CSS前缀的东西，只需按照最新的W3C规范来正常书写CSS即可。如果项目需要支持旧版浏览器，可修改browsers参数设置  。

​                                                                                                                                                                              2019/11/9

## Reference

1.https://www.cnblogs.com/madman-dong/p/5866286.html  浏览器默认标签样式总结及css初始化程序

2.https://blog.csdn.net/ixygj197875/article/details/79371508  浏览器私有前缀

3.https://baike.baidu.com/item/css%20hack  百度百科

4.https://segmentfault.com/a/1190000018188102  CSS浏览器兼容性的4个解决方案

