# ASP.NET MVC 的数据处理2

### 二、创建数据入口

1. 新建 action 方法

   在 EmployeeController 中新建 “AddNew”action 方法：

   ```
public ActionResult AddNew()
{
    return View("CreateUser");
}
   ```

2. 创建 View

   在View/User目录下 新建 View 命名为：CreateUser。

   ```
   @{
       Layout = null;
   }
   <!DOCTYPE html>
   <html>
       <head>
       	<meta name="viewport" content="width=device-width" />
   		<title>CreateEmployee</title>
   	</head>
   	<body>
   		<div>
   			<form action="/User/SaveUser" method="post">
   			UserName: <input type="text" id="TxtFName" name="UserName" value="" />
               <br />
   			Character: <input type="text" id="TxtCha" name="Character" value="" />
   			<br />
   			<input type="submit" name="BtnSave" value="Save User" />
   			<input type="button" name="BtnReset" value="Reset" />
   			</form>
   		</div>
   	</body>
   </html>
   ```

3. 创建Index View的链接

   打开 Index.cshtml 文件，添加指向 AddNew action方法的链接

   ```
   <ahref="/User/AddNew">Add New</a>
   ```



### 三、在服务器端（或Controller）获取Post数据

1. 创建 **SaveEmployee** action 方法

   在 Employee控制器中创建 名为 ”SaveEmployee“ action 方法：

   ```
   public string SaveUser(User e)
   {
      return e.UserName+"|"+e.Character;
   }
   ```



### 四、重置按钮和取消按钮

1. 添加重置和取消按钮

   ```
   ...
   <input type="submit" name="BtnSubmit” value="Save User" />
   <input type="button" name="BtnReset" value="Reset" onclick="ResetForm();" />
   <input type="submit" name="BtnSubmit" value="Cancel" />
   ```
   
2. 定义 **ResetForm** 函数 

   在Html的头部分添加脚本标签，并编写JavaScript 函数 命名为”ResetForm“如下：

   ```
   <script>
   	function ResetForm() {
   	document.getElementById('TxtFName').value = "";
   	document.getElementById('TxtLName').value = "";
   	document.getElementById('TxtSalary').value = "";
   	}
   </script>
   ```

3. 在 **UserController** 的 **SaveEUser** 方法中实现取消按钮的点击功能

   修改**SaveUser 方法：**

   ```
   public ActionResult SaveUser(User e, string BtnSubmit)
   {
   	switch (BtnSubmit)
   	{
   		case "Save User":
   			return Content(e.UserName + "|" + e.Salary);
   		case "Cancel":
   			return RedirectToAction("Index");
   	}
  	return new EmptyResult();
  }
   ```