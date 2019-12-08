# PHPStudy升级MySQL版本

phpstudy是一个很不错的集成开发环境，提供了很多PHP和Apache、nginx等web服务器各个版本之间的组合。但是，美中不足，phpstudy直至2018版本，其中使用的mysql一直都是5.5版本，而且没有提供设置和升级的地方。很多人都疑惑该如何升级数据库，而且百度搜索中的大部分方法都很复杂而且不是很实用。下面我就把我升级至mysql5.7.18的过程晒出来，跟大家分享。

1.从mysql官网下载windows的免安装版。
最新版下载地址是：[MySQL Community Server](https://dev.mysql.com/downloads/mysql/)
你也可以点击[这里](https://downloads.mysql.com/archives/community/)选择你需要的版本。我选择的是Windows (x86, 64-bit), ZIP Archive

![clipboard.png](https://segmentfault.com/img/bV6KXZ?w=1174&h=65)

2.备份mysq的数据，如果需要的话。

3.重命名phpstudy中的MySQL文件夹为MySQL5.5，相当于备份MySQL，也方便你切回去。

4.将刚下下来的mysql-5.7.18-winx64.zip解压至phpstudy目录中，并重命名为MySQL。

![clipboard.png](https://segmentfault.com/img/bV6KYV?w=385&h=266)

需要说明的是，mysql5.7解压之后，目录中是没有my.ini配置文件和data文件夹的。需要我们自定义一个my.ini文件。我的my.ini很简单，如下：  

注意一定不要写多了，写这么多就够了，我头一次把原来的my.ini copy过来，就出错了。

```
[client]
port=3306
[mysql]
default-character-set=utf8mb4

[mysqld]
port=3306
# 下面两项basedir和datadir根据你的目录来
basedir="D:/phpStudy/MySQL/"
datadir="D:/phpStudy/MySQL/data/"
# 编码和引擎各位就怎么开心怎么来
character-set-server=utf8mb4
default-storage-engine=INNODB

# explicit_defaults_for_timestamp 关闭了 timestamp 类型字段锁拥有的一些会让人感到奇怪的默认行为，加入了该参数之后，如果还需要为 timestamp类型的字段指定默认行为，那么就需要显示的在创建表时显示的指定。没有这一行在初始化的时候会报下面这个警告
# TIMESTAMP with implicit DEFAULT value is deprecated. Please use --explicit_defaults_for_timestamp server option (see documentation for more details).
explicit_defaults_for_timestamp=true
```

我的phpstudy是安装在D盘下的，各位看官根据情况

5.以管理员身份运行命令提示符，进入D:/phpStudy/MySQL/bin，执行mysqld --initialize命令

![clipboard.png](https://segmentfault.com/img/bV6K0j?w=376&h=33)

6.至此，你打开phpstudy就已经可以正常启动mysq了。

![clipboard.png](https://segmentfault.com/img/bV6K0V?w=395&h=324)

不过，mysq的密码已经不是默认的root了。

7.打开MySQL目录下的data文件夹，就是刚刚初始化时候自动生成的data文件夹。里面有个.err的文件，文件名默认是你的计算机名，用sublime text或者记事本等文本编辑器打开。

![clipboard.png](https://segmentfault.com/img/bV6K1C?w=767&h=284)

前几行都是一些正常的警告信息。最后一行是关键，也写的很清楚了，密码就在最后。我的这个就是Ktqa4byL<Z:<。这个密码不能直接使用，比如，用navicat等登录会提示的。

![clipboard.png](https://segmentfault.com/img/bV6K1N?w=724&h=129)

8.修改密码。在命令行登录以后，运行SET PASSWORD=PASSWORD("new_password")修改就可以了。

![clipboard.png](https://segmentfault.com/img/bV6K2u?w=703&h=299)

Enjoy It!