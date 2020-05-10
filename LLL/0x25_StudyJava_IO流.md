# StudyJava——IO流

## IO Stream（输入输出流）

数据流（Data Stream）：一个 Java I/O 对象。读取数据到内存的对象叫做输入流，内存写出数据的对象叫做输出流。

- 根据方向（以内存为参考）：输入流、输出流
- 根据数据单位：**字节流、字符流**
- 功能：节点流`（从特定的数据节点（文件、数据库、内存等）读写数据）`、处理流`（连接在已有的流上，通过对数据的处理为程序提供更多功能）`

![img](https://doc.shiyanlou.com/document-uid85931labid1097timestamp1436413740400.png)

> 蓝色：抽象类；绿色：派生类

![](https://doc.shiyanlou.com/document-uid85931labid1097timestamp1436412496895.png)

### 字节流

> 以字节为单位从 stream 中读取或往 stream 中写入信息。通常用来读取二进制数据。

**字节流能处理所有类型的数据（如图片、avi等）**

#### InputStream

抽象类，继承它的子类要重新定义其所定义的抽象方法。如System中的in对象就是实例。

| 方法                                  | 说明                                                     |
| ------------------------------------- | -------------------------------------------------------- |
| read()throws IOException              | 从输入流中读取数据的下一个字节（抽象方法）               |
| skip(long n) throws IOException       | 跳过和丢弃此输入流中数据的 n 个字节                      |
| available()throws IOException         | 返回流中可用字节数                                       |
| mark(int readlimit)throws IOException | 在此输入流中标记当前的位置                               |
| reset()throws IOException             | 将此流重新定位到最后一次对此输入流调用 mark 方法时的位置 |
| markSupport()throws IOException       | 测试此输入流是否支持 mark 和 reset 方法                  |
| close()throws IOException             | 关闭流                                                   |

在 InputStream 类中，方法 `read()` 提供了三种从流中读数据的方法：

1. `int read()`：从输入流中读一个字节，形成一个 0~255 之间的整数返回（是一个抽象方法）
2. `int read(byte b[])`：从输入流中读取一定数量的字节，并将其存储在缓冲区数组 `b` 中，**返回值为读取的字节长度。**
3. `int read(byte b[],int off,int len)`：从输入流中读取长度为 `len` 的数据，写入数组 `b` 中从索引 `off` 开始的位置，并返回读取得字节数。

对于这三个方法，若返回 -1，表明流结束，否则，返回实际读取的字符数。

#### OutputStream

抽象类，继承它的子类要重新定义其所定义的抽象方法。如System中的out对象类型是java.io.PrintStream，这个类是其子类。

| 方法                                                | 说明                                                         |
| --------------------------------------------------- | ------------------------------------------------------------ |
| write(int b)throws IOException                      | 将指定的字节写入此输出流（抽象方法）                         |
| write(byte b[])throws IOException                   | 将字节数组中的数据输出到流中                                 |
| write(byte b[], int off, int len)throws IOException | 将指定 byte 数组中从偏移量 off 开始的 len 个字节写入此输出流 |
| flush()throws IOException                           | 刷新此输出流并强制写出所有缓冲的输出字节                     |
| close()throws IOException                           | 关闭流                                                       |

```java
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

public class Test {

    /**
     * 把输入流中的所有内容赋值到输出流中
     * @param in
     * @param out
     * @throws IOException
     */
    public void copy(InputStream in, OutputStream out) throws IOException {
        byte[] buf = new  byte[4096];
        int len = in.read(buf);
        //read 是一个字节一个字节地读，字节流的结尾标志是-1
        // 循环输入输出
        while (len != -1){
            //len表示读取字节的长度，包括最后的结尾换行
            System.out.println(len);
            out.write(buf, 0, len);
            len = in.read(buf);
        }
    }
    public static void main(String[] args) throws IOException {
        // TODO Auto-generated method stub
        Test t = new Test();
        System.out.println("输入字符：");
        t.copy(System.in, System.out);
    }

}
```

```
输入字符：
abc
4
abc
x
2
x
```

### 字符流

> 以 Unicode 字符为单位从 stream 中读取或往 stream 中写入信息。

**字符流以字符为单位，根据码表映射字符，一次可能读多个字节，只能处理字符类型的数据**

#### Reader

抽象类，只提供了一系列用于字符流处理的接口。它们的方法与类 InputStream 类似，只不过其中的参数换成字符或字符数组。

| 方法                               | 返回值  |
| ---------------------------------- | ------- |
| close()                            | void    |
| mark (int readAheadLimit)          | void    |
| markSupported()                    | boolean |
| read()                             | int     |
| read(char[] cbuf, int off,int len) | int     |
| ready()                            | boolean |
| reset()                            | void    |
| skip(long n)                       | long    |

#### Writer

抽象类，只提供了一系列用于字符流处理的接口。它们的方法与类 OutputStream 类似，只不过其中的参数换成字符或字符数组。

| 方法                                | 返回值 |
| ----------------------------------- | ------ |
| close()                             | void   |
| flush()                             | void   |
| write(char[] cbuf)                  | void   |
| write(char[] cbuf, int off,int len) | void   |
| write(int c)                        | void   |
| write(String str)                   | void   |
| write(String str, int off, int len) | void   |

在这里我们就列举一下有哪些类。

1. 对字符数组进行处理： CharArrayReader、CharArrayWrite。
2. 对文本文件进行处理：FileReader、FileWriter。
3. 对字符串进行处理：StringReader、StringWriter。
4. 过滤字符流：FilterReader、FileterWriter。
5. 管道字符流：PipedReader、PipedWriter。
6. 行处理字符流：LineNumberReader。
7. 打印字符流：PrintWriter。

### 转换流

InputStreamReader 和 OutputStreamWriter 是 `java.io` 包中用于处理字符流的最基本的类，用来在字节流和字符流之间作为中介。

> 输入字节流→转换为字符→（...）→按编码规范转换为字节→输出字节流

使用这两者进行字符处理时，在构造方法中应指定一定的**平台规范**，以便把以字节方式表示的流转换为特定平台上的字符表示。

```java
InputStreamReader(InputStream in); //缺省规范说明
InputStreamReader(InputStream in, String enc);	//指定规范 enc

OutputStreamWriter(OutputStream out); //缺省规范说明
OutputStreamWriter(OutputStream out, String enc);	//指定规范 enc
```

统一的编码规范“ISO 8859_1”，这是一种映射到 ASCCII 码的编码方式，能够在**不同平台**之间正确转换字符。

```java
InputStreamReader ir = new InputStreamReader(is,"8859_1");
```

### 缓冲流

类 BufferedInputStream 和 BufferedOutputStream 实现了带缓冲的过滤流，它提供了缓冲机制，把任意的 I/O 流“捆绑”到缓冲流上，可以提高 I/O 流的读取效率。

在初始化时，除了要指定所连接的 I/O 流之外，还可以指定缓冲区的大小。缺省时是用 32 字节大小的缓冲区；最优的缓冲区大小常依赖于主机操作系统、可使用的内存空间以及机器的配置等；一般缓冲区的大小为内存页或磁盘块等的整数倍。

BufferedInputStream 的数据成员 `buf` 是一个位数组，默认为 2048 字节。当读取数据来源时例如文件，BufferedInputStream 会尽量将 `buf` 填满。当使用 `read()` 方法时，实际上是先读取 `buf` 中的数据，而不是直接对数据来源作读取。当 buf 中的数据不足时，BufferedInputStream 才会再实现给定的 InputStream 对象的 `read()` 方法，从指定的装置中提取数据。

BufferedOutputStream 的数据成员 `buf` 是一个位数组，默认为 512 字节。当使用 `write()` 方法写入数据时，实际上会先将数据写至 `buf` 中，当 `buf` 已满时才会实现给定的 OutputStream 对象的 `write()` 方法，将 `buf` 数据写至目的地，而不是每次都对目的地作写入的动作。

> 输入字节流→缓冲流→read()→（...）→write()→缓冲流→输出字节流

```java
//构造方法
//[ ]里的内容代表可选参数
BufferedInputStream(InputStream in [, int size])
BufferedOutputStream(OutputStream out [, int size])
```

```java
FileInputStream in = new FileInputStream("file.txt");
FileOutputStream out = new FileOutputStream("file2.txt");

//设置输入缓冲区大小为256字节
BufferedInputStream bin = new BufferedInputStream(in,256)
BufferedOutputStream bout = new BufferedOutputStream(out,256)

int len;
byte bArray[] = new byte[256];
len = bin.read(bArray); //len 中得到的是实际读取的长度，bArray 中得到的是数据
```

> 对于 BufferedOutputStream，只有缓冲区满时，才会将数据真正送到输出流，但可以使用 `flush()` 方法人为地将尚未填满的缓冲区中的数据送出。

#### BufferedReader 和 BufferedWriter

为了提高字符流处理的效率，java.io 中也提供了缓冲流 BufferedReader 和 BufferedWrite。其构造方法与 BufferedInputStream 和 BufferedOutPutStream 相类似。另外，除了 read() 和 write() 方法外，它还提供了整行字符处理方法：

1. public String readLine()：BufferedReader 的方法，从输入流中读取一行字符，行结束标志 `\n`、`\r` 或者两者一起（这是根据系统而定的）
2. public void newLine()：BufferedWriter 的方法，向输出流中写入一个行结束标志，它不是简单地换行符 `\n` 或`\r`，而是系统定义的行隔离标志（line separator）。

```java
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class FileToUnicode {
    public static void main(String args[]) {
        try {
            FileInputStream fis = new FileInputStream("file1.txt");
            InputStreamReader dis = new InputStreamReader(fis);
            BufferedReader reader = new BufferedReader(dis);
            String s;
            //每次读取一行，当改行为空时结束
            while((s = reader.readLine()) != null){
                System.out.println("read:" + s);
            }
            dis.close();
        }
        catch(IOException e) {
            System.out.println(e);
        }
    }
}
```

### 数据流

接口 `DataInput` 和 `DataOutput`，设计了一种较为高级的数据输入输出方式：除了可处理字节和字节数组外，还可以处理 `int`、`float`、`boolean` 等基本数据类型，这些数据在文件中的表示方式和它们在内存中的一样，无须转换，如 `read()`, `readInt()`, `readByte()`…; `write()`, `writeChar()`, `writeBoolean()`… 此外，还可以用 `readLine()` 方法读取一行信息。

| 方法                                | 返回值  | 说明                                                         |
| ----------------------------------- | ------- | ------------------------------------------------------------ |
| readBoolean()                       | boolean |                                                              |
| readByte()                          | byte    |                                                              |
| readShort()                         | short   |                                                              |
| readChar()                          | char    |                                                              |
| readInt()                           | int     |                                                              |
| readLong()                          | long    |                                                              |
| readDouble()                        | double  |                                                              |
| readFloat()                         | float   |                                                              |
| readUnsignedByte()                  | int     |                                                              |
| readUnsignedShort()                 | int     |                                                              |
| readFully(byte[] b)                 | void    | 从输入流中读取一些字节，并将它们存储在缓冲区数组 b 中        |
| reaFully(byte[] b, int off,int len) | void    | 从输入流中读取 len 个字节                                    |
| skipBytes(int n)                    | int     | 与 InputStream.skip 等价                                     |
| readUTF()                           | String  | 按照 UTF-8 形式从输入中读取字符串                            |
| readLine()                          | String  | 按回车 (\r) 换行 (\n) 为分割符读取一行字符串，不完全支持 UNICODE |
| writeBoolean(boolean v)             | void    |                                                              |
| writeByte(int v)                    | void    |                                                              |
| writeShort(int v)                   | void    |                                                              |
| writeChar(int v)                    | void    |                                                              |
| writeInt(int v)                     | void    |                                                              |
| writeLong(long v)                   | void    |                                                              |
| writeFloat(float v)                 | void    |                                                              |
| writeDouble(double v)               | void    |                                                              |
| write(byte[] b)                     | void    | 与 OutputStream.write 同义                                   |
| write(byte[] b, int off, int len)   | void    | 与 OutputStream.write 同义                                   |
| write(int b)                        | void    | 与 OutputStream.write 同义                                   |
| writeBytes(String s)                | void    | 只输出每个字符的低 8 位；不完全支持 UNICODE                  |
| writeChars(String s)                | void    | 每个字符在输出中都占两个字节                                 |

数据流类 `DataInputStream` 和 `DataOutputStream` 的处理对象除了是字节或字节数组外，还可以实现对文件的不同数据类型的读写：

1. 分别实现了 `DataInput` 和 `DataOutput` 接口。
2. 在提供字节流的读写手段同时，以统一的形式向输入流中写入 `boolean`，`int`，`long`，`double` 等基本数据类型，并可以再次把基本数据类型的值读取回来。
3. 提供了字符串读写的手段

```java
FileInputStream fis = new FileInputStream("file1.txt");
FileOutputStream fos = new FileOutputStream("file2.txt");
DataInputStream dis = new DataInputStream(fis);
DataOutputStream dos = new DataOutputStream(fos);
```

### 读写对象

通过 ObjectOutputStream 和 ObjectInputStream 将对象输入输出。 

将对象的状态信息转换为可以存储或者传输的形式的过程又叫序列化。

```java
import java.io.*;

public class ReadWriteObject {
    public static void main(String[] args) {
        File file = new File("/home/project/user.file");
        try (ObjectOutputStream objectOutputStream = new ObjectOutputStream(new FileOutputStream(file))) {
            //将匿名对象 写入到file中，注意：被写入的对象必须实现了Serializable接口
            objectOutputStream.writeObject(new User("shiyanlou", "password"));
            objectOutputStream.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
        //读取文件 打开输入流
        try (ObjectInputStream objectInputStream = new ObjectInputStream(new FileInputStream(file))) {
//            将信息还原为user实例
            User user = (User) objectInputStream.readObject();
            //打印user信息  和上面创建的匿名对象的信息一致
            System.out.println(user.toString());
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }

    }

//静态内部类 必须实现Serializable
    static class User implements Serializable {
        private String username;
        private String password;

        public User(String username, String password) {
            this.username = username;
            this.password = password;
        }

        @Override
        public String toString() {
            return "User{" +
                    "username='" + username + '\'' +
                    ", password='" + password + '\'' +
                    '}';
        }
    }
}
```

### NIO

Java NIO(New IO) 发布于 JDK1.4，用于代替 Java 标准 IO 。Java NIO 是面向缓存的、非阻塞的 IO，而标准 IO 是面向流的，阻塞的 IO。

首先理解 NIO 的重要概念：**Buffer**（缓冲区）

- NIO 读取或者写入数据都要通过 Buffer
- 通过 `allocate()` 方法分配 Buffer，Buffer 不可实例化，Buffer 是抽象类，需要使用具体的子类，比如 ByteBuffer。
- Buffer 的参数
  - `capacity` ：缓冲区的容量
  - `position` ：当前指针位置，每读取一次缓冲区数据或者写入缓冲区一个数据那么指针将会后移一位
  - `limit` ：限制指针的移动，指针不能读取 `limit` 之后的位置
  - `mark` ：如果设置该值，那么指针将移动到 0 - `position` 的位置
  - 最后可以这几个参数的关系如下：`mark` <= `position` <= `limit` <= `capacity`

```java
import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.charset.Charset;
import java.nio.charset.CharsetDecoder;
import java.util.Scanner;

public class NioDemo {
    public static void main(String[] args) {
        try {
            File file = new File("/home/project/nio.txt");
            if (!file.exists()) {
                file.createNewFile();
            }
            //创建channel  nio通过channel来连接文件 相当于桥梁
            FileChannel writeChannel = new RandomAccessFile(file, "rw").getChannel();
            //创建一个ByteBuffer 容量为100
            ByteBuffer byteBuffer = ByteBuffer.allocate(100);
            System.out.println("请输入字符串");
            Scanner in = new Scanner(System.in);
            String s = in.nextLine();
            //将字符串写入到缓冲区
            byteBuffer.put(s.getBytes());
            System.out.println("写入数据后指针变化-position:" + byteBuffer.position() + " limit：" + byteBuffer.limit() + " capacity :" + byteBuffer.capacity());
            //为输出数据做准备 将limit移动到position位置，position置0
            byteBuffer.flip();
            System.out.println("flip后指针变化-position:" + byteBuffer.position() + " limit：" + byteBuffer.limit() + " capacity :" + byteBuffer.capacity());
            //将缓冲区写入channel
            writeChannel.write(byteBuffer);
            //清除缓冲区 为下次写入或者读取数据做准备 恢复到初始状态 position=0 limit=capacity=100  因为我们这里分配的容量大小为100
            byteBuffer.clear();
            System.out.println("clear后指针变化-position:" + byteBuffer.position() + " limit：" + byteBuffer.limit() + " capacity :" + byteBuffer.capacity());
            //关闭channel
            writeChannel.close();
            FileChannel readChannel = new RandomAccessFile(file, "r").getChannel();
            //从channel中将数据读取到缓冲区
            while (readChannel.read(byteBuffer) != -1) {
                //为读取数据做准备
                byteBuffer.flip();
                //输出数据 设置解码器
                Charset charset = Charset.forName("UTF-8");
                CharsetDecoder decoder = charset.newDecoder();
                System.out.println("读取结果：" + decoder.decode(byteBuffer));
                //清除缓冲区
                byteBuffer.clear();
            }
            readChannel.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

```
`$ javac NioDemo.java
$` java NioDemo
请输入字符串
shiyanlou
写入数据后指针变化-position:9 limit：100 capacity :100
flip后指针变化-position:0 limit：9 capacity :100
clear后指针变化-position:0 limit：100 capacity :100
读取结果：shiyanlou
```

