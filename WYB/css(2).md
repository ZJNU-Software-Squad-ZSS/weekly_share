# CSS3 字体

- [CSS3 文本效果](https://www.w3school.com.cn/css3/css3_text_effect.asp)
- [CSS3 2D 转换](https://www.w3school.com.cn/css3/css3_2dtransform.asp)

![通过 CSS3，Web 设计师再也不必被迫使用“web-safe”字体了。](https://www.w3school.com.cn/i/css3_font.gif)

## CSS3 @font-face 规则

在 CSS3 之前，web 设计师必须使用已在用户计算机上安装好的字体。

通过 CSS3，web 设计师可以使用他们喜欢的任意字体。

当您您找到或购买到希望使用的字体时，可将该字体文件存放到 web 服务器上，它会在需要时被自动下载到用户的计算机上。

您“自己的”的字体是在 CSS3 @font-face 规则中定义的。

## 浏览器支持

|    属性    | 浏览器支持 |      |      |      |      |
| :--------: | :--------: | ---- | ---- | ---- | ---- |
| @font-face |            |      |      |      |      |

Firefox、Chrome、Safari 以及 Opera 支持 .ttf (True Type Fonts) 和 .otf (OpenType Fonts) 类型的字体。

Internet Explorer 9+ 支持新的 @font-face 规则，但是仅支持 .eot 类型的字体 (Embedded OpenType)。

**注释：**Internet Explorer 8 以及更早的版本不支持新的 @font-face 规则。

## 使用您需要的字体

在新的 @font-face 规则中，您必须首先定义字体的名称（比如 myFirstFont），然后指向该字体文件。

如需为 HTML 元素使用字体，请通过 font-family 属性来引用字体的名称 (myFirstFont)：

### 实例

```
<style> 
@font-face
{
font-family: myFirstFont;
src: url('Sansation_Light.ttf'),
     url('Sansation_Light.eot'); /* IE9+ */
}

div
{
font-family:myFirstFont;
}
</style>
```

[亲自试一试](https://www.w3school.com.cn/tiy/t.asp?f=css3_font-face_rule)

## 使用粗体字体

您必须为粗体文本添加另一个包含描述符的 @font-face：

### 实例

```
@font-face
{
font-family: myFirstFont;
src: url('Sansation_Bold.ttf'),
     url('Sansation_Bold.eot'); /* IE9+ */
font-weight:bold;
}
```

[亲自试一试](https://www.w3school.com.cn/tiy/t.asp?f=css3_font-face_rule_bold)

文件 "Sansation_Bold.ttf" 是另一个字体文件，它包含了 Sansation 字体的粗体字符。

只要 font-family 为 "myFirstFont" 的文本需要显示为粗体，浏览器就会使用该字体。

通过这种方式，我们可以为相同的字体设置许多 @font-face 规则。

## CSS3 字体描述符

下面的表格列出了能够在 @font-face 规则中定义的所有字体描述符：

| 描述符        | 值                                                           | 描述                                                         |
| :------------ | :----------------------------------------------------------- | :----------------------------------------------------------- |
| font-family   | *name*                                                       | 必需。规定字体的名称。                                       |
| src           | *URL*                                                        | 必需。定义字体文件的 URL。                                   |
| font-stretch  | normalcondensedultra-condensedextra-condensedsemi-condensedexpandedsemi-expandedextra-expandedultra-expanded | 可选。定义如何拉伸字体。默认是 "normal"。                    |
| font-style    | ormalitalicoblique                                           | 可选。定义字体的样式。默认是 "normal"。                      |
| font-weight   | normalbold100200300400500600700800900                        | 可选。定义字体的粗细。默认是 "normal"。                      |
| unicode-range | *unicode-range*                                              | 可选。定义字体支持的 UNICODE 字符范围。默认是 "U+0-10FFFF"。 |
