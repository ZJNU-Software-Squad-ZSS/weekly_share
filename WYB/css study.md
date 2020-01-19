## CSS 元素选择器

最常见的 CSS 选择器是元素选择器。换句话说，文档的元素就是最基本的选择器。

如果设置 HTML 的样式，选择器通常将是某个 HTML 元素，比如 p、h1、em、a，甚至可以是 html 本身：

```
html {color:black;}
h1 {color:blue;}
h2 {color:silver;}
```



可以将某个样式从一个元素切换到另一个元素。

假设您决定将上面的段落文本（而不是 h1 元素）设置为灰色。只需要把 h1 选择器改为 p：

```
html {color:black;}
p {color:gray;}
h2 {color:silver;}
```



## 类型选择器

在 W3C 标准中，元素选择器又称为类型选择器（type selector）。

“类型选择器匹配文档语言元素类型的名称。类型选择器匹配文档树中该元素类型的每一个实例。”

下面的规则匹配文档树中所有 h1 元素：

```
h1 {font-family: sans-serif;}
```

因此，我们也可以为 XML 文档中的元素设置样式：

### XML 文档：

```
<?xml version="1.0" encoding="ISO-8859-1"?>
<?xml-stylesheet type="text/css" href="note.css"?>
<note>
<to>George</to>
<from>John</from>
<heading>Reminder</heading>
<body>Don't forget the meeting!</body>
</note>
```

### CSS 文档：

```
note
  {
  font-family:Verdana, Arial;
  margin-left:30px;
  }

to
  {
  font-size:28px;
  display: block;
  }

from
  {
  font-size:28px;
  display: block;
  }

heading
  {
  color: red;
  font-size:60px;
  display: block;
  }

body
  {
  color: blue;
  font-size:35px;
  display: block;
  }
```

通过上面的例子，您可以看到，CSS 元素选择器（类型选择器）可以设置 XML 文档中元素的样式。
