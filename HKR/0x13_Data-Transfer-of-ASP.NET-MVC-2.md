# ASP.NET MVC 的数据传递2

### 三、强类型View

1. **创建View的强类型**

   在View的顶部添加以下代码：
   ```
   @model WebApplication1.Models.User
   ```
2. **显示数据**

   在View中输入 ：
   用character的值来辨别并显示该用户的角色

   ```
   User Details
   
   User Name : @Model.UserName
   
   @if(Model.Character=0)
   {
   	<span style="background-color:red">
   		User Character: 管理员
   	</span>
   }
   else
   {           
   	<span style="background-color:green">  
   		User Character: 普通用户
   	</span>
   }
   ```


3. **从Controller Action方法中传递Model数据。**

   修改action代码
   
   ```
   User user = new User();
   user.UserName = "Mary";
   user.Password="123456";
   user.Character = 1;         
   return View("MyView",user);
   ```



### 四、实现ViewModel

1. **新建文件夹**

    在项目中创建新文件夹并命名为ViewModels。 

2. **新建EmployeeViewModel** 

   在ViewModels类中，创建新类并命名为UserViewModel，如下所示：

   ```
   public class UserViewModel
   {
       public string UserName { get; set; }
       public string Character { get; set; }
       public string CharacterColor { get; set; }
   }
   ```

3. **View中使用ViewModel**

   ```
   @using WebApplication1.ViewModels
   @model UserViewModel
   ```

4. **在View中显示数据** 

   使用以下脚本代替View部分的内容

   ```
   Hello @Model.UserName
   <hr />
   <div>
   	<b>User Details</b><br />
   	User Name : @Model.UserName <br />
   	<span style="background-color:@Model.CharacterColor">
   		User Character: @Model.Character
   	</span>
   </div>
   ```

5. **新建并传递ViewModel** 

   在GetView方法中，获取Model数据并且将强制转换为ViewModel对象。

   ```
   public ActionResult GetView()
   {
   	User user = new User();
   	user.UserName = "Mary";
   	user.Character = 1; 
   
   	UserViewModel vmuser = new UserViewModel();
   	vmuser.UserName = user.UserName;
   	if(user.Character=0){
   		vmuser.Character = "管理员"
   		vmuser.CharacterColor="Red";
   	}
   	else{
   		vmuser.Character = "普通用户"
   		vmuser.CharacterColor= "green";
   	}
     
   	vmuser.UserName = "Admin"
     
   	return View("MyView", vmEmp);
   }
   ```