# Vue_2.0

![](https://theskyhouse.oss-cn-hangzhou.aliyuncs.com/[2286]幽世の番人-59072859.png)

------

[TOC]

------

### 循环

#### v-for

```html
<div id="div1">
	<table align="center" >
		<tr class="firstLine">
			<td>name</td>
			<td>hp</td>
		</tr>
		<!--这里的迭代不一定是hero 随意一个能表示意思的就可以-->
		<tr v-for="hero in heros">
			<td>{{hero.name}}</td>
			<td>{{hero.hp}}</td>
		</tr>
	</table>

</div>  
<script>
//搞个数组
var data = [
   		  {name:"盖伦",hp:341},
		  {name:"提莫",hp:225},
    ];
new Vue({
      el: '#div1',
      data:	{
    	  heros:data//这里不能加;的
      }
    })  
</script>


<!--这里迭代的过程还可以加个下标inddex（不一定是index，i也可以-->
<tr v-for="hero,index in heros">
			<td>{{index}}</td>
			<td>{{hero.name}}</td>
			<td>{{hero.hp}}</td>
</tr>
```

#### 纯数字遍历

```html
<div id="div1">
    <div v-for="i in 10">
     {{i}}
    </div>
</div>
   
<script>
    new Vue({
          el: '#div1'
        })
</script>
```

------

### 属性绑定

```html
<!-- 完整语法 --><v-bind:href >  
<!-- 缩写 -->< :href >

<!-- v-blind: 用于绑定属性 可以使后面属性中的js表达式合法 -->
<!-- 通俗的说 就是如果不绑定这个属性 鼠标放到这个按钮上提示的就是mytitle这个字符串 而不是js中的mytitle的值hhh -->
<div id="div1">
	<input type="button" value="按钮" v-bind:title="mytitle">
</div>
    
<script>
new Vue({
      el: '#div1',
      data:{
          mytitle:'hhh'
      }
    })
</script>
```

**button标签显示的内容可以使图片等非文字元素，但type=button元素不行，因为type=button本身就是标签中元素的一个值，不可以像button标签一样嵌套类似img的标签**（奇怪的知识增加了↑

------

### 双向绑定

之前绑定属性，把Vue对象数据显示在视图上，那我们想把视图上的数据放到Vue对象上就可以用到这个（比如input）

```html
<div id="div1">
	hero name: <input v-model="name">
	<button @click="Click">提交数据</button>
</div>

<script>
new Vue({
      el: '#div1',
      data:{
         name:"hhh"
      },
	  methods:{
          Click:function(){
              alert(this.name);
          }
      }
    })
</script>
```

```html
<!--灵活运用-->
<div id="div1"> 
    <table align="center">      
        <tr>
            <td>
                <input v-model="input" placeholder="输入数据">
            </td>
            <td>
                <p>{{ input }}</p>   
            </td>
        </tr>
		
        <tr>
            <td>
              <select v-model="selected">
                <option disabled value="">请选择</option>
				<option>AD</option>
                <option>ADC</option>
              </select>
            </td>
            <td>
                <p>{{ selected }}</p>   
            </td>
        </tr>
    </table>
  
</div>   
<script>
new Vue({
      el: '#div1',
      data: {
          input:'',
          selected:''    
      }
    })
</script>
```

###### .lazy

**上述的这种v-model绑定是同步绑定  一旦数据变化就绑定，我们可以加一手.lazy 监听这个改变  当失去焦点才绑定数据**

```html
<input v-model.lazy="input" placeholder="输入数据">
<p>{{ input }}</p>
这样的话 只有离开输入框 绑定的地方数据才会改变
```

###### .number

**有时候，拿到了数据需要进行数学运算， 为了保证运算结果，必须先把类型转换为number类型，而v-model默认是string类型，所以就可以通过.number方式确保绑定到的是数字类型了。**

```html
<input v-model="input1" type="number" placeholder="输入数据">
<input v-model.number="input"  type="number" placeholder="输入数据">
//首先type=“number”保证输入的一定是数字
再来看区别：
第一个绑定的数据是string类型的  第二个是number类型的
```

###### .trim

**去掉绑定数据前后的空白**

------

