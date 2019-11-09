# 0x1_areaproject
又到了实验室的保留内容、传统艺能的环节了
这次提前记录了在这一周里做项目爬的新坑，一周前还撞了N多墙，现在终于实现了一个简单的热力图。这次的坑也照例分几个板块
### PHP
因为并没有写很多关于PHP的代码，所以大多时候只是因为语法和json不熟悉而遇到的错误，而且解决起来也很快（可见PHP真的香
###### 获得从mysql的数据后，需要用函数处理下，不然会报错
`Object of class mysqli_result could not be converted to string`
很简单，只需要mysqli_fetch_array处理下数组就ok
###### PHP里Mysql使用的字符串书写
虽然我没有遇到，但别人遇到了，比较重要，记录下
PHP里字符串里变量写法 
和PHP的sql语句的字符串语句里面的变量写法有所区别
```php
//向数据库中插入数据
//$sql = "INSERT INTO list (openid, code) VALUES ('".$openid."', '" .$code ."')";
/*
('".$openid."', '" .$code ."')"中，格式应如VALUES ('XXX', 'XXX')"，XXX
外面是要有引号的,所以，改成参数后，拼接语句要格外注意，笔者在调试时因为这个小问题困扰了很久
*/
```
当然详细的应该直接查语法，这里仅记录下可能会遇到mysql写不对的问题
###### 数组以及其元素添加
```php
$a1[] = 0;//不断写可以不断往数组里添加数据
$a2=array('Longitude'=>$row['XH'],'Latitude'=>$row['XM'])//关联数组，并且初始化时就有了两个元素
$a3[]=array('Longitude'=>$row['XH'],'Latitude'=>$row['XM'])//向一个二维数组添加一个元素
```
###### PHP数据的返回
php数组需要用json_encode函数转换成json格式再发送给小程序或者网页
而那边也要相应的调用函数来转换
### 小程序上的热力图
###### heatmap.js
在网页上我通过使用heatmap.js很快的实现了一个热力图的绘制
我认为小程序应该和网页大致相同，然而却被打脸了
![](_v_images/20191109095625742_20797.png =739x)
（废止的小程序，花了大量时间来写结果大失败）
**首先是heatmap.js在小程序内部的失效**
无论是在wxml里直接添加heatmap.js全部代码或是用script连接，都无法显示热力图。一开始我以为是小程序对js不是完全支持的，后来去网上提问后dalao告诉我是小程序里没有dom
![](_v_images/20191109100853965_21439.png =755x)
当然这个是后话了，在此之前，我也尝试过遇到过其他问题
**微信中打开网页，在网页上加载热力图的方法**
奇怪的是如果网页通过script连接heatmap.js微信内不能加载
而网页直接添加js代码却能加载
应该是内置浏览器的锅
**微信小程序个人版不支持web-view**
在小程序内加载外部网页需要用web-view控件
然而这个是企业版才有的
所以刚刚想到的办法也被pass
**通过其他方法在微信小程序内部加载热力图**
为了能够绕过web-view这一关，我想了很多方法
包括用其他方法生成热力图（Echarts、matlab等）
将html转化成图片格式
在后端直接生成图片等等
但这些实现起来麻烦，并且也不符合预期的要求效果，都被pass
可能要在小程序上实现的方法真的是要去读heatmap.js源码了，但时间并不允许
### 网页以及js
最终还是决定放弃用小程序，投靠html了
小程序这样看起来像是刚起步
使用高德地图或者百度地图的API能够快速生成地图+热力图（地图在小程序上的API还不支持热力图
不得不说，除了麻烦一点，html的各种呈现方式是真的成熟
当然坑也不少，毕竟对html也不熟悉
**同步加载和异步加载**
一开始就碰到了这种有点难懂的东西，导致我百度地图API调用失败(后来用了高德地图）
因为网站很小所以直接同步加载了
等到需要时再进行异步优化
（回调函数什么的是真的烦
**高德地图和百度地图经纬度不对应**
这个真是前所未闻，原来经纬度的坐标都有好几种
主流的是高德地图、谷歌中国地图、腾讯地图的火星坐标系（国家测绘局
而百度地图非要搞什么加密，自己在此之上改了下，然而可以用算法转换，这么屑的加密有什么必要用吗（全恼
**jquery的按钮点击事件前最好加下ready**
有一次按钮一直不响应，后来试了试包了个ready就通了，很迷
顺便记一下jquery的ajax请求
```js
(document).ready(function(){
	$('#showPosition').click(function(){
		$.ajax({
			url:"http://49.233.171.101/AreaProject/connect.php",//url务必写全，尤其是前面的http://
			data:{
				lon:lon,
				lat:lat
			},
			type:"GET",//请求方式
			success:function(data){
				//格式转换
				data = JSON.parse(data);
				PositionData=data;
				var str=[];
				str.push('您现在所在景区为：'+data[1]);
				document.getElementById('position').innerHTML = str;
			},
			error: function (data){
				document.getElementById('position').innerHTML = "服务器不在状态QAQ";
        	}
		});
	});
});
```
另外，如果用html的请求而不是ajax的话无法实时加载（网上这样说的，实际没试过
**跨域大坑**
用ajax请求很迷的一点是，我在服务器上打开html时，明明请求的是自己站点下的php，但是却提醒我未跨名
wdnmd，我跨我自己
问了老师，老师不知道详细情况，也不清楚原因
还是老老实实去跨域试试
1、jsonp跨域名
第一个找到的就是这个方法
```js
//在ajax请求里添加
dataType: 'jsonp',  
crossDomain: true,
//并且将数据按jsonp解析

//php文件返回也必须为jsonp
$jsonCallback . "(" . $jsonData . ")";//$jsonData为所需要的data
```
然而结果ajax得到数据后却一直进入fail而不是success，网上查说是回调函数缺失的原因
然而回调函数却写的不仅不尽相同，还没写全，wdnmd

[
https://segmentfault.com/a/1190000012469713](https://segmentfault.com/a/1190000012469713)
在这网址里，详细述说了跨域问题，在jsonp方法第一句就说了这种方法已经过时了，wdnmd
于是用下面一种
在php文件开头添加了
```php
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept');
//如果要对允许跨域的域名或其他东西添加限制，网上百度以上两句话怎么改
```
OK解决，数据的传输方式还是json的，比那个jsonp不知道高到哪里去了
虽然里面说还要改网站配置文件，然而没改也过了
**网站在服务器端的调试**
接下来开始实现网站功能并且debug了
在本地文件一切正常后，却发现服务端的网页一直没法正常运行
打开开发者工具发现js文件都还是debug前的样子
因为浏览器会自动缓存这些js，所以每次debug前都要先清缓存
**js对ajax请求的不等待**
对于ajax中的success(还有fail啥的)，js是不等待的
因此在success外面是无法实时获得ajax请求成功时获得的数据（即使数据存在全局变量里，因为代码执行速度比请求速度快，所以执行代码时是得不到数据的）
把代码放在success里面就行，因为success里的代码依旧是要顺序执行的
调用请求的函数已经结束了，但请求成功时的函数还没有结束（这大概就是异步？）
