# Flutter包管理
一个APP在实际开发中往往会依赖很多包，而这些包通常都有交叉依赖关系、版本依赖等，如果由开发者手动来管理应用中的依赖包将会非常麻烦。因此，各种开发生态或编程语言官方通常都会提供一些包管理工具，比如在Android提供了Gradle来管理依赖，iOS用Cocoapods或Carthage来管理依赖，Node中通过npm等。而在Flutter开发中也有自己的包管理工具。即pubdpec.yaml
##pubspec.yaml
YAML是一种直观、可读性高并且容易被人类阅读的文件格式，它和xml或Json相比，它语法简单并非常容易解析，所以YAML常用于配置文件，Flutter也是用yaml文件作为其配置文件。  

	name: flutter_in_action
	description: First Flutter application.
	
	version: 1.0.0+1
	
	dependencies:
	  flutter:
	    sdk: flutter
	  cupertino_icons: ^0.1.2
	
	dev_dependencies:
	  flutter_test:
	    sdk: flutter
	
	flutter:
	  uses-material-design: true 
+ name：应用或包名称。
+ description: 应用或包的描述、简介。
+ version：应用或包的版本号。
+ dependencies：应用或包依赖的其它包或插件。
+ dev_dependencies：开发环境依赖的工具包（而不是flutter应用本身依赖的包）。
+ flutter：flutter相关的配置选项。

##Pub仓库
Pub（https://pub.dev/ ）是Google官方的Dart Packages仓库，类似于node中的npm仓库，android中的jcenter。我们可以在Pub上面查找我们需要的包和插件，也可以向Pub发布我们的包和插件。我们将在后面的章节中介绍如何向Pub发布我们的包和插件。

