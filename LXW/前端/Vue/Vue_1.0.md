# Vue_1.0

![](https://theskyhouse.oss-cn-hangzhou.aliyuncs.com/[2222]第二地区-59695820.png)

------

[TOC]

------

### 反思

说来也惭愧，已经有一段时间没有自己学习过前端的知识了（随便看看的bootstrap不算），说是因为疫情的缘故，更多的肯定是自己的惰性所致，愿现在重拾动力的自己能多点付出，勿让自己止步不前。

------

### 简介

Vue是什么？按以往知识，我们把json对象的数据显示到一个元素上去，可以通过JS或者JQuery（DOM）

如果通过Vue，仅需知道数据以及数据绑定的id。

```html
<!--js的方式-->
<div id="test">
</div>
<script>
//准备数据
var gareen = {"name":"盖伦","hp":616};
//获取 html dom
var dom = document.getElementById("test");
//显示数据
dom.innerHTML= gareen.name;
</script>

<!--Vue的方式-->
<script src="vue.min.js"></script>
<div id="test">
  {{gareen.name}}
  {{gareen.hp}}
</div>
<script>
var gareen = {"name":"盖伦","hp":616};
//通过vue.js 把数据和对应的视图关联
new Vue({
      el: '#test',
      data: {
        message: gareen
      }
    })
</script>
```

------

### 监听事件

#### v-on（缩写@）

```html
<div id="test">
<div>一共点击了{{num}}次数</div>
<!--这里v-on:可以直接缩写成@   @click="count" 即可-->	
<button v-on:click="count">点击</button>
</div>
<script>
new Vue({
      el: '#test',
      data:{
		  num:0
	  },
	  methods:{
		  count:function(){
			  this.num++;//这里记得加this，函数名自己取不一定是count
		  }
	  }    
    })
</script>
```

------

#### 冒泡

```html
<div id="father" v-on:click="doc">
father
	<div id="me" v-on:click="doc">
	me
		<div id="son" v-on:click="doc">
		son
		</div>
	</div>
</div>
<script>
    new Vue({
        el: "#father",//这里写根节点 如果写me 那么father的doc就无效了
        data: {
            id: ''
        },
        methods: {
            doc: function () {
                this.id= event.currentTarget.id;//绑定事件的元素
                alert(this.id)
            }
        }
    })
</script>
```

###### 阻止冒泡

```html
<div id="father" v-on:click="doc">
father
	<div id="me" v-on:click.stop="doc">//在@click后面加上.stop就可以阻止冒泡到father
	me
		<div id="son" v-on:click="doc">
		son
		</div>
	</div>
</div>
//下面的js部分一样的
```

###### 优先触发

```html
<div id="father" v-on:click="doc">//在@click后面加上.capture就可以优先触发father
father
	<div id="me" v-on:click="doc">
	me
		<div id="son" v-on:click="doc">
		son
		</div>
	</div>
</div>
//当然如果me和father都设置了优先触发 然后点击son  顺序是father->me->son（看来还是当爸爸的优先级比较高
```

###### 只有自己能触发

```html
<div id="father" v-on:click="doc">
father
	<div id="me" v-on:click.self="doc">
	me
		<div id="son" v-on:click="doc">
		son
		</div>
	</div>
</div>
这个时候点击son  冒泡过程会忽略掉me

```

###### 只监听一次（父元素依旧可以监听

```
.once 和上面同理  表示只能监听一次事件  但是它的父元素还是能监听到的
```

###### 阻止提交刷新

```
.prevent 阻止超链接和form会导致页面刷新的操作
```

------

### 条件语句

#### v-if

```html
<!-- v-if指令用于条件性地渲染一块内容。这块内容只会在指令的表达式返回truthy值的时候被渲染。-->
<div id="div1">
  <button @click="toggle">切换隐藏显示</button>
  <div v-if="flag"> 默认这一条是看得见的</div>
</div>
<script>
new Vue({
      el:'#div1',
      data: {
          flag:true
      },
      methods:{
          toggle: function(){
              this.flag=!this.flag;
          }
      }
    })
</script>
```

#### v-else

```html
<div id="div1">
  <button @click="choujiang">中奖率%10</button>
  <div v-if="show"> 中了500万！</div>
  <div v-else>谢谢惠顾！</div>    
</div>
<script>
new Vue({
      el: '#div1',
      data: {
          show:false
      },
      methods:{
          choujiang: function(){
             this.show=Math.random()<0.1;
          }
      }
    })
</script>
```

#### v-else-if

```html
<div id="div1">
  <button @click="toutai"> 看看下辈子投胎是做什么的 </button>
  <div v-if="number>98"> 神仙</div> 
  <div v-else-if="number>50"> 普通公务员</div> 
  <div v-else> 流浪汉</div> 
</div>
<script>  
new Vue({
      el: '#div1',
      data: {
          number:0
      },
      methods:{
    	  toutai: function(){
        	 this.number=Math.random()*100
          }
      }
    })
//这个差不多也没啥好说的
</script>
```

------

