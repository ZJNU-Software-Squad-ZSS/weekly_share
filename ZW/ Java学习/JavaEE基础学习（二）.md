### JavaEE基础学习（二）

#### 标识符与关键字

##### 标识符

标识符是类、变量和方法等的名字，标识符区分大小写，未规定最大长度。

1.Java中的标识符可以包括空格外的任何字符；

2.标识符必须以字母、美元符号、下划线字符作为开头，也不能用Java语言的关键字来作为标识符；

3.与C/C++语言不同的是，Java语言还可以将一些非拉丁字母（如汉字）包含在标识符中，原因是Java使用的是Unicode字符集。

##### 关键字

Java有48个关键字：

abstract,boolean,break,byte,case,cast,catch,char,class,continue,default,do,double,else,extends,false,final,finally,float,for,if,implements,import,instanceof,int,interface,long,native,new,null,package,private,protected,public,return,short,static,super,switch,synchronized,this,throw,throws,transient,true,try,void,volatile,while.

注意：

1.true、false和null为小写，而不是像C++语言中为大写；

2.无sizeof运算符；

3.goto和const不是Java编程语言中使用的关键字。

#### 数据类型

数据类型指定变量可以包含的数据的类型。

除了null，Java数据类型可以分为基本数据类型、引用类型两大类。

Java结构类型图如图：

![](图片\java 2-1.JPG)

在Java中“引用”是指向一个对象在内存中的位置，在本质上是一种带有很强的完整性和安全性限制的指针，当声明某个类、接口或数组类型的一个变量时，那个变量的值总是某个对象的引用或者时null引用。与C++中指针不同的是，指针可以有++、--运算，而引用无此运算。

Java具有8个基本数据类型，可以分为4大类：布尔型、字符型、整数型和浮点型。

可用int、short、long和byte4个数据类型来包含整数类型。使用double和float两个数据类型来包含浮点数据。基本数据类型boolean只包含两个可能值中的一个：true或false。

对包含单一字符文本的变量使用基本数据类型char。若要显示具有一个以上字符的文本，则使用String类。

Java还为每个原始类型提供了封装类，如下表：

| 原始类型 | boolean | char      | byte | short | int     | long | float | double |
| -------- | ------- | --------- | ---- | ----- | ------- | ---- | ----- | ------ |
| 封装类   | Boolean | Character | Byte | Short | Integer | Long | Float | Double |

引用类型和原始类型具有不同的语义，它们的行为完全不同。假定一个方法中有两个局部变量，一个变量为int原始类型，另一个变量是对一个Integer对象的引用，不能对原始类型调用方法，但可以对引用类型调用方法。