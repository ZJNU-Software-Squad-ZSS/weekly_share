# StudyJava——Lambda

Lambda表达式运行通过表达式来代替功能接口。

### 函数式编程

函数式编程（functional programming）或称函数程序设计，又称泛函编程，是一种编程典范，它将计算机运算视为数学上的函数计算，并且避免使用程序状态以及易变对象。函数编程语言最重要的基础是λ演算（lambda calculus）。而且λ演算的函数可以接受函数当作输入（引数）和输出（传出值）。

### 函数式接口（Functional Interface）

简单地说，接口中若只包含一个抽象方法，则称该接口为函数式接口。可以在接口前使用注解`@FunctionalInterface`检查该接口是否为函数式接口。接口中的方法默认就是public abstract的。

接口可能继承了一个 `Object` 已经提供的方法，比如 `toString()`，`equals( )`…这些都不属于函数式接口方法的范畴, 所以函数式接口中所说的方法不包括这些。例如下面FI接口也是一个函数式接口。

```java
@FunctionalInterface
Interface FI{
   judge(int a);
   equals();      
}
```

java.util.function 包中包含了大量的函数式接口，基本可以满足我们的日常开发需求。

更多的接口可以参考 Java 官方 API 手册：[java.lang.Annotation Type FunctionalInterface](https://docs.oracle.com/javase/8/docs/api/java/lang/FunctionalInterface.html)。

【使用已有的FI】

JDK 1.8 新增加的函数接口：java.util.function 中Predicate 接口是一个函数式接口，它接受一个输入参数 T，返回一个布尔值结果。

```java
@FunctionalInterface
public interface Predicate<T> {
    boolean test(T t);
}
```

```java
import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;

public class Java8Tester {
   public static void main(String args[]){
       
       	//简单使用  判断a是否大于50
        Predicate<Integer> predicate = a -> a > 50;
        System.out.println(predicate.test(52));
       
        //如果只断言int类型，可以直接使用 IntPredicate
        IntPredicate intPredicate = a -> a > 50;
        IntStream.of(10,11,44,59,46,55,99,88,50)
                //结合filter过滤数字 小于或等于50的数字被过滤
                .filter(intPredicate)
                .peek(System.out::println).count();
       
       
      	List<Integer> list = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9);
      	System.out.println("输出所有数据:");

      	// Predicate<Integer> predicate = n -> true
      	// n 是一个参数传递到 Predicate 接口的 test 方法
      	// n 如果存在则 test 方法返回 true

      	// 传递参数 n
      	eval(list, n->true);

      	// Predicate<Integer> predicate1 = n -> n%2 == 0
      	// n 是一个参数传递到 Predicate 接口的 test 方法
      	// 如果 n%2 为 0 test 方法返回 true

      	System.out.println("输出所有偶数:");
      	eval(list, n-> n%2 == 0 );

      	// Predicate<Integer> predicate2 = n -> n > 3
      	// n 是一个参数传递到 Predicate 接口的 test 方法
      	// 如果 n 大于 3 test 方法返回 true

      	System.out.println("输出大于 3 的所有数字:");
      	eval(list, n-> n > 3 );
   }

   public static void eval(List<Integer> list, Predicate<Integer> predicate) {
      for(Integer n: list) {

         if(predicate.test(n)) {
            System.out.print(n + " ");
         }
      }
   }
}
```

```
true
59
55
99
88
输出所有数据:
1 2 3 4 5 6 7 8 9 输出所有偶数:
2 4 6 8 输出大于 3 的所有数字:
4 5 6 7 8 9 
```

### Lambda表达式

- #### 语法

  ```
  //参数列表 -> 方法体（表达式和代码块）
  parameter -> expression body
  ```

- #### 特征

  - 实现的接口是函数式接口，即只包含一个抽象方法。
  - 参数列表的个数与类型应该一一对应。
  - 可选的类型声明：你不用去声明参数的类型。编译器可以从参数的值来推断它是什么类型。
  - 可选的参数周围的括号：你可以不用在括号内声明单个参数。但是对于很多参数的情况，括号是必需的。
  - 可选的大括号：如果表达式体里面只有一个语句，那么你不必用大括号括起来。
  - 可选的返回关键字：如果表达式体只有单个表达式用于值的返回，那么编译器会自动完成这一步。若要指示表达式来返回某个值，则需要使用大括号。

```java
public class LambdaTest {
    public static void main(String args[]){
        LambdaTest tester = new LambdaTest();

          // 带有类型声明的表达式
          MathOperation addition = (int a, int b) -> a + b;

          // 没有类型声明的表达式
          MathOperation subtraction = (a, b) -> a - b;

          // 带有大括号、带有返回语句的表达式
          MathOperation multiplication = (int a, int b) -> { return a * b; };

          // 没有大括号和return语句的表达式
          MathOperation division = (int a, int b) -> a / b;

          // 输出结果
          System.out.println("10 + 5 = " + tester.operate(10, 5, addition));
          System.out.println("10 - 5 = " + tester.operate(10, 5, subtraction));
          System.out.println("10 x 5 = " + tester.operate(10, 5, multiplication));
          System.out.println("10 / 5 = " + tester.operate(10, 5, division));

          // 没有括号的表达式            
          GreetingService greetService1 = message ->
          System.out.println("Hello " + message);

          // 有括号的表达式            
          GreetingService greetService2 = (message) ->
          System.out.println("Hello " + message);

          // 调用sayMessage方法输出结果
          greetService1.sayMessage("Shiyanlou");
          greetService2.sayMessage("Classmate");
       }

       // 下面是定义的一些接口和方法

       interface MathOperation {
          int operation(int a, int b);
       }

       interface GreetingService {
          void sayMessage(String message);
       }

       private int operate(int a, int b, MathOperation mathOperation){
          return mathOperation.operation(a, b);
       }
}
```

```
$ javac LambdaTest.java
$ java LambdaTest
10 + 5 = 15
10 - 5 = 5
10 x 5 = 50
10 / 5 = 2 
Hello Shiyanlou
Hello Classmate
```

> Lambda 表达式优先用于定义功能接口在行内的实现，即单个方法只有一个接口。在上面的例子中，我们用了多个类型的 Lambda 表达式来定义 MathOperation 接口的操作方法。然后我们定义了 GreetingService 的 sayMessage 的实现。
>
> Lambda 表达式让匿名类不再需要，这为 Java 增添了简洁但实用的函数式编程能力。

> 【Lambda表达式】
>
> ```java
> public class LambdaTest {
>     
>     public static void main(String args[]){
>         MathOperation add = (int a, int b) -> a + b;
>         System.out.println(add.operation(2, 3));
>     }
> 
>     interface MathOperation {
>         int operation(int a, int b);
>     }
> }
> ```
>
> 【匿名类】
>
> ```java
> public class LambdaTest {
>     
>     public static void main(String args[]){
>         MathOperation add = new MathOperation(){
>             public int operation(int a, int b){
>                 return a + b; 
>             }
>         };
>         System.out.println(add.operation(2, 3));
>     }
> 
>     interface MathOperation {
>         int operation(int a, int b);
>     }
> }
> ```

- #### 作用域

  - 可访问 static 修饰的成员变量，如果是 final static 修饰，不可再次赋值，只有 static 修饰可再次赋值；
  - 可访问表达式外层的 final 局部变量（不用声明为 final，隐性具有 final 语义），不可再次赋值。

  ```java
  public class LambdaTest {
          final static String salutation = "Hello "; //正确，不可再次赋值
          //static String salutation = "Hello "; //正确，可再次赋值
          //String salutation = "Hello "; //报错
          //final String salutation = "Hello "; //报错
  
      public static void main(String args[]){
          //final String salutation = "Hello "; //正确，不可再次赋值
          //String salutation = "Hello "; //正确，隐性为 final , 不可再次赋值
  
          // salution = "welcome to "  
          GreetingService greetService1 = message -> 
          System.out.println(salutation + message);
          greetService1.sayMessage("Shiyanlou");
      }
  
      interface GreetingService {
         void sayMessage(String message);
      }
  }
  ```

  ```
  $ javac LambdaTest.java
  $ java LambdaTest
  Hello Shiyanlou
  ```

- #### 方法引用

  方法引用提供了一个很有用的语义来直接访问类或者实例的已经存在的方法或者构造方法。

  方法引用可以通过方法的名字来引用其本身。方法引用是通过`::`符号（双冒号）来描述的。

  它可以用来引用下列类型的方法：

  - 构造器引用。语法是 Class::new，或者更一般的 Class< T >::new，要求构造器方法是没有参数；
  - 静态方法引用。语法是 Class::static_method。
  - 特定类的任意对象方法引用。它的语法是 Class::method。
  - 特定对象的方法引用，它的语法是 instance::method。

  ```java
  // LambdaTest.java
  import java.util.List;
  import java.util.ArrayList;
  
  public class LambdaTest {
  
      public static void main(String args[]){
          List<String> names = new ArrayList<>();
  
          names.add("Peter");
          names.add("Linda");
          names.add("Smith");
          names.add("Zack");
          names.add("Bob");
  
          //     通过System.out::println引用了输出的方法
          names.forEach(System.out::println);
      }
  }
  ```

  ```
  $ javac LambdaTest.java
  $ java LambdaTest
  Peter
  Linda
  Smith
  Zack
  Bob
  ```

