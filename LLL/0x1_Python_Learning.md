# 0x1_Python_Learning

学习Python的基本概念，主要介绍Python语言的不同之处。

## 函数

函数是重用的程序段，它通过 def 关键字定义。def 关键字后跟一个函数的标识符名称，然后跟一对圆括号。圆括号之中可以包括一些变量名，该行以冒号结尾。接下来是一块语句，它们是函数体。

调用函数，你可以在你的程序的任何地方使用这个函数标志符名称且任意多次地运行这个语句块。

**局部变量**

当你在函数定义内声明变量的时候，它们与函数外具有相同名称的其他变量没有任何关系，即变量名称对于函数来说是局部的。

```python
def sayHello(e):
    print(e + ', Hello World!')  # e为局部变量，与函数外具有相同名称的其他变量没关系

e='Lisa'
sayHello('John')
```

结果为：![Kxo3ZT.png](https://s2.ax1x.com/2019/11/04/Kxo3ZT.png)

在调用sayHello(e)函数时，传过去的实参为John，即形参e的值为John，与函数外的e的值无关。

**全局变量**

如果你想要为一个定义在函数外的变量赋值，那么你就得告诉 Python 这个变量名不是局部的，而是全局的。我们使用 **global** 语句完成这一功能。即在函数内为函数外的变量赋值，需要告诉函数这个变量是全局变量。

```python
def sayHello(e):
    print(e + ', Hello World!')  # e为局部变量，与函数外具有相同名称的其他变量没关系
    global name  # global定义全局变量，可指定多个全局变量，如global a,b,c
    name = 'Bian'
    print(name + ', Hello World!')
    
e = 'Lisa'
name = 'Wang'
sayHello('John')
print(name)
```

结果为：![Kxvk1U.png](https://s2.ax1x.com/2019/11/04/Kxvk1U.png)

使用global就是告诉sayHello这个函数，name是全局变量。因此如果在函数内改变name的值，最终不管是函数内还是函数外，name的值都会发生变化。

如果不使用global，则在sayHello函数内name变量是局部变量，不会影响函数外name变量的值。

```python
def sayHello(e):
    print(e + ', Hello World!')  # e为局部变量，与函数外具有相同名称的其他变量没关系
    # global name  # global定义全局变量，可指定多个全局变量，如global a,b,c
    name = 'Bian'
    print(name + ', Hello World!')
    
e = 'Lisa'
name = 'Wang'
sayHello('John')
print(name)
```

结果为：![KxX6xg.png](https://s2.ax1x.com/2019/11/04/KxX6xg.png)

此时，函数内name是局部变量，不论如何变化，都不会影响函数外name的值。

**默认参数值**

对于一些函数，你可能希望它的一些参数是可选的，如果用户不想要为这些参数提供值的话，这些参数就使用默认值。这个功能借助于默认参数值完成。你可以在函数定义的形参名后加上赋值运算符（=）和默认值，从而给形参指定默认参数值。

```python
def say(message, times=1):
# 其中times，如果用户没有提供times的值，它的默认参数值为1；申明形参时，有默认参数值的形参必须放在末尾
    print(message * times)
    
say('Hello')
say('Baek', 5)
```

结果为：![KxxoJP.png](https://s2.ax1x.com/2019/11/04/KxxoJP.png)

**关键参数**

如果你的某个函数有许多参数，而你只想指定其中的一部分，那么你可以通过命名来为这些参数赋值——这被称作
关键参数——我们使用**名字（关键字）**而不是位置（我们前面所一直使用的方法）来给函数指定实参。

```python
def func(a, b=5, c=10):
    print('a is', a, 'b is', b, 'c is', c)
    return None  # 每个函数结尾都暗含该语句，None表示没有任何东西的特殊类型

# 关键参数，使用名字来给函数指定实参，而不是位置
# 优势：1.不必担心参数顺序 2.假设其他参数都有默认值，我们可以只给我们想要的那些参数赋值
func(3, 7)
func(25, c=24)
func(c=50, a=100)
```

结果为：![KxzMQO.png](https://s2.ax1x.com/2019/11/04/KxzMQO.png)

func(3 , 7)中没有指定关键参数，但有两个默认参数值b与c，所以3,7,分别按顺序对于a,b，c为默认值10；

func(25 , c=24)中指定了关键参数c，所以a按顺序为25，b为默认参数值为5，c为指定参数值24；

func(c=50 , a=100)中指定了c与a两个关键参数，无关顺序，因此a为指定参数值100，b为默认参数值5，c为指定参数值50。

**return语句**

- return 语句用来从一个函数返回，即跳出函数。我们也可选从函数返回一个值。

- 没有返回值的 return 语句等价于 return None。None 是 Python 中表示没有任何东西的特殊类型。（上面的例子）

- 除非你提供你自己的 return 语句，每个函数都在结尾暗含有 return None 语句。

  ```python
  def maximum(a, b):
      if a > b:
          return a
      else:
          return b
  
  print(maximum(3, 7))
  ```

  结果为：![KzpFa9.png](https://s2.ax1x.com/2019/11/04/KzpFa9.png)

**pass语句**

pass 语句在 Python 中表示一个空的语句块。

```python
def someFunc():
    pass        # pass语句表示一个空的语句块
```

**DocStrings 文档字符串**

DocStrings 是一个重要的工具，由于它帮助你的程序文档更加简单易懂，你应该尽量使用它。你甚至可以在程序运行的时候，从函数恢复文档字符串！下面"""所包含的内容就是文档字符串。

```python
def printMax(x, y):
    # 文档字符串，DocStrings，适用于模块和类
    # 惯例：一个多行字符串，首行以大写字母开始，句号结尾；第二行是空行；第三行开始是详细的描述
    """Prints the maximum of two numbers.

    The two values must be integers."""
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is the maximum')

printMax(3, 5)
print(printMax.__doc__)     # 调用函数的文档字符串属性
help(printMax)      # 抓取函数的doc属性
```

结果为：

![Kz9I0g.png](https://s2.ax1x.com/2019/11/04/Kz9I0g.png)

 其中help()，抓取函数的 doc 属性，然后整洁地展示给你。

## Reference

[1]沈洁元. 简明Python教程-v1.1.pdf. 极客学院出版. [online] Available at:  www.byteofpython.info [Accessed 5 Nov. 2019].



> 此次学习过程主要通过运行代码直观地进行理解，代码为exe2.py

