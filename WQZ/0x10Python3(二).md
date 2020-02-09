# Python3(二)

# Python3 基本数据类型

**Python 中的变量不需要声明。每个变量在使用前都必须赋值**，变量赋值以后该变量才会被创建。

在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。

等号（=）用来给变量赋值。

等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：

```
counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串
 
print (counter)
print (miles)
print (name)
```

input：

```
100
1000.0
runoob
```

### 多个变量赋值

Python允许你同时为多个变量赋值。例如：

```
a = b = c = 1
```

以上实例，创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。

您也可以为多个对象指定多个变量。例如：

```
a, b, c = 1, 2, "runoob"
```

以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。

## 标准数据类型

Python3 中有六个标准的数据类型：

- Number（数字）
- String（字符串）
- List（列表）
- Tuple（元组）
- Set（集合）
- Dictionary（字典）

Python3 的六个标准数据类型中：

- **不可变数据（3 个）：**Number（数字）、String（字符串）、Tuple（元组）；
- **可变数据（3 个）：**List（列表）、Dictionary（字典）、Set（集合）。

## Number（数字）

Python3 支持 **int、float、bool、complex（复数）**。

在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。

像大多数语言一样，数值类型的赋值和计算都是很直观的。

内置的 type() 函数可以用来查询变量所指的对象类型。

```
>>> a, b, c, d = 20, 5.5, True, 4+3j
>>> print(type(a), type(b), type(c), type(d))
<class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
```

此外还可以用 isinstance 来判断：

```
a=111
print(isinstance(a,bool))
print(isinstance(a,int))

output：
False
Ture
```

isinstance 和 type 的区别在于：

- type()不会认为子类是一种父类类型。
- isinstance()会认为子类是一种父类类型。

当你指定一个值时，Number 对象就会被创建：

```
var1 = 1
var2 = 10
```

您也可以使用del语句删除一些对象引用。

您可以通过使用del语句删除单个或多个对象。例如：

```
del var
del var_a, var_b
```

测试

```
var1=25
var2=36
print(var1)
del var1
print(var1)
```

结果

```
25
Traceback (most recent call last):
  File "c:\Users\86188\Desktop\python3\number.py", line 17, in <module>
    print(var1)
NameError: name 'var1' is not defined
```

删除之后要重新赋值

### 数值运算

```
print(5//3) #整除
print(2**4) #乘方
```

Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型

## String（字符串）

Python中的字符串用单引号 **'** 或双引号 **"** 括起来，同时使用反斜杠 \ 转义特殊字符。

![11vEZV.png](https://s2.ax1x.com/2020/01/31/11vEZV.png)

加号 **+** 是字符串的连接符， 星号 ***** 表示复制当前字符串，紧跟的数字为复制的次数。

## List（列表）

List（列表） 是 Python 中使用最频繁的数据类型。

列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

列表是写在方括号 **[]** 之间、用逗号分隔开的元素列表。

和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。

```
list=['abc',2.53,40,'dfg',5]
list2=['flower',22]
print(list)
print(list[0])
print(list[2:4])  #第一个2是指从0开始算是第3个数，第二个4是指从1开始算第4个数
print(list[2:])
print(list*2)
print(list+list2) #list只能和list连接
```

output：

```
['abc', 2.53, 40, 'dfg', 5]
abc
[40, 'dfg']
[40, 'dfg', 5]
['abc', 2.53, 40, 'dfg', 5, 'abc', 2.53, 40, 'dfg', 5]
['abc', 2.53, 40, 'dfg', 5, 'flower', 22]
```

与Python字符串不一样的是，列表中的元素是可以改变的：

```
list=['abc',2.53,40,'dfg',5]
print(list)

list[1]=3.3
print(list)

list[2:5]=[16,17,18]
print(list)
```

output

```
['abc', 2.53, 40, 'dfg', 5]
['abc', 3.3, 40, 'dfg', 5]
['abc', 3.3, 16, 17, 18]
```

## Tuple（元组）

元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 **()** 里，元素之间用逗号隔开。

```
tuple=(1,2.5,'like',3.6)

print(tuple)
print(tuple[0])
print(tuple[1:])
print(tuple[1:3])
print(tuple*2)
```

## Set（集合）

集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。

基本功能是进行成员关系测试和删除重复元素。

可以使用大括号 **{ }** 或者 **set()** 函数创建集合，注意：创建一个空集合必须用 **set()** 而不是 **{ }**，因为 **{ }** 是用来创建一个空字典。

创建格式：

```
parame = {value01,value02,...}
或者
set(value)
```

测试：

```
student={'Tom','Annie','Bob','Tom',22}

print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Rose' in student :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')

 
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
 
print(a)
 
print(a - b)     # a 和 b 的差集
 
print(a | b)     # a 和 b 的并集
 
print(a & b)     # a 和 b 的交集
 
print(a ^ b)     # a 和 b 中不同时存在的元素
```

output：

```
PS C:\Users\86188\Desktop\python3> python -u "c:\Users\86188\Desktop\python3\set.py"
{'Annie', 'Tom', 'Bob', 22}
Rose 不在集合中
{'a', 'c', 'r', 'b', 'd'}
{'d', 'b', 'r'}
{'a', 'c', 'm', 'l', 'b', 'r', 'z', 'd'}
{'a', 'c'}
{'m', 'd', 'l', 'b', 'r', 'z'}
```

## Dictionary（字典）

字典（dictionary）是Python中另一个非常有用的内置数据类型。

<u>列表是有序的对象集合，字典是无序的对象集合。</u>两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用 **{ }** 标识，它是一个无序的 **键(key) : 值(value)** 的集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。

```
dict={}
dict['one']='你好'
dict[2]='I\'m fine'

dict2={'name':'runboob','code':1,'site':'www.runboob.com'}

print(dict['one'])       # 输出键为 'one' 的值
print(dict[2])           # 输出键为 2 的值
print(dict2)             # 输出完整的字典
print(dict2.keys())      # 输出所有键
print(dict2.values())    # 输出所有值
```

output：

```
你好
I'm fine
{'name': 'runboob', 'code': 1, 'site': 'www.runboob.com'}
dict_keys(['name', 'code', 'site'])
dict_values(['runboob', 1, 'www.runboob.com'])
```

## Python成员运算符

| 运算符 | 描述                                                    | 实例                                              |
| :----- | :------------------------------------------------------ | :------------------------------------------------ |
| in     | 如果在指定的序列中找到值返回 True，否则返回 False。     | x 在 y 序列中 , 如果 x 在 y 序列中返回 True。     |
| not in | 如果在指定的序列中没有找到值返回 True，否则返回 False。 | x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。 |

测试：

```
list=['adc','end',2,50,3.3]
a=5
b=3.3

if (a in list) :
    print('a in list')
else :
    print('a not in list')

if (b not in list) :
    print('b not in list')
else :
    print('b in list')

a=50

if(a in list) :
    print('a in list')
else :
    print('a not in list')
```

output：

```
a not in list
b in list
a in list
```

斐波那契数列

```
a,b=0,1
while b<10 :
    print(b,end=',')
    a,b=b,a+b
```

# Python3 条件控制

Python 条件语句是通过一条或多条语句的执行结果（True 或者 False）来决定执行的代码块。

## if 语句

```
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
```

Python 中用 **elif** 代替了 **else if**，所以if语句的关键字为：**if – elif – else**。

**注意：**

- 1、每个条件后面要使用冒号 **:**，表示接下来是满足条件后要执行的语句块。
- 2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
- 3、在Python中没有switch – case语句。

```
var1,var2=1,0

if var1 :
    print('1_true')
    print(var1)

if var2 :
    print('2_true')
    print(var2)
print('bye')
```

input：

```
1_true
1
bye
```

狗的年龄计算

```
age=int(input("请输入你家狗的年龄："))

if age<=0 :
    print('are you kidding me')
if age==1 :
    print('相当于14岁的人')
if age==2 :
    print('相当于22岁的人')
if age>2 :
    human=22+(age-2)*5
    print("对应人类的年龄：",human)

input("点击 enter 键退出")
```

output：

```
请输入你家狗的年龄：2
相当于22岁的人
点击 enter 键退出
```

## while 循环

Python 中 while 语句的一般形式：

```
while 判断条件(condition)：
    执行语句(statements)……
```

同样需要注意冒号和缩进。另外，在 Python 中没有 do..while 循环。

计算1~100之和

```
n=100
count=1
sum=0
while count<=100 :
    sum+=count
    count+=1           #count++用不了
print(sum)
```

python中没有++，--     

### while 循环使用 else 语句

在 while … else 在条件语句为 false 时执行 else 的语句块。

## for 语句

Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

for循环的一般格式如下：

```
for <variable> in <sequence>:
    <statements>
else:
    <statements>
```

实例

```
languages=['C','C++','java','Python']

for x in languages :
    print(x)
```

output：

```
C
C++
java
Python
```

以下 for 实例中使用了 break 语句，break 语句用于跳出当前循环体：

```
sites=['Baidu','Google','firefox','taobao']

for site in sites :
    if site=='Google' :
         print(site,"break")
         break
    print(site)
```

output：

```
Baidu
Google break
```

## range()函数

如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，例如:

```
for i in range(5) :
    print(i)
```

output：

```
0
1
2
3
4
```

- start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
- stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
- step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

使用range指定区间的值：

```
for i in range(2,8) :
    print(i)
```

也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):

```
for i in range(0,100,10) :
    print(i)
```

最后一个数表示步长

负数：

```
for i in range(-1,-10,-2) :
    print(i)
```

还可以使用range()函数来创建一个列表：

```
>>>list(range(5))
[0, 1, 2, 3, 4]
```

## pass 语句

Python pass是空语句，是为了保持程序结构的完整性。

pass 不做任何事情，一般用做占位语句

# 函数

函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

函数能提高应用的模块性，和代码的重复利用率。

## 定义一个函数

你可以定义一个由自己想要功能的函数，以下是简单的规则：

- 函数代码块以 **def** 关键词开头，后接函数标识符名称和圆括号 **()**。
- 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
- 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
- 函数内容以冒号起始，并且缩进。
- **return [表达式]** 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。

测试：

```
def hello():
    print('hellow world')

hello()
```

函数中带上参数变量:

```
def area(width,height) :
    return width*height

def print_welcome(name) :
    print('welcome',name)

print_welcome('queen')

a=4
b=6
print(area(a,b))
```

### 可更改(mutable)与不可更改(immutable)对象

在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

### python 传不可变对象实例

```
a=2
def changenum(x) :
    x=10

changenum(a)

print(a)
```

output：2

### 传可变对象实例

可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：

```
def changelist(list) :
    list.append([1,2,3,4])
    print('函数内取值：',list)
    return

mylist=[10,5,3,88]

changelist(mylist)

print('函数外取值：',mylist)
```

output：

```
函数内取值： [10, 5, 3, 88, [1, 2, 3, 4]]
函数外取值： [10, 5, 3, 88, [1, 2, 3, 4]]
```

### 不定长参数

你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下：

```
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
```

加了星号 ***** 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。

```
def print_info(arg,*tuple) :
    print(arg,tuple)

print_info(50,'hello',2.5)
```

output：

```
50 ('hello', 2.5)
```

还有一种就是参数带两个星号 ***\***基本语法如下：

```
def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
```

加了两个星号 ***\*** 的参数会以字典的形式导入。

```
def printinfo(arg,**vardict) :
    print(arg,vardict)

printinfo(1,a='2',b='3')
```

output：

```
1 {'a': '2', 'b': '3'}
```

输入参数时也必须以字典形式输入

声明函数时，参数中星号 ***** 可以单独出现，例如:

```
def f(a,b,*,c):
    return a+b+c
```

如果单独出现星号 ***** 后的参数必须用关键字传入。

```
>>> def f(a,b,*,c):
...     return a+b+c
... 
>>> f(1,2,3)   # 报错
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes 2 positional arguments but 3 were given
>>> f(1,2,c=3) # 正常
6
>>>
```

