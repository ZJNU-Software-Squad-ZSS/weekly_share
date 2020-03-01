# ASP.NET MVC 的数据传递3

### 五、带有集合的View

1. **保持UserViewModel 类** 

   ```
   public class UserViewModel
   {
       public string UserName { get; set; }
       public string Character { get; set; }
       public string CharacterColor { get; set; }
   }
   ```

2. **创建结合ViewModel** 

    在ViewModels 文件下，创建新类并命名为UserListViewModel 

   ```
   public class UserListViewModel
   {
   	public List<userviewmodel> Users { get; set; }
   	public string NickName { get; set; }
   }
   ```

3. **修改强类型View的类型** 

   ```
   @using WebApplication1.ViewModels
   @model UserListViewModel
   ```

4. **显示View中所有的User **

   ```
   <body>
   	Hello @Model.NickName
   	<hr />
   	<div>
   		<table>
   			<tr>
   				<th>User Name</th>
   				<th>Character</th>
   			</tr>
   			@foreach (UserViewModel item in Model.Users)
   			{
   				<tr>
   					<td>@item.UserName</td>
   					<td style="background-color:@item.CharacterColor">
   						@item.Character
   					</td>
   				</tr>
   			}
   		</table>
   	</div>
   </body>
   ```

5. **创建Employee的业务逻辑** 

    新建类并命名为UserBusinessLayer ，并带有GetUsers()方法。 

   ```
   public class UserBusinessLayer
   {
       public List<user> GetUsers()
       {
           List<user> users = new List<user>();
           User user = new User();
           user.UserName = "johnson";
           user.Character = 1;
           users.Add(user);
    
           user = new User();
           user.UserName == "michael";
           user.Character = 1;
           users.Add(user);
     
           user = new User();
           user.UserName == "robert";
           user.Character = 0;
           users.Add(user);
     
           return users;
       }
    }
    </user>
   ```

6. **从控制器中传参** 

   ```
   public ActionResult GetView()
   {
   	UserListViewModel userListViewModel = new UserListViewModel();
   
   	UserBusinessLayer userBal = new UserBusinessLayer();
   	List<user> users = userBal.GetUsers();
   
   	List<userviewmodel> userViewModels = new List<userviewmodel>();
   
   	foreach (User user in users){
   		UserViewModel userViewModel = new UserViewModel();
   		userViewModel.UserName = user.UserName;
   		if (user.Character = 0){
   			userViewModel.Character = "管理员";
   			userViewModel.CharacterColor = "red";
   		}
   		else{
   			userViewModel.Character = "普通用户";
   			userViewModel.CharacterColor = "green";
   		}
   		userViewModels.Add(userViewModel);
   	}
   	userListViewModel.Users = userViewModels;
   	userListViewModel.NickName = "Admin";
   	return View("MyView", userListViewModel);
   }
   </userviewmodel></userviewmodel></user>
   ```