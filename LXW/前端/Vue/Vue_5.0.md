# Vue_5.0

![](https://theskyhouse.oss-cn-hangzhou.aliyuncs.com/[2452]举头望明月-63363216.jpg)

------

[TOC]

------

#### 自定义指令

###### v-xart

1. 使用Vue.directive 来自定义
2. 第一个参数就是 指令名称 xart
3. el 表示当前的html dom对象

```html
<div v-xart> 好好学习，天天向上 </div>
<script>
Vue.directive('xart', function (el) {
    el.innerHTML = el.innerHTML + '自己加点自定义的内容';
    el.style.color = 'pink';
})
new Vue({
    el: '#div1'
}) 
</script>
```

**当然还可以传参(传个json对象啥的）**

```html
<div v-xart="{color:'red',text:'best learning video'}"> 好好学习，天天向上 </div>
<script>
Vue.directive('xart', function (el,canshu) {
    el.innerHTML = el.innerHTML + '( ' + canshu.value.text + ' )'
    el.style.color = canshu.value.color
})
</script>
```

###### 钩子函数

使用vue框架，需要在合适的时机做合适的事情（和生命周期挂钩）

vue生命周期经历的阶段：**开始创建、初始化数据、编译模板、挂载Dom、渲染→更新→渲染、销毁等一系列过程**

|         1.实例化vue对象          |           2.初始化事件和生命周期            |           3.beforeCreate函数（此时没有真实的DOM）            |
| :------------------------------: | :-----------------------------------------: | :----------------------------------------------------------: |
| 4.挂载数据（属性和computed运算） | 5.created函数（Vue对象有数据，但是没有DOM） |                6.检查（el属性和template属性）                |
|        7.beforeMount函数         |   8.模板编译（vue对象的数据替换模板内容）   | 9.monuted函数，数据挂载完毕 Vue对象加载成功（这个时候发送异步请求） |
|   10.beforeUpdate（组件更新前    |            11.update（组件更新后            |              12.销毁（销毁前还有组件激活函数）               |

目前还不是很能理解什么是钩子函数，大概是在对应的生命周期绑定函数吧，之后可以回来再看看

------

#### fetch+axios

Vue一般不用原生的Ajax而是使用比较流行的ajax框架---fetch，axios

vue-cli，vue crud 要用node.js方面以及webpack等的知识

具体的运用在后面的学习了这部分前端知识再进行补充

------

