# Vue_3.0

![](https://theskyhouse.oss-cn-hangzhou.aliyuncs.com/[2329]中国語／日本語  [ PF]四季之岛-64672286.jpg)

------

[TOC]

------

#### 计算属性

###### computed

进行运算时，我们的常规做法是

```html
￥: <input type="number" v-model.number = "rmb"/>
<td align="center">
 	$: {{ rmb/exchange }}
</td>
<script>
new Vue({
      el: '#div1',
      data: {
          exchange:6.4,
          rmb:0
      }
 })
</script>
```

当运算过程复杂以后，我们可以用method方法来封装调用

```html
￥: <input type="number" v-model.number = "rmb"  />
<td align="center">
	$: {{ getDollar() }}
</td>
<script>
new Vue({
      el: '#div1',
      data: {
          exchange:6.4,
          rmb:0
      },
      methods:{
          getDollar:function() {
              return this.rmb / this.exchange;
          }
      }
    })
</script>
```

但是我们还可以把运算过程放到computed里面去（调用的时候不用加() 它不是一个方法 而是把计算好的东西赋给dollar）

```html
￥: <input type="number" v-model.number = "rmb"  />
<td align="center">
    $: {{ dollar }}
</td>
<script>
new Vue({
      el: '#div1',
      data: {
          exchange:6.4,
          rmb:0
      },
      computed:{
          dollar:function() {
              return this.rmb / this.exchange;
          }
      }
    })
</script>
```

###### 区别

**computed 是有缓存的，只要rmb没有变化，dollar 会直接返回以前计算出来的值，而不会再次计算。 这样如果是复杂计算，就会节约不少时间。**
**而methods每次都会重新调用**

------

#### 监听属性

###### watch

监听某个值，当其发生变化执行相应的操作

（和computed的区别是：watch更适用于监听某一个值的变化并作出操作，比如请求后台接口，而computed适用于计算已有的值并返回结果---还有种说法就是watch适合处理一个数据影响多个数据  computed适用于 一个数据受多个数据影响）

```html
<td align="center">
    ￥: <input type="number" v-model.number = "rmb"  />
</td>
<td align="center">
    $: <input type="number" v-model.number = "dollar"   />
</td>
<script>
new Vue({
      el: '#div1',
      data: {
          exchange:6.4,
          rmb:0,
          dollar:0
      },
      watch:{
          rmb:function(val) {
              this.rmb = val;//val是输入的值
              this.dollar = this.rmb / this.exchange;
          },
          dollar:function(val) {
              this.dollar = val;
              this.rmb = this.dollar * this.exchange;
          },
      }
})
</script>
```

------

#### 过滤器

```html
<script> 
new Vue({
      el: '#div1',
      data: {
          data:''
      },
      filters:{
          //首尾字母大写
          capitalize:function(value) {
                if (!value) return '' //如果为空，则返回空字符串
                value = value.toString()
                return value.charAt(0).toUpperCase() + value.substring(1,value.length-1)+value.charAt(value.length-1).toUpperCase()
          }
      }
    })
</script>
```

这里过滤器是定义在Vue对象里的。 但是有时候，很多不同的页面都会用到相同的过滤器，如果每个Vue对象里都重复开发相同的过滤器，开发维护都不方便。
我们还可以通过全局过滤器的方式，只定义一次过滤器，然后就可以在不同的Vue对象里使用了。

```html
<script>
Vue.filter('capitalize', function (value) {
	if (!value) return ''
	value = value.toString()
	return value.charAt(0).toUpperCase() + value.slice(1)
})
</script>
```

------

