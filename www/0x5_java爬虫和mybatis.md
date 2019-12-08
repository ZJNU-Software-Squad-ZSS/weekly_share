上周学java网络编程学得迷迷糊糊，而本周效率奇低无比，就找了两个爬虫的实例简单看了看

##### MyBatis

MyBatis作为一款持久层框架，支持定制化 SQL、存储过程以及高级映射。MyBatis 避免了几乎所有的 JDBC 代码和手动设置参数以及获取结果集。MyBatis 可以使用简单的 XML 或注解来配置和映射原生类型、接口和 Java 的 POJO（Plain Old Java Objects，普通老式 Java 对象）为数据库中的记录。

其中，XML文件在学习java高级文件处理时有简单接触过，常用于简化数据的存储和共享。

xml声明语句：

```xml
<?xml version="1.0" encoding="UTF-8" ?>
```

官方说明文档与项目配置结构对比：

![](https://i.bmp.ovh/imgs/2019/12/7f045824c2344a9b.png)

进一步研读：

![](https://i.bmp.ovh/imgs/2019/12/462d9925a0b32959.png)



其中，**数据源（dataSource）**：

dataSource 元素使用标准的 JDBC 数据源接口来配置 JDBC 连接对象的资源。

- 许多 MyBatis 的应用程序会按示例中的例子来配置数据源。虽然这是可选的，但为了使用延迟加载，数据源是必须配置的。

有三种内建的数据源类型（也就是 type=”[UNPOOLED|POOLED|JNDI]”）

这里采用的是 pooled（数据池）（其属性包含unpooled的属性，种类更丰富）

其余详见https://mybatis.org/mybatis-3/zh/sqlmap-xml.html#Result_Maps



##### java爬虫

简单看了两个相关的实例

豆瓣热门电影抓取：

https://blog.csdn.net/qwe86314/article/details/91450098

https://github.com/zhoubiao188/douban

某生物网站数据摘取：

https://www.cnblogs.com/qianzf/p/6796588.html

