# javaEE入门到放弃：Servlet

![](https://theskyhouse.oss-cn-hangzhou.aliyuncs.com/wallhaven-lq6rmy.png)

------

[TOC]

------

#### 简介

- **Servlet = Server + Applet（Applet，小程序）**（简单来说就是运行在web服务器上的java小程序）

- 使用Servlet可以实现用户交互

- Serrvlet可以动态地生成网页

- 广义的Servlet指实现了Servlet接口的java程序

- **1)Servlet是按照Servlet规范编写的Java类。**

  **2)Servlet应用请求/响应模型，扩展了服务器的功能。**

  **Servlet是WEB应用程序中的一个组件。**

  概括来讲，它用来处理客户端发来的http请求，并返回一个响应。

------

#### 工作过程

1.     在客户端对web服务器发出请求
2.     web服务器接收到请求后将其发送给Servlet
3.     Servlet容器为此产生一个实例对象并调用ServletAPI中相应的方法来对客户端HTTP请求进行处理,然后将处理的响应结果返回给WEB服务器.
4.     web服务器将从Servlet实例对象中收到的响应结构发送回客户端.



在一个应用程序中，每种Servlet类型只能有一个实例。对于每一个应用程序，Servlet容器还会创建一个ServletContext对象（每个应用程序中都只有一个它），这个对象封装了上下文的环境详情。除此之外，每个Servlet对象也都有一个封装Servlet配置的ServletConfig对象。

------

#### Servlet生命周期

1. Servlet第一次被请求，Servlet容器会调用init()方法来初始化Servlet对象，后续不会再调用这个方法（毕竟人不能第二次出生嘛）----调用方法过程中，Servlet容器会传入ServletConfig对象对Servlet对象初始化。
2. 接着容器调用Servlet对象的service()方法进行工作（后续请求中，Servlet容器只会调用service方法了。）
3. 最后，Servlet容器调用destroy()销毁Servlet。

------

#### 接口

Servlet容器对于接受的http请求，将两个参数传给Service()方法---分别是ServletRequest和ServletResponse对象。（都实现了相应的接口）

###### ServletRequest接口

- get Parameter(String val)可以用于获取查询字符串的值，比较常用

###### ServletResponse接口

- 大多时候使用该对象向客户端发送HTML，发送之前，应该调用setContentType（）方法，设置响应的内容类型，将“text/html"作为参数传入，告诉浏览器响应的类型为html，还可以加上”charset=UTF-8“的参数设置响应的编码方式防止乱码。

###### ServletConfig接口

- 初始化Servlet时，容器给Servlet的init()方法传入一个实现此接口的ServletConfig对象。

###### ServletContext对象

- 前面提到过，每个应用程序只有一个此对象。有了这个对象，就可以共享从应用程序访问到的信息，并且可以动态注册Web对象。

###### GenericServlet抽象类 

- 该抽象类实现了Servlet接口和ServletConfig接口，默认实现了Servlet接口的方法，使用的时候只要修改就行，对ServletConfig对象的引用进行处理-----将config参数赋给内部的ServletConfig引用来保存，不用程序员自己维护。（毕竟每次实现Servlet接口定义中的所有方法还是比较麻烦的，即使该方法没有任何东西::>_<::）

- ```java
  public void init(ServletConfig config) throws ServletException {
      this.config = config;
      this.init();
  }
  //这就是保存Config对象，除此之外，GenericServlet抽象类中还有另外一个无参init()方法，它是为了防止别的类继承抽象类过程中方法覆盖，（相当于拿无参方法来做一手替身），导致程序员手动维护ServletConfig对象的问题
  public void init() throws ServletException {
  }
  ```

###### HttpServlet抽象类

- HttpServlet抽象类是由继承GenericServlet抽象类而来的，除此之外，它还需要HttpServletRequest和HttpServletResponse对象。

- HttpServlet中的service方法把接收到的ServletRequsest类型的对象转换成了HttpServletRequest类型的对象。（**Servlet的Service方法时，Servlet容器总会传入一个HttpServletRequest对象和HttpServletResponse对象，预备使用HTTP**，固转换类型没问题）

- 它不用覆盖service()方法，而是覆盖doGet或者doPost方法（比较常用，还有别的5个方法）这是GenericServlet所不具备的。

至于HttpServletRequest和HttpServletResponse接口具体响应的定义则在http协议里面提到过

------

#### 局限

我们在返回数据的时候，Servlet内部输出html语句

举个例子：

1.  response.getWriter().write("<h1>下面是获得的字符串</h1>");
2.  response.getWriter().write("<h1>method(HTTP方法):<h1>");

*

随着网页的发展，一个html可能就有好几千行代码，如果一句一句输出html代码，效率就比较底下。为此，就需要动态网页生成技术，PHP动态语言可以内嵌到html文件中，所以很多程序员转了PHP，sun公司为了解决这个问题，开发了属于自己的动态网页生成技术，也就是JSP，使得可以在HTML文件中内嵌java代码，这也是后话了。

------

