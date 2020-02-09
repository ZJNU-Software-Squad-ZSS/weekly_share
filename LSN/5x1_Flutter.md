# Flutter知识点
Flutter一切皆组件
每个组件用()包括所有属性，各个属性间用,分隔，属性也可能是组件
### 一、Text类
用来显示普通文本
第一行为文本内容，只能有一个文本
默认单词换行
|   参数名  |   作用  |  参数使用的类   |示例值|
| --- | --- | --- |---|
|文本|需要显示的文本内容|String类|"wdnmd"|
|  textAlign   |   显示文字的水平对齐方式，默认TextAlign.left  |  TextAlign类   |TextAlign.center|
|  maxLines   | 决定文字在组件内显示的最大行数，默认无    |   int类  |1|
|  overflow   |  决定多余的文字如何进行显示，默认TextOverflow.clip   |   TextOverflow  |TextOverflow.ellipsis|
|   style  |   决定文字的样式  |   TextStyle  |TextStyle()|
### 二、TextStyle类
TextStyle 设置文字属性值
|   参数名  |   作用  |  参数使用的类   |示例值|
| --- | --- | --- | --- |
| fontSize     |  决定文字大小，默认14  |  double类   |   23.0  |
|  color    |   决定文字颜色 默认黑色  |  Color类/Colors类   |  Color.fromARGB(a,r,g,b)   |
|  decoration   |  给文字添加装饰 默认无   |   TextDecoration类  |   TextDecoration.underline  |
|  decorationStyle   |  设置装饰样式   | TextDecorationStyle类    |   TextDecorationStyle.solid  |

### 三、Container类
和html里的div相似
|   参数名  |   作用  |  参数使用的类   |示例值|
| --- | --- | --- | --- |
|  alignment   |   设置内部内容的水平和垂直对齐方式  |  Alignment类  |    Alignment.center    |
| width    |  设置宽度   |   double类  |  200.0   |
|  height   |  设置高度   |  double类  |  200.0   |
|   color  |  设置背景颜色   |    Color类/Colors类  |  Colors.green   |
|   padding  |  设置内边距   |  EdgeInsets类   | const EdgeInsets.all(allvalue)    |
|   margin  |   设置外边距 |  EdgeInsets类   | const EdgeInsets.all(allvalue)    |
|  decoration   |   设置容器装饰  | BoxDecoration类    |  BoxDecoration(）   |

### 四、BoxDecoration类
设置容器装饰
|   参数名  |   作用  |  参数使用的类   |示例值|
| --- | --- | --- | --- |
|  gradient   | 设置变化效果    | LinearGradient类    | LinearGradient()    |
|  border   |  设置容器边框，默认无   |   Border类  |  Border.all()   |
### 五、LinearGradient类 
设置线性变化样式
|   参数名  |   作用  |  参数使用的类   |示例值|
| --- | --- | --- | --- |
|  colors  | 设置线性变化效果，默认从左到右    | Color类/Colors类数组    | [Colors.lightBlue,Colors.lightGreenAccent,Colors.pink]   |
### 六、Border类 
设置边框的样式
|   参数名  |   作用  |  参数使用的类   |示例值|
| --- | --- | --- | --- |
|  width   | 设置边框宽度    |  double类   |  2.0   |
|   color  |  设置边框颜色   |  Color类/Colors类   |  Colors.red   |

### 七、Image类
Image用来显示图片
Image有两个通道，dst和src，dst为目标图像通道，src为源图像通道，src默认比dst优先级高
四种加载图片的方式
**第一种为Image.asset(file)**
从APP的资源，即从项目目录加载图片，打包
**第二种为Image.file(file)**
从手机存储，即本地路径加载图片
**第三种为Image.memory(file)**
从内存加载图片（不准确）
**第四种为Image.network(file)**
从网络加载图片，用得较多
#### Image.network
|     参数名      |                                         作用                                         |   参数使用的类    |        示例值         |
| -------------- | ------------------------------------------------------------------------------------ | ---------------- | -------------------- |
| 路径           | 用路径加载的图片为dst通道！！！！ 直接填入路径，其他属性跟在路径后                         | String类         | "https://dsda.jpg"   |
| fit            | fit决定图片在容器中如何显示                                                            | BoxFit类         | BoxFit.contain       |
| color          | color将设置src通道内容                                                                | Color类/Colors类 | Colors.red           |
| repeat         | 设置图像的重复方式                                                                     | ImageRepeat类    | ImageRepeat.noRepeat |
| colorBlendMode | 图像混合模式，将dst通道和src通道以某种规则混合，见https://www.jianshu.com/p/4fb8f1a08d12 | BlendMode类      | BlendMode.lighten    |

### 八、ListView类
ListView组件默认生成一个纵向列表
|   参数名  |   作用  |  参数使用的类   |示例值|
| --- | --- | --- | --- |
| children    | 用来定义ListView内的内容    |   Widget数组  |  ` <Widget>[Container(),Container(),Container()]  `|
|   scrollDirection  |   设置列表方向  |  Axis类   |   Axis.horizontal  |
#### ListView.builder构造方法
|    参数名    |          作用           |                                      参数使用的类                                      |                                  示例值                                  |
| ----------- | ----------------------- | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| itemBuilder | 用来定义ListView内的内容 | 返回Widget（可能），含有context和index两个参数的方法,index将会从0开始到itemCount-1为止遍历 | `(context,index){return new ListTile( title:Text('${items[index]}') );` |
| itemCount   | 定义item数量            | int类                                                                                 | 20                                                                      |


### 九、ListTitle类
ListTitle组件生成一个表头（标题
|   参数名  |   作用  |  参数使用的类   |示例值|
| --- | --- | --- | --- |
| leading    |通常存放标题的图标    |  Icon类/CircleAvatar类   | Icons.access_time    |
|  title   |  通常存放标题的主标题   |  Text类   |   Text()  |

###  十、GridView类
GridView实现网格布局
|   参数名  |   作用  |  参数使用的类   |示例值|
| --- | --- | --- | --- |
| gridDelegate    |  网格委托，使用委托生成表格？   |  SliverGridDelegateWithFixedCrossAxisCount类/SliverGridDelegateWithMaxCrossAxisExtent类   |  SliverGridDelegateWithFixedCrossAxisCount()   |
|   children  | 定义GridView内容    |  Widget数组   |  `<Widget>[Container(),Container(),Container()]  `   |
#### GridView.count
较为简单的一种写法
|   参数名  |   作用  |  参数使用的类   |示例值|
| --- | --- | --- | --- |
|   padding  |  GridView和子元素间距   |   EdgeInsets   |   EdgeInsets.all(allvalue)   |
|  crossAxisSpacing   |   网格元素之间的间距  |   double类  |  10.0   |
|   crossAxisCount  |  每行的列数   |  int类   |  3   |
|   children  | 定义GridView内容    |  Widget数组   |  `<Widget>[Container(),Container(),Container()]  `   |

###  十一、SliverGridDelegateWithFixedCrossAxisCount类
定义生成网格的方法、样式等
|   参数名  |   作用  |  参数使用的类   |示例值|
| --- | --- | --- | --- |
|crossAxisCount     |   每行的列数  | int类    |  3   |
|   mainAxisSpacing  |    每行间的间隔 |  double类   |  2.0   |
|  crossAxisSpacing   |  每列的间隔   |  double类   |  2.0   |
|  childAspectRatio   |   每个格子的宽:长比值  |   double类  |0.75     |
### 十二、Row类
Row类使其子元素都放置在同一行内
|   参数名  |   作用  |  参数使用的类   |示例值|
| --- | --- | --- | --- |
| children    | 用来定义Row内的内容    |   Widget数组  |  ` <Widget>[Container(),Container(),Container()]  `|
| crossAxisAlignment   | 用来定义Row内垂直对齐方式       |  CrossAxisAlignment类 |  CrossAxisAlignment.start|
| mainAxisAlignment   | 用来定义Row内水平对齐方式       |   MainAxisAlignment类 |  MainAxisAlignment.end|
### 十三、Column类
Row类使其子元素都放置在同一列内
|   参数名  |   作用  |  参数使用的类   |示例值|
| --- | --- | --- | --- |
| children    | 用来定义Column内的内容    |   Widget数组  |  ` <Widget>[Container(),Container(),Container()]  `|
| crossAxisAlignment   | 用来定义Column内水平对齐方式       |  CrossAxisAlignment类 |  CrossAxisAlignment.start|
| mainAxisAlignment   | 用来定义Column内垂直对齐方式       |   MainAxisAlignment类 |  MainAxisAlignment.end|
### 十四、Expanded类
Expanded类使Row、Column、Flex等子组件在其主轴方向上展开并填充可用空间
|   参数名  |   作用  |  参数使用的类   |示例值|
| --- | --- | --- | --- |
| child    | 子组件，使其能自动充满整个空间    |   Widget  |   RaisedButton()  |
### 十五、RaisedButton类
按钮类，创造一个按钮
|   参数名  |            作用             | 参数使用的类 |                       示例值                        |
| --------- | --------------------------- | ----------- | -------------------------------------------------- |
| onPressed | 用来定义RaisedButton被点击时的事件     | 一个没有参数，无返回的方法  | `(){}  ` |
| color  | 用来定义RaisedButton背景颜色    | Color类/Colors类  |Colors.blue |
| child     | 用来显示RaisedButton里的内容 | Widget      | Text()                                          |
### 一些常用类
##### 1、Colors类 
存放一些常用的颜色
如Colors.lightBlue
##### 2、BlendMode类
存放一些图片的混合模式
如BlendMode.lighten
##### 3、Icons类
存放一些内置的图标
如Icons.access_time，使用时需要new一个Icon
##### 4、EdgeInsets类
用来插入padding,margin
EdgeInsets.all(values）四周相同
 EdgeInsets.fromLTRB(left,top,right,botton) 四周不同
##### 5、TextAlign类
设置文本对齐方式
TextAlign.center  居中对齐
TextAlign.left 左端对齐
TextAlign.right 右端对齐
TextAlign.start 文字开始处对齐
TextAlign.left 文字结束处对齐（以上两种可能考虑到不同语言的阅读方向习惯，中英文和left right无太大区别）
##### 6、TextOverflow类
设置文本溢出时的样式
TextOverflow.clip 不显示多余文字
TextOverflow.ellipsis 在末尾添加...
TextOverflow.fade 在末尾整一行添加从上到下的由深至浅的渐变效果，但看不太出来
##### 7、Color类/Colors类
设置颜色，Colors类为自带的一些颜色
Color.fromARGB(a,r,g,b)设置颜色 注意a透明度在第一个
##### 8、TextDecoratio类
设置文本装饰
TextDecoration.underline 添加下划线
##### 9、TextDecorationStyle类
设置文本装饰样式
TextDecorationStyle.solid 设置下划线为单实线
##### 10、 Alignment类
设置容器内部水平、垂直对齐方式
Alignment.center 设置为水平垂直居中
Alignment.centerLeft 设置为垂直居中，水平向左
Alignment.centerRight 设置为垂直居中，水平向右
Alignment.bottomCenter 设置为底部居中对齐
Alignment.topCenter 设置为顶部居中对齐
##### 11、BoxFit类
图片在容器中如何显示
BoxFit.contain 图片等比例缩放，直至其宽或高与容器宽或高相同（适应
BoxFit.fill 图片缩放，直至其宽或高与容器宽或高相同（填满
BoxFit.cover 图片等比例缩放，直至其宽或高都大于等于容器宽或高，多余部分将被裁切（平铺满
BoxFit.fitHeight 图片等比例缩放，直至其高等于容器高，多余部分将被裁切（高度满
BoxFit.fitWidth 图片等比例缩放，直至其宽等于容器宽，多余部分将被裁切（宽度满
BoxFit.none 图片按原分辨率展示，多余的将被裁切
BoxFit.scaleDown 图片不能被放大，但能被缩小显示，其余和contain相同
##### 12、ImageRepeat类
设置图像的重复方式
ImageRepeat.repeat 从正中央开始向四周重复
ImageRepeat.noRepeat 不重复，默认值
ImageRepeat.repeatX 从水平居中向左右横向重复
ImageRepeat.repeatY 从垂直居中向上下纵向重复
##### 13、BlendMode类
图像混合模式，更多模式见https://www.jianshu.com/p/4fb8f1a08d12
BlendMode.darken 通过从每个颜色通道中选择最小值来组合源图像和目标图像，和modulate相比
BlendMode.lighten 通过从每个颜色通道中选择最大值来组合源图像和目标图像。
BlendMode.colorDodge 用src的倒数除以dst
BlendMode.colorBurn 用dst函数的倒数除以src函数的倒数，然后求结果的倒数
BlendMode.hardLight 将src图像和dst图像的组件相乘，然后对它们进行调整，使之有利于src
BlendMode.softLight 对于小于0.5的src值使用[colorDodge]，对于大于0.5的src值使用[colorBurn]。这导致了与[overlay]相似但更柔和
##### 14、Axis类
设置列表的方向
Axis.horizontal 设置列表方向为横向
Axis.vertical 默认值，设置列表方向为纵向
##### 15、CrossAxisAlignment类
设置Row、Column内子元素副轴的对齐方式（Row的副轴是垂直方向
##### 16、MainAxisAlignment类
设置Row、Column内子元素副轴的对齐方式（Row的副轴是水平方向