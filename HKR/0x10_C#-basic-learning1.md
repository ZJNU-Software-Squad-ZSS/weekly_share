# C# 基础学习

### 1.类型转换

- 强制类型转换
```
double d = 5445.78
int i; 
i = (int)d; 
```
double类型转换为integer类型的结果是：		i=5445



- 一些类型转换方法

| 序号 | 方法 | 描述                                                  |
| :--- | :--- |------------------------------------------------------ |
| 1    | **ToBoolean**  |如果可能的话，把类型转换为布尔型。        |
| 2    | **ToByte**     |把类型转换为字节类型。                |
| 3    | **ToChar**     |如果可能的话，把类型转换为单个 Unicode 字符类型。 |
| 4    | **ToDateTime** |把类型（整数或字符串类型）转换为 日期-时间 结构。 |
| 5    | **ToDecimal**   |把浮点型或整数类型转换为十进制类型。     |
| 6    | **ToDouble**    |把类型转换为双精度浮点型。              |
| 7    | **ToInt16** |把类型转换为 16 位整数类型。                     |
| 8    | **ToInt32** |把类型转换为 32 位整数类型。                     |
| 9    | **ToInt64** |把类型转换为 64 位整数类型。                     |
| 10   | **ToSbyte** |把类型转换为有符号字节类型。                     |
| 11   | **ToSingle** |把类型转换为小浮点数类型。                      |
| 12   | **ToString** |把类型转换为字符串类型。                        |
| 13   | **ToType** |把类型转换为指定类型。                            |
| 14   | **ToUInt16** |把类型转换为 16 位无符号整数类型。              |
| 15   | **ToUInt32** |把类型转换为 32 位无符号整数类型。              |
| 16   | **ToUInt64** |把类型转换为 64 位无符号整数类型。              |



### 2.循环

- while 循环

    在循环头部测试循环条件 

  ```
  while(condition)
  {
     statement(s);
  }
  ```

- for/foreach 循环

  for：和 C语言中相似

  ```
  for ( init; condition; increment )
  {
     statement(s);
  }
  ```

  foreach：迭代数组或者一个集合对象 ，比如：

  ```
  foreach (int element in fibarray)//依次迭代数组内的整型，迭代一次执行一次循环语句
  {
      System.Console.WriteLine(element);//每次循环需要执行的内容
  }
  ```

- do...while 循环

    在循环的尾部检查它的条件。 

   ```
   do{
      statement(s);
   }while( condition );
   ```

- 嵌套循环

    在 while、for 或 do..while 循环内使用一个或多个循环。 



### 3.数组

- 声明一个数组 

  ```
  datatype[] arrayName;
  ```

- 初始化数组

   使用 **new** 关键字来创建数组的实例 ，如：

  ```
  double[] balance = new double[10];
  ```

- 赋值给数组

   赋值给一个单独的数组元素 

  ```
  balance[0] = 4500.0;
  ```

   声明数组的同时给数组赋值 

  ```
  double[] balance = { 2340.0, 4523.69, 3421.0};
  ```

   创建并初始化一个数组 

  ```
  int [] marks = new int[5]  { 99,  98, 92, 97, 95};
  ```

   可省略数组的大小 

  ```
  int [] marks = new int[]  { 99,  98, 92, 97, 95};
  ```

   也可以赋值一个数组变量到另一个目标数组变量中。在这种情况下，目标和源会指向相同的内存位置： 

  ```
  int [] marks = new int[]  { 99,  98, 92, 97, 95};
  int[] score = marks;
  ```

- 访问数组元素

   通过带索引的数组名称来访问 

  ```
  double salary = balance[9];
  ```



**多维数组**

 声明一个 string 变量的二维数组 

```
string [,] names;
```

声明一个 int 变量的三维数组，如下：

```
int [ , , ] m;
```



**传递数组给函数**

如下将main函数中的数组app传递到getAverage函数中

```
double getAverage(int[] arr, int size){
     int i;
     double avg;
     int sum = 0;
     
     for (i = 0; i < size; ++i){
      sum += arr[i];
     }

     avg = (double)sum / size;
     return avg;
}
static void Main(string[] args){
     MyArray app = new MyArray();
     int [] balance = new int[]{1000, 2, 3, 17, 50};
     double avg;

     /*传递数组的指针作为参数*/
     avg = app.getAverage(balance, 5 ) ;

     Console.WriteLine( "平均值是： {0} ", avg );
     Console.ReadKey();
} 
```