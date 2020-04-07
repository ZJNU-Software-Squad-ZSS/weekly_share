# JavaScript_v6.0

<img src="https://theskyhouse.oss-cn-hangzhou.aliyuncs.com/76613636.png" style="zoom:50%;" />

## AJAX

------

[TOC]

------

#### 介绍

AJAX 是一种用于创建快速动态网页的技术。

通过在后台与服务器进行少量数据交换，AJAX 可以使网页实现异步更新。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。

------

#### XHR（XMLHttpRequest）

```javascript
var xmlhttp;
if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
  xmlhttp=new XMLHttpRequest();
  }
else
  {// code for IE6, IE5
  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
```

**`XMLHttpRequest`对象的`open()`方法有3个参数，第一个参数指定是`GET`还是`POST`，第二个参数指定URL地址，第三个参数指定是否使用异步，默认是`true`，不能写成false 不然浏览器会停止响应。**（规定请求类型、URL、是否异步处理）

send（String）//string参数仅用于POST请求

以下情况使用POST （一般用GET就可以）

- 无法使用缓存文件（更新服务器上的文件或数据库）
- 向服务器发送大量数据（POST 没有数据量限制）
- 发送包含未知字符的用户输入时，POST 比 GET 更稳定也更可靠

------

#### 服务器响应

responseText 属性返回字符串形式的响应，因此您可以这样使用：

```javascript
document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
```

如果服务器的响应是XML，那么就使用responseXML属性，解析响应（暂时还不是很了解XML）

------

#### onreadystatechange

发送一个请求后，客户端无法确定什么时候会完成这个请求，所以需要用事件机制来捕获请求的状态，XMLHttpRequest对象提供了onreadyStateChange事件实现这一功能。这类似于回调函数的做法。

```javascript
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
    }
  }
```

| readyState | 4表示请求已完成                  |
| ---------- | -------------------------------- |
| status     | 200 表示响应就绪 404：未找到页面 |

------

## Promise

### Promise().then().then....catch() 多任务串行执行.

情景化记忆:在一个任务链中,比如我要向上级部门一层层的往上提交申请,if(某种条件)承诺帮你resolve解决问题,else承诺reject你的请求. 他给出的resolve问题的办法只是个空头Promise,then到总经理那实现具体承诺,如果总经理还是给一个空头承诺(返回Promise实例),还得then到董事长那里.... 任一一步做出的是reject的承诺,还有什么好说的,被拒绝了,后面的就不会再往上走了呀. 准备catch 拒绝通知吧

### Promise.all([p1,p2,...]) 多任务并行执行

都要成功才进入then,返回结果数组.

### Promise.race([p1,p2,...]) 多任务赛跑.

then()和catch(),谁先调用算谁的,其它任务中断.

**JS引擎是单线程的，但是浏览器是多线程的，其执行的方法如`setTimeOut`是由浏览器来调度的**

**Promise 无论成功或者失败都会进入then，在then中接受错误的对象后再进入的catch，所以换位子会出错。**

------

## Canvas

Canvas是HTML5新增的组件，它就像一块幕布，可以用JavaScript在上面绘制各种图表、动画等。（不需要借助FLASH插件）

```javascript
var ctx = canvas.getContext('2d');//拿到一个2D对象
```

可以用它的方法来绘制图形，文本等各种复杂操作

（可以创建多个重叠的Canvas绘制不同的层，尽量使用整数坐标而不是浮点数）

可能以后用到 就会了吧。。现在还不是很懂  