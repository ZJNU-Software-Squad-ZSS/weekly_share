# Node.js

![](https://theskyhouse.oss-cn-hangzhou.aliyuncs.com/[2501]イザナミの庭-65854354.jpg)

------

[TOC]

------

#### 简介

能在服务端运行的js（以前服务端开发以java居多，前端人员等着服务端准备好交互浪费时间）---主要是方便前端人员

也可以把node.js简单的看成JavaScript写的tomcat

```java
/*---Tomcat---
网上有段话很形象
--------------*/
我家有一台机器，可以把石头变成金子。你快递给我一箱子石头，让我把它们变成一箱子金子再快递给你。
这个机器就是web项目。石头是请求，金子是响应，我家就是服务器。如果你把一箱石头邮到我家，机器可不会自己接受快递然后把石头进行加工成金子再快递给你，这个时候帅气的我就登场了，我接受快递，把石头给机器变成金子后再打包快递给你。这里的我就是tomcat。没有我，你的一箱子石头邮过来也没用。我家机器不会搭理你。更不会给你金子。
```

------

#### hello node.js

```js
//新建server.js 文件  用cmd找到该目录---》node server.js
var http = require('http');//引入http模板
function service(request, response) {//类似servlet里的doGet,doPost方法
    //设置返回代码200以及返回格式
    response.writeHead(200, {'Content-Type': 'text/plain'});
    //设置返回内容
    response.end('Hello Node.js');
}
//基于service函数创建server服务器
var server = http.createServer(service);
//server服务器监听于8088端口
server.listen(8088);

```

访问地址http://127.0.0.1:8088/即可看到hello node.js

------

#### 模块系统

简单来说，别人写的js就是一个模块，我们在可以引用别人写的js文件

```js
/*xw.js*/
//service函数和之前一样
function service(request, response) {
    response.writeHead(200, {'Content-Type': 'text/plain'});
    response.end('Hello Node.js');
}
//加一个hello函数  在控制台打印
function Hello(){
    console.log('hello from xw.js');
}
/*
这两个函数是不能直接外部调用的！
我们得通过exports 指定如何调用他们
1.允许外部通过 hi() 这个函数名称调用 sayHello() 
2.允许外部通过 service() 函数名称调用service（）
*/
exports.hi = sayHello;
exports.service = service;

/*node.js*/
//引入http和xw模块
var http = require('http');
var xw = require('./xw');
xw.hi();
//基于xw.service()创建server服务器
var server = http.createServer(xw.service);
server.listen(8088);

/效果和前面一致，但是我们可以看到控制台多出一句hello from xw.js
```

------

#### 路由

requestHandlers.js

```js
function listCategory() { 
    return "a lot of categorys";
}    
function listProduct() { 
    return "a lot of products";
} 
exports.listCategory = listCategory; 
exports.listProduct = listProduct; 
```

 router.js

```js
function route(handle, pathname) { 
  if (typeof handle[pathname] === 'function') { 
    return handle[pathname](); 
  } else {
    return pathname + ' is not defined';
  } 
} 
exports.route = route;
```

 server.js

```js
var http = require("http"); 
var url = require("url"); 
   
function start(route, handle) { 
  function onRequest(request, response) { 
    var pathname = url.parse(request.url).pathname; 
    var html = route(handle, pathname); 
    response.writeHead(200, {"Content-Type": "text/plain"}); 
    response.write(html); 
    response.end(); 
  } 
  http.createServer(onRequest).listen(8088); 
} 
exports.start = start;
```

index.js（入口模块）

```javascript
var server = require("./server"); 
var router = require("./router"); 
var requestHandlers = require("./requestHandlers"); 
 
var handle = {} 
handle["/listCategory"] = requestHandlers.listCategory; 
handle["/listProduct"] = requestHandlers.listProduct; 
   
server.start(router.route, handle);
```

###### 总结

1. index.js调用sever.start函数，传递handle数组以及router.js作为参数
2. 通过8088端口启动服务，onRequest处理业务
3. router.js中通过pathname为下标获得调用的真正的业务函数
4. 虽然看起来麻烦，但是如果要开发新的功能，比如listUser 只需要增添listUser函数，在index.js进行映射进handle数组就好

------

#### npm安装模块

基于前面的模块，npm就会下载别人的模块和发布自己模块用的工具

###### cnpm

npm是从国外服务器下载别人的模块。cnpm 复制国外的库到国内的服务器上（用的时候cnpm install就行）

```
npm install -g cnpm --registry=https://registry.npm.taobao.org（网站是npm官网 -g是全局安装）
```

关于数据的库操作

```
npm install mysql --save（安装模块）
```

准备函数openConnection以及closeConnection和增删改查函数

具体以后用到再说

------

