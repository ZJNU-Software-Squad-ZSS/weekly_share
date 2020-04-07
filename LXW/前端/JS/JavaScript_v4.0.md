# JavaScript_v4.0

![](https://s2.ax1x.com/2019/11/15/MaIli8.md.jpg)

[TOC]

------

#### 箭头函数

```javascript
x=>x*x
等同于
function（x）{
 	return x*x；
}

// 两个参数:
(x, y) => x * x + y * y
// 无参数:
() => 3.14
// 可变参数:
(x, y, ...rest) => {
    var i, sum = x + y;
    for (i=0; i<rest.length; i++) {
        sum += rest[i];
    }
    return sum;
}
```

箭头函数可以修复了`this`的指向，`this`总是指向词法作用域，也就是外层调用者`obj`：(之前函数内部的函数 this 会指向winodw或undefined)

```javascript
var obj = {
    birth: 1990,
    getAge: function () {
        var b = this.birth; // 1990
        var fn = () => new Date().getFullYear() - this.birth; // this指向obj对象
        return fn();
    }
};
obj.getAge(); // 29
```

```javascript
var obj = {
    birth: 1990,
    getAge: function (year) {
        var b = this.birth; // 1990
        var fn = (y) => y - this.birth; // this.birth仍是1990（它已经通过箭头函数绑定作用域了）
        return fn.call({birth:2000}, year);
    }
};
obj.getAge(2015); // 25
```

------

#### generator

generator由`function*`定义，并且，除了`return`语句，还可以用`yield`返回多次。

```
fib(5); // fib {[[GeneratorStatus]]: "suspended", [[GeneratorReceiver]]: Window}
```

直接调用一个generator和调用函数不一样，`fib(5)`仅仅是创建了一个generator对象，还没有去执行它。

```javascript
fib(5); // fib {[[GeneratorStatus]]: "suspended", [[GeneratorReceiver]]: Window
var f = fib(5);
f.next(); // {value: 0, done: false}

//可以直接for of 循环迭代generator对象
for (var x of fib(10)) {
    console.log(x); // 依次输出0, 1, 1, 2, 3, ...
}

```

------

#### 对象

在js中，一切都是对象（可以用typeof获取对象类型，**但不能区分null和Array 它们都返回Object**）

###### Data

 JavaScript的Date对象月份值从0开始，牢记0=1月，1=2月，2=3月，……，11=12月。

###### RegExp（正则表达式）

- 用`\d`可以匹配一个数字，`\w`可以匹配一个字母或数字，`.`可以匹配任意字符

- 用`*`表示任意个字符（包括0个），用`+`表示至少一个字符，用`?`表示0个或1个字符，用`{n}`表示n个字符，用`{n,m}`表示n-m个字符

- `\s`可以匹配一个空格（也包括Tab等空白符）

- `^`表示行的开头，`^\d`表示必须以数字开头。`$`表示行的结束，`\d$`表示必须以数字结束。

- 可以用`[]`表示范围`[0-9a-zA-Z\_]`可以匹配一个数字、字母或者下划线；

- 写正则表达式可以直接/······/ 或者new RegExp（‘·······')出来  但是后者因为是字符串 所以要进行转义

- RegExp对象用test（）方法测试给定字符串是否符合条件

- 可以加？让\d+采用非贪婪匹配（尽可能少匹配）

- ```javascript
  var r1 = /test/g;
  //等价于r2！
  var r2 = new RegExp('test', 'g');
  
  //全局搜索
  var s = 'JavaScript, VBScript, JScript and ECMAScript';
  var re=/[a-zA-Z]+Script/g;
  
  re.exec(s); // ['JavaScript']
  re.lastIndex; // 10
  
  re.exec(s); // ['VBScript']
  re.lastIndex; // 20
  
  re.exec(s); // ['JScript']
  re.lastIndex; // 29
  
  re.exec(s); // ['ECMAScript']
  re.lastIndex; // 44
  
  re.exec(s); // null，直到结束仍没有匹配到
  ```

- 正则表达式还可以指定`i`标志，表示忽略大小写，`m`标志，表示执行多行匹配。

###### JSON

JavaScript对象变成JSON，就是把这个对象序列化成一个JSON格式的字符串，这样才能够通过网络传递给其他计算机。

如果我们收到一个JSON格式的字符串，只需要把它反序列化成一个JavaScript对象，就可以在JavaScript中直接使用这个对象了。（拿到一个JSON格式的字符串，用`JSON.parse()`把它变成一个JavaScript对象）

