# JSP（Java Server Pages）

![](https://theskyhouse.oss-cn-hangzhou.aliyuncs.com/mirror6.png)

------

[TOC]

------

#### 简介

- JSP是javaWeb服务器端动态资源，与html页面作用相同（获取数据、显示数据）
- jsp的组成：
  - jsp=html+java脚本+jsp标签（指令）
  - jsp中有9大内置对象

###### jsp和servlet区别和联系

1. jsp经编译后就变成servlet（Servlet中已经提到过JSP的本质就是Servlet，JVM不能识别JSP的代码只能识别java的类）
2. JSP比较擅长的是页面显示（视图），而Servlet更擅长逻辑控制
3. Servlet没有内置对象，jsp有9大内置对象（使用jsp只要完成程序员输出到客户端的内容，至于java脚本如何嵌入到一个类由jsp容器完成）
4. JSP是Servlet技术的扩展，最主要的不同在于：Servlet的应用逻辑在java文件中，完全和表示层的HTML分离。而JSP则是java和html组合成.jsp的文件。

------

#### jsp原理

1. 当jsp页面第一次被访问时，服务器把jsp编译成java文件
2. 把java编译成class
3. 创建该类对象
4. 调用对象service()方法
5. **第二次请求同一jsp时，直接调用service()方法**

------

#### 三大指令

###### page

**<%@page language=”java” ……%>**

```
1.pageEncoding和contentType：
pageEncoding=”utf-8” –--告诉服务器使用什么编码翻译jsp文件（成java文件）（可以解决乱码问题）
contentType=”text/html; charset=utf-8” 服务器发送浏览器的数据类型和内容编码
2.import：导包，这个没啥好说
3.errorPage和isErrorPage
errorPage：当前页面如果抛出异常，那么要转发到哪一个页面，由errorPage来指定
isErrorPage：它指定当前页面是否为处理错误的页面！当该属性为true时，这个页面会设置状态码为500！而且这个页面可以使用9大内置对象中的exception!

<error-page>
    <error-code>404</error-code>（指定响应码）
    <location>/error/errorPage.jsp</location>（跳转页面）
</error-page>
<error-page>
    <exception-type>java.lang.RuntimeException</exception-type>（指定抛出异常）
    <location>/index.jsp</location>
</error-page>

还有一些了解即可：
autoFlush：指定jsp的输出流缓冲区满时，是否自动刷新！默认为true，如果为false，那么在缓冲区满时抛出异常！
buffer：指定缓冲区大小，默认为8kb
info:信息
session：当前是否支持session
```

###### include--静态包含

<%@include file="xw.jsp"%>

①原理是把被包含的页面（xw.jsp）的内容翻译到包含页面（index.jsp）中，合并翻译成一个JAVA源文件，再编译运行，这种包含叫做静态包含（源码包含）
②如果使用静态包含，被包含页面中不需要再出现全局的HTML标签（如：html、head、body）

###### taglib –-导入标签库

<%@taglib prefix=”xw”  uri=”jsp/hhh.com” %> 

prefix：指定标签库在本页面中的前缀，由我们自己来起名称
uri: 指定标签库的位置(后续了解自定义标签后可能会用到)

------

#### 九大内置对象

内置对象，也叫隐含对象，不需要预先声明就可以在表达式中随意使用。

|  内置对象   |    对象名称    |              类型              |     作用域      |
| :---------: | :------------: | :----------------------------: | :-------------: |
|   request   |    请求对象    |  javax.servlet.ServletRequest  |   **Request**   |
|  response   |    响应对象    |  javax.servlet.SrvletResponse  |      Page       |
|     out     |    输出对象    |  javax.servlet.jsp.JspWriter   |      Page       |
|   config    |    配置对象    |  javax.servlet.ServletConfig   |      Page       |
|    page     |    页面对象    |     **javax.lang.Object**      |      Page       |
|  exception  |    里外对象    |    **javax.lang.Throwable**    |      Page       |
| pageContext | 页面上下文对象 | javax.servlet.jsp.PageContext  |      Page       |
|   session   |    会话对象    | javax.servlet.http.HttpSession |   **Session**   |
| application |  应用程序对象  |  javax.servlet.ServletContext  | **Application** |

除了请求对象、session会话对象，应用程序对象，其他作用域都为Page

------

