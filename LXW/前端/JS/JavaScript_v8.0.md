# JavaScript_v8.0

![](https://theskyhouse.oss-cn-hangzhou.aliyuncs.com/[2220]無題-64988447.png)

------

[TOC]

------

#### 事件

1. ​	click: 鼠标单击时触发； dblclick：鼠标双击时触发，hover：鼠标移入和移出时触发
2. keydown：键盘按下时触发； keyup：键盘松开时触发； keypress：按一次键后触发。
3.  change：当`<input>`、`<select>`或`<textarea>`的内容改变时触发； submit：当`<form>`提交时触发； ready：当页面被载入并且DOM树完成初始化后触发。
4. **`$(function () {...})`的形式，牢记这是`document`对象的`ready`事件处理函数。**
5. 取消绑定的事情可以用off('click',function)实现-----可以使用`off('click')`一次性移除已绑定的`click`事件的所有处理函数。
6. 可以直接调用change()方法来手动触发一个事件（毕竟用js戴拿改动文本框内容不会触发change事件）

------

#### 动画

- show()和hide(300)传个时间参数就可以实现

- toggle()方法 根据当前状态 决定是隐藏还是显示（如果显示的话 就隐藏）

- `show()`和`hide()`是从左上角逐渐展开或收缩的，而`slideUp()`和`slideDown()`则是在垂直方向逐渐展开或收缩的。（当然还有我们的slideToggle()方法）
- fadeIn()和fadeOut()以及fadeToggle()是淡入淡出

```javascript
//自定义动画
var div = $('#test-animate');
//传入DOM元素最终的CSS状态以及时间 jQuery会调整的
div.animate({
    opacity: 0.25,
    width: '256px',
    height: '256px'
}, 3000, function () {
    console.log('动画已结束');
    // 恢复至初始状态:
    $(this).css('opacity', '1.0').css('width', '128px').css('height', '128px');
});
```

**通过delay（1000）可以实现动画暂停1秒**

很多不是block性质的DOM元素，对它们设置`height`根本就不起作用，所以动画也就没有效果。同时要注意jQuery没有实现对background-color的动画效果。

------

#### AJAX

jQuery全局对象绑定了ajax（url,settings对象）函数

settings包括async：是否异步，method：可以指定为POST 默认为GET，data：发送的数据，dataType：接收的数据格式

jQuery的jqXHR对象类似一个Promise对象，我们可以用链式写法来处理各种回调

------

#### 编写jQuery插件

```javascript
//绑定新方法通过$.fn对象来实现
$.fn.highlight1 = function () {
    // this已绑定为当前jQuery对象:
    this.css('backgroundColor', '#fffceb').css('color', '#d85030');
    return this;
    //这里的return this 是为了jQuery对象链式操作下去
    //不然这之后写代码实现功能还得拆成两行	 		            	$('span.hl').highlight1().slideDown();
}
```

```javascript
$.fn.highlight = function (options) {
    // 合并默认值和用户设定值:
    var opts = $.extend({}, $.fn.highlight.defaults, options);
    this.css('backgroundColor', opts.backgroundColor).css('color', opts.color);
    return this;
}
//extend函数可以把后面obj对象的属性合并到第一个target对象中（target对象为触发事件的节点）
// 设定默认值:
$.fn.highlight.defaults = {
    color: '#d85030',
    backgroundColor: '#fff8de'
}

然后用户使用的时候直接$.fn.highlight.defaults.color = '#fff';把默认值设置好就完事。

```

------

## js的错误处理

和java有些类似，try catch finally  这里就不多赘述（无论有没有错误 finally一定会执行）

可以使用throw语句主动抛出错误（最好是Error对象）

[^如果函数内部发生了错误，没有被捕获到  会一直沿着函数调用链向上抛出，直到js引擎捕获，终止代码。]: 

**try-catch可以写在函数内部的**

------

## underscore

它提供了一套完善的编程接口（把自身绑定到全局变量_上）

_.map（）传入的函数为`function (value, key)`，第一个参数接收value，第二个参数接收key：

```javascript
//`groupBy()`把集合的元素按照key归类，key由传入的函数返回：
var scores = [20, 81, 75, 40, 91, 59, 77, 66, 72, 88, 99];
var groups = _.groupBy(scores, function (x) {
    if (x < 60) {
        return 'C';
    } else if (x < 80) {
        return 'B';
    } else {
        return 'A';
    }
});
// 结果:
// {
//   A: [81, 91, 88, 99],
//   B: [75, 77, 66, 72],
//   C: [20, 40, 59]
// }
```

shuffle()随机打乱一个集合

sample()随机选取一个多个元素

------

##### Array

```javascript
var arr = [2, 4, 6, 8];
_.first(arr); // 2
_.last(arr); // 8
_.flatten([1, [2], [3, [[4], [5]]]]); // [1, 2, 3, 4, 5]  接收Array  把嵌套的都取出来变成一个一维
//zip()把两个数组按索引嵌套
var names = ['Adam', 'Lisa', 'Bart'];
var scores = [85, 92, 59];
_.zip(names, scores);
//[['Adam', 85], ['Lisa', 92], ['Bart', 59]] 这里如果用Object的话就是直接把名字和分数弄成一个对象 
unzip反过来   把一个数组拆开
range(10)快速生成一个从0开始小于10的序列

```

------

##### Functions

- 当用一个变量fn指向一个对象（比如s）的方法时，直接调用fn()不行，丢失了this对象的引用，可以用bind()把s对象绑定在fn()的this指针上，修复这个问题。

- 偏函数的话 用var pow2N=_.partial(Math.pow,2);要用的时候再说吧  
- 用memoize()可以自动缓存函数计算的结果，下次遇到相同参数的直接返回结果
- once()保证某个函数只执行一次
- delay()延迟执行，和setTimeout()效果一样

------

##### Objects

- keys()返回object自身所有的key ，allKeys()返回自身加上原型链继承下来的keys

- values()返回value 没什么好说的  **但是没有allValues()**

- invert()把每个键值的 key和value 两级反转一下（不知道这有啥用。。加密吗=。=）

- extend()把多个object的key-value合并到第一个object并返回//后面有相同的key  value就覆盖掉前面的value

- clone()复制对象

- isEqual()对两个object，Array进行深度比较

- 用chain()函数可以把对象包装成能进行链式调用

  var r = _.chain([1, 4, 9, 16, 25])
           .map(Math.sqrt)
           .filter(x => x % 2 === 1)
           .value();//每一步返回的都是对象用value()获取最终结果

------

