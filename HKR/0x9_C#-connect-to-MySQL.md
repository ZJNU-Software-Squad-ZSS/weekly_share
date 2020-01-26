# C#  连接MySQL数据库

### 1.添加动态链接库文件

- 在Visual Studio中，右键项目 --》 管理NuGet程序包 ， 搜索MySql.Data并进行安装。 



### 2.连接到数据库

> using MySql.Data.MySqlClient;
>
> String connetStr = "server=127.0.0.1;port=3306;user=root;password=root; 
>
> // server=127.0.0.1/localhost 代表本机，端口号port默认是3306可以不写
>
> database=minecraftdb;";
>
> MySqlConnection conn = new MySqlConnection(connetStr);
> try
> {    
>       conn.Open();									//打开通道，建立连接，可能出现异常,使用try catch语句
>       Console.WriteLine("已经建立连接");
>       //在这里使用代码对数据库进行增删查改
> }
> catch (MySqlException ex)
> {
>       Console.WriteLine(ex.Message);
> }
> finally
> {
>       conn.Close();
> }



### 3.增删改查

- 查：

  > string sql= "select * from user";
  > MySqlCommand cmd = new MySqlCommand(sql,conn);
  > MySqlDataReader reader =cmd.ExecuteReader();						//得到sql语句执行的结果
  > while (reader.Read())													//初始索引是-1，执行读取下一行数据
  > {
  >     Console.WriteLine(reader.GetInt32("userid") + reader.GetString("username") + reader.GetString("password"));	//这里输出了user数据表中userid，username，password三项值

  

- 增删改：

  > string sql = "insert into user(username,password) values('张三','123456')";						//增
  > //string sql = "delete from user where userid='1'";																	//删
  > //string sql = "update user set username='李四',password='654321' where userid='1'";	//改
  > MySqlCommand cmd = new MySqlCommand(sql,conn);
  > int result =cmd.ExecuteNonQuery();//执行插入、删除、更改语句。