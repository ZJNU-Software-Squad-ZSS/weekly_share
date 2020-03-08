# ASP.NET MVC 的数据处理1

### 一、添加数据访问层

1. **创建数据库**

   连接SQL SERVER ,创建数据库 “SalesERPDB”。

   

2. **创建连接字符串（ConnectionString）**

   打开Web.Config 文件，在< Configuration >标签内添加以下代码：

   ```
   <connectionStrings>
   	<add connectionString="Data Source=(local);Initial Catalog=SalesERPDB;Integrated Security=True"
   		name="SalesERPDAL"       
   		providerName="System.Data.SqlClient"/>
   </connectionStrings>
   ```

   

3. **添加EF引用**

   右击项目->管理Nuget 包。选择Entity Framework 并点击安装。

   

4. **创建数据访问层**

   在根目录下，新建文件夹”Data Access Layer“，并在Data Access Layer文件夹中新建类” SalesERPDAL “

   在类文件顶部添加 Using System.Data.Entity代码。

   继承DbContext类

   ```
   public class SalesERPDAL: DbContext{ }
   ```

   

5. **创建User类的主键**

   打开User类，输入using语句

   ```
   using System.ComponentModel.DataAnnotations;
   ```

   添加Employee的属性，并使用Key 关键字标识主键。

   ```
   public class User
   {
   	[Key]
   	public int UserId { get; set; }
   	public string UserName { get; set; }
   	public string Password { get; set; }
   	public int Character { get; set; }
   }
   ```

   

6. **定义映射关系**

   在SalesERPDAL类文件输入using语句。

   ```
   using WebApplication1.Models;
   ```

   在 SalesERPDAL 类中重写 OnModelCreating方法，代码如下：

   ```
   protected override void OnModelCreating(DbModelBuilder modelBuilder)
   {
       modelBuilder.Entity<user>().ToTable("TblUser");
       base.OnModelCreating(modelBuilder);
   }
   </user>
   ```

   注意：上述代码中提到“TblUser”是表名称，是运行时自动生成的。

   

7. **在数据库中添加新属性User**

   在 SalesERPDAL 类中添加新属性 User。

   ```
   public DbSet<user> Users{ get; set;}
   </user>
   ```

   DbSet表示数据库中能够被查询的所有User

   

8. **改变业务层代码，并从数据库中获取数据**

   打开 UserBusinessLayer 类，输入Using 语句。

   ```
   using WebApplication1.DataAccessLayer;
   ```

   修改GetUsers 方法：

   ```
   public List<user> GetUsers()
   {
       SalesERPDAL salesDal = new SalesERPDAL();
       return salesDal.Users.ToList();
   }
   </user>
   ```

