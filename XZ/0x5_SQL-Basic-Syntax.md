## 创建、删除库

```
-- 创建新数据库 
CREATE DATABASE 数据库名; 
-- 删除数据库 
DROP DATABASE 数据库名;
```



## 增加

1. **添加列名、设置主键、设置自动增长列**

   primary key表示当前列为主键列，不能重复，不能为空

   out_increment表示当前列为自动增长列，由DBMS分配该列的值，可以保证不重复

   ```
   CREATE TABLE t_user(
       id INT PRIMARY KEY AUTO_INCREMENT, -- 编号 
       userName VARCHAR(20),-- 用户名 
       birthday DATE,-- 生日 
       tel CHAR(11),-- 电话
       -- 枚举类型，该列的值只能取男和女 
       sex ENUM('男','女'),
       -- 性别 -- 最后一列不能加“，”。 
       money INT -- 账户余额 
   );
   ```

2. **新增记录**

   如果添加多条信息，中间用“，”分割。BALUES只需要写一次，写在表头和表值之间。

   如果列名和列的值不写，则默认添加为空。

   ```
   INSERT INTO t_user(表头1，表头2) values(值1，值2)； 
   例如： 
   INSERT INTO t_user(userName,pwd,birthday,tel,sex,money) 
   VALUES ('张无忌','123','1980-05-09','13948577789','男',2000); 
   例如： 
   INSERT INTO t_student(userName,pwd,birthday,tel,sex) 
   VALUES('张勇','111','1998-01-01','13112341234','男');
   ```

3. 添加列（多用于维护）

   ```
   ALTER TABLE t_student ADD address BARCHAR(50);
   ```

   

## 删除

1. **删除表**

   ```
   -- t_user:表名 
   DROP TABLE t_user;
   ```

2. **删除列**

   ```
   -- t_student：表名；userAddress：列名 
   ALTER TABLE t_student DROP COLUMN userAddress;
   ```

3. **删除记录**

   ```
   -- 如果不加where 后面的条件则全部删除。 
   DELETE FROM t_user WHERE id=2;
   ```

   

## 修改

1. **修改列**

   修改列的值必须与修改后的类型相符，如果修改列的值为null，则可以改为任意类型。如果修改列的值类型为varchar，最长为20，则修改后的类型必须为char类型，长度不能低于20。

   ```
   ALTER TABLE t_student CHANGE address userAddress VARCHAR(100);
   ```

2. **修改值**

   ```
   UPDATE t_product SET 修改列名=修改后新值 WHERE id=1; 
   -- 修改，将张无忌的密码修改为333，工资修改为2500 
   UPDATE t_user SET pwd='333',money='2500' WHERE userName='张无忌';
   ```

   

## 查询

1. **查询表中所有数据**

   *表示显示所有的列，也可以指定显示列的列表，中间用“，”分割。

   ```
   SELECT * FROM t_user; 
   -- 例如(显示姓名和工资列)： 
   select userName,money from t_user
   ```

2. **查询返回限定行**

   第一个参数为起始记录数，从0开始，第二个参数为显示记录数

   ```
   -- MySQL语法
   SELECT * FROM t_student LIMIT 0,3;
   ```

3. **查询空值Null**

   null不能用=，只能用is null 或 is not null

   ```
   SELECT *FROM t_student WHERE money IS NULL;
   ```

4. **查询多条信息**

   ```
   -- 查询张三和李四的信息 
   SELECT * FROM t_student WHERE userName='张三' OR userName='李四'; 
   SELECT * FROM t_student WHERE userName IN('张三','李四');
   ```

5. **模糊查询（_或%)**

   ```
   -- 查询姓李的二个字的员工 
   SELECT * FROM t_student WHERE userName LIKE '李_'; 
   -- 查询出所有商品名包括“糕”的商品的信息 
   SELECT * FROM t_product WHERE productName LIKE '%糕%';
   ```

6. **查询多条件+显示部分（LIMIT）**

   ```
   -- 查询前5条价格在100-1000的酒类商品 (MySQL语法)
   SELECT * FROM t_product WHERE productType='酒类' AND price>=100 AND price<=1000 LIMIT 0,5 ;
   ```

7. **查询去除重复的类名**

   ```
   -- 查询所有的性别，distinct 表示去除重复记录 
   SELECT DISTINCT sex FROM t_student;
   ```

8. **查询排序显示**

   ```
   -- 按员工工资排序，默认为升序ASC，降序需要加上DESC。 
   -- 工资相同，按年龄大小排序。 
   SELECT * FROM t_student ORDER BY money DESC,birthday;
   ```

9. **查询当前日期**

   ```
   select curdate() from 表名
   ```

   

## 判断语句

1. **单分支条件判断**

   ```
   if(条件，返回值1，返回值2)
    -- 例如： 
   select s.*,if(grade>=60,'合格','不合格')appraise from t_students;
   ```

2. **多分支条件判断**

   ```
   (case 
   when 条件1 then 返回值1 
   when 条件2 then 返回值2 
   else 返回值3 END) 
   -- 例子1（选择显示）： 
   SELECT p.*,(CASE 
               WHEN money<5000 THEN '低薪阶层' 
               WHEN money>=5000 AND money<=10000 THEN '中薪阶层' 
               WHEN money>10000 THEN '高薪阶层' 
               ELSE '实习生' END) grade FROM t_student p; 
   -- 例子2（选择添加）： 
   UPDATE t_product SET price =price+(CASE 
                                       WHEN productType='药品类' THEN 5 
                                       WHEN productType='食品类' THEN 2 
                                       WHEN productType='酒类' THEN 100 END);
   ```

   

## 聚合函数的应用

```
-- 学生成绩表 
CREATE TABLE t_grade( 
    id INT PRIMARY KEY AUTO_INCREMENT,-- id 主键 
    sname VARCHAR(20),-- 学生姓名 
    sex ENUM('男','女'),-- 学生性别 
    className VARCHAR(20),-- 学生班级 
    grade INT -- 学生成绩 
);
```

1. **统计学生的人数**

   ```
   -- count（*）只要是记录都要统计。count（列名）只统计非空列。 
   SELECT COUNT(*) '学生总人数', COUNT(grade)'参考人数' FROM t_grade;
   ```

2. **统计学生的总分、平均分、最高分、最低分**

   ```
   -- avg求平均分，也只统计非空列 
   SELECT SUM(grade) ,AVG(grade),SUM(grade)/COUNT(*), MAX(grade),MIN(grade) FROM t_grade
   ```

3. **统计每个班的人数**

   ```
   SELECT className,COUNT(*) num FROM t_grade GROUP BY className;
   ```

4. **统计每个班的总分和平均分**

   ```
   SELECT className,SUM(grade)'总分',SUM(grade)/COUNT(*) '平均分' FROM t_grade GROUP BY className;
   ```

   

## having

```
-- 列出班级人数小于等于3个人的班级 
SELECT className,COUNT(*) FROM t_grade GROUP BY className HAVING COUNT(*)<=3; 
-- 列出班级总分大于300分的班级 
SELECT className,SUM(grade) FROM t_grade GROUP BY className HAVING SUM(grade)>300;
```



## 复制表

```
create table 新表名 select * from 原表名;
```



## where和if条件连用

```
WHERE  IF(条件,  true执行条件, false执行条件 )
select * from sys_user where if(id<10,name='zhangsan',name='lisi')
```

