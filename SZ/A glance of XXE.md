# XXE入门

## 训练平台

Pikachu：[链接](https://github.com/zhuifengshaonianhanlu/pikachu)
WebGoat：[链接](https://github.com/WebGoat/WebGoat)

## XXE(XML External Entity Injection)

即"XML外部实体注入漏洞"，这是一个注入类型的漏洞，那我们一句话就可以想到 “输入做过滤，输出做转移”  
简单的说，就是 攻击者通过向服务器**注入指定的XML实体内容**, 从而让服务器**按照攻击者指定的配置进行执行**, 从而导致问题"  
那么，漏洞利用需要的两个条件就很明确了：  
1. 服务端**接收和解析**了来自用户端的xml数据。（很多语言里面对应的解析XML的函数默认是禁止解析外部实体内容，从根本上避免了该漏洞）
2. 服务端对上述XML数据没有做严格的安全控制（例如过滤）

### 什么是XML？
参考：[链接](https://hpdoger.cn/2019/01/07/%E4%BB%8E%E4%B8%A4%E9%81%93CTF%E9%A2%98%E7%9B%AE%E5%AD%A6%E4%B9%A0XXE%E6%BC%8F%E6%B4%9E/)
英文名：Extensible Markup Language，也是一种标记语言（e.g. HTML）主要将文本（Text）以及文本相关的其他信息结合起来，展现出关于**文档结构和数据处理细节**的计算机文字编码。  

#### 用途

XML被广泛用来作为**跨平台之间交互数据**（传输数据）的形式，主要**针对数据的内容**（存储数据），通过不同的格式化描述手段（XSLT，CSS等）可以完成最终的形式表达（生成对应的HTML，PDF或者其他的文件格式）。简单来说，就是存储数据的一种格式，e.g. JSON。

#### 结构

这是一个XML例子：
![XML例子](https://image-host-toky.oss-cn-shanghai.aliyuncs.com/20191116030140.png)

主要由以下三部分组成：
1. XML声明
2. DTD（Document Type Definition，文档类型定义）
可以理解为一个专门定义全局变量的区域，在其中可以定义实体（Entity）。
实体根据类型可分为：
- 内置实体 (Built-in entities)
- 字符实体 (Character entities)
- 通用实体 (General entities)
- 参数实体 (Parameter entities)  
根据引用方式可分为：
- 内部引用（格式：```<!ENTITY 实体名称 "实体的值">```）
- 外部引用（格式：```<!ENTITY 实体名称 SYSTEM "URI">```）
注意，这个外部的含义，是相对于这个XML文档来说，只要不是这个文档的，就算外部，而不是特定要其他网络上服务器的

3. 文档元素/正文



### 看懂XML外部实体

![字真难看](https://image-host-toky.oss-cn-shanghai.aliyuncs.com/20191116023747.png)  
注意，图中file://协议，主要就是用于访问本地（相对于服务端）文件的。  
不同的URI：
<!ENTITY 实体名称 "实体的值">

### 举个栗子🌰

![接受XML的一个API](https://image-host-toky.oss-cn-shanghai.aliyuncs.com/20191116032414.png)

对XML内容的处理，使用函数simplexml_load_string()，将**形式良好，符合规范**的XML字符串转换为 SimpleXMLElement对象。问题就出在PHP解析XML使用libxml，而后者在2.9.0版本之前，没有禁止解析XML外部实体内容。

![对XML内容的处理](https://image-host-toky.oss-cn-shanghai.aliyuncs.com/20191116032519.png)

Pikachu XXE练习：[链接](http://119.3.78.82:8089/vul/xxe/xxe_1.php)

### 练习一下

《API调用》：[链接](http://web.jarvisoj.com:9882/)

CTF Blind XXE
