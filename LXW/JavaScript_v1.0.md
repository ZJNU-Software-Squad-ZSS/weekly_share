# JavaScript_v1.0

![](https://s2.ax1x.com/2019/11/10/MuGRzR.md.jpg)

[TOC]

------

#### 数据类型

- Number（不区分整数和浮点数）

---NaN表示无法计算结果，是一个没有意义的数字（它与任何值都不相等包括它本身  可以通过isNaN（）函数判断）

- 字符串：单引号或双引号括起来的文本，单引号和双引号可以嵌套使用

- java中的比较运算符：

1. == 自动转换数据类型再比较
2. ===不转换数据类型，比较

（通常使用===比较）

- `null`表示一个“空”的值，它和`0`以及空字符串`''`不同，`0`是一个数值，`''`表示长度为0的字符串，而`null`表示“空”。

- 而`undefined`表示值未定义，一般还是用null居多

- 数组用【】表示，元素用，隔开

  Array（）也可以创建数组。

- 对象是键-值组成的无序集合（有点像结构体吧）

在JavaScript中，使用等号`=`对可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量，注意只能用`var`申明一次，例如：

```
var a = 123; // a的值是整数123
a = 'ABC'; // a变为字符串
```

这种变量本身类型不固定的语言称之为动态语言（要显示变量的内容可以用console.log(x)它代替alert()可以避免对话框23333）

如果一个变量没有通过`var`申明就被使用，那么该变量就自动被申明为全局变量：（因为这个设计缺陷，推荐使用strict模式）

------

#### 字符串

如果字符串内部既包含`'`又包含`"`怎么办？可以用转义字符`\`来标识，比如：

```javascript
'I\'m \"OK\"!';    //表示I‘m “OK"！
```

由于\n写起来比较烦一般用· 反引号来表示

```javascript
`这是一个
多行
字符串`;
```

字符串连接和java一样这点不多说明（但是我们可以写成你好, ${name}, 你今年${age}岁了!`;这种模板字符串形式方便一点）

**需要特别注意的是，字符串是不可变的，如果对字符串的某个索引赋值，不会有任何错误，但是，也没有任何效果：**

和java类似 也有toUpperCase和toLowerCase、indexOf、substring等方法

------

#### 数组

*请注意*，直接给`Array`的`length`赋一个新的值会导致`Array`大小的变化：

如果通过索引赋值时，索引超过了范围，同样会引起`Array`大小的变化：**所以一般不建议直接修改Array的大小，访问索引时确保不会越界。**

数组的slice()方法类似字符串的substring（）  截取部分的元素  然后 返回一个新的Array

`push()`向`Array`的末尾添加若干元素，`pop()`则把`Array`的最后一个元素删除掉：

如果要往`Array`的头部添加若干元素，使用`unshift()`方法，`shift()`方法则把`Array`的第一个元素删掉：

还有sort、reverse方法就不提了

splice（）可以从指定索引删除若干个元素，再添加若干元素

concat可以把两个array连接起来，返回新的array

join把每个元素用指定字符串连接  返回字符串！

```javascript
var arr = ['A', 'B', 'C', 1, 2, 3];
arr.join('-'); // 'A-B-C-1-2-3'
```

------

#### 对象

访问属性是通过`.`操作符完成的，如果属性名包含特殊字符，就必须用`''`括起来：

```
var xiaohong = {
    name: '小红',
    'middle-school': 'No.1 Middle School'
};
```

属性名`middle-school`不是一个有效的变量，就需要用`''`括起来。访问这个属性也无法使用`.`操作符，必须用`['xxx']`来访问：

```javascript
xiaohong['middle-school']; // 'No.1 Middle School'
xiaohong['name']; // '小红'
xiaohong.name; // '小红'
```

如果要检测是否拥有某一属性，可以用in操作符例如  ‘name’ in xw返回true or false（但是这个属性还可以是继承得到的）

判断属性是否自身拥有，可以用`hasOwnProperty()`方法

JavaScript把`null`、`undefined`、`0`、`NaN`和空字符串`''`视为`false`，其他值一概视为`true`。

------

#### 循环

`for`循环的一个变体是`for ... in`循环，它可以把一个对象的所有属性依次循环出来：

```javascript
var o = {
    name: 'Jack',
    age: 20,
    city: 'Beijing'
};
for (var key in o) {
    console.log(key);// 'name', 'age', 'city'
    //if(o.haseOwnProperty(key))这样子的可以选择部分属性打印出来
}
**for...in 对Array循环得到的是String不是Number**
```

------

#### Map &&Set

###### Map（查找比较快）

1. 一个key只能对应一个value，如果放入多个value，会覆盖掉前面的值（类似常量吧）
2. 初始化Map需要一个二维数组或者空
3. 有set 添加新的键值对、 has查找是否有这个key、 get得到键值的方法

###### Set（去重复）

1. 它只存储key，不允许重复的key
2. 初始化Set要提供Array作为输入
3. 有add 添加key的方法

------

#### Iterable

​	遍历Map和Set不能使用下标。Array，Map和Set都属于iterable类型。

​	用`for ... of`循环遍历集合（Map同理）

```javascript
var s = new Set(['A', 'B', 'C']);
for (var x of s) { // 遍历Set
    console.log(x);
}
```

for of 和for in的区别如下

```
var a = ['A', 'B', 'C'];
a.name = 'Hello';
for (var x in a) {
    console.log(x); // '0', '1', '2', 'name'
}//for ... in循环将把`name`包括在内，但`Array`的`length`属性却不包括在内
```

```
//`for ... of`循环则完全修复了这些问题，它只循环集合本身的元素：
var a = ['A', 'B', 'C'];
a.name = 'Hello';
for (var x of a) {
    console.log(x); // 'A', 'B', 'C'
}
```

