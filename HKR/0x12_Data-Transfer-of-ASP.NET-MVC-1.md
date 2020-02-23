# ASP.NET MVC 的数据传递1

### Controller与 View之间的值传递

在实际使用情况下，View常用于显示动态数据。 View将从从Controller获得Model中的数据。 

#### 一、 使用View数据传递

ViewData相当于数据字典，包含Controlle和View之间传递的所有数据。Controller会在该字典中添加新数据项，View从字典中读取数据。 

1. **创建Model 类**

    在Model文件夹下新建User类，如下:

   ```
   public class User{
   	public string UserName { get; set; }
   	public string Password { get; set; }  
   	public int Character { get; set; } 
   }
   ```

2. **在Controller中获取Model**

   首先需要引用model类

   ```
   using WebApplication1.Models;
   ```

    然后在GetView 方法中创建User对象 

   ```
   User user = new User();
   user.UserName = "Mary";
   user.Password="123456";
   user.Character = 1;
   ```

3. **创建ViewData并返回View**

    在ViewData中存储Employee 对象。 

   ```
   ViewData["User"] = user;
   return View("MyView");
   ```

4. **在View中显示User数据** 

   打开MyView.cshtml。

   从ViewData中获取User数据并按照如下代码显示：

   ```
   <div>
   	@{
   		WebApplication1.Models.User user=(WebApplication1.Models.User)
   		ViewData["User"];
   	}
      
   	<b>User Details </b><br />
   	User Name : @user.UserName <br />
   	Character : @user.Character.ToString("C")
   </div>
   ```





#### 二、使用ViewBag传递

 ViewBag比ViewData慢 ， 但在ViewPage中查询数据时不需要类型转换 

1.  **创建View Bag** 

   在上一种方法中保留前两步，第三步改变为：

   ```
   ViewBag.User = user;
   ```

2.  **在View中显示EmployeeData** 

   第四步改变为：

   ```
   @{
   	WebApplication1.Models.User user=(WebApplication1.Models.User)
   	ViewBag.User;
   }
   User Details   
   User Name : @user.UserName
   Character : @user.Character.ToString("C")
   ```