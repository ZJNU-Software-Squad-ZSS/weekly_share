# Misc - Advertising for Marriage

这是第三届红帽杯的Misc题目：Advertising for Marriage，一道做了挺久，但是还是差一个关键步骤的题目。在做题过程中也学到了新的内存取证的知识，因此以此题作为切入，写下本片WP/学习笔记。

## 题目：

### 题目内容

以下为题目：
<img src="https://image-host-toky.oss-cn-shanghai.aliyuncs.com/20191113004921.png" alt="题目" style="zoom:50%;" />

### 题目下载

某云备份：[q4nw](https://pan.baidu.com/s/19IReJhHKDNa7EC4cjGSpaw)

### ⚠️注意：
这次题目，给我的一个很大教训就是，题目中的信息！Misc作为CTF中的一种题型，它的特点之一就是“脑洞”和“列文虎克”般的观察能力以及对信息的逻辑整合能力。  
题目中的 "Someone want" 其实在题目最后几个步骤中，是一个很重要的提示——确定这个someone是谁，也就是补充完整后面得到的密钥内容（hint，后面会讲到）。  

### ✈️启发：
本题作为一道内存取证题，体现的考察内容，其实不单单与解题的工具、技巧有关，很大程度上也是考察一种通用能力：
<img src="https://image-host-toky.oss-cn-shanghai.aliyuncs.com/20191113005806.png" alt="TK公开课" style="zoom:50%;" />
（来自TK的公开课，[链接](https://www.leiphone.com/news/201704/4qTw6sbX8AlTlbOs.html)）
其中，我们可以看到，对Misc/取证分析题目的信息进行分析的能力（是否为hint？）判断能力（是否重要？）规划能力（解题的总体步骤和阶段性步骤？）搜集能力（哪些地方得到信息？）学习能力（如何获取信息？）提炼能力（信息间如何进行整合？）都是非常重要的，对做题还是其他的学习和生活。  
**努力提高自己的通用能力，能想清楚，能写清楚，能讲清楚，逻辑严密，语句通顺，表达清晰**。“无论以后你想从事什么工作，在学生时代加强这些能力的培养，对你整个人生都会有很大的帮助。”	——TK

## 做题笔记

以下是我做题时的一些笔记，有些并不正确或者对解该题没有帮助，放在这里，记录自己的想法：

1. 查看可能是个Windows磁盘镜像
![可疑文件](https://image-host-toky.oss-cn-shanghai.aliyuncs.com/20191113014150.png)
发现可疑文件，但可能只是用户的头像，注意时间

2. 发现cookies文件
![cookies文件](https://image-host-toky.oss-cn-shanghai.aliyuncs.com/20191113014305.png)

010打开发现全为空00

3. 发现桌面PNG文件
4. Stegsolve打开
![Stegsolve打开](https://image-host-toky.oss-cn-shanghai.aliyuncs.com/20191113014411.png)
眼睛上像不像二维码？？  > https://xz.aliyun.com/t/2788
5. IHDR报错，猜测修改宽高，计算CRC
计算得211，修改IHDR，显示正常
6. 发现IDAT有问题
![IDAT问题](https://image-host-toky.oss-cn-shanghai.aliyuncs.com/20191113014444.png)
7. 扩展：PNG图像隐写
https://3gstudent.github.io/3gstudent.github.io/%E9%9A%90%E5%86%99%E6%8A%80%E5%B7%A7-%E5%88%A9%E7%94%A8PNG%E6%96%87%E4%BB%B6%E6%A0%BC%E5%BC%8F%E9%9A%90%E8%97%8FPayload/
8. 尝试LSB
使用工具https://github.com/livz/cloacked-pixel
9. 去除了IEND后面（82）的00


## 解题过程

### 判断文件/题目类型

首先，拿到题目文件，使用binwalk分析，判断文件类型（输出到txt文件，方便查询信息）
```binwalk xxx.raw > fileInfo.txt```
可以看到其中有很多Microsoft到信息，且文件形式中很类似于磁盘文件，可以初步判断这是一个Windows磁盘镜像，这很有可能是一道内存取证题。
> ⚠️注意：此时，判断好类型题目，就应该在心态上调整过来，这是一道取证分析题目，取证分析 = 取证 + 分析，因此，在做题过程中，核心就是做细致的取证工作，获取充分的信息，以及很重要的逻辑分析、串联、整合、归纳。  

### 查看镜像信息

接下来，确定此为磁盘镜像后，使用内存取证工具```Volatility```**查看镜像信息**（常常含有出题人的hint）：
```volatility imageinfo -f xxx.raw```

//TODO 图：查看镜像信息

从结果中，可以看到，Suggest Profile为WinXPSP2x86，也就是，Volatility对该镜像文件的架构识别为WinXPSP2x86，此后对该镜像的很多操作，都需要指定预设，例如 ``` --profile WinXPSP2x86```。因此，需要将磁盘镜像中的这个关键信息记录下来，以备后面使用。

💡Tips：可以列举该架构可以使用的命令, e.g.
```volatility -f xxx.raw --profile=Win7SP1x64 --help```

### 方式一：使用DiskGenius

使用数据恢复综合软件DiskGenius打开虚拟磁盘——恢复文件，可以直接以GUI的形式看到磁盘镜像的内容。然后需要不断翻阅文件目录，寻找可疑的文件/文件夹（重点看一下桌面）。

// TODO 图·桌面的vegetable.png

发现桌面可疑文件 vegetable.png，PNG图片，恢复可得，根据图片内容猜测为图片隐写。

### 方式二：使用Volatility

使用Volatility可以更加方便于严谨地分析文件的内容。具体的教程可以查看该博客：[链接](https://mengsec.com/2018/10/20/CTF-Volatility/)  
1. 首先，**查看进程：**
```
volatility pslist -f xxx.raw
```
// TODO 图·进程显示
pslist可以用来列出运行的进程。如果Exit所在的一列显示了日期时间，则表明该进程已经结束了。 在图中，我们看到，存在notepad.exe, mspaint.exe，也就是取证对象（出题人）使用过记事本、画图程序。
> 在查看进程的显示时，注意一下记事本程序notepad.exe, 画画工具mspaint.exe以及DumpIt等使用过的软件，这些就是取证对象的操作，其中很有可能有重要信息。因此在逻辑清晰的一个做题过程中，我们需要对取证对象的操作，分别进行纵向地分析，然后回过头来结合起来进行分析。   
>
> Dumpit.exe 一款内存镜像提取工具
> TrueCrypt.exe 一款磁盘加密工具
> Notepad.exe windows自带的记事本
> Mspaint,exe windows自带画图工具

2. **查看notepad.exe**

如果需要查看Notepad程序编辑的内容，需要使用Volatility的Notepad插件：
```
volatility notepad -f xxx.raw 
```
// TODO 图·Notepad中的Hint  
可以看到提示：```hint:????needmoneyandgirlfirend```。  

⚠️注意：在做题过程中，我忽略了hint中的问号????，这个其实是个重要的提示，结合前面题目中的提示 Someone want，可以推测出，这是让我们确定someone的名字，而且这个句子在一个内存取证结合图片隐写（后面会发现）的题目中，很有可能是一个密钥key。

3. **查看mspaint.exe**

接下来，我们查看内存操作中对画图程序操作的内容，使用插件mspaint。
详细教程查看：[《利用volatility与Gimp实现Windows内存取证》](https://segmentfault.com/a/1190000018813033)


把mspaint文件dump下来：
//TODO ```volatility -f xxx.raw --profile=WinXPSP2x86 dumpfiles -Q xxxxxxxx --dump-dir=./```

//TODO 图·mspaint文件dump下来后


4. 扫描所有文件

使用Volatility中的filescan功能：
```
volatility filescan -f xxx.raw
````
// TODO 图·Volatility文件扫描

找到一张 png 图片：vegetable.png



## 其他调查

查看文档
```volatility -f xxx.raw --profile=WinXPSP2x86 filescan | grep "doc\|docx\|rtf"```

查看图片
```volatility -f xxx.raw --profile=WinXPSP2x86 filescan | grep "jpg\|jpeg\|png\|tif\|gif\|bmp"```

查看桌面
```volatility -f xxx.raw --profile=WinXPSP2x86 filescan | grep "Desktop"```

查看命令行输入
```volatility -f xxx.raw --profile=WinXPSP2x86 cmdline```

查看系统用户名
```volatility -f xxx.raw --profile=WinXPSP2x86 printkey -K "SAM\Domains\Account\Users\Names"```

查看网络连接
```volatility -f mem.data --profile=WinXPSP2x86 netscan```




## 小结一下

1. 熟悉使用各类取证分析工具，是快速解题的关键
2. 参透出题人心理，猜测可能的flag位置
3. 对Hint信息仔细观察并进行逻辑串联，不要忽视Hint中的部分信息

## Reference

[1] https://segmentfault.com/a/1190000018813033
[2] https://cloud.tencent.com/developer/article/1527140