# HTML 脚本

**JavaScript 使 HTML 页面具有更强的动态和交互性。。**

HTML script 元素

<script> 标签用于定义客户端脚本，比如 JavaScript。

script 元素既可包含脚本语句，也可通过 src 属性指向外部脚本文件。

必需的 type 属性规定脚本的 MIME 类型。

JavaScript 最常用于图片操作、表单验证以及内容动态更新。

下面的脚本会向浏览器输出“Hello World!”：

```
<script type="text/javascript">
document.write("Hello World!")
</script>
```

**提示：**如果需要学习更多有关在 HTML 中编写脚本的知识，请访问我们的 [JavaScript 教程](https://www.w3school.com.cn/js/index.asp)。

## <noscript> 标签

<noscript> 标签提供无法使用脚本时的替代内容，比方在浏览器禁用脚本时，或浏览器不支持客户端脚本时。

noscript 元素可包含普通 HTML 页面的 body 元素中能够找到的所有元素。

只有在浏览器不支持脚本或者禁用脚本时，才会显示 noscript 元素中的内容：

```
<script type="text/javascript">
document.write("Hello World!")
</script>
<noscript>Your browser does not support JavaScript!</noscript>
```

## 如何应付老式的浏览器

如果浏览器压根没法识别 <script> 标签，那么 <script> 标签所包含的内容将以文本方式显示在页面上。为了避免这种情况发生，你应该将脚本隐藏在注释标签当中。那些老的浏览器（无法识别 <script> 标签的浏览器）将忽略这些注释，所以不会将标签的内容显示到页面上。而那些新的浏览器将读懂这些脚本并执行它们，即使代码被嵌套在注释标签内。

### 实例

#### JavaScript:

```
<script type="text/javascript">
<!--
document.write("Hello World!")
//-->
</script>
```

#### VBScript:

```
<script type="text/vbscript">
<!--
document.write("Hello World!")
'-->
</script>
```



# HTML 文件路径

| 路径                            | 描述                                         |
| :------------------------------ | :------------------------------------------- |
| <img src="picture.jpg">         | picture.jpg 位于与当前网页相同的文件夹       |
| <img src="images/picture.jpg">  | picture.jpg 位于当前文件夹的 images 文件夹中 |
| <img src="/images/picture.jpg"> | picture.jpg 当前站点根目录的 images 文件夹中 |
| <img src="../picture.jpg">      | picture.jpg 位于当前文件夹的上一级文件夹中   |

## HTML 文件路径

文件路径描述了网站文件夹结构中某个文件的位置。

文件路径会在链接外部文件时被用到：

- 网页
- 图像
- 样式表
- JavaScript

## 绝对文件路径

绝对文件路径是指向一个因特网文件的完整 URL：

### 实例

```
<img src="https://www.w3school.com.cn/images/picture.jpg" alt="flower">
```

<img> 标签以及 src 和 alt 属性在 HTML 图像这一章做了讲解。

## 相对路径

相对路径指向了相对于当前页面的文件。

在本例中，文件路径指向了位于当前网站根目录中 images 文件夹里的一个文件：

### 实例

```
<img src="/images/picture.jpg" alt="flower">
```

在本例中，文件路径指向了位于当前文件夹中 images 文件夹里的一个文件：

### 实例

```
<img src="images/picture.jpg" alt="flower">
```

在本例中，文件路径指向了位于当前文件夹的上一级文件夹中 images 文件夹里的一个文件：

### 实例

```
<img src="../images/picture.jpg" alt="flower">
```

## 好习惯

使用相对路径是个好习惯（如果可能）。

如果使用了相对路径，那么您的网页就不会与当前的基准 URL 进行绑定。所有链接在您的电脑上 (localhost) 或未来的公共域中均可正常工作。
