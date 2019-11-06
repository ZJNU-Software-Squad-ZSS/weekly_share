# Python Learning v0.1

暑期课程中初次接触Python，想要深入学习之。因此本次学习成果主要是介绍Python的基本概念，以及将Python与之前学习过的语言（比如C，C++）进行对比，比较不同。

## 字符串

字符串是字符的序列 ，字符串基本上就是一组单词。

但是不同于C语言等的字符串表示方法，Python使用字符串是这样的。

**字符串，不可变**

这意味着一旦你创造了一个字符串，你就不能再改变它了。虽然这看起来像是一件坏事，但实际上它不是。我们将会在后面的程序中看到为什么我们说它不是一个缺点。

**按字面意义级连字符串**

如果你把两个字符串按字面意义相邻放着，他们会被 Python 自动级连。例如，"What's" "your name?"会被自动转为"What's your name?"。

```python
print('What\'s''your name?')  # 这只是将两个字符串拼接
print('What\'s', 'your name?')  # 自动转成What's your name?
```

结果：![KXhKsg.png](https://s2.ax1x.com/2019/11/03/KXhKsg.png)

**''与""用法相同**

你可以用单引号或者双引号指示字符串，就如同'Quote me on this'或者"Quote me on this"这样。所有的空白，即空格和制表符都照原样保留。

```python
print('hello world')
print("hello World")
```

他们输出的结果都是一样的：![result](https://s2.ax1x.com/2019/11/03/KXDEef.png)

**三引号'''或"""的用法**

'''与"""可以指示多行的字符串，在三引号里面可以自由的使用单引号和双引号。

```python
e = '''hello pip "install" flask'!' '''
print(e)
```

它的结果如下：![KXrSBV.png](https://s2.ax1x.com/2019/11/03/KXrSBV.png)

**转义符**（\）

1. 在Python中表示字符串 What's your name?。

   > 不能用'What's your name?'来指示它，因为 Python 会弄不明白这个字符串从何处开始，何处结束。

   - 使用转义符来表示

   ```python
   print('What\'s your name')
   ```

   用转义符（\）'来指示单引号——注意这个反斜杠。

   - 使用双引号""来表示

   ```python
   print("What's your name")
   ```

   > 类似地，要在双引号字符串中使用双引号本身的时候，也可以借助于转义符。

2. 行末\表示在下一行继续,不是开始新的行。

   ```python
   print("This is one." \
         "This is two.")
   print("This is one."
         "This is two.")
   print("This is one.\
   This is two.")
   print('''This is one.
   This is two.''')
   ```

   它的输出结果：

   ![KX24PK.png](https://s2.ax1x.com/2019/11/03/KX24PK.png)

   从以上结果可以看出，在代码行中转义符\就是表示代码的继续读取。第三个输出等价于"This is one.This is two."，并不是说换行了结果就会换行。

**自然字符串**

指示某些不需要如转义符那样的特别处理的字符串。加上前缀r或R。

> 正则表达式一定要使用自然字符串

```python
print(r"Newlines are indicated by \n")
```

结果：![KXfcrQ.png](https://s2.ax1x.com/2019/11/03/KXfcrQ.png)

**Unicode字符串**

Unicode字符串，书写国际文本的标准方法。加前缀u或者U。

> 处理文本文件的时候用Unicode字符串，特别是文件含有非英语语言的文本。

```python
print(u"This is 中国")
```

结果：![KXfLZ9.png](https://s2.ax1x.com/2019/11/03/KXfLZ9.png)

## 标志符

• 标识符的第一个字符必须是字母表中的字母（大写或小写）或者一个下划线（‘ _ ’）。
• 标识符名称的其他部分可以由字母（大写或小写）、下划线（‘ _ ’）或数字（0-9）组成。
• 标识符名称是对大小写敏感的。例如，myname 和 myName 不是 不是一个标识符。注意前者中的小写 n 和后者中的大写 N。

## 分号

分号表示一个逻辑行/语句的结束，可以用但是避免使用分号。

```python
i = 5
print(i)

i = 5;
print(i);
# i = 5;print(i);
# i = 5;print(i)
# 可以并排，但是不推荐，且python会要求你format
```

## 控制流

冒号结尾

**if..elif..else**

> 在 Python 中没有 switch 语句。你可以使用 if..elif..else 语句来完成同样的工作（在某些场合，使用字典会更加快捷。）

```python
number = 23
guess = int(raw_input('Enter an integer: '))  # raw_input将字符串打在屏幕上，等待用户输入

if guess == number:
    print('''Congratulation!
    (but you don't win any prizes!)''')
elif guess < number:
    print('No, it is a little higher than that')
else:
    print('No, it is a little lower than that')
print('Done')
```

比如输入23，它输出：

![KjnhRJ.png](https://s2.ax1x.com/2019/11/03/KjnhRJ.png)

**while循环**

>  while 循环中有一个可选的 else 从句

```python
number = 23
running = True
while running:
    guess = int(raw_input('Enter an integer: '))  # raw_input将字符串打在屏幕上，等待用户输入
    
    if guess == number:
        print('''Congratulation!
        (but you don't win any prizes!)''')
    elif guess < number:
        print('No, it is a little higher than that')
    else:
        print('No, it is a little lower than that')
        running = False
    print('Done')
else:
    print('You are loser!')
```

比如输入25，它输出：

![KjubXn.png](https://s2.ax1x.com/2019/11/03/KjubXn.png)

**for..in循环**

> 使用于任何种类、任何对象的序列。它在一序列的对象上 递归 即逐一使用队列中的每个项目。

`Python 的 for 循环从根本上不同于 C/C++的 for 循环。C#程序员会注意到 Python 的 for 循环与 C#中的 for each 循环十分类似。Java 程序员会注意到它与 Java 1.5 中的 for (int i : IntArray)相似。 在 C/C++中，如果你想要写 for(int i = 0; i < 5; i++)，那么用 Python，你写成 for i in range(0,5)。你会注意到，Python 的 for循环更加简单、明白、不易出错。`

```python
for i in range(1, 5):  # range左闭右开为[1,2,3,4]; range(1,5,2)中2为步长,为[1,3]  
    print(i)
else:
    print('The for loop is over!')
```

结果为：

![KjKacj.png](https://s2.ax1x.com/2019/11/03/KjKacj.png)

**break和continue语句**

break 语句是用来 终止 循环语句的，即哪怕循环条件没有称为 False 或序列还没有被完全递归，也停止执行循环语句。一个重要的注释是，如果你从 for 或 while 循环中 终止 ，任何对应的循环 else 块将不执行。

continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。

## Reference

[1]沈洁元. 简明Python教程-v1.1.pdf. 极客学院出版. [online] Available at:  www.byteofpython.info [Accessed 3 Nov. 2019].



> 此次学习过程主要通过运行代码直观地进行理解，代码为exe1.py

