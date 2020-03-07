# Spring_v1

![](https://theskyhouse.oss-cn-hangzhou.aliyuncs.com/wallhaven-wy3wj6.jpg)

------

[TOC]

------

#### 简介

spring是J2EE应用程序框架，**是轻量级的控制反转（IOC)和面向切面(AOP)的容器框架，主要是针对javaBean的生命周期进行管理的轻量级容器**，可以单独使用，也可以和Struts框架，ibatis框架等组合使用。

###### 优点

- 简化开发（专业来说事高内聚低耦合）

  Spring就是一个容器，可以将对象创建和依赖关系维护交给spring来管理，它用于生产Bean

- 支持AOP编程

  提供面向切面编程，可以实现对程序进行权限拦截、运行监控。

- 降低javaEE API的使用难度

- 方便程序测试（支持Junit，可以通过注解测试）

- 方便集成各种框架（支持Struts、Hibernate、MyBatis）

###### 名词介绍

IoC：控制反转。有一个类，我们想要调用类里面的方法（非静态方法），按我们以前的思维来做，就是创建该类的一个实例对象，用这个对象再调用方法。但对于Spring而言，创建对象的过程，不是在代码里面实现，而是让它来配置实现。

AOP:面向切面编程。通俗来说，**就是在运行时，动态地将代码切入到类的指定方法、指定位置上的编程思想就是面向切面的编程，**具体运用到权限拦截后面再提。

------

### Spring的IoC的底层实现

Spring的IoC的底层实现原理是**工厂设计模式+反射+XML配置文件。**

这边直接以dao层开发为例（data access object，数据访问对象）

```java
//先创建一个接口
public interface UserDao {
	public void add();
}
//然后创建接口实现类
public class UserDaoImpl implements UserDao {
    public void add() {
	    balabala......
    }
}
//最后在service层调用dao层
/* 接口 实例变量 = new 实现类
这一步也叫接口回调，这样接口变量dao就可以调用被类实现接口中的方法，不同的类在实现统一接口时会产生不同的功能体现
*/
UserDao dao = new UserDaoImpl();
dao.add();

/*从上面我们可以看到，dao层和service层耦合度很高，接口和实现类耦合度高（联系密切），一旦我们切换掉底层的实现类UserDaoImpl，我们就需要修改源代码。好的程序设计应当遵循OCP原则（开闭原则），尽量不改动源代码的基础上对程序扩展。*/
---------------------------------------------------------------------------------
//为了解决这个问题，工厂设计模式是一个很棒的选择，我们不妨来创建一个工厂类，提供方法，返回对象
public class BeanFactory {
    // 提供返回实现类对象的方法
    public static UserDao getUserDao() {
        return new UserDaoImpl();
    }
}
//service层中调用dao层的代码也更改
UserDao dao = BeanFactory.getUserDao();
dao.add();

/*不难看出，虽然接口和实现类没有耦合了，service层和工厂类耦合。这个时候，就可以引出工厂设计模式+反射+XML配置文件*/
------------------------------------------------------------------------------------
//配置XML文件    
<bean id="userDao" class="com.meimeixia.dao.impl.UserDaoImpl" />   
 
//创建工厂类，但是不直接返回new的实现类了，而是使用SAX解析配置文件，根据bean中的id属性得到相应的class属性值，使用反射来创建实现类对象！（瞬间高大上了好多）
public class BeanFactory {
    public static Object getBean(String id) {
        // 使用SAX解析得到配置文件内容，根据id值userDao得到class属性值
        String classvalue = "class属性值";
        // 使用反射得到对象
        Class clazz = Class.forName(classvalue);
        UserDaoImpl userDaoImpl = (UserDaoImpl)lazz.newInstance();
        return userDaoImpl;
    }
}

```

------

