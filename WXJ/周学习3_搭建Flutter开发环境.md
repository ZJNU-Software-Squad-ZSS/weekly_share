#搭建Flutter开发环境
使用Flutter框架可以实现跨平台移动应用开发，因实验室配备Mac，学习在macOS上搭建flutter开发环境
##获取Flutter SDK
1. 在flutter官网下载最新可用的安装包，官网地址：https://flutter.io/sdk-archive/#macos
2. 解压安装包到想安装的目录
3. 运行flutter doctor命令，查看是否还需要安装其他依赖，如果需要，安装他们

##更新环境变量
1. 确定Flutter SDK的目录"FLUTTER\_INSTALL\_PATH"
2. 打开（或创建）
```
$HOME/.bash_profile
```
3. 添加以下路径：
```
export PATH=[FLUTTER_INSTALL_PATH]/flutter/bin:$PATH
```
4. 运行
```
source $HOME/.bash_profile
```刷新当前终端窗口
5. 验证"flutter/bin"是否已在PATH中
```
echo $PATH
```

##安装Xcode
过程简单，不再描述

##安装Android Studio
同上

##IDE配置与使用
###安装Flutter和Dart插件
1. 启动AS
2. 打开插件首选项（macOS: Preferences>Plugins）
3. 选择Browse repositories...,选择flutter插件点击install
4. 重启AS后插件生效

###创建Flutter应用
1. 选择File>New Flutter Project.
2. 选择Flutter application作为project类型，然后点击Next.
3. 输入项目名称，然后点击Next
4. 点击Finish
5. 等待AS安装SDK并创建项目

##连接设备运行Flutter应用
###连接IOS真机设备
要将Flutter应用安装到IOS真机设备，需要一些额外的工具和一个Apple账户，还需要在Xcode中进行一些设置。  

1. 安装homebrew  
2. 打开终端并运行如下这些命令：
```
brew update
brew install --HEAD libimobiledevice
brew install ideviceinstaller ios-deploy cocoapods
pod setup
```

3. 遵循Xcode签名流程来配置项目

+ 在Flutter项目目录中通过
```
open ios/Runner.xcworkspace
```打开默认的Xcode workspace  

+ 在Xcode中，选择导航面板左侧中的Runner项目
+ 在Runner target设置页面中，确保在General > Siging > Team下选择自己的开发团队
+ 要开始第一个IOS开发项目，可能需要使用Apple ID登录Xcode
+ 如果Xcode中的自动签名失败，请验证项目的General > Identity > Bundle Identifier值是否唯一
+ 运行flutter run启动flutter应用程序
