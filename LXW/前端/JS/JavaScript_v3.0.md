# JavaScript_v3.0

![](https://s2.ax1x.com/2019/11/14/MUpPeS.md.jpg)



[TOC]

------

### 高阶函数

#### map/reduce

Array.map() 方法返回一个新数组，此方法可以以一个函数为参数，循环数组的每一个元素，函数将数组中的元素接收为单个参数。

```javascript
var arr = [8, 10, 13, 10, 8, 1, 5];
 function double(num){
     return num * 2;
 }
 alert(arr.map(double));//16, 20, 26, 20, 16, 2, 10
```

Array.reduce()方法接收两个参数，然后结果继续和序列下一个元素累计计算(如果只有一个参数的话 就会返回那个参数 )

```javascript
var arr = [1, 3, 5, 7, 9];
arr.reduce(function (x, y) {
    return x*y;
});//945
var arr = [1, 3, 5, 7, 9];
arr.reduce(function (x, y) {
    return x * 10 + y;
}); // 13579
```

这里有个注意的点

```javascript
var arr=['1','2','3'];
var r=arr.map(parseInt);
//结果是 1 NaN NaN
因为map()实际上会传入三个参数：(currentValue, index, callingArray)。parseInt接受两个参数(string, radix)，

当arr = [1,2,3]时，arr.map(parseInt)实际为：
parseInt('1', 0);    // 按十进制转换'1'
parseInt('2', 1);    // 按一进制转换'2'，但一进制中只有0没有1
parseInt('3', 2);    // 按二进制转换3，但二进制中只有0和1没有2
所以后两个只能报错了。
```

------

#### filter

过滤元素，根据返回值的Boolean决定元素是保留还是丢弃

```javascript
var arr = ['A', '', 'B', null, undefined, 'C', '  '];
var r = arr.filter(function (s) {
    return s && s.trim(); // 注意：IE9以下的版本没有trim()方法
});
r; // ['A', 'B', 'C']
```

可以去除Array中的重复元素

```javascript
r = arr.filter(function (element, index, self) {
    return self.indexOf(element) === index;
});
//indexOf会返回元素的第一个位置
```

------

#### sort

```javascript
//要按数字大小排序，我们可以这么写：
arr.sort(function (x, y) {
    if (x < y) {
        return -1;
    }
    if (x > y) {
        return 1;
    }
    return 0;
});
console.log(arr); // [1, 2, 10, 20]
//不要直接掉调用  sort()默认把所有元素转换成String排序
//'10'排在了'2'的前面，因为字符'1'比字符'2'的ASCII码小
```

------

#### Array

every（）方法可以用于判断数组元素是否满足条件

```javascript
var arr = ['Apple', 'pear', 'orange'];
console.log(arr.every(function (s) {
    return s.length > 0;
})); // true, 因为每个元素都满足s.length>0

console.log(arr.every(function (s) {
    return s.toLowerCase() === s;
})); // false, 因为不是每个元素都全部是小写
```

find()查找符合条件的第一个元素，返回元素，没找到返回undefined

findIndex()查找元素，返回这个元素索引，没找到返回-1

foreach（）作用类似于map() 把传入的函数作用于每个元素

------

### 闭包

```javascript
//闭包可以返回函数延迟执行  每次调用都会返回一个新的函数
function count() {
    var arr = [];
    for (var i=1; i<=3; i++) {
        arr.push(function () {
            return i * i;
        });
    }
    return arr;
}

var results = count();
var f1 = results[0];
var f2 = results[1];
var f3 = results[2];

f1(); // 16
f2(); // 16
f3(); // 16

//**返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了4，因此最终结果为16。**


```

通常，一个立即执行的匿名函数可以把函数体拆开，一般这么写：

这样可以解决上面的那个问题   

```javascript
(function (x) {
    return x * x;
})(i);
```

闭包还可以让我们封装私有变量（毕竟js没有class机制）换句话说，闭包就是携带状态的函数，并且它的状态可以完全对外隐藏起来。

闭包还可以把多参数的函数变成单参数的函数。例如，要计算xy可以用`Math.pow(x, y)`函数，不过考虑到经常计算x2，我们可以利用闭包创建新的函数`pow2`

```javascript
function make_pow(n) {
    return function (x) {
        return Math.pow(x, n);
    }
}
var pow2=make_pow(2);
console.log(pow2(5));//25
```

总的来说：1、在函数内部定义函数，2、函数不调用不执行。