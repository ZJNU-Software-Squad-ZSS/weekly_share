# Flutter初次接触
Unity3d的课后面都是讲C#的，然而C#已经自学过了
相比于继续学习web，我更觉得移动端app开发有优势，因此准备学习这款早已闻其名的框架——Flutter
### Flutter安装
按照网上教程进行安装
https://www.jianshu.com/p/b24ae445e167
安装过程十分顺利，没有遇到什么地方卡住，不过需要注意Intellij家的软件也会被Flutter检测，但不管他也没事
### Flutter生态资源
https://github.com/Solido/awesome-flutter
https://flutter.io/showcase
### Flutter虚拟机安装
在安装AndroidStudio是可以选择安装一个
或者：
AndroidStudio新建Flutter项目 
Tools->AVD manager->新建虚拟机->选择型号（默认Nexus5X)->选择安卓系统版本
回到AS主界面，如果运行显示no device，则在flutter控制台下输入
flutter config --android-sdk 安卓SDK路径
重启AS
### Intellij IDEA上安装Flutter
和在AS上安装一样，在设置里添加Flutter和Dart插件，并且手动选择AndroidSDK位置就行
在Visual Code上安装也大致相同
### 使用真机调试
使用模拟机果然会很卡——尤其是在使用Intellij这样沉重的编译器时
所以我个人以前就有一只备用机，这里拿来用作测试机
手机是Oppo R11st，打开开发者选项（OPPO是点击版本号6次进入）后用USB连接电脑。电脑会自动检测到这个手机的
# Dart语法部分
粗看一下基础语法和Js有点像，在此按照网上视频流程进行一些基础语法的记录
```dart
引入包：
import 'package:flutter/material.dart';//MaterialUI库
main方法：
void main()=>runApp(MyApp());//=>也可以用{}代替，感觉和Lambda有点像，MyApp是自己的类
class MyApp extends StatelessWidget{
  @override
  Widget build(BuildContext context){//接受一个BuildContext内容，返回一个窗口部件
    return MaterialApp(
      title:"Welcome to Flutter",
      home:Scaffold(
        appBar:AppBar(
          title:Text("Welcome to Flutter")
        ),//标题
        body:Center(
          child:Text("Hello World!")
        ),//Center使文字在屏幕中间
      ),
    );
  }
}
```
