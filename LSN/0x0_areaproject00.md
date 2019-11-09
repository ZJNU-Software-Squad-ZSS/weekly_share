# 0x0_areaproject
最近做一个项目 需要用到的知识太过杂乱，为了防止以后再把这些坑再爬一遍，在这里进行记录（坑还没爬完）
## 项目总览
该项目希望能够实时监测景区的人数并生成热力图反映在微信小程序上
![](vimages/0x001.png =697x)

### 爬坑——opencv
光是实时监测这一点就给传感器带来很大限制，讨论了好几次最后决定还是使用景区的监控摄像获取的图像来分析人数
**然而密集人群人数检测是一个大坑**
一开始以为在人脸识别已经发展较为完备的情况下，人头检测应该也有简便的解决方案，然而并没有
于是了解到可以使用opencv的训练器来实现对某种物体的检测，原理是通过大量的正负样本进行某种特征（HAAR等）的提取，和人工智能似乎有点相似
###### 坑-opencv的新老版本
训练器名字为opencv_traincascade
一开始我下载了opencv的最新版本，然而里面并没有exe文件的训练器，只有用C++写的训练器源码。
于是花了半天时间尝试去编译成exe文件，但里面的代码组织的并不友好，许多无法被找到的结构大量出现.
如果不花大量时间把训练器源码和其定义的头文件读下来是无法编译的。
然而opencv的老版本不但有源码还有已经生成好的exe文件，所以前面花的时间完全可以被省略
###### 坑-训练器语句检测大小写
因为网上有很多用训练器训练的教程，所以拿到exe文件后进展的比较快
唯一一点又卡了我几个小时的点是
`Traincascade Error: Bad argument (Can not get new positive sample. The most possible reason is insufficient count of samples in given vec-file`
网上大多都是说负样本太少，正样本太多，导致我修改了好几次正负样本的比例
然而最终的原因是
`opencv_traincascade.exe -data xml -vec pos.vec -bg neg.txt -numPos 30 -numNeg 50 -numStages 20 -featureType LBP -w 24 -h 24`
这句话是区分大小写的，如果numStage,numPos等没有按规定写，是无法修改参数的，会导致报错（网上有些大写有些小写产生误导）
修改后训练成功，贴一下目录结构

![](vimages/0x002.png =697x)
neg存放负文件目录，里面有neg.txt存放负文件一览（这里只是为了方便把neg.txt拿到外面
pos存放正文件目录，里面有pos.txt存放正文件一览
tempuseless训练器运行后生成的文件夹
xml存放产生的训练结果
pos.vec，中间文件，由opencv_createsamples.exe生成

```
cmd在该目录下
dir /b >pos.txt
dir /b >neg.txt
opencv_createsamples.exe -info pos\pos.dat -vec pos.vec -bg neg.txt -num 30 -w 24 -h 24
opencv_traincascade.exe -data xml -vec pos.vec -bg neg\neg.txt -numPos 30 -numNeg 50 -numStages 20 -featureType LBP -w 24 -h 24
```
图片大小都应该为24X24，配合网上的教程应该没有其他的坑了
###### 不算坑的坑-大量的数据集
那么问题来了，要训练就必须有大量的数据集
正样本3k张，负样本5k左右才有效果，但自己一个个去截是在太累
想偷懒看看有没有图像数据库啥的
ImageNet、CIFAR、MNIST等一个个访问过去
没卵用，人家是给深度学习用的，不是给你opencv训练的
所以还是得自己截（最终搁置了）
### 复习——JDBC连接数据库
上次用JDBC还是社团实验室考试时候了
这次我们更进一步，用JDBC连接云数据库，而不是自己的（其实没多大区别
因为JAVA还算熟悉，所以碰到的坑就比较少
```java
//mysql drive加载
String driver = "com.mysql.jdbc.Driver";
//访问数据库（外网连接）
String url = "jdbc:mysql://cdb-ha5tv078.bj.tencentcdb.com:10225/AreaProject?useSSL=false";
//加载驱动程序
Class.forName(driver);
```
唯一碰到的奇怪的坑就是url的填写，中间“cdb-ha5tv078.bj.tencentcdb.com:10225”是云数据库的外网端口
注意云端mysql数据库版本应该要对应导入Jar包的版本
### 爬坑——微信小程序（第一部分
###### 坑-调用wx函数返回的res
在小程序里本来想创建一个（云）函数专门来获取位置信息
想法是将调用wx.getLocation成功时返回的res再返回给需要的地方（然而并不行
花了很长时间去解决、思考哪里出问题，最后被告知是无法直接实现的
需要用Promise什么的，但没学过js的我只好将代码写的不好看了...
###### 坑-小程序连接mysql
小程序按道理是没法直接操作mysql的，但有一位大大给出用云函数连接数据库的方法
自己亲自尝试后并不能复现
虽然不质疑大大的代码，但还是老老实实按传统开发连接mysql好
另外小程序自带的云数据库并不适合这个项目，当初纠结了好久