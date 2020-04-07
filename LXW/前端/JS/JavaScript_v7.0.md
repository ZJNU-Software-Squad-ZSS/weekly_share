# JavaScript_v7.0

<img src="https://theskyhouse.oss-cn-hangzhou.aliyuncs.com/[2213]Lillie-60167508.png" style="zoom: 33%;" />

------

[TOC]

------

## jQuery

#### 和DOM区别

DOM对象：使用JavaScript的方法获取的对象就是DOM对象。

jQuery对象：使用jQuery的方法获取的对象就是jQuery对象。

jQuery对象其实就是DOM对象的包装集（包装了DOM对象的集合（伪数组） ）

区别

DOM对象与jQuery对象的方法不能混用。

联系

jQuery对象与DOM对象可以互相转换。

DOM  ——>  jQuery    //$( dom obj)

jQuery  ——>  DOM    //li是一个jQuery对象 li [ 0 ]  或  li.get( 0 )

**在jQuery对象中无法使用任何DOM对象的方法。**

------

#### 作用

- 消除浏览器差异：你不需要自己写冗长的代码来针对不同的浏览器来绑定事件，编写AJAX等代码；
- 简洁的操作DOM的方法：写`$('#test')`肯定比`document.getElementById('test')`来得简洁；
- 轻松实现动画、修改CSS等各种操作。（是一个js文件）

在页面<head>处引入文件即可使用<script src="//code.jquery.com/jquery-1.11.3.min.js"></script>

$是变量`jQuery`的别名，本质上是一个函数,也是对象

------

#### 选择器

可以帮助我们快速定位到多个DOM节点

```javascript
1.按id查找
// 查找<div id="abc">:
var div = $('#abc');//（以#开头）
返回jQuery对象，它类似于数组 如果id为abc的div不存在  那么返回的jQuery对象就是[] 这样就不用判断（div===undefined）
jQuery对象和DOM对象可以相互转换
var jQuery= $(DOM);//把DOM元素包装为jQuery对象

2.按tag查找
var ps=$('p');//直接写上标签名称

3.按class查找(在class名称前加一个.)
//我们可以查找同时包含red和green的节点：
var a = $('.red.green'); //没有空格！
// <div class="red green">...</div>
// <div class="blue green red">...</div>

4.按属性查找（用[])
var email = $('[name=email]'); // 找出<??? name="email">
var a = $('[items="A B"]'); // 找出<??? items="A B"> 如果包含空格或者特殊字符，要用到双引号

var icons = $('[name^=icon]'); 
// 找出所有name属性值以icon开头的DOM
// 例如: name="icon-1", name="icon-2"
var names = $('[name$=with]');
// 找出所有name属性值以with结尾的DOM
// 例如: name="startswith", name="endswith

5.组合起来
var tr = $('tr.red'); // 找出<tr class="red ...">...</tr>

6.多项选择器
$('p,div'); // 把<p>和<div>都选出来
$('p.red,p.green'); // 把<p class="red">和<p class="green">都选出来
<p class="red green">不会被上面的$('p.red,p.green')选择两次。
```

如果两个元素有层级关系，中间可以用空格隔开（层级选择器）

```javascript
$('ul.lang li.lang-javascript'); // [<li class="lang-javascript">JavaScript</li>]
$('div.testing li.lang-javascript'); // [<li class="lang-javascript">JavaScript</li>]
```

子选择器$('parent>child')规定层级关系必须是父子关系（比如div和li就不构成父子关系，但是li和ul可以）

此外 jQuery还有很多有用的选择器，例如：input、：file、div：visible

------

#### 查找过滤

*查找*

```javascript
//可以用find()进行查找
var ul = $('ul.lang'); // 获得<ul>
var dy = ul.find('.dy'); // 获得JavaScript, Python, Scheme
var swf = ul.find('#swift'); // 获得Swift
//都是ul层里的元素

//从当前节点开始向上查找，使用parent()方法：
var swf = $('#swift'); // 按id获得Swift
var ul=swf.parent();

//对于同一级的节点 可以用next()和prev()方法

```

*过滤*

```javascript
//filter()方法可以保留符合条件的节点
var langs = $('ul.lang li'); // 拿到JavaScript, Python, Swift, Scheme和Haskell
var a = langs.filter('.dy'); // 拿到class=dy的JavaScript, Python, Scheme

//函数内部的this绑定为DOM对象 不是jQuery对象

//map()方法把一个jQuery对象里的DOM节点转换成其他对象（如arr数组） map有点像遍历方法
var langs = $('ul.lang li'); // 拿到JavaScript, Python, Swift, Scheme和Haskell
var arr = langs.map(function () {
    return this.innerHTML;
}).get();  
//Array：['JavaScript', 'Python', 'Swift', 'Scheme', 'Haskell']

//jQuery里的slice(2,4)方法很不错  可以筛选下标为多少的元素

```

------

#### 操作DOM

- jQuery的text()和html()方法可以获取节点文本或html文本 设置的话就直接传入参数就好

- 一个jQuery对象可以包含0个或多个DOM对象，使用一个方法如果该节点不存在，也不会报错

- 修改css的话  $('#test-css li.dy>span').css('background-color', '#ffd351').css('color', 'red');   //属性name加value就可以

- css()方法作用的是style属性，具有**最高优先级**，如果修改class属性可以用addClass()或者removeClass()方法

- 现实和隐藏DOM元素，直接用jQuery提供的show()和hide()方法，不用关心它如何修改display属性

- attr()和removerAtter()用于操作DOM节点属性

- ```javascript
  div.attr('data'); // undefined, 属性不存在
  div.attr('name'); // 'Test'
  div.attr('name', 'Hello'); // div的name属性变为'Hello'
  ```

- **对于表单属性，jQuery对象提供val()方法获取设置value属性**

------

#### 添加DOM

```javascript
//向已有列表添加新内容（利用append）
var ul = $('#test-div>ul');
ul.append('<li><span>Haskell</span></li>');
//prepend()把DOM添加到最前面  
//如果已经存在该节点会先移除再添加
同级节点用after()或者before()方法
删除节点的话用jQuery的remove()方法就好

```

