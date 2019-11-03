# Linux服务器宝塔面板和远程桌面（本地是Windows）

使用实例：CentOS 7.6（阿里云）	本地：Win 10

------

### 宝塔面板安装及后台登陆

------

#### 开放安全组

在ESC实例的安全组配置里开放 **<u>8888</u>** 端口（入方向），如果要使用宝塔面板的全部功能， 888、80、443、20、21，这5个端口也要开放 。

![这是安全组开放示意](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1572765712028&di=3ad84d60c1dde3183cfe0b58eeb3e3bb&imgtype=0&src=http%3A%2F%2Fstatic.oneinstack.com%2Fimages%2Fsecuritygroup%2Fcvm-sg-add.png)

#### 安装宝塔面板

 执行命令：
`yum install -y wget && wget -O install.sh http://download.bt.cn/install/install_6.0.sh && sh install.sh`

然后输入字母“y”，等待程序自行安装

#### ⚠保存宝塔面板后台<u>安全入口</u>、登录名和密码

下载成功后会显示complete之类的单词，后面就是宝塔后台的信息了。

![这是一张下载成功后的截图](https://www.laoyangblog.com/wp-content/uploads/2018/09/20180923232950.png)

记录下随机生成的三条信息。（图片源于网络，并不是最新版本）

⚠在当前最新版的宝塔（2019.10）中Bt-Panel安全入口这一项有变化，访问后台的登陆地址不再是 ：

http://你的服务器IP:8888 

系统在后面随机加上了八个字符，以提高安全性。

#### 登陆后台，选择环境安装

如果没有登陆地址的后八位字符，网页会有如下显示（早期版本除外）

![这是地址错误是网页显示的截图](http://www.mabiji.com/wp-content/uploads/2019/01/btrukou.jpg)

按照提示在终端输入

`/etc/init.d/bt default`

查询入口。

【当前（2019.10）版本的后台在登陆后长时间未操作也会跳出上面的这个显示，其实是入口被网页改成  http://你的服务器IP:8888  了，加上后面的字符串重新登陆就好。】

登陆后台后会有推荐安装环境，也可以自己选择。解析域名、上传站点、创建ftp和数据库都是一键进行，很方便。

#### 其他

宝塔面板后他支持多个并发线程，可以在面板设置里修改，但不建议有超过十人同时访问，如果有多人同时编辑的需要，可以用Linux的SSH密钥来实现。

如果宝塔后台的地址不对还有可能是端口不是8888的问题，可以在SSH输入

`cat /www/server/panel/data/port.pl`

来查询端口。

------

### Win10远程桌面连接CentOS7

远程桌面主要是为了把原本的命令行输入改为图形界面操作，但在有宝塔的情况下远程桌面似乎没有什么意义。连接的方法主要有用VNC和用Windows自己的 mstsc 命令两种，前者需要在本机上安装VNC软件而且不够安全， 因此在linux上配置Xrdp服务器，再使用Windows上具有连线加密功能的远程桌面连接会比较好。 具体的流程直接附教程链接 https://cloud.tencent.com/developer/article/1439820 （记得打开端口）。

​                                                                                                                                                                             2019/11/3