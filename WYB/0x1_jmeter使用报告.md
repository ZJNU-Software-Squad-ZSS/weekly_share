# JMeter使用报告

前言：这是一份简单的使用jmeter进行压测实验的报告

 

## 步骤：

使用我上学期java ee的课设进行测试。

现有一个http请求接口http://localhost:8080/Test/Library/HTML/show.jsp，要使用Jmeter对其进行压测，测试步骤如下:

 

**a.新建一个线程组。**

![在这里插入图片描述](https://img-blog.csdn.net/20180921120508682?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lhb3JvbmdrZQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

**b. 设置线程组参数**。这里配置为：10个线程，同时启动，循环一次。

![在这里插入图片描述](https://img-blog.csdn.net/2018092112051715?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lhb3JvbmdrZQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

**c. 新增http请求默认值。** 在上一步创建的线程组上，新增http请求默认值，所有的请求都会使用设置的默认值，这设置协议为`http`，IP为`localhost`，端口为`8080`。

![在这里插入图片描述](https://img-blog.csdn.net/20180921120527812?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lhb3JvbmdrZQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

![在这里插入图片描述](https://img-blog.csdn.net/20180921120539687?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lhb3JvbmdrZQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

**d. 添加要压测的http请求。**

![在这里插入图片描述](https://img-blog.csdn.net/20180921120552903?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lhb3JvbmdrZQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

下图第一个红框内的协议、IP、端口不需要设置，会使用步骤c中设置的默认值，只需设置请求路径`Path`即可，这里填入`/goods/to_list`。

![在这里插入图片描述](https://img-blog.csdn.net/20180921120600481?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lhb3JvbmdrZQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

**e. 新增监听器，用于查看压测结果**。这里添加三种：聚合报告、图形结果、用表格查看结果，区别在于结果展现形式不同。

![在这里插入图片描述](https://img-blog.csdn.net/20180921120606903?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lhb3JvbmdrZQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

**f. 点击运行按钮开始压测，并查看结果。**

![在这里插入图片描述](https://img-blog.csdn.net/20180921120612724?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lhb3JvbmdrZQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

## 1、表格查看结果

参数解释：

Sample：每个请求的序号

Start Time：每个请求开始时间

Thread Name：每个线程的名称

Label：Http请求名称

Sample Time：每个请求所花时间，单位毫秒

Status：请求状态，如果为勾则表示成功，如果为叉表示失败。

Bytes：请求的字节数

Sent Bytes：发送的字节数

Latency：等待时长

Connect time：连接时间

## 2、聚合报告

参数解释：

 

Label：每个 JMeter 的 element（例如 HTTP Request）都有一个 Name 属性，这里显示的就是 Name 属性的值

\#Samples：表示你这次测试中一共发出了多少个请求，如果模拟20个用户，每个用户迭代100次，那么这里显示2000

Average：平均响应时间——默认情况下是单个 Request 的平均响应时间，当使用了 Transaction Controller 时，也可以以Transaction 为单位显示平均响应时间

Median：中位数，也就是 50％ 用户的响应时间

90% Line：90％ 用户的响应时间

Min：最小响应时间

Max：最大响应时间

Error%：本次测试中出现错误的请求的数量/请求的总数

Throughput：吞吐量——默认情况下表示每秒完成的请求数

KB/Sec：每秒从服务器端接收到的数据量



## 3、图形结果

参数解释：

 

No of Samples：发送到服务器的总请求数

Latest Sample：服务器响应最后一个请求的时间值

Throughput：服务器每分钟处理的请求数

Average：总运行时间除以发送到服务器的请求数

Median：有一半的服务器响应时间低于该值而另一半的高于该值

Deviation：服务器响应时间变化、离散程度测量值的大小

