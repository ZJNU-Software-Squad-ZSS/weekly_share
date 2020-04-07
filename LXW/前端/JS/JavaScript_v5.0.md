# JavaScript_v5.0

![](https://theskyhouse.oss-cn-hangzhou.aliyuncs.com/F79DF235-A5F7-4035-B01B-5310EDA24AAB.JPG)

PicGo真香！

[TOC]

------

#### 原型继承

```javascript
　　function Cat(name,color){

　　　　this.name = name;

　　　　this.color = color;

　　　　this.type = "猫科动物";

　　　　this.eat = function(){alert("吃老鼠");};

　　}//type 和eat这个属性是个猫都会有 这样写构造函数（constructor）每生成一个实例就会重复内容多占用内存，所以 可以通过Cat.prototype.type=“猫科动物”这种方法 直接定义在它的原型对象上 （可以理解成java中的父类吧）
```

不是很懂廖雪峰老师网站中写的js**原型继承**等思路，选择性跳过吧

#### Class继承

```javascript
class PrimaryStudent extends Student {
    constructor(name, grade) {
        super(name); // 记得用super调用父类的构造方法!
        this.grade = grade;
    }

    myGrade() {
        alert('I am at grade ' + this.grade);
    }
}
//和java区别不大，可惜不是所有的主流浏览器都支持ES6的class，需要一个工具把class代码转换为传统的prototype代码，可以试试Babel这个工具。
```

------

#### 浏览器对象

- window对象（全局作用域||浏览器窗口）有innerWidth和innerHeight属性，可以获取浏览器窗口的内部宽度和高度。
- screen表示屏幕的信息， colorDepth 可以返回颜色位数
- location 表示当前页面的URL location.reaload()可以重新加载当前页面 location.assign()可以加载一个新的页面
- document 对象表示当前页面.html在浏览器中以DOM形式表示为树形结构 document对象就是整个DOM树的根节点
- document对象的getElementById()和getElementsByTagName()方法可以按ID获得一个DOM节点和按Tag名称获得一组DOM节点
- 为了确保安全，服务器端在设置Cookie时，应该始终坚持使用httpOnly

------

#### DOM

```javascript
// 先定位ID为'test-table'的节点，再返回其内部所有tr节点：
var trs = document.getElementById('testtable').getElementsByTagName('tr');

// 先定位ID为'test-div'的节点，再返回其内部所有class包含red的节点：
var reds = document.getElementById('test-div').getElementsByClassName('red');

// 获取节点test下的所有直属子节点:
var cs = test.children;

// 获取节点test下第一个、最后一个子节点：
var first = test.firstElementChild;
var last = test.lastElementChild;

//更新DOM
/*
拿到DOM节点后 可以修改innnerHTML 和innerText属性或者说是style（CSS）对它的内容进行修改（我理解的innerHTML就是该节点后面的全部代码（包括标签）；innerText指该节点后面的全部文本内容（忽略标签） 一般来说用前者多一点 符合W3C的标准
*/

//插入DOM
/*
var
    list = document.getElementById('list'),
    haskell = document.createElement('p');
haskell.id = 'haskell';
haskell.innerText = 'Haskell';
list.appendChild(haskell);
产生一个新的节点，然后插入到指定位置
parentElement.insertBefore(newElement, referenceElement);，子节点会插入到referenceElement之前。
比如list.insertBefore(haskell, ref);  将haskell 插入到ref之前 
list是外面的div层的id
*/

//删除DOM
/*
// 拿到待删除节点:
var self = document.getElementById('to-be-removed');
// 拿到父节点:
var parent = self.parentElement;
// 删除:	调用父节点的removeChild 
var removed = parent.removeChild(self);  
removed === self; // true
（这里要注意被删除的节点还在内存中可以被添加到别的位置）
还有一点要注意的就是删除多个节点的时候 children 的属性会实时变化
*/


```

------

#### 操作表单

- 如果我们得到了一个input节点的引用，我们就可以直接调用value获取用户输入的值
- 对于单选框或者复选框（我们要获取的是用户是否勾上了选项  要用checked判断true or false， 此时value属性返回的是HTML预设的值）
- 标准控件，如date color 都使用input标签，如果是不支持的空间，就会自动当成type=text来显示 （<input type="color" value="#ff0000">）
- 提交表单 

```javascript
<!-- HTML -->
<form id="login-form" method="post" onsubmit="return checkForm()">
    <input type="text" id="username" name="username">
    <input type="password" id="input-password">
    <input type="hidden" id="md5-password" name="password">//不加hidden 口令框会有32个* （MD5有32个字符）
    <button type="submit">Submit</button>
</form>

<script>
function checkForm() {
    var input_pwd = document.getElementById('input-password');
    var md5_pwd = document.getElementById('md5-password');
    // 把用户输入的明文变为MD5:
    md5_pwd.value = toMD5(input_pwd.value);
    // 继续下一步:
    return true;
}
</script>
//没有name属性的input数据不会被提交
```

