### v-for:循环

```
遍历data中的数据。这里的数据可以是数组[]，也可以是json对象
v-for：有个特点，当循环的数据发生变化时，会自动再次调用v-for指令，实现数据的刷新操作。
{name:"A",age:'B'}

var app=new Vue({
    el:'#app',
    data:{
      foodList:[
          {
              name:"葱",
              price:5
          },
          {
              name:"姜",
              price:5
          },
          {
              name:"蒜",
              price:4.5
          }
      ]
    }
})


<div id="app">
  <ul>
  //Vue1.0版本：这里也可以用v-for="(index,food) in foodList"来显示出下标index和相对应的值。
  //Vue2.0版本：v-for="(food,index) in foodList，即索引是后面一个参数
      <li v-for="food in foodList">{{food.name}} ￥{{food.price}}</li>
  </ul>
</div>
```

### v-bind:为属性绑定值

```
    <style type="text/css">
        .active{
            background: #a10;
        }
    </style>
</head>
<body>
<div id="app">
    <a :class="{active:isActive}"  :href="url">点我</a>
    
    <a v-bind="{href:'url固定部分'+{data变量}}">
    :表示加上了v-bind属性，相当于v-bind:class=""
    这里的{{active:isActive}}表示当vue.js中的isActive为真的时候，会给a标签加上active属性，要是不为真就不加该属性。
</div>
```

### v-on:事件

```
var app = new Vue({
    el: '#app',
    data: {
        url: "http://www.baidu.com",
        isActive:true
    },
    methods:{
        onClick:function(){
            console.log("显示哈哈哈");
            return false;
        },//点击操作
        onEnter:function(){
            console.log("on Enter");
            return false;
        },//鼠标移入
        onLeave:function(){
            console.log("on Leave");
            return false;
        }//鼠标移出
         onSubmit:function(){
            console.log('Submit');
        }//表单提交
    }

})

<div id="app">
    <a v-on:click="onClick" v-on="{mouseenter:onEnter,mouseleave:onLeave}">点我</a>
    v-on表示绑定事件：前一个用冒号表示一个一个事件的绑定，这里的意思是当点击的时候(click事件)，触发onClick事件，这个事件写在methods:{}里面。后面一次性绑定多个事件，用等号相连(因为等号后面会自动填上"")，然后在冒号里面以json数据格式 键为事件，值为绑定的操作
    
     <form v-on:submit.prevent="onSubmit" v-on:keyup.enter="onEnter"> 
     这里表示当表达那提交的时候，绑定为自定义的onSubmit事件，里面的.prevent是用来阻止表单提交数据，类似于return false,使他失去原有的功能
     
     v-on:keyup.enter="onEnter"，表示当在输入框按下Enter键的时候（.Enter）
        <input type="text">
        <button type="submit">提交</button>
    </form>
</div>

v-bind:可以用冒号代替
v-on:可以用@来代替 v-on:click="onClick"  => @click="onClick"
```

### v-model:

```
<input v-model.trim="name"> //表示去掉前后空格 <pre>标签显示完整数据内容，有多少空格都会显示出来，原生的html只保留一个空格

v-model.lazy="name" //当光标离开输入框才会显示改变，不再实时改变
v-model.number="price"//把输入的值转换成数字类型
```

#### v-model在表单中的使用，把js的数据与前台表单数据结合，同步

```
var app = new Vue({
    el: '#app',
    data: {
        sex: null,
        fruit:[],
        article:"ajjajajajaj",
        from:1, //单选，不用数组
        dest:[]//多选用数组
    },

})

<div id="app">
    <label >
        男
        <input  v-model="sex" value="男" type="radio">
    </label>
    <label >
        女
        <input v-model="sex" value="女" type="radio" >
    </label>
    <pre>{{sex}}</pre>
    <!--===================-->
    <label >
        苹果
        <input  v-model="fruit" value="苹果" type="checkbox">
    </label>
    <label >
        香蕉
        <input v-model="fruit" value="香蕉" type="checkbox" >
    </label>
    <pre>{{fruit}}</pre>
    <!--=======================-->
    <textarea v-model="article"></textarea>
    <pre>{{article}}</pre>
    <!--==========================-->
    <div>你来自哪里？</div>//单选
    <select v-model="from">
        <option value="1">北京</option>
        <option value="2">上海</option>
        <option value="3">广州</option>
        <option value="4">深圳</option>
    </select>
    <pre>{{from}}</pre>
    <!--++++++++++++++++++++++++-->
    <div>你来自哪里？</div>//多选
    <select v-model="dest" multiple>
        <option value="1">北京</option>
        <option value="2">上海</option>
        <option value="3">广州</option>
        <option value="4">深圳</option>
    </select>
    <pre>{{dest}}</pre>
</div>
```

![1537621933282](C:\Users\郑江\AppData\Local\Temp\1537621933282.png)

#### v-model计算学生总分平均分，可动态改变

```
var app = new Vue({
    el: '#app',
    data: {
        // sex: null,
        // fruit:[],
        // article:"ajjajajajaj",
        // from:1, //单选，不用数组
        // dest:[],//多选用数组\
        // rule:'hr'
        china:60,
        math:90,
        english:80
    },
    computed:{ //计算属性
        sum:function(){
            return parseFloat(this.china)+parseFloat(this.math)+parseFloat(this.english);
        },
        average:function(){
            return Math.round(this.sum/3);
        }
    }

})

<div id="app">
    <table border="1px">
        <thead>
        <th>学科</th>
        <th>分数</th>
        </thead>
        <tbody>
        <tr>
            <td>语文</td>
            <td><input type="text" v-model="china"></td>
        </tr>
        <tr>
            <td>数学</td>
            <td><input type="text" v-model="math"></td>
        </tr>
        <tr>
            <td>英语</td>
            <td><input type="text" v-model="english"></td>
        </tr>
        <tr>
            <td>总分</td>
            <td>{{sum}}</td>
        </tr>
        <tr>
            <td>平均分</td>
            <td>{{average}}</td>
        </tr>
        </tbody>
    </table>
</div>
```

![1537624371998](C:\Users\郑江\AppData\Local\Temp\1537624371998.png)

### 组件component

可以认为new Vue()这个对象实例就是一个根组件，因为在其内部有components:{}来注册子组件

感觉就是自定义一个标签，表面看上去就是一个标签，实际上内部可以设定一大堆的方法啊，效果啊。分为全局组件（定义以后任何域里面都可以使用），局部组件（只有在特定的域里面起效果）

```js
//定义一个组件alert，在前台页面上只要写上<alert></alert>就可以使用给组件里的功能了
Vue.component('alert',{
    //template模板，表示这个自定义的alert标签在浏览器里实际的东西
    //这里表示自定义的alert标签实际上是个button，然后自己有事件绑定on_Click，可视化的内容，用来给用户看的
    template:'<button @click="on_Click">谈谈</button>',
    //下面是对绑定的on_Click事件的定义
    methods:{
        on_Click:function(){
            alert('Yo');
        }
    }
});
//上面只是把模板设置好了，但是这个模板要有个域，来实现自己的功能
//不然这个component也不知道自己要去哪儿
//下面就是要给这个alert定义一个域，感觉Vue要放在一个域里面，才会有效果
//不然浏览器就不知道这个东西要用Vue来解析
//自定义组件要在域里面才能存活，要是放在一个没用定义的域里面就没有效果
new Vue({
    //定义一个域，为id=app的dom标签里面
    el:"#app",
})

//定时上面的自定义的组件是在任何域里面都可以用
//类似全局变量了，但是有时候我们想要只在某个特殊的域里面使用
//这就要用到局部组件定义了
new Vue({
    el:'#app2',
    //注意这里的component要加s表示复数，可能有多个
    components:{
        'peo':{
            template:'<button @click="on_Click">点我</button>',
            methods:{
                on_Click:function(){
                    alert('haha');
                }
            }
        }
    }
})
```

#### 组件component的点赞实例（用户点一下赞的数目加一，再点一下，就取消点赞）

```js
//定义一个全局组件like
Vue.component('like',{
    //在前台页面上显示给用户看的是一个button标签
    //当被点击的时候，调用方法toggle_like()
    //当当前用户组件的liked值为true时，便给这个button标签绑定上liked类
    //就是相当于加了个样式，让用户知道已经点过赞的
    //点过赞就给按钮加上样式，没点赞就给按钮删除这个样式

    //这个组件的template属性（显示给用户看的），可以写在前台html中
    //然后通过id调用到template的值里面
    // template:'#like_component_tpl',
//    <template id="like_component_tpl">
//     <button :class="{liked:liked}" @click="toggle_like()">👍 {{like_count}}</button>
//    </template>

    template:'<button :class="{liked:liked}" @click="toggle_like()">👍 {{like_count}}</button>',
    
    //因为要记录点赞数，所以要用data把点赞数存下来
    //但是这里的data和Vue实例里面的单纯的记录变量的data不一样
    //因为一个组件可能被多个域来实例化
    //这里要是一个函数，返回数据每个实例的本身的点赞数
    data:function(){
        //renturn 一个对象
        return {
            like_count:10,
            //判断用户是否已经点过赞了
            liked:false,
        }
    },
    methods:{
        toggle_like:function(){
            //因为用户不能一直点赞加赞数，所以在加赞数之前
            //要进行判断，判断该用户是否已经点过了
            if(!this.liked){
                this.like_count++;
            }else{
                this.like_count--;
            }
            this.liked=!this.liked;
        }
    }
})
new Vue({
    //定义一个域名为id='app'的范围中
    el:'#app'
})

```

#### 组件传递参数（外部往里面传参数 父->子）

```
1.0：现在子组件中定义props:['要传入子组件的值的变量名']
2.0：通过在父组件中调用子组件的时候利用：(v-bind)绑定对应的props[]数组里面定义的参数，再将值传递给子组件便可。

//前台的alert标签的msg属性是什么值，我就弹窗显示什么值

//js文件
Vue.component('alert', {
    template: '<button @click="on_Click()">点我</button>',
    //这个属性可以用来接收到前台的自定义alert标签的msg属性的值
    props: ['msg'],
    methods: {
        on_Click:function(){
            alert(this.msg);
        }
    }
})
new Vue({
    el:'#app',
})

//前台文件代码
<div id="app">
    <alert msg="哈哈"></alert>
</div>
```

```
//根据用户信息自动的生成不同的 @用户 的链接

Vue.component('user',{
    //注意这里最里面的单引号和外面的单引号冲突了，可以用转义\，避免冲突
    //也可以用` (Esc下面的键)来表示引号
    template:'<a :href="\'/user/\'+username">@{{username}}</a>',
    props:['username']
})

<div id="app">
    <user username="hh"></user>
</div>
```

#### 子父通信（显示余额）

```
//定义父组件 balance，当子组件的show按钮被点击的时候
//会触发show-balance自定义事件，在这个过程中也可以传值
//父组件监听show-balance事件，当事件被触发的时候，调用自生的函数show0balance
//这个函数会把自生的data数据里的show给改为true,
//这样再div v-if="show"中就能显示具体的余额了
Vue.component('balance', {
    template: `
    <div>
    <!--再这里监听子元素的触发事件-->
    <!--这里表示当监听到触发事件后，就调用show_balance放法-->
    <show @show-balance="show_balance"></show>
	<!--如果组件里的show的值为true，就显示文字-->
    <div v-if="show">
    您的余额为：99员；
    </div>
</div>
    `,
    methods:{
        //这里还可以使用触发事件的参数
        show_balance: function(data){
            this.show=true;
            console.log(data);
        }
    },
    data: function () {
        return {
            show:false,
        }

    }


})
;
Vue.component('show', {
    template: '<button @click="on_Click">显示余额</button>',
    methods: {
        on_Click: function () {
            //这个this.$emit表示手动触发show-balance事件
            //就像点击事件，，鼠标划入事件一样的事件
            //最骚的是，后头还可以传递数据进去
            this.$emit('show-balance', {a:1,b:2});
        }
    }
    });



<div id="app">
    <balance></balance>
</div>


==================================================================
<div id="app">
    <child @send="getData"></child>
</div>
</body>
<script>
    new Vue({
        el:"#app",
        methods:{
          getData:function(index){
              alert(index);
          }
        },
        components:{
            'child':{
                template:"<div><button @click='senddata'>点击发送数据</button></div>",
                methods:{
                    senddata:function(){
                        //设置发送hello数据和触发的事件send
                        this.$emit('send',"hello")
                    }
                }
            }
        }
    })
</script>
```

#### 同级之间通信（利用一个额外的调度器，其实也就是个Vue对象）

```js
用这个额外的调度器，在其中一个组件中注册一个事件（把要传递的参数放入其中），再另一个组件中监听这个事件，取出这个事件中的传递的参数
下面就是 huahua组件 和 shuandan组件的通信，huahua说什么，suandan就要显示出来

//注册事件调度器
var Even=new Vue();
//huahua组件，负责接收输入消息
Vue.component('huahua',{
    template:'<div>花花说：<input v-model="huahua_said" @keyup="on_change"></div>',
    data:function(){
        return {
            huahua_said:'',
        }
    },
    methods:{
        on_change:function(){
            //事件调度器触发一个事件
            Even.$emit('huahua_said',this.huahua_said);
        }
    }
})
//shuandan组件，负责输出消息
Vue.component('shuandan',{
    template:'<div>栓蛋听到{{huahua_said}}</div>',
    data:function(){
        return {
            huahua_said:'',
        }
    },
    //mounted表示组件刚刚被创建的时候，
    //这里表示事件刚被创建的时候，就调用Even事件调度器监听自己的触发事件
    mounted:function(){
        //先把shuandan这个对象保存到me变量里面
        var me=this;
        //监听自己的huahua_said事件，并调用回调函数把事件传过来的数据
        //给更新到shuandan组件的huahua_said变量里面
        Even.$on('huahua_said',function(data){
            me.huahua_said=data;
        })
    }

})

```

#### 不同组件间的切换

```
当定义多个组件的时候，不同的条件下显示不同的组件，这这时候就可以用到<component :is="自定义组件名"></component>

<div id="app">
    <a href="#" @click="cname='login'">登陆</a>
    <a href="#" @click="cname='register'">注册</a>
    <component :is="cname"></component>
</div>
</body>
<script>
    Vue.component('login',{
        template:"<div>登陆组件！</div>",
    });
    Vue.component('register',{
        template:'<div>注册组件！</div>',
    })
    new Vue({
        el:"#app",
        data:{
            cname:'login'
        }
    })
</script>
```



### Vue.filter过滤器

```js
用于把数据进行一定的加工，比方说加个单位呀，之类的东西
例子：我现在要把货物的price后面都统一加上单位‘元’
//这里表示把price作为参数传递到currency函数里面，最后页面上的显示值为函数的返回值
{{price|currency}} 

Vue.filter('currency',function(price){
    return price+'元';
})
new Vue({
    el: '#app',
    data:{
        price:10,
    }
})

<div id="app">
    <span>书本的价格是<h2>{{price|currency}}</h2></span>
</div>
```

### 自定义指令

```
vue内置的指令有v-model,v-blind等，但是可以自定义指令，来实现某种特定的功能。

例子：自定义一个pin指令，用来给div加上position="fixed"效果


Vue.directive('pin',function(el,binding){
    //el表示使用了这个指令的元素，这里为class="card"的div
    //binding表示这个指令的值
    var pinned=binding.value;
    if(pinned){//当前台传入的数据为真时，给div加上固定效果
        el.style.position='fixed';
        el.style.top='10px';
        el.style.left='10px';
    }else{//当指令传入的值为假时，取消div的固定效果
        el.style.position='static'
    }

})
new Vue({
    el:'#app',
    data:{//域中的属性与其属性值
        card1:{
            pinned:false,
        },
        card2:{
            pinned:false
        }
    }
});

<div id="app">
    <div class="card" v-pin="card1.pinned">
    
    在这里当点击按钮时，会触法@click，就会把card1.pinned变为相反的结果然后自定义指令中把card1.pinned
    的值传入js中，根据这个值进行判断，当其为真的时候，把这个div加上position='fixed'的style，实现固定效果。再次点击，card1.pinne的值再次取反，此时后台会把div去掉fixed效果，实现取消固定。
    
    
        <button @click="card1.pinned=!card1.pinned">固定</button>
        用于把数据进行一定的加工，比方说加个单位呀，之类的东西
        例子：我现在要把货物的price后面都统一加上单位‘元’
    </div>
    <div class="card" v-pin="card2.pinned">
        用于把数据进行一定的加工，比方说加个单位呀，之类的东西
        例子：我现在要把货物的price后面都统一加上单位‘元’
    </div>
</div>

```

#### 自定义指令的传参（1.传参，2.传修饰符）

```
自定义指令
1.传递修饰符，用binding.modifiers获取，用v-pin.{修饰符}来传递
其实就是在v-pin后面加上.{参数}来表示要传过去的修饰符，然后用binding.modifiers获取一组修饰符对象数组。
eg:v-pin.buttom.left，就表示传了button和left两个参数过去，然后
   在Vue.directive('pin',function(el,binding)){}中还是利用binding	  来获取数据  var position=binding.modifiers;这时候的position就等    于{buttom:true,left:true}的对象

2.传递参数，用binding.arg获取，格式为v-pin:{参数}

要先传参数，再传修饰符:v-pin:{参数arg}.{修饰符modifiers}



```

### 组件 mixins

```
当定义多个组件的时候，可能会有些公用的methods、data等数据，比方说隐藏和显示功能，此时就可以用到组件里面的mixins属性。把公共的部分引用过来
但是再组件里重新定义的比方说data会把公共部分内的给覆盖掉，权限较高，类似于公共css和标签style的关系

mixins:[base]

//公共部分base
var base = {
	//公共data数据
    data: function () {
        return {
            visibled: false,
        }
    },
    //公共methods方法
    methods: {
        toggle: function () {
            this.visibled = !this.visibled;
        },
        show: function () {
            this.visibled = true;
        },
        hide: function () {
            this.visibled = false;
        }
    }
}

//两个自定义组件
Vue.component('tooltip', {
    template: `
    <div>
    <button @click="toggle">Tooltip</button>
    <div v-if="visibled">
    <span @click="hide">X</span>
    <h2>中秋节</h2>
    <p>中秋节快乐！！</p>
</div>
</div>
    `,
    //引入公共部分
    mixins: [base],

})
Vue.component('popup', {
    template: `
    <div>
    <button @mouseenter="show" @mouseleave="hide">Tooltip</button>
    <div v-if="visibled">
    <h2>中秋节</h2>
    <p>中秋节快乐！！</p>
</div>
</div>
    `,
    //引入公共部分
    mixins: [base],

})
new Vue({
    el: "#app"
})
```

### 插槽slot

```
感觉超级像tp模板的{block}{/blobk}
应用场景：当一个Vue.component自定义组件的template属性的属性值为前台的代码时，由于实际的内容会重用，所以要在里面加上<slot></slot>标签来表示这个内容自定义组件里面是可以重写的。同时，根据slot标签里面的name属性，可以指定重写那个slot，简直和{block name=""}{/block}一模一样有没有？

<div id="app">
    <pan>
    //这里用div 的slot属性表示要替换的内容
       <div slot="inner">
           inereere
       </div>
    </pan>
</div>
<template id="pan">
    <div class="content">
        <div class="title">
        title
        </div>
        <slot name="inner">
            <div class="inner">
                inner
            </div>
        </slot>
        <div class="footer">
            footer
        </div>
    </div>
</template>
```
### v-text和v-html

``` 
由于浏览器解析解析文件是从上往下，当引入的Vue.js文件没有被解析完，那么{{name}}这种显示数据的指令就会被当作字符串来处理，解析玩之后参会被加载为相应的数据（出现闪烁现象）。为了防止这种事情的发生，可以用v-text和v-html来告诉浏览器，我这个东西就是有特殊用处的，别把我解析为字符串了
v-html可以解析样式，如<h1></h1>标签；v-text:就是按照字符串来解析

eg:<span v-html="name"></span>  //name为data数据
```

### v-if逻辑判断和v-show

```
两者都可以完成对对象的显示和隐藏
但是v-if:是对dom元素的操作，在源码里都看不见了
v-show:是对元素加上display:none，来使表面上看不见，但是实际上代码里面还是有一些东西的。
```

### Vue 的Ajax请求

### Vue的动画效果

```
<style type="text/css">
        .show-enter-active,.show-leave-active{
            transition: all 0.4s ease;
            padding-left: 10px;
        }
        .show-enter,.show-leave-active{
            padding-left:100px;
        }
</style>

<div id="app">
    <button @click="toggle">切换</button>
    <br>
    <transition name="show"> //台面包裹上transition标签
        <span v-if="isshow" transition="show">is show</span>
    </transition>

</div>
</body>
<script>
    new Vue({
        el:'#app',
        data:{
            isshow:false,
        },
        methods:{
            toggle:function(){
                this.isshow=!this.isshow;
            }
        }
    })
</script>
```

#### Vue动画效果结合animate扩展css

```
    //引入animate.css文件
    <link rel="stylesheet" href="lib/animate.css">
    <script src="lib/vue.js"></script>
    //设置show类，表示这个元素要应用动画效果
    <style type="text/css">
       .show{
           transition: all 0.4s ease;
       }
    </style>
</head>
<body>
<div id="app">
    <button @click="toggle">切换</button>
    <br>
    //2.0版本里边要用transition标签包裹住要实行动画的标签
    //enter-active-class表示入场动画
    //leave-active-class表示出场动画
    <transition enter-active-class="fadeInRight" leave-active-class="fadeOutRight">
        //class="animated"表示这个元素要用到animated动画扩展类
        //class="show" 表示这个元素要用到show动画效果
        <div v-if="isshow" class="animated" class="show">is show</div>
    </transition>

</div>
</body>
<script>
    new Vue({
        el:'#app',
        data:{
            isshow:false,
        },
        methods:{
            toggle:function(){
                this.isshow=!this.isshow;
            }
        }
    })
</script>
```

### Vue获取DOM元素和自定义组件信息

```
有点像 getElementById("元素id")

<div id="app">
//这里定义的ref表示这个组件我会用到，
//会在脚本里面通过this.$refs.组件名称来获取
//this.$refs中储存了所有的标记的组件，从里面通过名字取就可以了
//类似于js中的getElementById()
    <div ref="mydom">data</div>
    <button @click="getDom">获得Dom元素</button>

    <book ref="book"></book>
    <button @click="getCom">获取组件的内部data值</button>
</div>
<template id="book">
    <div><h1>my name</h1></div>
</template>
</body>
<script>
   new Vue({
       el:"#app",
       methods:{
           //获取一般DOM元素的值
           getDom:function(){
                console.log(this.$refs.mydom.innerHTML);
           },
           //获取自定义组件内部的值
           getCom:function(){
                console.log(this.$refs.book.name);
           }
       },
       //自定义组件
       components:{
            "book":{
                //通过id引用外部定义的<template>中的值
                template:"#book",
                //组件内部的数据name
                data:function(){
                    return {
                        name:"我叫奥特玛",
                    }
                }
            }
       }
   })
</script>
```

### Vue路由

```
<div id="app">
    <!--表示这个是个路由链接，其实相当于a标签了，路由目标是/login，
    这个请求会被发送到路由规则对象里，然后去里面的routers[]数组里面匹配，
    最后显示相应的组件-->
    <router-link to="/login">登陆</router-link>
    <router-link to="/register">注册</router-link>

    <!--路由占位符：先占下一块地方，为后来显示不同组件
    提供场地，最终所有组件的内容都会替换这个占位符-->
    <router-view></router-view>
</div>
</body>
<script>
    //1.0 准备组件
    //注意这里的组件知识定义好了，没有像Vue.component()那样实例化成了真正的组件
    var App=Vue.extend({});  //根组件
    var login=Vue.extend({
        template:"<div><h1>登陆</h1></div>"
    }); //登陆组件
    var register=Vue.extend({
        template:"<div><h1>注册</h1></div>"
    });    //注册组件

    //2.0 初始化路由规则对象
    var router=new VueRouter({
        routes:[
        	//当当前页面为根目录时，把路由导到login组件去
            {path:'/',redirect:"/login"},
            //当页面url后面有 /login 时，则加载名字叫做 login 的组件对象
            {path:'/login',component:login},
            //当页面url后面有 /register 时，则加载名字叫做 register 的组件对象
            {path:'/register',component:register},

        ]
    })

    //3.0 开起路由对象
    new Vue({
        el:"#app",
        router:router,  //开启路由对象
    })
</script>


================================================================================================
//url带参数传值。
<div id="app">
    <!--表示这个是个路由链接，其实相当于a标签了，路由目标是/login，
    这个请求会被发送到路由规则对象里，然后去里面的routers[]数组里面匹配，
    最后显示相应的组件-->
    <router-link to="/login">登陆</router-link>
    //当要传值的时候，就在后面加上要传过去的值
    <router-link to="/register/总结">注册</router-link>

    <!--路由占位符：先占下一块地方，为后来显示不同组件
    提供场地，最终所有组件的内容都会替换这个占位符-->
    <router-view></router-view>
</div>
</body>
<script>
    //1.0 准备组件
    //注意这里的组件知识定义好了，没有像Vue.component()那样实例化成了真正的组件
    var App=Vue.extend({});  //根组件
    var login=Vue.extend({
        template:"<div><h1>登陆</h1></div>"
    }); //登陆组件
    var register=Vue.extend({
        template:"<div><h1>注册{{name1}}</h1></div>",
        data:function(){
            return {
                name1:"",
            }
        },
        created:function(){
            //用this.$route.params.{路由规则处定义的参数名}来取
            //通过url传来的信息
            this.name1=this.$route.params.name
        }

    });    //注册组件

    //2.0 初始化路由规则对象
    var router=new VueRouter({
        routes:[
            //当当前页面为根目录时，把路由导到login组件去
            {path:'/',redirect:"/login"},
            //当页面url后面有 /login 时，则加载名字叫做 login 的组件对象
            {path:'/login',component:login},
            //当页面url后面有 /register 时，则加载名字叫做 register 的组件对象
            //路由规则要定义一下，我要带参数name
            {path:'/register/:name',component:register},

        ]
    })

    //3.0 开起路由对象
    new Vue({
        el:"#app",
        router:router,  //开启路由对象
    })
</script>








================================================================================================
//嵌套路由，注意在父组件里面加上<router-view></router-view>预留空间
<div id="app">
    <router-link to="/account/login">登陆</router-link>
    <router-link to="/account/register">注册</router-link>

    <router-view></router-view>
</div>
</body>
<script>
    var App=Vue.extend({});

    var account=Vue.extend({
        template:'<div><h1>账号组件</h1><router-view></router-view></div>',
    });

    var login=Vue.extend({
        template:'<h1>登陆</h1>'
    });

    var register=Vue.extend({
        template:'<h1>注册</h1>'
    })

    //注册路由对象，并给对象添加路由规则
    var router=new VueRouter({
        //注意这里是routes，没有r
        routes:[
            {
                path:'/account',
                component:account,
                //定义子路由，注意子路由没有反斜杠
                children:[
                    {path:'login',component:login},
                    {path:"register",component:register}
                ],
            },
        ],
    })

    //使路由生效
    new Vue({
        el:"#app",
        //使前面定义的router路由对象生效
        router:router
    })

</script>
```

### Vue watch

```
//eg:监控输入框里的值，动态改变fullName
<div id="app">
    <input type="text" v-model="firstName">
    <input type="text" v-model="lastName">
    {{fullName}}
</div>
</body>
<script>
    new Vue({
        el:'#app',
        data:{
            firstName:'itcase',
            lastName:'heima',
            fullName:null
        },
        //指定监控的值
        watch:{
            //firsrName表示监控域中的data里面的firstName的值
            //只要他发生变化，则会自动调用后面的回调函数
            //newval为该变量的新值，oldvel为该变量的旧值
            'firstName':function(newval,oldval){
               this.fullName=newval+this.lastName;
            },
            'lastName':function(newval,oldvel){
                this.fullName=this.firstName+newval;
            }
        }
    })
</script>

======================================================================================
//这个还可以监控路由对象
在开启路由时，
new Vue({
    el:'#app',
    route:route,	//开起路由对象
    watch:{
    //这里的$route是系统自带的对象，专门表示路由对象(好像加上$符号的都是系统内部的特殊对象
    //newRoute表示新状态，oldRoute表示就状态
        '$route':function(newRoute,oldRoute){
        //这样就可以获得路由对象了，获取到当前的路由规则字符串是谁(path)，这样就
        //能够针对特殊的页面(url)做出特殊的处理了。
        //比方说，在特殊的页面专门显示或者专门不显示某些内容
            console.log(newRoute,oldRoute);
        }
    }
})
```

### Vue computed计算属性

```
//通过计算属性实时修改fullName的值
<div id="app">
    <input type="text" v-model="firstName">
    <input type="text" v-model="lastName">
    {{fullName}}
</div>
</body>
<script>
    new Vue({
        el:'#app',
        data:{
            firstName:'郑',
            lastName:'江',
        },
        computed:{
        //注意这里是函数的return 值
        //firstName或者lastName任何一个值发生改变都会重新触发这个function的调用
        //一次实现实时更新，而且会刷新时先检查缓存，若数据没变则不计算，提高效率
            fullName:function(){
                return this.firstName+this.lastName;
            }
        }

    })
</script>
```

