# JavaScript_v2.0

![](https://s2.ax1x.com/2019/11/10/MuzVij.md.jpg)

[TOC]

------

#### 函数定义调用

```javascript
//函数的另一种定义方式   只要调用abs（10）就可以调用函数 
var abs = function (x) {
    if (x >= 0) {
        return x;
    } else {
        return -x;
    }
};
```

```javascript
//利用`arguments`，你可以获得调用者传入的所有参数。通常用于判断传入参数的个数
function abs() {
    if (arguments.length === 0) {
        return 0;
    }
    var x = arguments[0];
    return x >= 0 ? x : -x;
}

abs(); // 0
abs(10); // 10
abs(-9); // 9
```

```javascript
//可以用这种写法获取除了a，b以外的参数
function foo(a, b, ...rest) {//这个...不能省略 用来接收多余的参数，如果没有多余的 rest会接收一个空数组 不是undefined！
    console.log('a = ' + a);
    console.log('b = ' + b);
    console.log(rest);
}

foo(1, 2, 3, 4, 5);
// 结果:
// a = 1
// b = 2
// Array [ 3, 4, 5 ]

foo(1);
// 结果:
// a = 1
// b = undefined
// Array []
```

```javascript
//注意return 语句问题
function foo() {
    return; // js行末会自动添加分号，相当于return undefined;
        { name: 'foo' }; // 这行语句已经没法执行到了
}
```

------

#### 解构赋值

JavaScript的函数定义有个特点，它会先扫描整个函数体的语句，把所有申明的变量“提升”到函数顶部：

```javascript
'use strict';
function foo() {
    var x = 'Hello, ' + y;//并不报错，原因是变量`y`在稍后申明了。
    console.log(x);//`Hello, undefined`，说明变量`y`的值为`undefined`。
    var y = 'Bob';
}
foo();
//js自动提升了变量`y`的声明，但不会提升变量`y`的赋值。
//因为这一特性，所以应该一开始首先申明变量
```

**js中有个默认全局对象window，全局变量都是它的属性**。

###### 命名空间（暂时不是很懂）

全局变量会绑定到`window`上，不同的JavaScript文件如果使用了相同的全局变量，或者定义了相同名字的顶层函数，都会造成命名冲突，并且很难被发现。

减少冲突的一个方法是把自己的所有变量和函数全部绑定到一个全局变量中

```javascript
// 唯一的全局变量MYAPP:
var MYAPP = {};
// 其他变量:
MYAPP.name = 'myapp';
MYAPP.version = 1.0;
// 其他函数:
MYAPP.foo = function () {
    return 'foo';
};
```

###### 局部作用域

由于JavaScript的变量作用域实际上是函数内部，我们在`for`循环等语句块中是无法定义具有局部作用域的变量的：

```javascript
'use strict';

function foo() {
    for (var i=0; i<100; i++) {
        //
    }
    i += 100; // 仍然可以引用变量i
}//要解决这个问题可以用let 代替var  这样才是在for循环语句中声明局部作用域变量
```

**const可以定义常量（它和let相似 是块级作用域）  且不会变量提升**

解构赋值：把一个数组的元素分别对多个变量进行赋值

```javascript
var [x, , z] = ['hello', 'JavaScript', 'ES6'];//解构赋值可以忽略某些元素
```

```javascript
var {name, age, passport} = person;
//使用解构赋值对对象属性进行赋值时，如果对应的属性不存在，变量将被赋值为`undefined`，如果要使用的变量名和属性名不一致，可以用下面的语法获取：
let {name, passport:id} = person;
//把passport属性赋给id
//还可以默认值 这样就避免了undefined
var {name, single=true} = person; 
```

*下面举个容易出错的地方*

```javascript
// 如果变量已经被声明
var x, y;
// 再解构赋值:
{x, y} = { name: '小明', x: 100, y: 200};
// 会报错这是因为JavaScript引擎把`{`开头的语句当作了块处理，于是`=`不再合法。解决方法是用小括号括起来：({x, y} = { name: '小明', x: 100, y: 200});
```

解构赋值可以交换两个x和y的值[x,y]=[y,x] 不用临时变量

------

#### 方法

要保证`this`指向正确，必须用`obj.xxx()`的形式调用！由于这是一个巨大的设计错误，要想纠正可没那么简单。ECMA决定，在strict模式下让函数的`this`指向`undefined`

```javascript
'use strict';
var xiaoming = {
    name: '小明',
    birth: 1990,
    age: function () {
        var y = new Date().getFullYear();
        return y - this.birth;
    }
};
var fn = xiaoming.age;
fn(); // Uncaught TypeError: Cannot read property 'birth' of undefined
```

**这里有个要注意的点**

```javascript
'use strict';
var xiaoming = {
    name: '小明',
    birth: 1990,
    age: function () {
        function getAgeFromBirth() {
            var y = new Date().getFullYear();
            return y - this.birth;
        }
        return getAgeFromBirth();
    }
};

xiaoming.age(); // Uncaught TypeError: Cannot read property 'birth' of undefined
//`this`指针只在`age`方法的函数内指向`xiaoming`，在函数内部定义的函数
//`this`又指向`undefined`了！（在非strict模式下，它重新指向全局对象`window`！）

//为了这个问题，我们可以用一个that变量获取this  然后在内部函数中用 that 调用
```

###### apply()&&call()

```javascript
//要指定函数的`this`指向哪个对象，可以用函数本身的`apply`方法，它接收两个参数，第一个参数就是需要绑定的`this`变量，第二个参数是`Array`，表示函数本身的参数。
getAge.apply(xiaoming, []); // 25, this指向xiaoming, 参数为空
```

与`apply()`类似的方法是`call()`，唯一区别是：

- `apply()`把参数打包成`Array`再传入；
- `call()`把参数按顺序传入。

```javascript
Math.max.apply(null, [3, 5, 4]); // 5
Math.max.call(null, 3, 5, 4); // 5 对普通函数 this绑定为null
```

