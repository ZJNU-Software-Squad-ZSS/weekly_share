# JSP（Java Server Pages）

![](https://theskyhouse.oss-cn-hangzhou.aliyuncs.com/mirror5.png)

------

[TOC]

------

#### 动作标签

**动作标签是由tomcat(服务器)来解释执行，而html标签由浏览器来执行**

###### \<jsp:include\>(动态包含)

- <jsp:include page="xxx"/>，用来包含指定的页面。假如有两个jsp分别为a.jsp和b.jsp,他们分别编码成Servlet，**然后在执行Servlet时才会执行包含过程**。这也是include指令与include标签的区别。
- 注意：<jsp:include page="<%=myfile%>">，这是可以的！因为include指令是在执行时才完成的包含，在执行时已经可以确定myfile这个变量的值。

###### \<jsp:forward>

- 例如在a.jsp中存在如下内容：<jsp:fowrad page="b.jsp"/>
  a.jsp中的内容不会显示在浏览器上，而只是显示b.jsp的内容。并且在\<jsp:forwad\>标签下面的内容不会被执行。

###### \<jsp:param\>

它是前两个标签的子标签，用来向包含或转发的页面传递参数

```jsp
<%--举个例子就是--%>
<jsp:includepage =”b.jsp”/>
	<jsp:param name=”xx” value=”XXXX”/>
</jsp:include>

//我们在b.jsp中可以通过request.getParamer(“”);方法来获取参数的值（forword也一样）
```

------

#### JavaBean

Bean指豆子，通俗来说，JavaBean是一种特殊的java类，可以将多个对象封装到一个对象（bean）中，是java可重用软件组件的惯用叫法。

```java
//借用网上代码来讲
public class car {	
	private int 车轮 = 4 ;
	private int 座位 = 5;
		
	public int get车轮() {
		return 车轮;
	}
	public void set车轮(int 车轮) {
		this.车轮 = 车轮;
	}
	public int get座位() {
		return 座位;
	}
	public void set座位(int 座位) {
		this.座位 = 座位;
	}
}
/*一开始学习的时候，我们管car叫对象类，到了后期，我们称之为javaBean
总的来说：
 1.所有属性为private
 2.提供默认构造方法
 3.提供getter和setter
 4.实现serializable接口（序列化）
*/
```

###### JSP与JavaBean

<jsp:useBean id="user1" class="包名.类名" />

- 查看page域中是否存在user1这个域属性，如果存在就获取，不存在就创建

```java
等价于<->
User user1 = pageContext.getAttribute(“user1”);
if(user1 == null) {
user1 = new User();//创建user1对象
pageContext.setAttribute(“user1”, user1);//保存到page域
}
```

<jsp:setProperty property="username" name="user1" value="admin"/>

- property：指定要设置的属性名称

- name：指定名为user1的JavaBean(也可以说是javaBean的实例对象)
- value：指定要设置的属性值

```java
等价于<->
User user1 = (User)pageContext.getAttribute(“user1”);
user1.setUsername(“admin”);
```

<jsp:getProperty property="username" name="user1"/>

- 和setProperty类似，根据属性名获取属性值

```jsp
等价于<->
User user1 = (User)pageContext.getAttribute(“user1”);
out.print(user1.getUsername());
```

------

#### EL表达式

代替JSP原本要用的java语言，简化代码。基本语法${express}

比如${sessionScope.user.sex}---从Session的范围中，取得用户的性别。

```java
//等价于
User user =(User)session.getAttribute("user");
String sex =user.getSex( );
```

###### 获取显示数据

1. 从四个域中通过key找到数据并显示出来------${name} **它会按顺序从page，request，session，application四个域中寻找**，如果没找到 ，**显示一个空的字符串**。倘若我们知道在request域中，则可以直接${requestScope.name} （这简化很香不是吗）

2. 从封装了数据的javaBean中得到并显示对象的某个属性值

   ```jsp
   <%
   User user = new User();
   user.setUsername(“zhangSan”);
   user.setPassword(“123”);
   pageContext.setAttribute(“user”, user);
   %>
   ${pageScope.user.username}
   ${pageScope.user.password}
   ```

3. 从list集合对象中获取某个值并显示

   ```jsp
   <%
   	List<Person> list = new ArrayList<Person>();
   	list.add(new Person("aaa"));
   	list.add(new Person("bbb"));
   	list.add(new Person("ccc"));
   	application.setAttribute("list_1", list);
   %>
   ${list_1[1].name }
   ```

4. 还可以操作Map（   ${pageScope.map['a1'].username}   括号里面一定是字符串类型，或者可以写成${pageScope.map.a1.username}  ）

------

#### JSTL

它是EL表达式的扩展，现在常用的还有：

core（核心标签库）

- \<c：out>---输出字符串或者域属性
- \<c：set>-----创建域属性
- \<c：remove>----删除域属性
- \<c：url>输出url或者保存url到page域中
- \<c：if test=“ ${条件} “>条件为true执行标签体里的内容
- \<c：forEach>迭代集合或数组

fmt库（格式化标签库）

<fmt:formatDate value=”” pattern=”“>
pattern：用来指定输出的模板！例如：yyyy-MM-dd HH:mm:ss
<fmt:formatNumber value=”${num1}” pattern=”0.00”>
保留小数点后2位，它会四舍五入。

------







