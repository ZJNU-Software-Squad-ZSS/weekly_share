# StudyJava——异常

异常通常有四类：

- Error：系统内部错误，这类错误由系统进行处理，程序本身无需捕获处理
- Exception：可以处理的异常
- RuntimeException：可以捕获，也可以不捕获的异常
- 继承 Exception 的其他类：必须捕获，通常在 API 文档中会说明这些方法抛出哪些异常

RuntimeExcption 异常(运行时异常)通常有以下几种：

- 错误的类型转换
- 数组访问越界
- 访问 null 指针
- 算术异常

> 一般来说，RuntimeException 都是程序员的问题。

非 RuntimeException（受查异常）一般有：

- 打开一个不存在的文件
- 没有找到具有指定名称的类
- 操作文件异常

> 受查异常是编译器要求必须处理的异常，必须使用 try catch 处理，或者向上抛出，给上层处理。

### throw抛出异常

当程序运行时数据出现错误或者我们不希望发生的情况出现的话，可以通过抛出异常来处理。

```java
throw new 异常名();
```

【例】

```java
public class ThrowTest {
    
    public static void main(String[] args) {
        Integer a = 1;
        Integer b = null;
        //当a或者b为null时，抛出异常
        if (a == null || b == null) {
            throw new NullPointerException();
        } else {
            System.out.println(a + b);
        }
    }
}
```

```
$ javac ThrowTest.java
$ java ThrowTest
Exception in thread "main" java.lang.NullPointerException
    at ThrowTest.main(ThrowTest.java:8)
```

### throw声明异常

throws 用于声明异常，表示该方法可能会抛出的异常。如果声明的异常中包括 checked 异常（受查异常），那么调用者必须处理该异常或者使用 throws 继续向上抛出。throws 位于方法体前，多个异常使用,分割。

【例】

```java
import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class ThrowsTest {

    public static void main(String[] args) throws FileNotFoundException {
        //由方法的调用者捕获异常或者继续向上抛出
        throwsTest();
    }

    public static void throwsTest() throws FileNotFoundException {
        new FileInputStream("/home/project/shiyanlou.file");
    }
}
```

```
$ javac ThrowsTest.java
$ java ThrowsTest
Exception in thread "main" java.io.FileNotFoundException: /home/project/shiyanlou.file (系统找不到指定的路径。)
    at java.io.FileInputStream.open0(Native Method)
    at java.io.FileInputStream.open(FileInputStream.java:195)
    at java.io.FileInputStream.<init>(FileInputStream.java:138)
    at java.io.FileInputStream.<init>(FileInputStream.java:93)
    at ThrowsTest.throwsTest(ThrowsTest.java:13)
    at ThrowsTest.main(ThrowsTest.java:8)
```

### 捕获异常

通常抛出异常后，还需要将异常捕获。使用`try`和`catch`语句块来捕获异常，有时候还会用到`finally`。

对于上述三个关键词所构成的语句块，`try`语句块是必不可少的，`catch`和`finally`语句块可以根据情况选择其一或者全选。你可以把可能发生错误或出现问题的语句放到`try`语句块中，将异常发生后要执行的语句放到`catch`语句块中，而`finally`语句块里面放置的语句，不管异常是否发生，它们都会被执行。

> try语句块是用来捕获出现的异常，所以在try语句是不会抛出异常结果的，即不会在命令行出现
>
> “Exception in thread "main" java.lang.NullPointerException
>     at ThrowTest.main(ThrowTest.java:8)”这样的信息。
>
> 而是直接由catch捕获该异常，进入catch语句块里面。

【例】

```java
public class CatchException {
    public static void main(String[] args) {
        try {
            // 下面定义了一个try语句块

            System.out.println("I am try block.");

            Class<?> tempClass = Class.forName("");    
            // 声明一个空的Class对象用于引发“类未发现异常”
            System.out.println("Bye! Try block.");

        } catch (ClassNotFoundException e) {
            // 下面定义了一个catch语句块
            System.out.println("I am catch block.");

            e.printStackTrace();
            //printStackTrace()的意义在于在命令行打印异常信息在程序中出错的位置及原因

            System.out.println("Goodbye! Catch block.");

        } finally {
            // 下面定义了一个finally语句块
            System.out.println("I am finally block.");
        }
    }
}
```

```
$ javac CatchException.java
$ java CatchException
I am try block.
I am catch block.
java.lang.ClassNotFoundException:
        at java.lang.Class.forName0(Native Method)
        at java.lang.Class.forName(Unknown Source)
        at CatchException.main(CatchException.java:8)
Goodbye! Catch block.
I am finally block.
```

### 捕获多个异常

```java
import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class MultipleCapturesDemo {
    public static void main(String[] args) {
        try {
            new FileInputStream("");
        } catch (FileNotFoundException e) {
            System.out.println("IO 异常");
        } catch (Exception e) {
            System.out.println("发生异常");
        }
    }
}
```

```
$ javac MultipleCapturesDemo.java
$ java MultipleCapturesDemo
IO 异常
```

> 在处理异常时，并不要求抛出的异常同 catch 所声明的异常完全匹配，子类的对象也可以匹配父类的处理程序。比如异常 A 继承于异常 B，那么在处理多个异常时，一定要将异常 A 放在异常 B 之前捕获，如果将异常 B 放在异常 A 之前，那么将永远匹配到异常 B，异常 A 将永远不可能执行，并且编译器将会报错。

### 自定义异常

- 继承Exception或其子类
- 建议同时提供无参数构造方法和带字符串参数的构造方法

【例】

```java
// MyAriException.java
public class MyAriException extends ArithmeticException {
    //自定义异常类，该类继承自ArithmeticException

    public MyAriException() {

    }
    //实现默认的无参构造方法

    public MyAriException(String msg) {
        super(msg);
    }
    //实现可以自定义输出信息的构造方法，将待输出信息作为参数传入即可
}
```

【test】

```java
// ExceptionTest.java
import java.util.Arrays;

public class ExceptionTest {
    public static void main(String[] args) {
        int[] array = new int[5];
        //声明一个长度为5的数组

        Arrays.fill(array, 5);
        //将数组中的所有元素赋值为5

        for (int i = 4; i > -1; i--) {
            //使用for循环逆序遍历整个数组，i每次递减

            if (i == 0) {
            // 如果i除以了0，就使用带异常信息的构造方法抛出异常

                throw new MyAriException("There is an exception occured.");
            }

            System.out.println("array[" + i + "] / " + i + " = " + array[i] / i);
            // 如果i没有除以0，就输出此结果
        }
    }
}
```

```
$ javac ExceptionTest.java MyAriException.java
$ java ExceptionTest
array[4] / 4 = 1
array[3] / 3 = 1
array[2] / 2 = 2
array[1] / 1 = 5
Exception in thread "main" MyAriException: There is an exception occured.
    at ExceptionTest.main(ExceptionTest.java:17)
```

### 异常堆栈

```java
public class ExceptionStackTrace {
    private static void method1() {
        method2();
    }

    private static void method2() {
        throw new NullPointerException();
    }
    public static void main(String[] args) {
        try {
            method1();
        } catch (Exception e) {
            //打印堆栈轨迹
            e.printStackTrace();
        }
    }
}
```

```
$ javac ExceptionStackTrace.java
$ java ExceptionStackTrace
java.lang.NullPointerException
    at ExceptionStackTrace.method2(ExceptionStackTrace.java:7)
    at ExceptionStackTrace.method1(ExceptionStackTrace.java:3)
    at ExceptionStackTrace.main(ExceptionStackTrace.java:11)
```

> 异常信息中首先打印的是距离抛出异常最近的语句，接着是调用该方法的方法，一直到最开始被调用的方法。从下往上看，就可以得出程序运行的轨迹。

