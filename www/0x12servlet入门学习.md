这周都去刷通识网课了，没咋学习

##### servlet applet：运行在服务器端的小程序

动态资源：每个用户访问到的资源不一样

这种逻辑由java来完成

满足某规范（接口 即servlet）的java类，依赖于服务器才能运行

-servlet作为一个接口，定义了java类被浏览器访问到（Tomcat识别的规则）

-在自定义一个类时，实现servlet接口，复写方法。

web.xml配置servlet

```xml
 <!--servlet配置-->
    <servlet>
        <servlet-name>demo</servlet-name>
        <servlet-class>edu.vivien.demo.servlet.MyServlet</servlet-class>
    </servlet>
    <servlet-mapping>
        <servlet-name>demo</servlet-name>
        <url-pattern>/demo</url-pattern>
    </servlet-mapping>
```



翻到上次的javaweb项目里的注释：Date: 2019/9/18Time: 18:46，扪心自问，我上个学期究竟在干嘛。扪心再问，是因为知乎上看到jsp过时硬生生拖着没去再看。。。

REFERENCE

------

https://www.bilibili.com/video/av50351111?p=229

下周一定好好学习系列