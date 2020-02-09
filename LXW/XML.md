# XML

![](https://theskyhouse.oss-cn-hangzhou.aliyuncs.com/[66093]浴衣とお面-57793944.png)

------

[TOC]

------

#### XML

XML（传输数据） HTML (显示数据)

如果内容中有特殊符号，需要使用转义字符举几个常用的：（点击表格中右边内容

|  <   |  &lt;  |
| :--: | :----: |
|  >   |  &gt;  |
|  &   | &amp;  |
|  "   | &quot; |
|  '   | &apos; |

XML文档结构大致：

```java
<?xml version="1.0" encoding="UTF-8" ?>
<book id="1">
    <name>Java核心技术</name>
    <author>Cay S. Horstmann</author>
    <isbn lang="CN">1234567</isbn>
    <tags>
        <tag>Java</tag>
        <tag>Network</tag>
    </tags>
    <pubDate/>
</book>
```

------

#### DOM+SAX

XML是一种树形结构的文档，有两种解析API：DOM（一次性读取，树形结构）和SAX（以流形式读取，事件回调）

```java
InputStream input = Main.class.getResourceAsStream("/book.xml");
DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
DocumentBuilder db = dbf.newDocumentBuilder();
Document doc = db.parse(input);
//通过DocumentBuilder.parse()接收inputStream、File、URL获取document对象后，遍历读取
//从根节点Document出发，遍历所有子节点，获取所有元素、属性、文本数据，这些节点被统称为Node，每个Node都有自己的Type，根据type确定类型
```

相比DOM解析---SAX占用内存很小（一边读一边解析）

```java
InputStream input = Main.class.getResourceAsStream("/book.xml");
SAXParserFactory spf = SAXParserFactory.newInstance();
SAXParser saxParser = spf.newSAXParser();
saxParser.parse(input, new MyHandler());
//对比DOM 它的parse不仅要传入一个inputstream流  还要传入一个继承DefaultHandler的回调对象
SAX的解析是触发一系列事件 打印出来结果大致如下：
    start document//开始读取XML文档
    start element:  book//读取到了一个book元素
    characters://读取到了字符

    start element:  name
    characters: Java核心技术
    end element:  name//读取到了一个结束元素
    characters:

    //相比之下读取文本定位还是DOM方便...（SAX可以用栈保存定位节点）
```

------

#### JSON

jackson（第三方库）可以轻松使XML转换成JavaBean---目前不是很了解JavaBean 后面再补充

XML标签繁琐，格式复杂，取而代之越来越多人使用JSON（JavaScript Object Notation）

优点

1. UTF-8编码，不存在编码问题
2. 格式简单（双引号做key，特殊字符\转义）
3. 浏览器支持，可以用js直接处理

jackson也可以解析JSON，使JSON和JavaBean之间转换，方便利用





