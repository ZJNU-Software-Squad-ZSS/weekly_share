# Vue_4.0

![](https://theskyhouse.oss-cn-hangzhou.aliyuncs.com/[2405]大人って-65006441.jpg)

------

[TOC]

------

#### 组件

##### 简介

例如淘宝一页下来各个商品，每个商品都可以看成是一个模板，每个产品之间传递了不同的参数（价格，图片，文字描述），这样的模板就是组件。

------

##### 局部组件

```html
<!--通过标签调用模板  多个模板多次调用即可-->
<product></product>
<product></product>
<product></product>
<script>
new Vue({
  el: '#div1',
  components:{
      'product':{
          template:'<div class="product" >模板</div>'
      }
  }
})
</script>
```

##### 全局组件

和过滤器类似，有的组件需要在不同页面中出现

```html
Vue.component('product', {
	  template: '<div class="product" >模板</div>'
	})
```

------

##### 参数

传递参数给组件

```html
<product name="模板1"></product>
<product name="模板2"></product>
Vue.component('product', {
	  props:['name'],
	  template: '<div class="product" >{{name}}</div>'
	})
```

###### 动态参数

组件内的参数和组件外的值关联（比如input输入的数据传递到组件内）

```html
组件外的值：<input v-model="outName" ><br>  //双向绑定
<product v-bind:name="outName"></product>
<script>
Vue.component('product', {
      props:['name'],
      template: '<div class="product" >{{name}}</div>'
    })
 
new Vue({
  el: '#div1',
  data:{
      outName:'产品名称'
  }
})
</script>
```

------

##### 自定义事件

和在Vue对象上增加methods类似

```html
<script>
//在模板上绑定点击的methods
Vue.component('product', {
      props:['name','sale'],
      template: '<div class="product" v-on:click="increaseSale">{{name}} 销量: {{sale}} </div>',
      methods:{
          increaseSale:function(){
              this.sale++
          }
      }
    })
</script>
```

##### 遍历json数组

```html
<product v-for="item in products" v-bind:product="item"></product>
<script>
//准备产品数组
products:[
            {"name":"模板1","sale":"18"},
            {"name":"模板2","sale":"35"},
            {"name":"模板3","sale":"29"}
          ]
    
Vue.component('product', {
	  props:['product'],//参数是产品对象
	  template: '<div class="product" v-on:click="increaseSale">{{product.name}} 销量: {{product.sale}} </div>',
	  methods:{
		  increaseSale:function(){
			  this.product.sale++
		  }
	  }
	})   
</script>
```

##### 注意 

**template 部分因为比较复杂，就不好写在一个 单引号 ' ' 里维护起来，所以就直接写在html里，然后通过html dom 获取出来，这样编写起来略微容易一点。**

```HTML
<div id="tempalate">
   ******
</div>
<script>
var tempalateDiv=document.getElementById("tempalate").innerHTML;
var templateObject = {
    props: ['product'],
    template: tempalateDiv,
      methods: {
            *******
          }
}
Vue.component('product', templateObject);
</script>
```

------

#### 路由

**vue.js 里的路由相当于就是局部刷新。**

（需要额外的库：vue-router.min.js）

##### 具体步骤

1.定义路由组件，就是定义template 

2.定义路由，为路由赋值这些路由组件 

3.实例路由，就是用到VueRouter包 

4.挂载路由，就是用到Vue包

```html
<div class="menu">
    <!--	router-link相当于就是 href-->
    <router-link to="/user">用户管理</router-link>
    <router-link to="/product">产品管理</router-link>
    <router-link to="/order">订单管理</router-link>
</div>

<div style="float: right">
    <!--点击上面的/user,那么/user对应的内容就会显示在router-view这里-->
    <router-view></router-view>   
</div>

<script>
    var User={template:'<div>用户管理页面的内容</div>'}
    var Product={template: '<div>产品管理页面的内容</div>'}
    var Review={template:'<div>订单管理页面的内容</div>'}
    var routes=[
        {path:'/user',component:User},
        {path:'/product',component: Product},
        {path:'/review',component:Review}
    ]
 	//创建VueRouter实例
     var router = new VueRouter({
        routes:routes
    });
    //绑定路由
    new Vue({
        el:"#app",
        router
    })
</script>
```

------

