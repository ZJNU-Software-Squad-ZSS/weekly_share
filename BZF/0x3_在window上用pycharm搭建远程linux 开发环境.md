

# 在window上用pycharm搭建linux开发环境

## 方案一： 云服务器+pycharm SSH

### SSH：

 	SSH 为 [Secure Shell](https://baike.baidu.com/item/Secure Shell) 的缩写，由 IETF 的网络小组（Network Working Group）所制定；SSH 为建立在应用层基础上的安全协议。SSH 是较可靠，专为[远程登录](https://baike.baidu.com/item/远程登录/1071998)会话和其他网络服务提供安全性的协议。利用 SSH 协议可以有效防止远程管理过程中的信息泄露问题。SSH最初是UNIX系统上的一个程序，后来又迅速扩展到其他操作平台。SSH在正确使用时可弥补网络中的漏洞。SSH客户端适用于多种平台。几乎所有UNIX平台—包括[HP-UX](https://baike.baidu.com/item/HP-UX)、[Linux](https://baike.baidu.com/item/Linux)、[AIX](https://baike.baidu.com/item/AIX)、[Solaris](https://baike.baidu.com/item/Solaris/3517)、[Digital](https://baike.baidu.com/item/Digital) [UNIX](https://baike.baidu.com/item/UNIX)、[Irix](https://baike.baidu.com/item/Irix)，以及其他平台，都可运行SSH。 

### 步骤：

1. 随便选一个云计算平台，购买一个云服务器

   我这里买了腾讯的学生云服务器

2. 获取服务器的ip、用户名和密码

3. 打开pycharm

   ![image-20191124215822709]( https://user-images.githubusercontent.com/48949693/69496239-0455a500-0f0b-11ea-9baf-8bb811f4302a.png )



4. 输入ip，用户名和密码
   ![image-20191124215946044]( https://user-images.githubusercontent.com/48949693/69496245-0e77a380-0f0b-11ea-8c35-1a4892192e08.png )

5. 打开远程到服务器的terminal

   ![image-20191124220415764]( https://user-images.githubusercontent.com/48949693/69496257-2d763580-0f0b-11ea-845a-f4fabf8c64a7.png )



**这样就可以使用命令行和远程文件管理器操作linux服务器了**

**在开发的时候还可以通过ssh使用服务器上的python解释器**



## 方案二： WSL

## WSL：

 Windows Subsystem for Linux（简称WSL）是一个在Windows 10上能够运行原生Linux二进制可执行文件（ELF格式）的兼容层。它是由[微软](https://baike.baidu.com/item/微软/124767)与Canonical公司合作开发，其目标是使纯正的Ubuntu 14.04 "Trusty Tahr"映像能下载和解压到用户的本地计算机，并且映像内的工具和实用工具能在此子系统上原生运行。 

wsl是在windows上搞linux环境的一个解决方案（别问我为什么不用vm虚拟机，用了就捣鼓不出这篇文章了）

1. 开启windows的子系统服务（如果你要使用wsl2，那还要开启虚拟机服务，wsl2还在测试阶段，我捣鼓了一下午最后还是因为bug多失败了）

2. 在windows store 里随便下载一个linux的发行版（我用的是ubuntu18.04）

3. 然后就可以使用了（是不是很简单？可惜这个wsl是没有linux内核的，如果想用linux内核还得用wsl2，可是wsl2还在测试，过一段时间或许会比较好用起来）

4. wsl和本机在很大程度上是共享文件系统的，所以也很方便，之间用pycharm建项目就行了

   

## 方案三 docker for window的linux镜像

docker for window 比较复杂，需要window专业版。暂时还没有研究，先占个坑。



## 以上就是我暂时能想到的在windows 上搞linux的办法（别问为什么不用虚拟机，问就是不想）
