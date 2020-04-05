# StudyJava——IO_File

整个 Java.io 包中最重要的就是 5 个类，指的是 File、OutputStream、InputStream、Writer、Reader。

## 文件File

Java 使用 File 类来直接处理文件和文件系统。File 类描述了文件本身的属性。File 对象用来获取或处理与磁盘文件相关的信息，例如权限，时间，日期和目录路径。此外，File 还浏览子目录层次结构。Java 中的目录当成 File 对待，它具有附加的属性——一个可以被 list( )方法检测的文件名列表。

- 构造方法

```java
//通过将给定路径名字符串转换为抽象路径名来创建一个新 File 实例       
File(String pathname) 

// 根据 parent 路径名字符串和 child 路径名字符串创建一个新 File 实例
File(String parent, String child) 
    
//根据 parent 抽象路径名和 child 路径名字符串创建一个新 File 实例。 
File(File parent, String child) 

//通过将给定的 file: URI 转换为一个抽象路径名来创建一个新的 File 实例
File(URI uri) 
```

- 使用示例

```java
//一个目录路径参数
File f1 = new File("/home/project/");

//对象有两个参数——路径和文件名
File f2 = new File("/home/project/","a.bat");

//指向f1文件的路径及文件名
File f3 = new File(f1,"a.bat");
```

- 常用方法

| 方法                                                         | 说明                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| boolean canExecute()                                         | 测试应用程序是否可以执行此抽象路径名表示的文件               |
| boolean canRead()                                            | 测试应用程序是否可以读取此抽象路径名表示的文件               |
| boolean canWrite()                                           | 测试应用程序是否可以修改此抽象路径名表示的文件               |
| int compareTo(File pathname)                                 | 按字母顺序比较两个抽象路径名                                 |
| boolean createNewFile()                                      | 当且仅当不存在具有此抽象路径名指定名称的文件时，不可分地创建一个新的空文件 |
| static File createTempFile(String prefix, String suffix)     | 在默认临时文件目录中创建一个空文件，使用给定前缀和后缀生成其名称 |
| static File createTempFile(String prefix, String suffix, File directory) | 在指定目录中创建一个新的空文件，使用给定的前缀和后缀字符串生成其名称 |
| boolean delete()                                             | 删除此抽象路径名表示的文件或目录                             |
| void deleteOnExit()                                          | 在虚拟机终止时，请求删除此抽象路径名表示的文件或目录         |
| boolean equals(Object obj)                                   | 测试此抽象路径名与给定对象是否相等                           |
| boolean exists()                                             | 测试此抽象路径名表示的文件或目录是否存在                     |
| File getAbsoluteFile()                                       | 返回此抽象路径名的绝对路径名形式                             |
| String getAbsolutePath()                                     | 返回此抽象路径名的绝对路径名字符串                           |
| File getCanonicalFile()                                      | 返回此抽象路径名的规范形式                                   |
| String getCanonicalPath()                                    | 返回此抽象路径名的规范路径名字符串                           |
| long getFreeSpace()                                          | 返回此抽象路径名指定的分区中未分配的字节数                   |
| String getName()                                             | 返回由此抽象路径名表示的文件或目录的名称                     |
| String getParent()                                           | 返回此抽象路径名父目录的路径名字符串；如果此路径名没有指定父目录，则返回 null |
| File getParentFile()                                         | 返回此抽象路径名父目录的抽象路径名；如果此路径名没有指定父目录，则返回 null |
| String getPath()                                             | 将此抽象路径名转换为一个路径名字符串                         |
| long getTotalSpace()                                         | 返回此抽象路径名指定的分区大小                               |
| long getUsableSpace()                                        | 返回此抽象路径名指定的分区上可用于此虚拟机的字节数           |
| int hashCode()                                               | 计算此抽象路径名的哈希码                                     |
| boolean isAbsolute()                                         | 测试此抽象路径名是否为绝对路径名                             |
| boolean isDirectory()                                        | 测试此抽象路径名表示的文件是否是一个目录                     |
| boolean isFile()                                             | 测试此抽象路径名表示的文件是否是一个标准文件                 |
| boolean isHidden()                                           | 测试此抽象路径名指定的文件是否是一个隐藏文件                 |
| long lastModified()                                          | 返回此抽象路径名表示的文件最后一次被修改的时间               |
| long length()                                                | 返回由此抽象路径名表示的文件的长度                           |
| String[] list()                                              | 返回一个字符串数组，这些字符串指定此抽象路径名表示的目录中的文件和目录 |
| String[] list(FilenameFilter filter)                         | 返回一个字符串数组，这些字符串指定此抽象路径名表示的目录中满足指定过滤器的文件和目录 |
| File[] listFiles()                                           | 返回一个抽象路径名数组，这些路径名表示此抽象路径名表示的目录中的文件 |
| File[] listFiles(FileFilter filter)                          | 返回抽象路径名数组，这些路径名表示此抽象路径名表示的目录中满足指定过滤器的文件和目录 |
| File[] listFiles(FilenameFilter filter)                      | 返回抽象路径名数组，这些路径名表示此抽象路径名表示的目录中满足指定过滤器的文件和目录 |
| static File[] listRoots()                                    | 列出可用的文件系统根                                         |
| boolean mkdir()                                              | 创建此抽象路径名指定的目录                                   |
| boolean mkdirs()                                             | 创建此抽象路径名指定的目录，包括所有必需但不存在的父目录     |
| boolean renameTo(File dest)                                  | 重新命名此抽象路径名表示的文件                               |
| boolean setExecutable(boolean executable)                    | 设置此抽象路径名所有者执行权限的一个便捷方法                 |
| boolean setExecutable(boolean executable, boolean ownerOnly) | 设置此抽象路径名的所有者或所有用户的执行权限                 |
| boolean setLastModified(long time)                           | 设置此抽象路径名指定的文件或目录的最后一次修改时间           |
| boolean setReadable(boolean readable)                        | 设置此抽象路径名所有者读权限的一个便捷方法                   |
| boolean setReadable(boolean readable, boolean ownerOnly)     | 设置此抽象路径名的所有者或所有用户的读权限                   |
| boolean setReadOnly()                                        | 标记此抽象路径名指定的文件或目录，从而只能对其进行读操作     |
| boolean setWritable(boolean writable)                        | 设置此抽象路径名所有者写权限的一个便捷方法                   |
| boolean setWritable(boolean writable, boolean ownerOnly)     | 设置此抽象路径名的所有者或所有用户的写权限                   |
| String toString()                                            | 返回此抽象路径名的路径名字符串                               |
| URI toURI()                                                  | 构造一个表示此抽象路径名的 file: URI                         |

【例】

```java
import java.io.File;
import java.io.IOException;

public class  FileDemo {
    public static void main(String[] args){
        File f1 =new File("/home/project/1.txt");
        File f2 =new File("/home/project","2.txt");
        //separator 跨平台分隔符
        File f3 =new File("/home"+File.separator+"project");
        File f4 =new File(f3,"3.txt");

        try {
             System.out.println(f1);
                //当文件存在时返回 false；不存在时返回 true
                System.out.println(f2.createNewFile());
                //当文件不存在时返回 false
                System.out.println(f3.delete());
        }catch(IOException e) {
                e.printStackTrace();
        }

        //列出磁盘下的文件和文件夹
        File[] files =File.listRoots();
        for(File file:files){
            System.out.println(file);
            if(file.length()>0){
                String[] filenames =file.list();
                for(String filename:filenames){
                    System.out.println(filename);
                }
            }
        }
    }

}
```

### 文件流

java.io 包中提供了文件操作类：

1. 用于读写本地文件系统中的文件：FileInputStream 和 FileOutputStream
2. 描述本地文件系统中的文件或目录：File、FileDescriptor 和 FilenameFilter
3. 提供对本地文件系统中文件的随机访问支持：RandomAccessFile

#### FileInputStream

| **序号** | **方法及描述**                                               |
| :------- | :----------------------------------------------------------- |
| 1        | **public void close() throws IOException{}** 关闭此文件输入流并释放与此流有关的所有系统资源。抛出IOException异常。 |
| 2        | **protected void finalize()throws IOException {}** 这个方法清除与该文件的连接。确保在不再引用文件输入流时调用其 close 方法。抛出IOException异常。 |
| 3        | **public int read(int r)throws IOException{}** 这个方法从 InputStream 对象读取指定字节的数据。返回为整数值。返回下一字节数据，如果已经到结尾则返回-1。 |
| 4        | **public int read(byte[] r) throws IOException{}** 这个方法从输入流读取r.length长度的字节。返回读取的字节数。如果是文件结尾则返回-1。 |
| 5        | **public int available() throws IOException{}** 返回下一次对此输入流调用的方法可以不受阻塞地从此输入流读取的字节数。返回一个整数值。 |

#### FileOutputStream

| **序号** | **方法及描述**                                               |
| :------- | :----------------------------------------------------------- |
| 1        | **public void close() throws IOException{}** 关闭此文件输入流并释放与此流有关的所有系统资源。抛出IOException异常。 |
| 2        | **protected void finalize()throws IOException {}** 这个方法清除与该文件的连接。确保在不再引用文件输入流时调用其 close 方法。抛出IOException异常。 |
| 3        | **public void write(int w)throws IOException{}** 这个方法把指定的字节写到输出流中。 |
| 4        | **public void write(byte[] w)** 把指定数组中w.length长度的字节写到OutputStream中。 |

FileInputStream 类用于打开一个输入文件，若要打开的文件不存在，则会产生异常 FileNotFoundException，这是一个非运行时异常，必须捕获或声明抛弃；

FileOutputStream 类用来打开一个输出文件，若要打开的文件不存在，则会创建一个新的文件，否则原文件的内容会被新写入的内容所覆盖；

在进行文件的读/写操作时，会产生非运行时异常 IOException，必须捕获或声明抛弃（其他的输入/输出流处理时也同样需要进行输入/输出异常处理）。

- 构造方法

```java
//打开一个以 f 描述的文件作为输入
FileInputStream(File f)

//打开一个文件路径名为 name 的文件作为输入
FileInputStream(String name)

//创建一个以 f 描述的文件作为输出
//如果文件存在，则其内容被清空
FileOutputStream(File f)

//创建一个文件路径名为 name 的文件作为输出
//文件如果已经存在，则其内容被清空
FileOutputStream(String name)

//创建一个文件路径名为 name 的文件作为输出
//文件如果已经存在，append为true时，则在该输出上输出的内容被接到原有内容之后
FileOutputStream(String name, boolean append)
```

【例】使用输入流和输出将 file1.txt 的内容复制到 file2.txt。

```java
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

public class Test {

    public static void main(String[] args) {
        try {
            //inFile 作为输入流的数据文件必须存在，否则抛出异常
            // file1.txt在项目根目录下
            File inFile = new File("./file1.txt");

            //file2.txt没有，系统可以创建
            // file2.txt放在项目根目录下
            File outFile = new File("file2.txt");
            FileInputStream fis = new FileInputStream(inFile);
            FileOutputStream fos = new FileOutputStream(outFile);
            
            // read方法从 InputStream 对象读取指定字节的数据。返回为整数值。
            // 返回下一字节数据，如果已经到结尾则返回-1
            // c为字符的ASCII码
            int c;
            while((c = fis.read()) != -1){
                fos.write(c);
            }
            //打开了文件一定要记着关，释放系统资源
            fis.close();
            fos.close();
        }catch(FileNotFoundException e) {
            System.out.println("FileStreamsTest:" + e);
        }catch(IOException e){
            System.err.println("FileStreamTest:" + e);
        }
    }
}
```

### FileReader、FileWriter

```java
FileReader file = new FileReader("file1.txt");
FileWriter file2 = new FileWriter("file2.txt");

int data = 0;

while((data=file.read())!=-1){
    //在while循环中使用read()方法持续读取file，数据赋到data中
    //如果读取失败或者结束，则将返回-1，这个特殊的返回值可以作为读取结束的标识

    file2.write(data);
}

file.close();
file2.close();
```

### RandomAccessFile随机读写

类 RandomAccessFile 则允许文件内容同时完成读和写操作，它直接继承 object，并且同时实现了接口 DataInput 和 DataOutput。

随机访问文件的行为类似存储在文件系统中的一个大型 byte 数组。存在指向该隐含数组的光标或索引，称为文件指针；输入操作从文件指针开始读取字节，并随着对字节的读取而前移此文件指针。如果随机访问文件以读取/写入模式创建，则输出操作也可用；输出操作从文件指针开始写入字节，并随着对字节的写入而前移此文件指针。

RandomAccessFile 提供了支持随机文件操作的方法：

1. readXXX()或者 writeXXX():如 ReadInt(),ReadLine(),WriteChar(),WriteDouble()等
2. int skipBytes(int n):将指针向下移动若干字节
3. length():返回文件长度
4. long getFilePointer():返回指针当前位置
5. void seek(long pos):将指针调用所需位置

在生成一个随机文件对象时，除了要指明文件对象和文件名之外，还需要指明访问文件的模式。

来看看 RandomAccessFile 的构造方法：

```java
RandomAccessFile(File file,String mode)
RandomAccessFile(String name,String mode)
```

mode 的取值：

- `r`:只读，任何写操作都将抛出 IOException
- `rw`:读写，文件不存在时会创建该文件，文件存在是，原文件内容不变，通过写操作改变文件内容。
- `rws`:打开以便读取和写入，对于 "rw"，还要求对文件的内容或元数据的每个更新都同步写入到底层存储设备。
- `rwd`:打开以便读取和写入，对于 "rw"，还要求对文件内容的每个更新都同步写入到底层存储设备。

【例1】

- 从偏移量为 10 的位置开始读取文件 randomAccess.file 的内容
- 输出文件内容（以字符串形式，不能直接输出字节内容）

```java
import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.util.Arrays;

public class RandomFile {
    public static void main(String[] args) {
        RandomAccessFile file;
        try {
            // 已存在该file
            File d = new File("randomAccess.file");
            file = new RandomAccessFile(d, "rw");
            file.seek(10);
            byte[] b = new byte[(int) file.length()-10];
            file.read(b);
            System.out.println(new String(b));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

【例2】

```java
// FileDemo.java
import java.io.IOException;
import java.io.RandomAccessFile;

public class  FileDemo {
    public static void main(String[] args){

            int data_arr[] = {12, 32, 43, 45, 1, 5};
            try {
                RandomAccessFile randf=new RandomAccessFile("temp.dat","rw");
                for(int i = 0; i < data_arr.length; i++){
                    randf.writeInt(data_arr[i]);
                }
                for(int i = data_arr.length-1 ; i >= 0; i--){
                    //int 数据占4个字节
                    // L表示long数据类型
                    randf.seek(i * 4L);
                    System.out.println(randf.readInt());
                }
                randf.close();
            }catch(IOException e){
                System.out.println("File access error" + e);
            }
    }
}
```

```
$ javac FileDemo.java
$ java FileDemo
5
1
45
43
32
12
```

## 文件操作

### 拷贝

使用 Files 工具类的 copy(Path source,Path target,CopyOption... options)拷贝文件或者目录。

- 如果目标文件或目录存在，那么拷贝将失败，除非我们在 options 中指定了`REPLACE_EXISTING`属性。

- 在REPLACE_EXISTING属性下，该命令复制文件时，如果target文件已存在，则覆盖，不存在则新建。

- 该命令复制目录时，如果source目录中存在文件，则文件将不会被复制，即target是一个同链接的空目录。

CopyOption 参数支持以下 StandardCopyOption 和 LinkOption 枚举：

- REPLACE_EXISTING - 即使目标文件已存在，也执行复制。如果目标是符号链接，则复制链接本身（不复制链接的文件）。如果目标是非空目录，则复制将失败并显示 FileAlreadyExistsException 异常。
- COPY_ATTRIBUTES - 将与文件关联的文件属性复制到目标文件。支持的确切- 文件属性是文件系统和平台相关的，但 last-modified-time 跨平台支持并复制到目标文件。 NOFOLLOW_LINKS - 表示不应遵循符号链接。如果要复制的文件是符号链接，则复制链接（而不是链接的目标）。

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

public class CopyDemo {
    public static void main(String[] args) {
        try {
            //被拷贝的文件一定要存在 否则会抛出异常  这里的1.txt一定要存在
            Files.copy(Paths.get("1.txt"), Paths.get("2.txt"), StandardCopyOption.REPLACE_EXISTING);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### 移动和重命名

Files 类的 move(Path, Path, CopyOption... options)方法移动文件或者目录。同样目标目录存在，那么比如使用`REPLACE_EXISTING`。 options 参数支持 StandardCopyOption 的以下枚举：

- REPLACE_EXISTING - 即使目标文件已存在，也执行移动。如果目标是符号链接，则替换符号链接，但它指向的内容不受影响。
- ATOMIC_MOVE - 将移动作为原子文件操作执行。如果文件系统不支持原子移动，则抛出异常。使用，ATOMIC_MOVE 您可以将文件移动到目录中，并保证观察目录的任何进程都可以访问完整的文件。

move 方法除了可以移动之外，也可以用于重命名。

```java
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

public class MoveDemo {
    public static void main(String[] args) {
        try {
            //将1.txt 重命名为3.txt 如果只需要移动到不同的目录，文件名不变即可
            Files.move(Paths.get("1.txt"), Paths.get("3.txt"), StandardCopyOption.REPLACE_EXISTING);

        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
```

### 删除

通过 Files 的 delete(Path path)方法或者 deleteIfExists(Path path)方法删除文件。

```java
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class DeleteDemo {
    public static void main(String[] args) {
        try {
            //删除文件，文件必须存在，否则抛出异常
            Files.delete(Paths.get("3.txt"));
            //删除文件，返回是否删除成功 即使文件不存在，也不会保存，直接返回false
            System.out.println(Files.deleteIfExists(Paths.get("3.txt")));
            //或者使用File类的delete方法
            File file = new File("4.txt");
            System.out.println(file.delete());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### 文件属性

```java
import java.io.File;
import java.util.Arrays;

public class FileInfo {
    public static void main(String[] args) {
        File file = new File("/home/project");
        System.out.println("文件或者目录名：" + file.getName());
        System.out.println("绝对路径：" + file.getAbsolutePath());
        System.out.println("父目录：" + file.getParent());
        System.out.println("文件路径：" + file.getPath());
        //判断文件是否是目录
        if (file.isDirectory()) {
            //打印目录中的文件
            Arrays.stream(file.list()).forEach(System.out::println);
        }
        System.out.println("是否隐藏：" + file.isHidden());
        System.out.println("是否存在：" + file.exists());
    }
}
```

```
$ javac FileInfo.java
$ java FileInfo
文件或者目录名：project
绝对路径：/home/project
父目录：/home
文件路径：/home/project
FileInfo.class
FileInfo.java
是否隐藏：false
是否存在：true
```

### 目录读取

Java 中读取目录中的文件可以直接使用 listFiles()方法读取，但是也只能读取当前目录中的文件，如果当前目录中还有二级目录如何解决呢？三级目录呢？接下来将使用 Java 读取当前目录和子目录中的所有文件。

```java
import java.io.File;
public class ReadDir {
    public static void main(String[] args) {
        readDir(new File("/home"));
    }

    static void readDir(File file) {
        if (file == null) {
            return;
        }
        //如果当前file是目录
        if (file.isDirectory()) {
            File[] files;
            //如果目录不为空
            if ((files = file.listFiles()) != null) {
                for (File file1 : files) {
                    //递归读取目录内容
                    readDir(file1);
                }
            }
        } else {
            //如果不是目录 直接输出文件名
            System.out.println(file.getName());
        }
    }
}
```

