# 0x3_Python_Learning

## 数据结构

数据结构——处理或是存储一组相关数据的结构。

在Python中有三种内建的数据结构：**列表、元祖和字典**。

### 列表

- list 是处理一组有序项目的数据结构
- 列表中的项目应该包括在**方括号**中，这样 Python 就知道你是在指明一个列表
- 每个项目之间用逗号分割
- Python 从 0 开始计数，使用方括号指明项目位置
- 列表可以添加、删除和修改项目

```python
# 列表list：处理一组有序项目的数据结构。项目应该包括在方括号中，每个项目之间用逗号分割，python以0开始计数
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), 'items to purchase.')	# len方法获取列表长度
print('These items are:')
for item in shoplist:
    print(item)
```

结果：![MO8AoD.png](https://s2.ax1x.com/2019/11/24/MO8AoD.png)

**添加项目**

append方法在列表尾部添加项目。

```python
print('I also have to buy rice.')
shoplist.append('rice')  # append在列表尾添加一个项目
print('My shopping list is now', shoplist)
```

结果：![MO8YWj.png](https://s2.ax1x.com/2019/11/24/MO8YWj.png)

**队列排序**

sort方法直接改变列表本身的序列，即从小到大排序。

```python
print('I will sort my list now.')
shoplist.sort()  # sort影响列表本身
print('Sorted shopping list is', shoplist)
```

结果：![MO8dO0.png](https://s2.ax1x.com/2019/11/24/MO8dO0.png)

**删除项目**

del语句删除指定序列的列表元素。

```python
print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]  # del语句删除列表元素
print('I bought the', olditem)
print('My shopping list is now', shoplist)
```

结果：![MOGSAS.png](https://s2.ax1x.com/2019/11/24/MOGSAS.png)

**修改项目**

```python
shoplist[0] = 'bana'
print('My shopping list is', shoplist)
```

结果：![MOGZ7T.png](https://s2.ax1x.com/2019/11/24/MOGZ7T.png)

**更多**

从help方法可以知道更多更详细的有关list列表的方法。

```python
print(help(list))
```

### 元祖

- 元祖是处理一组有序项目的数据结构
- 列表中的项目包括在**圆括号**中，这样 Python 就知道你是在指明一个元祖
- 每个项目之间用逗号分割
- Python 从 0 开始计数，使用方括号指明项目位置
- 元祖不可变，不可修改
- 元组之内的元组仍是一个元祖，即元祖是一个不可变的整体
- 元祖可以是只含有0个或1个项目

```python
# 元祖，不可变。通过圆括号中用逗号分割的项目定义
zoo = ('wolf', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))
```

结果：![MOYR6s.png](https://s2.ax1x.com/2019/11/24/MOYR6s.png)

**元祖是一个不可变的整体**

```python
new_zoo = ('monkey', 'dolphin', zoo)	#new_zoo元祖包含zoo元祖
print('Number of animals in the new zoo is', len(new_zoo))
print('ALL animals in the new zoo are', new_zoo)
print('Animals bought from old zoo are', new_zoo[2])
print('Last animal bought from old zoo is', new_zoo[2][2])
```

结果：![1574586483320](C:\Users\BaekLi\AppData\Roaming\Typora\typora-user-images\1574586483320.png)

`元祖的长度 = 元祖项目个数，一个元祖算是一个项目。如上面的new_zoo[2] = zoo，new_zoo[2][2] = zoo[2] = 'penguin'。`

**0个与1个项目的元祖**

- 元祖可以为空
- 单个元素的元祖必须在第一个项目后跟一个逗号，来区分元祖和表达式中一个带圆括号的对象

```python
# 含有0个或者1个项目的元祖
myempty = ()
singleton = (2,)  
# 单个元素的元祖必须在第一个项目后跟一个逗号，来区分元祖和表达式中一个带圆括号的对象
```

**使用元祖输出**

- print 语句可以输出跟着%符号的项目元组。
- 输出具备定制的功能，可以满足某种特定的格式。
- 定制可以是%s 表示字符串或%d 表示整数。
- 元组必须按照相同的顺序来对应这些定制。

```python
age = 22
name = 'Swaroop'
# print语句可以使用跟着%符号的项目元祖的字符串，必须按照相同的顺序来定制
print('%s is %d years old' % (name, age))  
# 如果元祖只有一个项目，可以没有圆括号
print('Why is %s playing with that python?' % name)
```

结果：![MOaVBR.png](https://s2.ax1x.com/2019/11/24/MOaVBR.png)

## Reference

[1]沈洁元. 简明Python教程-v1.1.pdf. 极客学院出版. [online] Available at:  www.byteofpython.info [Accessed 24 Nov. 2019].



> 此次学习过程主要通过运行代码直观地进行理解，代码为exp3.py







