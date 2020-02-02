## 静态变量和静态方法
+ 静态变量被类中的所有对象共享。静态方法不能访问类中的实例成员（实例变量，实例方法）。
+ 一般类中的常量是被所有对象共享的，所以应该定义为fianl static
+ 实例方法和实例变量要在对象被创建之后才能使用，静态方法和静态变量可以通过引用变量或类名来调用
+ 实例方法可以访问实例成员和静态成员，静态方法只能访问静态成员，不能访问实例成员

## 可见性修饰符
+ 可修饰对象：**类**、**方法**、**数据域**
+ public修饰符：表示被修饰对象可以被其他任何类访问，
+ 如果没有使用修饰符，则默认被修饰对象可以被**同一包**中的任何类访问
+ private修饰符：限定方法和数据域只能在自己的**类中**被访问
+ private只能应用在类的成员上，public可以应用在类或类的成员上。局部变量不能使用private和public
+ pretected修饰符：允许子类访问父类的数据域及方法，非子类在同一包中可访问，其他不可访问

## Final修饰符
+ 可修饰对象：类、方法、数据域
+ 被修饰的类和对象不能被扩展，被修饰的数据域是一个常数且不能被修改

## this引用
+ 使用this引用隐藏数据域，如
  ```
  public class Knowledge {
	  private int number;
  	
  	public Knowledge(int number) {
	  	this.number = number;
	  }	
  }
  ```
+ 使用this调用构造方法，如
  ```
  public class Knowledge {
	private int number;
	
	public Knowledge(int number) {
		this.number = number;
	}
	
	public Knowledge() {
		this(1);
	}
	
  }
  ```

## String类
+ 字符串一旦创建，内容不可修改
  ```
  String str = "hello";
	str = "hi";
  ```
  "hello"仍然存在，只是str重新指向了"hi"
+ 构造字符串
  - String str = new String("hello java")
  - String str = "hello java"  Java将**字符串直接量**看做String对象
+ 对具有相同字符序列的**字符串直接量**使用同一个实例
  - String s1 = "hello";   String s2 = "hello";  String s3 = new String("hello");
  - 上述三个变量中，s1和s2存储的引用变量都指向同一个String类实例，s3区别于s1和s2指向另一个String类实例，尽管它们的值都是"hello"
  - s1和s2指向的实例类型被称为**限定字符串**
+ **正则表达式** + String类
  - 通过正则表达式来增强String类中的方法
  - String.matches()方法："java is fun".matches("java.*)结果是true。java.*就是一个正则表达式
  - "440-02-035".matches("\\d[3]-\\d[2]-\\d[3]")
  - 方法replaceAll、replaceFirst、split也可以和正则表达式结合使用
  ```
  String s = "a+b$#c".replaceAll("[$#+]","NNN");
	System.out.print(s + "\n");
  
	String[] token = "Java.C?C++,C#".split("[.,?;:]");
	for(String e: token) {
		System.out.print(e + "\t");
  ```
+ **字符串**转化为**数组**：toCharArray()
  ```
  char[] chars = "Java".toCharArray();
  
  //将字符串"CS3720"中下标从2到6的字符串复制到数组下标为4开始的位置
  char[] chars2 = ['J','a','v','a','1','2','3','4'];
  "CS3720".getChar(2,6,chars2,4)
  ```
+ 字符、数字、字符串的转换
  - Double.parseDouble(str)、Integer.parseInt(str)将一个字符串转换为一个Double或者int值
  - String.valueOf(5.44)将一个Double值转化为字符串
+ 格式化字符串
  - String s = String.format("%7.2f%6d%-4s", 45.556, 14, "AB");
  
## StringBuilder类和StringBuffer类
+ 多任务并发使用StringBuffer，单任务访问使用StringBuilder

## 继承
+ 父类中的**私有数据域**在该类之外是不可访问的，因此在子类中也不能直接使用，可以通过父类中的提供的修改器进行操作
+ Java不允许多重继承，但可以通过接口来实现
+ 关键字super
  - 调用父类的**构造方法**
  - 调用父类的**方法**
+ 重写
  - 只修改方法体，不修改方法的头，即方法的签名和返回值类型
+ Object类
  - Java中所有的类都继承自java.lang.Object类
  - Object类的toString()方法返回一些**描述该类**的信息，一般需要重写该方法来得到自己想要的信息je
  - Object类的equals()方法，通过比较两个引用变量是否指向同一个对象来判断两个对象是否相等
  
## 多态
+ 父类变量可以指向子类对象

## Arraylist类
+ 用来存储一个对象列表
+ 用来存储**不限定个数**的对象
+ 构造：ArrayList<E> array = new Array<>(); E是泛型类型
+ 方法：get(index),set(index,E),size(),add(),add(index,E),remove(index),remove(E),clear()
+ 通过对象数组创建一个数组列表
  ```
  String[] array = {red", "blue", "green"};
  ArrayList<String> list = new ArrayList<>(Array.asList(array));
  ```
+ 通过数组列表获得一个对象数组
  ```
  String[] array1 = new String[list.size()];
  list.toArray(array1);
  ```
  
 ## 异常处理
 + 声明异常
   - 除了Error和RuntimeException不用在方法中**显式**声明，其他抛出的异常都**必须**在方法头中显示声明
   ```
   public void myMethod() throws IOException
   public void myMethod() throws Exception1,Exception2,Exception3,......ExceptionN
   ```
 + 抛出异常
   ```
   throw new IllegalArgumentException("wrong Argument")
   ```
 + 捕获异常
   ```
   try{
     statemets;//Statements that may throw exception
   }
   catch (Exception1 exVar1){
     handler for exception1;
   }
   catch (Exception2 exVar2){
     handler for exception2;
   }
   ......
   catch (ExceptionN exVarN){
     handler for ExceptionN;
   }
   
   /**
   *对于使用同样的处理代码处理多个异常的情况
   */
   catch (Exception1 | Exception2 | Exception3 | ... | Exception ex){
     handler for each exception
   }
   ```
   
 ## 文件IO
 + File类
   - 相对文件名、绝对文件名
   - new File("C\\book"),new File("C\\book\\hello.txt"),new File("hello.txt")
   - File.isDirectory(),File.isFile()判断文件是否为目录、文件
   - 在Java中，目录分隔符使用双斜杠(\\)
   - **File类不包括*创建文件*的方法，也不包括对文件进行*读取和写*操作**
   - 通过File.isExist()方法判断new的File对象包含的文件路径（也即文件）是否存在
 + 文件输入输出
   - 使用**PrintWriter**类***创建*并写入**数据
     1.为文本文件创建一个PrintWriter对象PrintWriter writer = new PrintWriter(**new File(pathName)**)
     2.使用print、printf、println方法向文件写入数据
     3.使用try-with-resources自动关闭文件
       try(声明和创建文件){
       使用资源处理文件
       }
       ```
       	try(
		PrintWriter writer = new PrintWriter(file);
	   ) {
	writer.print("Tepnys is ");
	writer.println("22");
	writer.print("Traynor is 23");
	}
	```
   - 使用**Scanner**类**读取**数据
     1.Scanner scanner = new  Scanner(new File(fileName))
     2.scanner.hasNext(),scanner.next(),scanner.nextInt(),scanner.close()
     3.Scanner如何工作
       用Scanner提供的方法，读取用**分隔符**分隔开的标记，**默认分隔符为*空格***
 
 
 ## 抽象类
 + **构造方法**定义为protected
 + 不能使用new操作符创建它的实例
 + **抽象方法**只有定义没有实现，**实现由子类提供**
 + 一个**包含*抽象方法***的类，必须声明为抽象类
 
 ## 接口
 + 只包含**常量**和**抽象方法**
 + 父类是接口，子类如果不是抽象类就必须实现接口定义的方法
 
  
