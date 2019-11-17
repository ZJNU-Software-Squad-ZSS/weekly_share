# 微信小程序回顾（归纳）

​	本文只是一些微信小程序的注意点和坑作为归纳



## rpx与px区别

rpx会随着屏幕大小改变

 px是固定的

如果要用px的话就需要数值除余2 （iPhone 6 上面的）



## 流程

产生事件->捕捉事件->回调函数->处理事件



## 代码复用

template实现前端代码的复用



## 设计思路

先静后动，先样式再数据



## 经典的水平居中的方式

position: absolute;

left: 50%;

margin-left: -51rpx;



## event.currentTarget.dataset.postId 元素

currentTarget:当前鼠标点的组件

dataset：用户自定义的属性

postId:属性



## jsBoolean小坑

'false' 为true

只有'{{false}}'和'' 才为false



## page页面生命周期顺序

onload

onshow

onready



## 我最常用的设计布局flex

就三行自己看真的好用

