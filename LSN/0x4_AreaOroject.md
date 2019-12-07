# 0x4_AreaProject
### 写网页时的坑
这次写网页和上星期的加在一起又可以出一期坑合集了
##### 函数后面带和不带括号
因为没有系统的学习js知识，所以对js函数的了解很不透彻
一直对函数赋值给变量不理解
现在用的多了，认为函数是一种特殊的对象
直接写函数名不加括号是直接使用这个函数对象，并不会调用该函数
##### jQuery的show和hide动画
虽然不知道其动态特效是如何形成的，但可以清楚的是
show动画最终会使对象的display设置为block,
hide动画最终会使对象的display设置为none
##### jQuery的live方法、on方法和js事件
首先，最新的jQuery中已经没有了live方法，统一使用on方法，
而使用js代码后期生成的元素是不能使用js的onclick来绑定事件的
**需要在生成元素的时候进行事件绑定**
##### promise和asycn
写代码时遇到需要把异步回调函数的返回值作为外部函数的返回值使用
然而用了很多方法都不行，其中也包括了promise和asycn
promise把一些需要异步做的事包装成对象，在事情结束或者出错时能够自动做其他的事
而asycn则是一种语法糖，在函数前加上asycn，就能够使用await来等待异步结束后继续做下面的事
这两者是把本身是异步的事转换成同步
但对这些异步操作之外的代码（promise是promise对象之外，asycn是asycn函数之外）来说，这两者依旧是异步的，不会等promise或者asycn执行完毕后再进行下一步
##### php和html混编时的编码
php和html混杂时，注意php的编码格式
在php文件开头，添加php头命令设置为utf8
html的head里也要添加meta设置为utf8
除了代码上添加外，写代码时的软件应该要设置编码格式为utf8
比如eclipse默认格式会使浏览器第一次解析php时将中文解析成乱码
这一点找了很久才解决的
### jQuery
#### jQuery事件
##### 文档就绪事件
$(document).ready(function(){
})
$(function(){
})
第二个是简写
文档就绪事件是指等html的dom加载完毕后执行其中的代码，不需要等待具体资源的加载
**一切jQuery应该写在文档就绪事件中，防止出错**
##### 点击事件
$("p").click(function(){
})
元素被点击时的事件
##### 双击事件
$("p").dbclick(function(){
})
##### 鼠标移入事件
$("p").mouseenter(function(){
})
##### 鼠标移出事件
$("p").mouseleave(function(){
})
##### 鼠标按下事件
$("p").mousedown((function(){
})
##### 鼠标弹起事件
$("p").mouseup(function(){
})
##### 鼠标悬浮事件
$("p").hover(function(){
})
##### 获得焦点事件
//就是选中某些元素（比如input)时触发
$("p").mouseup(function(){
})
##### 失去焦点事件
$("p").blur(function(){
})

##### jQuery动画
**隐藏和显示动画**
$().hide(speed,select,callback)
$().show(speed,select,callback)
$().toggle(speed,select,callback)
三个参数都是可选的
第一个设置动画时长，默认为0
第二个设置展示方式，jQuery自带"linear" 和 "swing"，前者时动画均匀变化，后者是默认设置，动画慢->快->慢，可以使用插件有更多选择
第三个为回调函数，默认为null

toggle函数使元素在两者间切换
**淡入淡出动画**
$().fadeIn(speed,callback);
$().fadeOut(speed,callback)
$().fadeToggle(speed,callback)
两个参数都是可选的
第一个设置动画时长，默认为0
第二个设置回调函数，默认为null
fadeToggle函数使元素在两者间切换

$().fadeTo(speed,opacity,callback);
fadeTo函数使元素渐变为指定透明度
需要注意其第一个第二个参数必选
第一个参数为动画时长
第二个参数为所需要变成的透明度
**滑动动画**
$().slideDown(speed,callback);
$().slideUp(speed,callback);
$().slideToggle(speed,callback);
两个参数都是可选的，和之前的类似
Down向下滑，Up向上滑，Toggle在两者间切换
需要注意并不是位置移动，而是disply或者height发生了改变