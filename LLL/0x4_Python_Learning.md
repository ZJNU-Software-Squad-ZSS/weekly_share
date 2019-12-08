# 0x4_Python_Learning

## 数据结构

数据结构——处理或是存储一组相关数据的结构。

在Python中有三种内建的数据结构：**列表、元祖和字典**。

### 字典

d = {key1 : value1, key2 : value2 }

- 字典是另一种可变容器模型，且可存储任意类型对象，由**键值（key=>value ）对**组成
- 字典的每个键值 key=>value 对用**冒号 :** 分割
- 字典里的**键名是唯一**的，且只能使用不可变的对象来作为字典的键，所以可以用**数字，字符串或元组**充当，而用列表就不行
- 字典的每个键值对直接用**逗号 ,** 分割
- 整个字典包括在**花括号{}**中
- 字典可以添加、删除和修改键值对
- 字典中的键/值对是没有顺序的
- 字典是dict类的实例/对象

```python
ab = {'Swaroop': 'swaroop@byteofpythyon.info',
      'Larry': 'larry@wall.org',
      'Mark': 'mark@163.com',
      'Spammer': 'spammer@hotmail.com'}

print("Swaroop's address is %s" % ab['Swaroop'])
```

结果：![QiNfqP.png](https://s2.ax1x.com/2019/11/28/QiNfqP.png)

> 字典ab有四个键值对，每个都有唯一的键名，我们可以通过键名来得到键值。比如ab['Swaroop']可以得到'Swaroop'这个键名的键值，为'swaroop@byteofpythyon.info'

**添加、删除、修改键值对**

- 修改键值对：只要指明键名，就可以用赋值语句将它的键值改变
- 添加键值对：和修改键值对一样的操作，其中键名是新添加的键名
- 删除键值对：使用del语句，指明所要删除的键名
- 使用for...in语句循环遍历，使用字典的items方法来使用字典中的每一个键值对

```python
ab['Mark']='Mark@163.com'
# add a key/value pair
ab['Lily'] = 'lily@python.org'
# delete a key/value pair
del ab['Spammer']
print('\nThere are %d contacts in the address-book\n' % len(ab))
for name, address in ab.items():  # 使用字典的items方法来使用字典中的每一个键/值对
    print('Contact %s at %s' % (name, address))
```

结果：

![QiLY7R.png](https://s2.ax1x.com/2019/11/28/QiLY7R.png)

**字典内置函数**

| 序号 | 函数及描述                                                   |
| :--- | :----------------------------------------------------------- |
| 1    | [cmp(dict1, dict2)](https://www.runoob.com/python/att-dictionary-cmp.html) 比较两个字典元素。 |
| 2    | [len(dict)](https://www.runoob.com/python/att-dictionary-len.html) 计算字典元素个数，即键的总数。 |
| 3    | [str(dict)](https://www.runoob.com/python/att-dictionary-str.html) 输出字典可打印的字符串表示。 |
| 4    | [type(variable)](https://www.runoob.com/python/att-dictionary-type.html) 返回输入的变量类型，如果变量是字典就返回字典类型。 |

**字典内置方法**

| 1    | [dict.clear()](https://www.runoob.com/python/att-dictionary-clear.html) 删除字典内所有元素 |
| ---- | :----------------------------------------------------------- |
| 2    | [dict.copy()](https://www.runoob.com/python/att-dictionary-copy.html) 返回一个字典的浅复制 |
| 3    | [dict.fromkeys(seq[, val\])](https://www.runoob.com/python/att-dictionary-fromkeys.html)  创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值 |
| 4    | [dict.get(key, default=None)](https://www.runoob.com/python/att-dictionary-get.html) 返回指定键的值，如果值不在字典中返回default值 |
| 5    | [dict.has_key(key)](https://www.runoob.com/python/att-dictionary-has_key.html) 如果键在字典dict里返回true，否则返回false |
| 6    | [dict.items()](https://www.runoob.com/python/att-dictionary-items.html) 以列表返回可遍历的(键, 值) 元组数组 |
| 7    | [dict.keys()](https://www.runoob.com/python/att-dictionary-keys.html) 以列表返回一个字典所有的键 |
| 8    | [dict.setdefault(key, default=None)](https://www.runoob.com/python/att-dictionary-setdefault.html) 	 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default |
| 9    | [dict.update(dict2)](https://www.runoob.com/python/att-dictionary-update.html) 把字典dict2的键/值对更新到dict里 |
| 10   | [dict.values()](https://www.runoob.com/python/att-dictionary-values.html) 以列表返回字典中的所有值 |
| 11   | [pop(key[,default\])](https://www.runoob.com/python/python-att-dictionary-pop.html) 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。 |
| 12   | [ popitem()](https://www.runoob.com/python/python-att-dictionary-popitem.html) 返回并删除字典中的最后一对键和值。 |

## Reference

[1]沈洁元. 简明Python教程-v1.1.pdf. 极客学院出版. [online] Available at:  www.byteofpython.info [Accessed 28 Nov. 2019].



> 此次学习过程主要通过运行代码直观地进行理解，代码为exp3-1.py



