# webpack，什么东西都可打包为js文件

### 下载安装

```
1. 下载node.js并安装。
2. cmd npm install nrm -g 、nrm ls、nrm use taobao
3. npm install webpack@1.14.0 -g //全局安装webpack
```

### js文件的打包使用

```
eg:
=====在clas.js中定义了一个add函数 传入两个数，返回两个数的和=================
function add(v1,v2){
    return v1+v2;
}
//这时候我要把我的add方法导出
module.exports=add; //表示导出add方法

======在main.js文件中，要引用calc.js exports出来的add方法==================
//1.0获取dom对象
var v1=document.querySelector("#v1");
var v2=document.querySelector("#v2");
var bt=document.querySelector("#bt");
var result=document.querySelector("#result");

bt.onclick=function(){
    //2.0获取calc.js中导出的add方法并且调用它计算结果
    var v1value=parseFloat(v1.value);
    var v2value=parseFloat(v2.value);

    //调用add方法
    //这个require要指名目标js文件(clac.js)的位置
    var add=require('./calc.js');
    result.value=add(v1value,v2value);
}

==========================================================================
经过上面两步，两个js文件中的关联已经建立好了，下面就是见证奇迹的时刻
在文件夹下打开cmd输入， webpack main.js build.js
解析：这个意思就是入口文件时main.js，个人感觉就是在html文件中被调用的js。而输出的出口文件是bulid.js，
	 最后会产生一个build.js文件，这个文件中会根据入口文件main.js中所require()的文件地址，一层层的找下	  去，最后生成一个合并了main.js，clac.js功能的build.js。这个js文件可以被浏览器所认识。
	 
================================================================================
为什么要这样调用来调用去的呢？
解析：这样可以使业务层次分名，计算是计算，逻辑是逻辑，只要require一下我所需要的函数就ok了。主要的main.js	 里面就可以不用考虑计算该怎么弄，只要require()一下就ok了，美滋滋。打包后的文件巨复杂，也起到了代码	  	   保护的功能！
```



### 配置文件的使用

```
1.首先，项目的源文件（自己手敲的），放在项目目录下的src文件夹下。而最后打包好的文件，放在项目目录下的dist文件夹中。
2.在项目根目录下面建一个webpack.config.js文件（会被认为是webpack的配置文件而读取），
    module.exports={
        entry:'./src/main.js', //入口文件的位置
        output:{
            path:__dirname+'/dist', //出口文件的放置地址，要用绝对路径
            filename:'build.js', //出口文件的地址
        }
    }	
3.最后在文件目录下cmd 直接webpack，就自动打包好了。
```

### css包

```
1.npm init //生成配置文件package.json
2.npm install css-loader style-loader --save-dev //表示下载文件，并把相关信息（loader版本号等信息）记录到packahe.json里面去。
3.这样有了package.json文件，下次只要在这个文件同文件夹下 直接 npm install 就可以根据这个配置文件下载所   需要的所有依赖包了，美滋滋。
    module.exports={
        entry:'./src/main.js', //入口文件的位置
        output:{
            path:__dirname+'/dist', //出口文件的放置地址，要用绝对路径
            filename:'build.js', //出口文件的地址
        },
        //要打包css文件，要在webpack.config.js中加入module
        module:{
            loaders:[
                {
                    //正则表达式，所有.css结尾的文件都被此loader所处理
                    test:/\.css$/,
                    //固定写法，中间是感叹号
                    loader:'style-loader!css-loader'
                }
            ]
        }
    }
  
  4.在main.js中require要打包的文件
        //导入site.css
        require('../static/css/site.css');
```

### 打包url资源

```
应用背景：在css样式中，有些地方要用到url资源，比方说background-image:url('图片路径')。这时候，我们就可以把小一些的图片以base64编码手段储存在打包好的bulid.js文件里面，这样就不会多次加载了。大一些的图片则会以文件路径的的方式储存在build.js文件里面

下载node包：npm install url-loader file-loader --save-dev

在webpack.config.js中配置这两个loader
{
    test:/\.(png|jpg|gif|ttf)$/,	//正则匹配，所有后缀为png|jpg|gif|ttf的文件都交给									这个loader来处理。
    loader:"url-loader?limit=40000"  //限制图片大小，零界点为40000byte(40k)
}

在site.css文件中导入图片
#bg{
    width:300px;
    height:300px;
    background-image:url('../image/home.png')
}

在入口文件导入
require('../static/css/sit.css')
```

### ECMA Script6转ECMA Script5语法

```
npm install{} --save-dev 下载node包

babel-core
babel-loader
babel-plugin-transform-runtime
babel-preset-es2015

var htmlwp=require('html-webpack-plugin');
module.exports={
    entry:'./src/main.js', //入口文件的位置
    output:{
        path:__dirname+'/dist', //出口文件的放置地址，要用绝对路径
        filename:'build.js', //出口文件的地址
    },
    //要打包css文件，要在webpack.config.js中加入module
    module:{
        loaders:[
            {
                //正则表达式，所有.css结尾的文件都被此loader所处理
                test:/\.css$/,
                //固定写法，中间是感叹号
                loader:'style-loader!css-loader'
            },
            {
                test:/\.(png|jpg|gif)$/, //打包url请求的资源文件
                //limit表示文件大小小于40000kb的我打包到build.js，
                // 大于40000的我把文件路径打包到build.js里
                loader:"url-loader?limit=40000"
            },
            ==================================================
            {
                test:/\.js$/, //将.js结尾的文件中es6语法转成es5语法
                loader:"babel-loader",  //用这个loader转换
                //把第三方包(node_modules中的js文件排除掉)，因为这里的文件肯定是es5的
                exclude:/node-modules/
            }
        ]
    },
    babel:{
      presets:['es2015'],    //配置将es6语法转换成es5语法的指令
      plugins:['transform-runtime']     //动态编译vue文件
    },
    ==================================================
    plugins:[
        new htmlwp({
            title:"首页",  //生成页面标题
            //webpack-dev-server 在内存中生成的文件名称，
            // 自动将build注入到这个页面底部
            filename:'index.html',
            //根据index.html这个模板来生成（这个文件请程序员自己生成）
            //要和自己ide实际的入口文件名字一样
            template:'index.html'
        })
    ]
}
```



