# 0x3_Areaproject
这星期也继续在摸这个项目的鱼
主要记录下AMD规范和jQuery
### AMD规范架构
##### 导入require.js
在网页的head里写入
`<script data-main="js/configJs" src="js/require.js"></script>`
这样就导入了require.js
同时将configJS作为一个全局JS使用（本质是个js文件），常用来存放全局变量、函数已经设置等
###### 在configJS里进行设置
```js
require.config({//因为是在data-main里的，所以加载paths时以configJs.js的位置为准
	baseUrl : "js/",//手动设置下路径
    paths : {//设置需要引用的模块,后缀名.js不用写
        "jquery" : "jquery.min",//前面命名的模块名称，后面是指向路径
		"amap":"Amap",
		"heatmap":"HeatmapControll",
		"popper":"popper",
		"boost":"bootstrap.min",
		"mapmessage":"mapmessage"
    },
	shim: {//非AMD规范的js文件
    	'amap': {
        	exports: 'amap'
        },
		'boost':{
			exports:['jquery']
		},
	},//一些非AMD文件只通过shim也无法解决
	map: {//加载popper和boostrap的解决方案 https://www.cnblogs.com/manongxiaobing/p/10238085.html
		  //大佬太强了
    	'*': {
      		'popper.js': 'popper'
    	}
  	}
})
```
##### define定义模块
```js
define("alpha", ["require", "exports", "beta"], function (require, exports, beta) {
    //"alpha"为命名该模块名称，可以省略，省略后为匿名模块
    //推荐使用匿名模块，这时它的模块名就是路径名
    //["require", "exports", "beta"]里是该模块需要用到的其他模块
    //function (require, exports, beta)里是用到的其他模块在该模块的对象，即调用其他模块均需要通过该对象实现
    var returnfun={
		close:closefun,
		load:loadfun
	}
	return returnfun;
	//returnfun是返回对外接口的，即别的模块使用该模块时，只能使用returnfun里面的对象
	//returnfun里的close何load为在外部使用的对象名，closefun和loadfun为在该模块定义的对象
	//这些对象可以为函数或者变量
	//对于其他定义在该模块的变量、函数，它们总是'私有'的
});
```
#####  require引用模块
```js
require(['foo', 'bar'], function ( foo, bar ) {//除了没有模块名外，参数和define相同
        foo.doSomething();
        //没有return语句
        //第一个function()为引用模块成功时的回调函数
        //除此之外还可以有失败时的回调函数
        
});
```
**在define里可以使用require实现动态加载**
##### 小结
可以看到require的内容非常简单
因为它只是一个工具类JS
但刚开始入手时还是会遇到不少困惑

### jQuery简化编程
##### jQuery引入
和其他js文件一样正常引入就行
因为支持AMD规范，所以在AMD规范中也只设置paths就行
引入后jQuery的一切操作通过$进行
$是jQuery的对象，用来进行jQuery的操作

##### jQuery选择对象
```html
$(this) 选择当前元素
$("*") 选择所有元素
$("p") 选择所有 <p> 元素
$("p.test").hide() 选择所有 class="test" 的 <p> 元素
$("#test").hide() 选择所有 id="test" 的元素
$("p:first") 选择第一个<p> 元素
$("ul li:first") 选择第一个 <ul> 元素的第一个 <li> 元素 
$("ul li:first-child") 选择每个 <ul> 元素的第一个 <li> 元素
$("[href]") 选择带有 href 属性的元素
$("a[target='blank']") 选择所有 target 属性值等于 "blank" 的 <a> 元素（=前面加!就是获取不等于"blank"的元素
$(":button") 选择所有 type="button" 的元素
$("tr:even") 选择偶数位置的 <tr> 元素
$("tr:odd") 选择奇数位置的 <tr> 元素  

var doc=Document.creat("div") 通过DOM新建对象
$(doc) 使DOM对象编程jQuery对象
```

##### jQuery遍历对象
上次说到DOM对象是树形结构
因此根据这个特点可以进行DOM对象之间的遍历
###### 遍历祖先
```html
$("span").parent(); 返回所有<span>的直接父元素
$("span").parents("ul"); 返回所有<span>的所有是<ul>元素的祖先，如果去掉"ul"则返回所有祖先
$("span").parentsUntil("div");返回所有介于<span>和<div>的祖先
```
###### 遍历孩子
```html
$("div").children("p.1");返回所有<div>的直接儿子，且该儿子为类名为1的<p>元素，如果去掉则返回所有<div>的所有直接儿子
$("div").find("span"); 返回所有<div>的所有<span>孩子
```
###### 遍历兄弟
```html
 $("h2").siblings("p");返回所有<h2>的<p>兄弟，去掉后返回所有兄弟
 $("h2").next();返回所有<h2>的下一个弟弟
 $("h2").nextAll();返回所有<h2>的弟弟
 $("h2").nextUntil("h6");返回所有<h2>的弟弟，<h6>的哥哥
 prev()就是找其哥哥，和next相似
```
###### 过滤元素
以上返回的大多是jQuery对象集合
可以进行元素的过滤
```html
$("div p").first(); 返回第一个<div>的第一个<p>元素
$("div p").last();  返回最后一个<div>的最后一个<p>元素
$("p").eq(1); 返回第二个<p>元素， 1是索引号，从0开始
$("p").filter(".url"); 返回所有类名为url的<p>元素
$("p").not(".url"); 返回所有类名不带有url的<p>元素
```
### 下星期讲jQuery的具体使用
（因为这星期被AMD规范搞了很久）