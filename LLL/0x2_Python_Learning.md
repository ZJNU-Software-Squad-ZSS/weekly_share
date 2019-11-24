# 0x2_Python_Learning

## 模块

1. 一个包含了所有你定义的函数和变量的文件，以.py 为扩展名。如exp2.py文件，模块的名字为exp2。
2. 模块能定义函数，类和变量，模块里也能包含可执行的代码。
3. 模块里面函数与变量通过 . 来引用，这些叫做模块的成员。

**标准库模块——sys模块**

- 首先，我们利用 **import 语句**输入 sys 模块 。

  ```python
  import sys	# sys是system的缩写
  ```

- sys 模块中的变量通过使用点号指明——如sys.argv(sys.argv 变量是一个字符串的列表 )

  优势：这个名称不会与任何在你的程序中使用的 argv 变量冲突。另外，它也清晰地表明了这个名称是 sys 模块的一部分。

- 使用 python 命令运行模块，后面跟着的内容被作为参数传递给程序。Python 为我们把它存储在 sys.argv 变量中。sys.argv 列表的第一个参数总是脚本的名称。

  ```python
  print('The command line arguments are:')
  for i in sys.argv:  # sys.argv变量是一个字符串的列表，包含命令行参数的列表。
      print(i)  # 执行python exp2.py we are students时，sys.argv[0]='exp2.py',sys.argv[1]='we'...
  ```

  在终端输入python exp2.py we are students的结果：

  ![MrgsXj.png](https://s2.ax1x.com/2019/11/17/MrgsXj.png)

- sys.path 包含输入模块的目录名列表。

  ```python
  print('\n\nThe PYTHONPATH is', sys.path, '\n')  # sys.path包含输入模块的目录名列表
  ```

  结果：

  ![Mrgx3D.png](https://s2.ax1x.com/2019/11/17/Mrgx3D.png)

**字节编译的.pyc文件**

创建以.pyc作为扩展名的字节编译文件，可以使输入模块更加快一些。字节编译的文件与 Python 变换程序的中间状态有关，当你在下次从别的程序输入这个模块的时候，.pyc 文件是十分有用的——它会快得多，因为一部分输入模块所需的处理已经完成了。

**from...import语句**

相比于import语句，如果你想要直接输入模块中的变量，可以使用from...import语句，这样可以避免每次使用该变量名的时候打模块名.变量名，直接打变量名就可以了。

```python
# from...import 语句
# 如果想直接输入argv变量 或 所有sys模块使用的名字
from sys import argv	#不需要每次都输入sys.argv,输入argv就可以了
from sys import *
```

`一般说来，应该避免使用 from..import 而使用 import 语句，因为这样可以使你的程序更加易读，也可以避免名称的冲突。`

**模块的name属性**

- 每个模块都有一个名称，文件的名字就是模块的名字。

- 每个模块都有一个内置的系统字符串变量name

  当这个模块是被import时，name变量的值为模块的名字；

  当这个模块是主模块（可以调用其他模块的模块）时，name变量的值设置为main。

**创建模块**

1. 创建.py文件

2. 定义函数，类和变量，也可包含可执行的代码

   ```python
   #创建模块module1.py
   def sayhi():
       print('Hi, this is module1 speaking.')
   
   
   version = '0.1'
   
   print(__name__)
   
   if __name__ == '__main__':	#该模块独自运行时
       print('The program is being run by itself\n')
       print(__name__)	#__name__值为__main__
   else:	#该模块被其他模块import时
       print('I am being imported from another module\n')
       print(__name__)	#__name__值为模块名
   ```

   该模块独自运行的结果：

   ![Mrb9K0.png](https://s2.ax1x.com/2019/11/17/Mrb9K0.png)

   > 从上图观察name变量的值。

3. 最好与使用该模块的主模块保存在同个目录下

4. 在其他模块中使用该模块

   ```python
   # 创建自己的模块module1.py,在同一个目录里，或者在sys.path所列目录之一
   #使用import
   import module1
   
   module1.sayhi()
   print('Version', module1.version)
   
   #使用from..import..
   from module1 import *
   
   sayhi()
   print('Version', version)
   ```

   结果：

   ![MrbA54.png](https://s2.ax1x.com/2019/11/17/MrbA54.png)

   > 从上图观察此时name的值，两次运行结果的name值不一样。

**dir()函数**

使用内建的 dir 函数来列出模块定义的标识符。标识符有函数、类和变量。

当你为 dir()提供一个模块名的时候，它返回模块定义的名称列表。如果不提供参数，它返回当前模块中定义的名
称列表。

```python
# dir函数，来列出模块定义的标识符。标识符有函数、类和变量
print(dir(sys))
print(dir(module1))
```

结果为：

![Mrqs0K.png](https://s2.ax1x.com/2019/11/17/Mrqs0K.png)

```python
print(dir())    # 返回当前模块exp2的属性列表
```

结果为：![MrqX1s.png](https://s2.ax1x.com/2019/11/17/MrqX1s.png)

```python
a = 5	#在exp2.py添加一个新变量a
print(dir())
```

结果为：![MrLnHK.png](https://s2.ax1x.com/2019/11/17/MrLnHK.png)

## Reference

[1]沈洁元. 简明Python教程-v1.1.pdf. 极客学院出版. [online] Available at:  www.byteofpython.info [Accessed 17 Nov. 2019].



> 此次学习过程主要通过运行代码直观地进行理解，代码为exp2.py与module1.py





