#### MySQL相关复习

感觉之前有几节数据库的课都划水了，写数据库的实验题时才开始懊悔自己基础不牢，写个执行语句都会报错。

Variables,Literals,Parameters,Comments

The `DECLARE` statement allows us to create a variable. 

###### Data type:

String  data types

enum data types(枚举类型)：不建议存值为数字

```sql
CREATE PROCEDURE sp_enums(in_option ENUM('Yes','No','Maybe'))
BEGIN
  DECLARE position INTEGER;
  SET position=in_option;
  SELECT in_option,position;
END
--------------

Query OK, 0 rows affected (0.01 sec)

--------------
CALL sp_enums('Maybe')
--------------

+-----------+----------+
| in_option | position |
+-----------+----------+
| Maybe     |        3 |
+-----------+----------+
1 row in set (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

--------------
CALL sp_enums(2)
--------------

+-----------+----------+
| in_option | position |
+-----------+----------+
| No        |        2 |
+-----------+----------+
1 row in set (0.00 sec)

Query OK, 0 rows affected (0.00 sec)

--------------
CALL sp_enums('What?')
--------------

ERROR 1265 (01000): Data truncated for column 'in_option' at row 1


```

set data type:

similar to the enum type, except that multiple values from the list of allowable values can occur in the variables 

Numeric Data Types

Date and Time Data Types

TEXT and BLOB Data Types

###### 触发器辨析：

insert (new)

delete(old)

update(new/old)

before:验证新数据是否满足使用的限制

after:在激活触发器的语句执行之后执行几个或更多的改变