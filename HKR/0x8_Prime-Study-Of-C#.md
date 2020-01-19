# 初入C#

首先使用C#语言说出第一个问候：Hello World !

> **using** System;																*/\* **using** 用于在程序中包含 **System** 命名空间\*/*
> **namespace** HelloWorldApplication{						*/\* 一个 **namespace** 里包含了一系列的类\*/*
> 		**class** HelloWorld{												*/\* 类包含了程序使用的数据和方法声明,一般多个方法\*/*
> 				**static** **void** Main(**string**[] args){				*/\* **Main** 方法，所有 C# 程序的 **入口点**\*/*		
> 						*/\* 定义在System命名空间的Console类的一个方法，该语句会在屏幕上显示：Hello World!\*/*
> 						Console.WriteLine("Hello World");	
> 						Console.ReadKey();							*/\* 等待一个按键的动作\*/*
> 				}
> 		}
> } 



### C# 数据类型

- 值类型（Value types）

   值类型直接包含数据。比如 **int、char、float**，它们分别存储数字、字符、浮点数。当您声明一个 **int** 类型时，系统分配内存来存储值。 

- 引用类型（Reference types）

   引用类型不包含存储在变量中的实际数据，但它们包含对变量的引用。 

   换句话说，它们指的是一个内存位置。使用多个变量时，引用类型可以指向一个内存位置。如果内存位置的数据是由一个变量改变的，其他变量会自动反映这种值的变化。**内置的** 引用类型有：**object**、**dynamic** 和 **string**。 

- 指针类型（Pointer types）

   指针类型变量存储另一种类型的内存地址。C# 中的指针与 C 或 C++ 中的指针有相同的功能。 



### ref与out关键字的使用
- ref关键字可以让值类型的变量在方法参数传递时按照引用类型传递。即在方法里面修改值，方法外的那个实参也会被修改。需要注意的是，在调用方法的时候需要在变量名前面加上ref关键字说明一下，在定义方法时，也需要在形参的数据类型前面加上ref关键字；同时要注意的是，使用ref传递的参数必须有初值才行。

- out关键字也可以让值类型的数据在传递的时候按照引用类型传递，不同于ref的是，out关键字主要是用来获取一个结果，ref是为了传参。当我们的方法需要返回多个返回值时，我们可以使用out关键字用来获取想要返回的结果，然后在方法内部对其进行赋值。在调用的时候同样需要加上out关键字标明，在调用前对值没有要求。

- ref使用案例：

     > public class Child{
     >          public int age = 9;
     >   }
     >   class Program{
     >          static void Main(string[] args){
     >                 int age = 3;
     >                 Child xiaoming = new Child();
     >                 Console.WriteLine("我今年{0}岁了！",age);
     >                 Console.WriteLine("小明今年{0}岁了！",xiaoming.age);
     >                 Add(ref age);
     >                 Add(ref xiaoming.age);//参数为类的字段也可以
     >                 Console.WriteLine("我今年{0}岁了！",age);
     >                 Console.WriteLine("小明今年{0}岁了！",xiaoming.age);
     >                 Console.ReadKey();
     >          }
     >          static public void Add(ref int age){
     >                 age++;
     >                 Console.WriteLine("长大一岁了！");
     >          }
     >   }

- out使用案例： 

  > class Program{
  >       static void Main(string[] args){
  >                    //使用out关键字可以让方法返回多个值
  >                    int td, yd = 9;
  >                    GetData(out td,out yd);
  >                    Console.WriteLine("昨天是{0}号，今天是{1}号。",yd,td);
  >                    Console.ReadKey();
  >             }
  >             static public void GetData(out int td,out int yd){
  >                    //方法内部必须为其赋值
  >                    td = 13;
  >                    yd = 12;
  >             }
  >      }

