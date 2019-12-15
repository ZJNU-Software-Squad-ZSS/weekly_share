本质上还是讨厌前端的，感觉永远学不会

DOM：

节点=HTML元素

一些常用的 HTML DOM 方法：

- 访问HTML元素，然后进行更为复杂的操作：

  --getElementById(id) - 获取带有指定 id 的节点（元素）

  --getElementsByTagName()- 如<p>

  --getElementsByClassName() -查找带有相同类名的所有 HTML 元素  ~~可以想象和CSS一块混用时有多复杂~~

  ```javascript
  document.getElementsByClassName("intro"); //class = intro
  ```

- appendChild(node) - 插入新的子节点（元素）

  *必须创建该元素，然后把它追加到已有的元素上*

  ```javascript
  <body>
  
  <div id="div2">
  <p id="p1">This is a paragraph.</p>
  <p id="p2">This is another paragraph.</p>
  </div>
  <div id = "div1">
  </div>
  
  <script>
  var para=document.createElement("p");
  var node=document.createTextNode("This is new.");
  para.appendChild(node);
  
  var element=document.getElementById("div1");
  element.appendChild(para);
  </script>
  ```

- removeChild(node) - 删除子节点（元素）

一些常用的 HTML DOM 属性：

- innerHTML - 获取节点（元素）的文本值

  **也可用于更改HTML元素**

  ```javascript
  <!DOCTYPE html>
  <html>
  <body>
  
  <p id="p1">Hello world!</p>
  
  <script>
  function ChangeText()
  {
  document.getElementById("p1").innerHTML="New text!";
  }
  </script>
  
  <input type="button" onclick="ChangeText()" value="改变文本" />
  
  </body>
  </html>
  ```

  

- parentNode - 节点（元素）的父节点

- childNodes - 节点（元素）的子节点

- attributes - 节点（元素）的属性节点

##### jQuery

jQuery 语法是通过选取 HTML 元素，并对选取的元素执行某些操作。

基础语法： **$(selector).action()**

- 美元符号定义 jQuery
- 选择符（selector）"查询"和"查找" HTML 元素
- jQuery 的 action() 执行对元素的操作

实例:

- $(this).hide() - 隐藏当前元素
- $("p").hide() - 隐藏所有 <p> 元素
- $("p.test").hide() - 隐藏所有 class="test" 的 <p> 元素
- $("#test").hide() - 隐藏所有 id="test" 的元素

响应式滑块插件：http://responsiveslides.com/

bootstrap：https://www.imooc.com/video/3399 下周开始，本周太颓了