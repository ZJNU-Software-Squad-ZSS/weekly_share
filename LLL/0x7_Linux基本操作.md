# 0x7_Linux基本操作

## 一、Linux 目录结构

Linux 文件系统是树状结构的，系统中每个分区都是一个文件系统，都有自己的目录层次。Linux 会将这些分属不同分区的、单独的文件系统按照树状的方式形成一个系统的总目录层次结构。目录提供了一个管理文件方便而有效的途径， 最上层是根目录，其它所有目录都是从根目录出发而生成的。

Linux 使用标准的目录结构，在安装的时候，安装程序就已经为用户创建了文件系统和完整而固定的目录结构，并指定了每个目录的作用和其中的文件类型。

根目录，一般根目录下只存放目录，不要存放文件，/etc、/bin、/dev、/lib、 /sbin 应该和根目录放置在一个分区中。

1. /bin：存放可执行二进制文件的目录，如常用的命令 ls、tar、mv、cat 等。 通常它与/usr/bin 的内容是一样的。  

2. /boot：放置 linux 系统启动时用到的一些文件。/boot/vmlinuz 为 linux 的内 核文件，以及/boot/gurb。 

3. /dev：存放 linux 系统下的设备文件，访问该目录下某个文件，相当于访 问某个设备，常用的是挂载光驱 mount /dev/cdrom /mnt。  

4. /etc：系统配置文件存放的目录，如 LILO 的参数、用户的账号和密码， 以及系统的主要设置。不建议在此目录下存放可执行文件，重要的配置文件有 /etc/inittab、/etc/fstab、/etc/init.d、/etc/X11、/etc/sysconfig、/etc/xinetd.d 修改配置 文件之前记得备份。（注：/etc/X11 存放与 Windows 有关的设置。）  

5. /home：为用户设置的目录，如用户 user 的主目录就是/home/user，也可 以用~user 表示。  

6. /lib 标准程序设计库，又叫动态链接库，在 Linux 执行或编译内核时均会 用到。系统使用的函数库的目录，程序在执行过程中，需要调用一些额外的参数 时需要函数库的协助，比较重要的目录为/lib/modules。  

7. /lost+fount：系统异常产生错误时，会将一些遗失的片段放置于此目录下， 通常这个目录会自动出现在装置目录下。如加载硬盘于/disk 中，此目录下就会 自动产生目录/disk/lost+found 。 

8. /mnt: /media：光盘默认挂载点，通常光盘挂载于/mnt/cdrom 下，也不一定， 可以选择任意位置进行挂载。  

9. /opt：给主机额外安装软件所摆放的目录。如：FC4 使用的 Fedora 社群开 发软件，如果想要自行安装新的 KDE 桌面软件，可以将该软件安装在该目录下。 以前的 Linux 系统中，习惯放置在 /usr/local 目录下。  

10. /proc：此目录的数据都在内存中，如系统核心，外部设备，网络状态， 由于数据都存放于内存中，所以不占用磁盘空间，比较重要的目录有/proc/cpuinfo、 /proc/interrupts、/proc/dma、/proc/ioports、/proc/net/*等。 
11. /root：系统管理员 root 的家目录，系统第一个启动的分区为/，所以最好 将/root 和/放置在一个分区下。  

12. /sbin:  /usr/sbin:  /usr/local/sbin：放置系统管理员使用的可执行命令， 如 fdisk、shutdown、mount 等。与/bin 不同的是，这几个目录是给系统管理员 root 使用的命令，一般用户只能"查看"而不能设置和使用。  

13. /tmp：一般用户或正在执行的程序临时存放文件的目录，任何人都可以 访问，重要数据不可放置在此目录下。  

14. /srv：服务启动之后需要访问的数据目录，如 www 服务需要访问的网页 数据存放在/srv/www 内。 

15. /usr：应用程序存放目录，/usr/bin 存放应用程序，/usr/share 存放共享数 据，/usr/lib 存放不能直接运行的，却是许多程序运行所必需的一些函数库文件。 /usr/local:存放软件升级包。/usr/share/doc:系统说明文件存放目录。/usr/share/man: 程序说明文件存放目录，使用 man ls 时会查询/usr/share/man/man1/ls.1.gz 的内容。  

16. /var：放置系统执行过程中经常变化的文件，如随时更改的日志文件 /var/log，/var/log/message：所有的登录文件存放目录，/var/spool/mail：邮件存放 的目录，/var/run:程序或服务启动后，其 PID 存放在该目录下。

## 二、Linux 有关目录的命令

1. ls  (显示目录内容） 

命令格式 ls [选项][目录或是文件] 

说明：对于每个目录，该命令将列出其中的所有子目录与文件。对于每个文件，ls 将列出其文件名极强所要求的其它信息。当未给出目录名或是文件名时， 则显示当前目录的信息。该命令类似于 DOS 下的 dir 命令。 

2. cat (显示文件) 

命令格式 cat [选项]文件列表

cat 命令的功能是显示文件内容，也可用于文件的连接。此命令常用来快速浏览文件。如果没有指定文件或连接符号（-），就从标准输入读取。 

​	3. chmod（改变文件或目录的访问权限） 

chomod 命令用来重新设定不同的访问权限，用户用它控制文件或目录的访问权限。该命令有两种方法，一种是包含字母和操作符表达式的文字设定法，另一种是包含数字的数字设定法。

4. cp(文件或目录的复制) 

命令格式 cp [选项] 源文件或目录 目标文件或目录 

5. mv(文件或目录更名或将文件由一个目录移到另一个目录中) 

命令格式 mv [选项] 源文件或目录 目标文件或目录 

说明：根据 mv 命令中第二个参数类型的不同（是目标文件还是目标目录）， mv 命令会将文件重命名或将其移至一个新的目录。当第二个参数类型为文件时， mv 命令完成文件的重命名。此时源文件只能由一个（也可以是原目录名），它将所给的源文件或目录重命名为给定的目标文件名。当第二个参数是已存在的目录 名称时，源文件或目录参数可以有多个，mv 命令将各参数指定的源文件均移至 目标目录中。

​	6.rm（删除文件或目录） 

命令格式 rm [选项] 文件名|目录名  

说明：该命令的功能为删除一个目录中的一个或多个文件或目录，它也可以将某个目录及其下的所有文件及子目录全部删除。

​	7.mkdir(创建目录) 

命令格式 mkdir [选项] dir-name 

说明：该命令创建由 dir-name 命名的目录。要求创建目录的用户在当前目录中（dir-name 的父目录中）具有写权限，并且 dir-name 不能使当前目录中已有 的目录或文件名。 

​	8.rmdir（删除空目录） 

命令格式 rmdir [选项]  dir-name 

说明 dir-name 表示目录名。使用该命令可以从某个目录中删除一个或多个子目录项。需要特别注意的是，一个目录被删除之前必须是空的。rm –r dir 命令可替代 rmdir，但是有危险性。删除某目录时也必须具有对其父目录的写权限。 

9. cd(改变工作目录) 

命令格式 cd [路径] 

说明:该命令将目录改变至 directory 所指定的目录。若没有指定 directory， 则回到用户的主目录。为了改变到指定目录，用户必须拥有对指定目录执行和读 权限。该命令可以使用通配符。 

## 三、Linux 的其它命令 

1. date（显示和设置系统日期和时间） 

命令格式 date [选项] +显示时间格式

2. echo（显示字符串） 

命令格式 echo [-n] 字符串 

说明:选项 n 表示输出文字后不换行；字符串可以加引号，也可以不加引号。 用 echo 命令输出加引号的字符串时，将字符串原样输出；用 echo 命令输出不加 引号的字符串时，将字符串的各个单词作为字符串输出，各字符串之间用一个空 格分隔。

​	3.cal(显示日历) 

命令格式  cal [选项] [月份] [年] 

​	4.clear(清屏) 

命令格式 clear 

说明:清除屏幕上所有内容用法如同 DOS 中的 cls 命令。 

5. kill（向指定进程发送信号） 

命令格式 kill [-signal] 进程号 

说明:kill 命令可以终止后台进程。kill 命令是通过向进程发送指定的信号来 结束进程的。如果没有发送指定型号，那么默认值为 SIGTERM 信号。SIGTERM信号将终止所有不能获该信号的进程号。至于那些可以捕获该信号的进程可能就需要使用 kill -9 信号了，该信号是不能被捕捉的。 

​	6.ps（进程查看命令） 

命令格式 ps [选项] 

说明：该命令可以确定有哪些进程正在运行以及运行的状态、进程是否结束、 哪些进程占用了过多的资源等待。ps 命令用于监控后台进程的工作情况。 

​	7.who（查看当前在线用户的情况） 

命令格式 who 

说明:该命令主要用于查看当前线上用户情况，系统管理员可以用此命令来监视每个登录用户的情况。

8. reboot 命令 

reboot 命令的功能是重新启动系统，用法是： $reboot 

9. passwd（修改用户口令） 

命令格式 passwd [用户名] 

说明:处于系统安全考虑，Linux 系统中的每一个用户除了有其用户名外，还有其对应的用户口令。只有超级用户可以使用“passwd 用户名”修改其它用户的口令，普通用户能用不带参数的 password 修改自己的口令。输入口令时，为了系统的安全，口令不在屏幕上显示。

10. su(改变用户权限) 

命令格式 su {使用者账号} 

说明:它可以让一个普通用户拥有超级用户或其他用户的权限，也可以让超级用户以普通用户的身份做一些事情。普通用户使用这个命令时必须有超级用户或其他用户的口令。如果要离开当前用户的身份，可以输入命令 exit。若没有指定的使用者账号，则系统预设值为超级用户 root。