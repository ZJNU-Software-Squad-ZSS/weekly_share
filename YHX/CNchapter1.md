[TOC]



# 第一章

1. 互联网边缘和核心部分的作用，分组交换的概念。
2. 计算机网络的性能指标。
3. 计算机网络分层次的体系结构。

21世纪重要特征：数字化、网络画和信息化，以网络为核心。

三大网络：电信网络、有线电视网络和计算机网络（发展最快，起核心作用）。

三网融合

互连网 internet <互联网=Internet

互联网基本特点：连通性、共享。



## 网络的网络

若干结点和连接这些结点的链路组成——计算机网络。

网络可由路由器互连——互连网，网络的网络。

> 结点：计算机、集线器、交换机、路由器等。



## 互连网基础结构发展的三个阶段

### 第一个阶段

单个网络ARPANET—>互连网。

1983年TCP/IP协议成为ARPANET上的标准协议——互联网的诞生时间。

### 第二个阶段

建成了三级结构的互联网，分为主干网、地区网和校园网（企业网）。

### 第三个阶段

形成多层次ISP结构的互联网。

ISP可以从互联网管理机构申请到很多IP地址，同时拥有通信线路以及路由器等连网设备。主干ISP10Gbit/s或更高，地区ISP，本地ISP。

IXP允许两个网络直接相连并交换分组，不需要通过第三个网络来转发分组。



## 互联网的标准化工作

互联网协会ISOC>互联网体系结构委员会IAB>互联网工程部IETF>WG

​																				>互联网研究部IRTF>FG

互联网草案——建议标准（RFC）——互联网标准



## 互联网的组成

互联网拓扑结构：边缘部分，核心部分。

### 边缘部分

用户直接使用通信和资源共享。

端系统通信方式：

C/S，服务请求方和提供方都要使用网络核心部分所提供的服务。

P2P

### 核心部分

为边缘部分提供服务。

特殊作用路由器，实现分组交换的关键构件，转发收到的分组。

电路交换：建立连接——通话——释放连接。在通话的全部时间内，通话的两个用户始终占用端到端的通信资源。线路传输效率低。

分组交换：采用存储转发，把一个报文划分为几个分组后再进行传送。

​		报文：要发送的整块数据。

​		一个分组（包）：一个为1024bit的数据段+首部（包头）。

分组交换的优点：

高效——在分组传输过程中动态分配传输宽带，对通信链路是逐段占用。

灵活——为每个分组独立选择做合适的转发路由。

迅速——以分组作为传送单位，可以不先建立连接就能向其他主机发送分组。

可靠——保证可靠性的网络协议；分布式多路由的分组交换网，是网络有很好的生存性。

缺点：

分组在各路由器存储转发时需要排队，造成时延。

各分组必须携带的控制信息造成开销。



## 计算机网络类别

作用范围：广域网WAN、城域网MAN、局域网LAN、个人区域网PAN

使用者：公用网、专用网

用户接入：接入网（本地接入网、居民接入网）



## 计算机网络的性能

速率bit/s	b/s	bps 额定速率、标称速率

带宽：信号具有的频带宽度；某通道传送数据的能力，单位时间内网络中某信道所能通过的最高数据率。bit/s

吞吐量：单位时间内通过某个网络（信道、接口）的实际数据量。

时延：

​		发送时延：数据帧长度/发送速率

​		传播时延：信道长度/电磁波在信道上的传播速率

​		处理时延

​		排队时延

​		总时延：以上四个相加

时延带宽积：传播时延*带宽

往返时间RTT

利用率

非性能特征：费用、质量、标准化、可靠性、可拓展性和可升级性、易于管理和维护。







