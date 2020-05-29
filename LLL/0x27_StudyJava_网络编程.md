# StudyJava——网络编程

网络编程是指编写运行在多个设备（计算机）的程序，这些设备都通过网络连接起来。

`java.net` 包中 J2SE 的 API 包含有类和接口，它们提供低层次的通信细节。

### Socket简介

> Socket = IP +端口号

建立网络通信连接至少要一对端口号 (socket)。socket 本质是编程接口 (API)，对 TCP/IP 的封装，TCP/IP 也要提供可供程序员做网络开发所用的接口，这就是 Socket 编程接口；HTTP 是轿车，提供了封装或者显示数据的具体形式；Socket 是发动机，提供了网络通信的能力。

在 Internet 上的主机一般运行了多个服务软件，同时提供几种服务。每种服务都打开一个 Socket，并绑定到一个端口上，不同的端口对应于不同的服务。

### TCP

一种面向连接的、可靠的、基于字节流的传输层通信协议。（三次握手）

应用层向 TCP 层发送用于网间传输的、用 8 位字节表示的数据流，然后 TCP 把数据流分区成适当长度的报文段（通常受该计算机连接的网络的数据链路层的最大传输单元（MTU）的限制）。之后 TCP 把结果包传给 IP 层，由它来通过网络将包传送给接收端实体的 TCP 层。TCP 为了保证不发生丢包，就给每个包一个序号，同时序号也保证了传送到接收端实体的包的按序接收。然后接收端实体对已成功收到的包发回一个相应的确认（ACK）；如果发送端实体在合理的往返时延（RTT）内未收到确认，那么对应的数据包就被假设为已丢失将会被进行重传。TCP 用一个校验和函数来检验数据是否有错误；在发送和接收时都要计算校验和。

### UDP

UDP 协议全称是用户数据报协议，在网络中它与 TCP 协议一样用于处理数据包，是一种无连接的协议。

UDP 有不提供数据包分组、组装和不能对数据包进行排序的缺点，也就是说，当报文发送之后，是无法得知其是否安全完整到达的。UDP 用来支持那些需要在计算机之间传输数据的网络应用。

UDP 协议的主要作用是将网络数据流量压缩成数据包的形式。

### HttpURLConnection

HttpURLConnection 位于 java.net 包中，支持 HTTP 特定功能。我们可以使用它来发起网络请求，获取服务器的相关资源。（[API 文档](https://docs.oracle.com/javase/8/docs/api/java/net/HttpURLConnection.html)）

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class HttpUrlTest {
    public static void main(String[] args) {
        try {
            //设置url
            URL shiyanlou = new URL("https://www.shiyanlou.com");
            //打开连接
            HttpURLConnection urlConnection = (HttpURLConnection)shiyanlou.openConnection();
            //设置请求方法
            urlConnection.setRequestMethod("GET");
            //设置连接超时时间
            urlConnection.setConnectTimeout(1000);
            //获取输入流
            InputStream inputStream = urlConnection.getInputStream();
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream));
            //打印结果
            bufferedReader.lines().forEach(System.out::println);
            //关闭连接
            inputStream.close();
            bufferedReader.close();
            urlConnection.disconnect();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

```
`$ javac HttpUrlTest.java
$` java HttpUrlTest
<!DOCTYPE html>
<html lang="zh-CN">
.....内容过长省略.....
    </body>
</html>
```

### InetAddress 类

`InetAddress`类用于表示 IP 地址

`InetAddress`没有公共构造方法，我们只能使用它提供的静态方法来构建一个 `InetAddress` 类实例

- `getLocalHost()`： 返回本地主机地址
- `getAllByName（String host）`：从指定的主机名返回 InetAddress 对象的数组，因为主机名可以与多个 IP 地址相关联。
- `getByAddress（byte [] addr）`：从原始 IP 地址的字节数组中返回一个 InetAddress 对象。
- `getByName（String host）`：根据提供的主机名创建一个 InetAddress 对象。
- `getHostAddress()`：返回文本表示的 IP 地址字符串。
- `getHostname()`：获取主机名。

```java
import java.net.InetAddress;
import java.net.UnknownHostException;

public class InetAddressDemo {
    public static void main(String[] args) {
        try {
            InetAddress shiyanlou = InetAddress.getByName("www.shiyanlou.com");
            //toString 方法将输出主机名和ip地址
            System.out.println(shiyanlou.toString());
            //获取ip地址
            String ip = shiyanlou.toString().split("/")[1];
            //根据IP地址获取主机名
            InetAddress byAddress = InetAddress.getByName(ip);
            System.out.println("get hostname by IP address:" + byAddress.getHostName());
            System.out.println("localhost: "+InetAddress.getLocalHost());
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
    }
}
```

```java
www.shiyanlou.com/115.29.233.149
get hostname by IP address:www.shiyanlou.com
localhost: user-441493.weave.local/192.168.42.16
```

### Socket

`Socket存在于服务端和客户端，用于客户端与服务端的通信连接。`

`Socket` 类代表一个**客户端**套接字，可以使用该类向服务器发送和接受数据。一般需要通过下面几个步骤：

1. 建立与服务器的连接；
2. 使用输出流将数据发送到服务器；
3. 使用输入流读取服务器返回的数据；
4. 关闭连接。

Socket 常用构造方法：

- `Socket(InetAddress address, int port)`：创建一个套接字，连接到指定 IP 地址和端口的服务器
- `Socket(String host, int port)`：创建一个套接字，连接到指定的主机名和端口的服务器
- `Socket(InetAddress address, int port, InetAddress localAddr, int localPort)`：创建一个套接字连接到指定的 IP 地址和端口的服务器，并且显示的指定客户端地址和端口。

在创建 Socket 时，需要捕获异常。

**getOutputStream()**

该方法可以获取输出流，在建立连接后，可以使用该方法获取输出流，发送数据到服务器。发送数据的方式和使用 IO 流是相同的，使用 write 方法发送指定的数据即可。

**getInputStream()**

用户获取输入流，通过该方法获取输入流之后可以读取服务器发送来的数据。使用方法和 IO 流相同，使用 read 方法即可。

**close()**

关闭 Socket，可能抛出 IO 异常，所以我们同样需要捕获异常。

### ServerSocket

`ServerSocket`是与 Socket 类相对应的用于表示通信双方中的服务器端，用于在服务器上开一个端口，被动地等待数据（使用 accept() 方法）并建立连接进行数据交互。

创建一个 `ServerSocket` 一般需要以下几个步骤：

1. 创建服务器套接字并将其绑定到特定的接口
2. 等待客户端连接
3. 通过客户端套接字获取输入流，从客户端读取数据
4. 通过客户端套接字获取输出流，发送数据到客户端
5. 关闭套接字

常见构造方法：

- `ServerSocket()`：创建一个未绑定端口的服务器套接字。
- `ServerSocket(int port)`：创建绑定到指定端口号的服务器套接字。
- `ServerSocket(int port,int backlog)`：创建一个绑定到指定端口号的服务器套接字，并且`backlog` 参数指定了最大排队连接数。
- `ServerSocket(int port,int backlog,InetAddress bindAddr)`：创建服务器套接字并将其绑定到指定的端口号和本地 IP 地址。

**accept()**

用于监听客户端连接请求，当调用该方法时，会阻塞当前线程，直到有客户端发起请求与其建立连接，否则将一直等待。当连接成功后，将返回一个 `Socket` 对象。

> listen函数接收客户端的连接请求， accept仅仅是把建立好连接的socket从就绪队列拿出一个返回而已，当然了如果就绪队列为空（没有就绪连接） 则会阻塞

**close()**

用于关闭服务器套接字，服务器停止后，将断开所有连接。

**其他方法**（可以查阅[官方文档](https://docs.oracle.com/javase/8/docs/api/java/net/ServerSocket.html)。）

> 假设一共有3个客户端连接到服务器端。那么在服务器端就一共有4个套接字：第1个是socket()返回的、用于监听的套接字；其余3个是分别调用3次accept()返回的不同的套接字
>

***个人理解 Socket与 ServerSocket：每一次网络连接都需要有客户端与服务端的套接字，即是成对出现的。ServerSocket 一般仅用于设置端口号和监听，真正进行通信的是服务器端的 Socket与客户端的 Socket，在 ServerSocket 进行 accept之后，就将主动权转让了。***

***在客户端的网络编程里，建立的 Socket对象是客户端的，他后面带的参数表示这个 Socket是指向这个 ”IP+端口 “的服务器，即在客户端建立一个客户端的套接字去连接服务端，那么 getInputStream()和 getOutputStream()就是以客户端为中心，获得输入流（服务端发来的信息）和获得输出流（从客户端发送信息给服务端）。***

***在服务端的网络编程里，先建立一个 ServerSocket对象，他是属于服务端的，他后面的端口号参数用来指定服务器向客户端开放的端口号，同时服务端有一个特殊的 Socket是用来监听的，当服务端口使用 accept()方法时，表示服务端在等待客户端连接，连接成功后，将返回一个新的客户端的 Socket对象，该 Socket对象绑定了客户端的 IP地址或端口号，表示这个套接字是用来连接客户端的，那么此时的 getInputStream()和 getOutputStream()就是以服务端为中心，获得输入流（客户端发来的信息）和获得输出流（从服务端发送信息给客户端）。***

***交互过程：***

1. ***服务器端创建一个 ServerSocket（服务器端套接字），调用 accept() 方法等待客户端来连接。***
2. ***客户端程序创建一个 Socket，请求与服务器建立连接。***
3. ***服务器接收客户的连接请求，同时创建一个新的 Socket 与客户建立连接，服务器继续等待新的请求。***

**【一个简单的 Socket 应用，实现客户端发送信息给服务端，服务端再将信息发送回客户端的回显的功能。】**

【服务端】

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;


public class EchoServer {
    public static void main(String[] args) {
        try {
            //服务端需要使用ServerSocket类
            ServerSocket serverSocket = new ServerSocket(1080);
            //阻塞 等待客户端连接
            Socket client = serverSocket.accept();
            // reader和writer可以直接读取字节流？？？可能getInputStream没指是字节流？
            PrintWriter out = new PrintWriter(client.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
            String userIn;
            while ((userIn = in.readLine()) != null) {
                System.out.println("收到客户端消息：" + userIn);
                //发回客户端
                out.println(userIn);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

【客户端】

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class EchoClient {
    public static void main(String[] args) {
        String hostname = "127.0.0.1";
        //socket端口
        int port = 1080;
        Scanner userIn = new Scanner(System.in);
        try {
            //建立socket连接
            Socket socket = new Socket(hostname, port);
            //获取socket输出流
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            //获取输入流
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String userInput;
            System.out.println("请输入信息：");
            //当用户输入exit时退出
            while (!"exit".equals(userInput = userIn.nextLine())) {
                out.println(userInput);
                System.out.println("收到服务端回应:" + in.readLine());
            }
            //关闭socket
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

编译运行：

打开两个 terminal，一个运行服务端，一个运行客户端。

首先启动服务端，不能先启动客户端，否则报错。

服务端启动命令：

```bash
`$ javac EchoServer.java
$` java EchoServer
```

接着切换到客户端 terminal。客户端启动命令

```bash
`$ javac EchoClient.java
$` java EchoClient
```

运行结果：

- 客户端

```
请输入信息：
shi
收到服务端回应:shi
yan
收到服务端回应:yan
lou
收到服务端回应:lou
exit
```

- 服务端

```
收到客户端消息：shi
收到客户端消息：yan
收到客户端消息：lou
```



**【多线程服务器】**

- Server 可以同时接受多个客户端的连接
- 每个线程负责一个连接
- 客户端发送消息给服务端，服务端再将客户端发送的消息发回客户端

【client】

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        String hostname = "127.0.0.1";
        //socket端口
        int port = 1080;
        Scanner userIn = new Scanner(System.in);
        try {
            //建立socket连接
            Socket socket = new Socket(hostname, port);
            //获取socket输出流
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            //获取输入流
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String userInput;
            System.out.println("请输入信息：");
            //当用户输入exit时退出
            while (!"exit".equals(userInput = userIn.nextLine())) {
                out.println(userInput);
                System.out.println("收到服务端回应:" + in.readLine());
            }
            //关闭socket
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

【server】

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;


public class Server {
    public static void main(String[] args) {
        try {
            //服务端需要使用ServerSocket类
            ServerSocket serverSocket = new ServerSocket(1080);
            //阻塞 等待客户端连接
            while (true) {
                Thread thread = new Thread(new ServerThread(serverSocket.accept()));
                thread.start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static class ServerThread implements Runnable {
        Socket client;

        public ServerThread(Socket client) {
            this.client = client;
        }

        @Override
        public void run() {
            try {
                PrintWriter out = new PrintWriter(client.getOutputStream(), true);
                BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
                String userIn;
                while ((userIn = in.readLine()) != null) {
                    System.out.println("收到客户端消息：" + userIn);
                    //发回客户端
                    out.println(userIn);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
```

> 有关线程的详细内容请看0x28_StudyJava_多线程.md

