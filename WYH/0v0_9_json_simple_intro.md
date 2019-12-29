# JSON语言

## **JSON** **语法规则**

JSON 语法是 JavaScript 对象表示语法的子集。

- 数据在名称/值对中
- 数据由逗号分隔
- 大括号保存对象
- 中括号保存数组



## **JSON** **名称****/****值对**

JSON 数据的书写格式是：名称/值对。

名称/值对包括字段名称（在双引号中），后面写一个冒号，然后是值：

```json
"name" : "菜鸟教程"
```

这很容易理解，等价于这条 JavaScript 语句：

```json
name = "菜鸟教程"
```





## **JSON** **值**

JSON 值可以是：

- 数字（整数或浮点数）
- 字符串（在双引号中）
- 逻辑值（true     或     false）
- 数组（在中括号中）
- 对象（在大括号中）
- null



## **JSON** **数字**

JSON 数字可以是整型或者浮点型：

```json
{ "age":30 }
```



## **JSON** **对象**

JSON 对象在大括号（{}）中书写：

对象可以包含多个名称/值对：

```json
{ "name":"菜鸟教程" , "url":"www.runoob.com" }
```

这一点也容易理解，与这条 JavaScript 语句等价：

```json
name = "菜鸟教程" url = "www.runoob.com"
```



## **JSON** **数组**

JSON 数组在中括号中书写：

数组可包含多个对象：

```json
{ 
"sites": [
 { "name":"菜鸟教程" , "url":"www.runoob.com" }, 
 { "name":"google" , "url":"www.google.com" }, 
 { "name":"微博" , "url":"www.weibo.com" } 
] 
}
```

在上面的例子中，对象 "sites" 是包含三个对象的数组。每个对象代表一条关于某个网站（name、url）的记录。