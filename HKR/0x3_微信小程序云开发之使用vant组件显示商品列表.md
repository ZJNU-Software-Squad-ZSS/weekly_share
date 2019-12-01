# 微信小程序云开发之使用vant组件显示商品列表

##  一、安装vant

1. 使用npm安装vant

   在终端：

   > npm init
   >
   > npm i vant-weapp -s --production

2. 在小程序中构建npm

   菜单栏点击工具---构建npm，构建完成后在根目录下会显示带有vant-weapp的miniprogran_npm文件夹。

3. 修改项目设置

   在项目详情中，勾选使用npm模块。

   
## 二、使用vant，显示商品列表

1. 引用组件

   在页面的.json中引用需要的组件vant

   > "usingComponents": {
   > 　　"van-card": "../../miniprogram_npm/vant-weapp/button/index" 


2. 使用组件,基础显示

   > <van-card  
   > num="2"  
   > tag="标签"  
   > price="2.00"  
   > desc="描述信息"    
   > title="商品标题" 
   > thumb="https://img.yzcdn.cn/vant/t-thirt.jpg"  
   > origin-price="10.00" 
   > /> 

   ![image text]( https://github.com/KerenHHH/MyWeeklyShare/blob/master/pictures/vant1.png  )
   
3. 将集合显示到页面上成为商品列表

   将商品信息存放在页面的.js中的

   > data{
   >
   > ​	goodslist:商品信息集
   >
   > }

   在页面wxml中使用wx:for表示显示一个数据集中的每条数据

   > <view wx:for="{{goodslist}}">
   >
   > ​	<van-card  
   > ​	num="{{item.num}}"  
   > ​	tag="{{item.tag}}"  
   > ​	price="{{item.price}}"  
   > ​	desc="{{item.desc}}"    
   > ​	title="{{item.title}}" 
   > ​	thumb="{{item.picture}}"  
   > ​	origin-price="{{item.origin-price}}" 
   >   /> 
   >
   > </view>

   效果类似于下面这个

   ![image text]( https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1574422244563&di=8be5f488b45415b0fae62ba5a4b1c5a0&imgtype=0&src=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F01fe295541ee58000001714a20fd7a.jpg%401280w_1l_2o_100sh.png )
