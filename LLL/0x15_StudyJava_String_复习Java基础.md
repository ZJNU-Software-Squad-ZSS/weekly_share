# StudyJava——复习Java基础

1. 问题：string字符串是不可变的，那如何将字符串里的空格去除呢？

   方法：用StringBuilder构造一个新变量，将空格删除。

   【例】从控制台输入一行字符串—>去除字符串中的所有空格—>打印去除空格后的字符串

   ```java
   import java.util.Scanner;
   public class StudyJava1 {
       public static void main(String[] args) {
           Scanner in = new Scanner(System.in);
           String a = in.nextLine();
           StringBuilder stringBuilder = new StringBuilder(a);
           for(int i=0;i<stringBuilder.length();i++){
               if(stringBuilder.charAt(i)==' '){
                   stringBuilder.deleteCharAt(i);
                   i--;
               }
           }
           System.out.println(stringBuilder);
       }
   }
   ```

2. 最大最小值问题

   【例】现给出一串数据（313, 89, 123, 323, 313, 15, 90, 56, 39）求出最小值和最大值并输出。

   ```java
   import java.util.Arrays;
   public class MaxAndMin {
       public static void main(String[] args) {
           int[] data = {313, 89, 123, 323, 313, 15, 90, 56, 39};
           //方法一
           Arrays.sort(data);
           System.out.println(data[0]);
           System.out.println(data[data.length - 1]);
           //方法二
           System.out.println(Arrays.stream(data).min().getAsInt());
           System.out.println(Arrays.stream(data).max().getAsInt());
       }
   }
   ```

3. 向上转型（即父类引用指向子类对象），在运行时，会遗忘子类对象中与父类对象中不同的方法，也会覆盖与父类中相同的方法——重写。（方法名，参数都相同）

   > 注：不能使用一个子类的引用去指向父类的对象。

   ```java
   class Animal {
       //父类方法
       public void bark() {
           System.out.println("动物叫！");
       }
   }
   
   class Dog extends Animal {
       //子类重写父类的bark方法
       public void bark() {
           System.out.println("汪、汪、汪！");
       }
       //子类自己的方法
       public void dogType() {
           System.out.println("这是什么品种的狗？");
       }
   }
   
   public class Test {
       public static void main(String[] args) {
           Animal a = new Animal();
           Animal b = new Dog();
           Dog d = new Dog(); 
   
           a.bark();
           b.bark();
           //b.dogType()编译不通过
           d.bark();
           d.dogType();
       }
   }
   ```

4. 多态

   - 三个必要条件：继承、重写和向上转型（即父类引用指向子类对象）

   - 实现方式：继承父类进行方法重写，抽象类和抽象方法，接口实现

5. 抽象类和抽象方法：限制规定子类必须实现某些方法，但不关注实现细节

   - 用 abstract 修饰符定义抽象类

   - 用 abstract 修饰符定义抽象方法，只用声明，不需要实现

   - 包含抽象方法的类就是抽象类

   - 抽象类中可以包含普通的方法，也可以没有抽象方法

   - 抽象类的对象不能直接创建，通常是定义引用变量指向子类对象。

     - 需要子类实现的抽象方法

     ```java
     //抽象类
     public abstract class TelePhone {
         public abstract void call();  //抽象方法,打电话
         public abstract void message(); //抽象方法，发短信
     }
     ```

     - 构建子类，并实现抽象方法

     ```java
     public class CellPhone extends TelePhone {
     
         @Override
         public void call() {
             System.out.println("我可以打电话！");
         }
     
         @Override
         public void message() {
             System.out.println("我可以发短信！");
         }
     
         public static void main(String[] args) {
             CellPhone cp = new CellPhone();
             cp.call();
             cp.message();
         }
     
     }
     ```

     - 运行结果

     ```
     $ javac CellPhone.java TelePhone.java
     $ java CellPhone
     
     我可以打电话！
     我可以发短信！
     ```

6. 接口：用于描述类所具有的功能，而不提供功能的实现，功能的实现需要写在实现接口的类中，并且该类必须实现接口中所有的未实现方法。

   - 接口不能用于实例化对象

   - 接口中方法只能是抽象方法、default 方法、静态方法

   - 接口成员是 static final 类型

   - 接口支持多继承

     - 声明一个 Animal 接口

     ```java
     // Animal.java
     //修饰符 interface A extends 接口1，接口2
     interface Animal {
             //int x;
             //编译错误,x需要初始化，因为是 static final 类型
             int y = 5;
             //不能写方法体
             public void eat();
             public void travel();
     }
     ```

     - 实现上面的接口

     ```java
     // Cat.java
     public class Cat implements Animal{
     
          public void eat(){
              System.out.println("Cat eats");
          }
     
          public void travel(){
              System.out.println("Cat travels");
          }
          public static void main(String[] args) {
             Cat cat = new Cat();
             cat.eat();
             cat.travel();
         }
     }
     ```

     - 编译运行

     ```
     $ javac Cat.java Animal.java
     $ java Cat
     Cat eats
     Cat travels
     ```

7. 内部类

   将一个类的定义放在另一个类的定义内部，这就是内部类。而包含内部类的类被称为外部类。

   - 内部类提供了更好的封装，可以把内部类隐藏在外部类之内，不允许同一个包中的其他类访问该类
   - 内部类的方法可以直接访问外部类的所有数据（方法和属性），包括私有的数据
   - 定义成员内部类后，必须使用外部类对象来创建内部类对象，即 `内部类 对象名 = 外部类对象.new 内部类();`
   - 如果外部类和内部类具有相同的成员变量或方法，内部类默认访问自己的成员变量或方法，如果要访问外部类的成员变量，可以使用 this 关键字

   > 成员内部类不能含有 static 的变量和方法

   ```java
   // People.java
   //外部类People
   public class People {
       private String name = "LiLei";         //外部类的私有属性
       //内部类Student
       public class Student {
           String ID = "20151234";               //内部类的成员属性
           //内部类的方法
           public void stuInfo(){
               System.out.println("访问外部类中的name：" + name);
               System.out.println("访问内部类中的ID：" + ID);
           }
       }
   
       //测试成员内部类
       public static void main(String[] args) {
           People a = new People();     //创建外部类对象，对象名为a
           Student b = a.new Student(); //使用外部类对象创建内部类对象，对象名为b
           // 或者为 People.Student b = a.new Student();
           b.stuInfo();   //调用内部对象的suInfo方法
       }
   }
   ```

8. 静态内部类

   - 静态内部类不能直接访问外部类的非静态成员，但可以通过 `new 外部类().成员` 的方式访问
   - 如果外部类的静态成员与内部类的成员名称相同，可通过`类名.静态成员`访问外部类的静态成员；如果外部类的静态成员与内部类的成员名称不相同，则可通过`成员名`直接调用外部类的静态成员
   - 创建静态内部类的对象时，不需要外部类的对象，可以直接创建 `内部类 对象名= new 内部类();`

   ```java
   // People.java
   //外部类People
   public class People {
       private String name = "LiLei";         //外部类的私有属性
   
   /*外部类的静态变量。
   Java 中被 static 修饰的成员称为静态成员或类成员。它属于整个类所有，而不是某个对象所有，即被类的所有对象所共享。静态成员可以使用类名直接访问，也可以使用对象名进行访问。
   */
       static String ID = "510xxx199X0724XXXX"; 
   
       //静态内部类Student
       public static class Student {
           String ID = "20151234";               //内部类的成员属性
           //内部类的方法
           public void stuInfo(){
               System.out.println("访问外部类中的name：" + (new People().name));
               System.out.println("访问外部类中的ID：" + People.ID);
               System.out.println("访问内部类中的ID：" + ID);
           }
       }
   
       //测试成员内部类
       public static void main(String[] args) {
           Student b = new Student();   //直接创建内部类对象，对象名为b
           b.stuInfo();                 //调用内部对象的suInfo方法
       }
   }
   ```

9. 局部内部类：指内部类定义在方法和作用域内

   ```java
   // People.java
   //外部类People
   public class People {    
       //定义在外部类中的方法内：
       public void peopleInfo() {
           final String sex = "man";  //外部类方法中的常量
           class Student {
               String ID = "20151234"; //内部类中的常量
               public void print() {
                   System.out.println("访问外部类的方法中的常量sex：" + sex);
                   System.out.println("访问内部类中的变量ID:" + ID);
               }
           }
           Student a = new Student();  //创建方法内部类的对象
           a.print();//调用内部类的方法
       }
       //定义在外部类中的作用域内
       public void peopleInfo2(boolean b) {
           if(b){
               final String sex = "man";  //外部类方法中的常量
               class Student {
                   String ID = "20151234"; //内部类中的常量
                   public void print() {
                       System.out.println("访问外部类的方法中的常量sex：" + sex);
                       System.out.println("访问内部类中的变量ID:" + ID);
                   }
               }
               Student a = new Student();  //创建方法内部类的对象
               a.print();//调用内部类的方法
           }
       }
       //测试方法内部类
       public static void main(String[] args) {
           People b = new People(); //创建外部类的对象
           System.out.println("定义在方法内：===========");
           b.peopleInfo();  //调用外部类的方法
           System.out.println("定义在作用域内：===========");
           b.peopleInfo2(true);
       }
   }
   ```

10. 匿名内部类：就是没有名字的内部类。正因为没有名字，所以匿名内部类只能使用一次，它通常用来简化代码编写。但使用匿名内部类还有个前提条件：必须继承一个父类或实现一个接口。

    - 匿名内部类是`不能加访问修饰符`的。要注意的是，`new 匿名类，这个类是要先定义的`
    - 当所在的方法的形参需要在内部类里面使用时，该形参必须为`final`。

    ```java
    // Outer.java
    public class Outer { 
    
        public Inner getInner(final String name, String city) { 
            return new Inner() { 
                private String nameStr = name; 
                public String getName() { 
                    return nameStr; 
                } 
            };
        } 
    
        public static void main(String[] args) { 
            Outer outer = new Outer(); 
            Inner inner = outer.getInner("Inner", "NewYork"); 
            System.out.println(inner.getName()); 
        } 
    } 
    interface Inner { 
        String getName(); 
    }
    ```

    





