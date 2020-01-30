# Python3

## 标识符

- 第一个字符必须是字母表中字母或下划线 **_** 。
- 标识符的其他的部分由字母、数字和下划线组成。
- 标识符对大小写敏感。

## 注释

Python中单行注释以 **#** 开头

```
#第一行代码
print ("Hello,world!")  #没有以;结尾
```

执行以上代码，输出结果为：

```
Hello, world!
```

多行注释可以用多个 **#** 号，还有 **'''** 和 **"""**：

```
#注释1
#注释2
'''
注释3
注释4
'''
"""
注释5
注释6
"""
```

## 行与缩进

python最具特色的就是使用缩进来表示代码块，不需要使用大括号 **{}** 。

缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。

## 多行语句

Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句

```
total = item_one + \
        item_two + \
        item_three
```

在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：

```
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
```

## 数字(Number)类型

python中数字有四种类型：整数、布尔型、浮点数和复数。

- **int** (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
- **bool** (布尔), 如 True。
- **float** (浮点数), 如 1.23、3E-2
- **complex** (复数), 如 1 + 2j、 1.1 + 2.2j

## 字符串(String)

- python中单引号和双引号使用完全相同。
- 使用三引号('''或""")可以指定一个多行字符串。
- 转义符 '\'
- 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
- 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
- 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
- Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
- Python中的字符串不能改变。
- Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
- 字符串的截取的语法格式如下：**变量[头下标:尾下标:步长]**

```
str='robot'

print(str)          # 输出字符串
print(str[0:-1])    # 输出第一个到倒数第二个的所有字符
print(str[0])       # 输出字符串第一个字符
print(str[2:5])     # 输出从第三个开始到第五个的字符
print(str[2:])      # 输出从第三个开始后的所有字符
print(str*2)        # 输出字符串两次
print(str+' hello') # 连接字符串

print('------------------------------')

print('hello\nrobot') # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrobot')# 在字符串前面添加一个 r，表示原始字符串，不会发生转义
```

output：

```
robot
robo
r   
bot
bot
robotrobot
robot hello
------------------------------
hello
robot
hello\nrobot
```

## 空行

函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。

空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

**记住：**空行也是程序代码的一部分。

## 等待用户输入

```
a=input("input：")
print(type(a))
print(a)
```

type函数显示其括号内容的数字类型

## 同一行显示多条语句

Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，

```
import sys;x='runoob';sys.stdout.write(x+'\n')
```

# sys模块

### sys.argv

**获取命令行参数，返回值是List，第一个元素是程序本身**

```
import sys
print(sys.argv)
```

1.输入一个参数

测试：

```
PS C:\Users\86188\Desktop\python3> 52
52
PS C:\Users\86188\Desktop\python3>
```

2.若输入两个参数中空格隔开（结果：会产生错误）

测试：

```
PS C:\Users\86188\Desktop\python3> 32  21
所在位置 行:1 字符: 5
+ 32  21
+     ~~
表达式或语句中包含意外的标记“21”。
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : UnexpectedToken
```

小结：sys.argv 只能输入单一参数并输出

修改程序

```
import sys
print(eval(sys.argv[1]))
```

测试：

```
PS C:\Users\86188\Desktop\python3> 6+2+3
11
PS C:\Users\86188\Desktop\python3> 6+5+2+3+5+2
23
PS C:\Users\86188\Desktop\python3> 6*2
12
PS C:\Users\86188\Desktop\python3> 5/3
1.66666666666667
```

能够进行数学运算，输出运算结果

说明sys.argv获得的是输入值的字符串类型

#### eval() 函数

eval() 函数用来执行一个字符串表达式，并返回表达式的值。

```
x=5
print(eval('2+x'))
```

input

```
7
```

### sys.exit(n)

**程序退出，如果是正常退出是sys.exit(0)，这里的参数可以自己填，但是对于程序是怎样退出的应该传参是几，应该自己定义好，这样别人在运行你的程序的时候才知道你是怎样退出的，是正餐退出还是意外退出。**

**例子**：

```dart
import sys
print('hello')
sys.exit(0)
print('python')
```

运行程序后发现在，程序输出`hello`后并没有继续输出`python`。因为在执行到`sys.exit(0)`的时候程序就结束了。

小结：sys.exit(n)函数用来执行退出程序操作

### sys.version

**获取Python解释程序的版本信息**

### sys.maxsize

**获取最大的Int值**

### sys.path

**返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值**
 比如就是我们在python源文件中`import`引入模块的时候就会在`sys.path`的目录中查找相应的模块，如果在这里面的目录中没有找到你要倒入的模块则会报错。

返回值是一个`list`则我们如果想倒入一个自定义模块下面的的包或者是模块则可以使用`list`的`append`方法在PYTHONPATH环境变量中增加相应的路径。

### sys.platform

**返回操作系统的名称**

### sys.stdout, sys.stdin, sys.stderror

**分别和输出输入，错误输出相关**

```css
sys.stdout.write(str)
```

`sys.stdout.write`和`print` 都是输出相关的函数`print`内部也是调用的`sys.stdout`，`sys.stdout`默认输出是屏幕。

```python
import sys
s = 'test stdout'

print('--')
sys.stdout.write(s)
print('--')

class A(object):
    pass

print(A)

sys.stdout.write(A)
```

`print` 什么类型都可以输出，但是`sys.stdout.write`只可以输出字符串类型,否则报错。`print`默认是最后换行，但是`sys.stdout.write`默认不换行。
 下面看我在百度找到的别人大佬写的一段代码：

```python
import sys
file = sys.stdout    # 存储原始的输出对象
sys.stdout = open('1.txt', 'w')  # 重定向所有的写入内容到 1.txt 文件,
print('Citizen_Wang')   # 写入到 1.txt 文件中，在上一行语句中改变了输出流到文件中
print('Always fall in love with neighbours')  # 继续写入到文件中
sys.stdout.close()    # 其实就是 open 文件之后的关闭
sys.stdout = file  # 将 print 命令的结果返回给控制台
print('输出信息返回在控制台')  # 该信息会在控制台也显示
```

#### 下面讲一个有趣的实例(python实现命令行进度提示)：

特别是在使用linux下载依赖或者软件的时候，都会提示一个百分数的进度，这种进度提示是怎么实现的呢？

我猜你肯定知道`\n`, `\t`, `\d`等转移字符，但是你应该不知道、`\r`这个转移字符，这个转移字符有什么用呢？看如下代码：

```swift
import time
import sys

for i in range(20):
    print("个测试数据" + str(i), end="")
    sys.stdout.flush()    # 刷新缓冲区
    time.sleep(1)
```

`sys.stdout.flush()`的作用：强制输出缓冲区的内容, 同时缓冲区被清空。
 这是一个简单的不能再简单的代码了，但是注意这里一直**没有输出换行**，接着看下面的代码，感受其中`\r`的作用：

```swift
import time
import sys

for i in range(20):
    if i%5 == 0:
        print("\r", end="")
    print("个测试数据" + str(i), end="")
    sys.stdout.flush()
    time.sleep(1)
```

当我们输出`\r`的时候，在一行中并且在`\r`前的所有字符将被清理掉。修改下代码继续运行测试：

```swift
import time
import sys

for i in range(20):
    if i%5 == 0:
        print("\r", end="")
    print("个测试数据" + str(i)) # 去掉了, end=""，末尾会打印出换行
    sys.stdout.flush()
    time.sleep(1)
```

当出现换行时，并不会清理掉在`\r`字符前的内容，所以`\r`只会清理掉只在一行中的内容。
 **补充**, 这样更能理解

```swift
import time
import sys

for i in range(20):
    print("\r", end="")
    time.sleep(1)
    print("个测试数据" + str(i), end="")
    sys.stdout.flush()
    time.sleep(1)
```

我们清楚了`\r`的用法那就可以实现一个**命令行进度提示**了：

```python
import sys
import time

print("downloading：")
def view_bar(num, total):
    rate = float(num) / float(total)
    rate_num = int(rate * 100)
    r = "\r"+("="*(2*rate_num//10)+">")+(" "*(20-2*rate_num//10))+'%d%%' % (rate_num, )
    sys.stdout.write(r)
    sys.stdout.flush() # 刷新缓冲区


if __name__ == '__main__':
    for i in range(0, 101):
        time.sleep(0.01)
        view_bar(i, 100)


print("\ndownload successful\n")
```

## Print 输出

print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 **end=""**：

```
x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('---------')
# 不换行输出
print( x, end=" " )
print( y, end=" " )
print()
```

output：

```
a
b
---------
a b
```

## import 与 from...import

在 python 用 **import** 或者 **from...import** 来导入相应的模块。

将整个模块(somemodule)导入，格式为： **import somemodule**

从某个模块中导入某个函数,格式为： **from somemodule import somefunction**

从某个模块中导入多个函数,格式为： **from somemodule import firstfunc, secondfunc, thirdfunc**

将某个模块中的全部函数导入，格式为： **from somemodule import \***

**导入sys模块**

```
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
```

**导入sys模块的argv，path成员**

```
from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path
```

