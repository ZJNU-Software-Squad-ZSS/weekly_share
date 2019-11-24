## 0x3_1 Note_python_2

1. 循环

​       for  i  in   set : 

​               #缩进

​       for  i  in  range(15) :

​               #缩进，i依次=0，1，。。。，14

​       while   判断：

​              #缩进

2. list

   list是一个可以存放不同类型的数据的容器

   例：

   ​     list_1 = [ 12 , "abc" , 45 , 9 , 1.1]

   ​     list_2 = [ [ 14 , 'hjg' , 'gkk' , 9 ] , "cc" , [ 89 , 'jh' ] ]        #相当于二维数组了

3. if boolean ：

   ​     #缩进

   else 

   ​    #缩进

   if 条件 ：

   ​    #缩进

   else ：

   ​    #缩进

4. if  sth  in  set :

   ​    #缩进

   即直接完成一个foreach循环进行判断是否有sth元素

5. dict字典 类型

   dict1={ 'a' : 1 , 'b' : 5 , ...}   # 'key' : value

   （可用于统计集合里的各元素个数。)

6. alist.append(data)   #将data放入列表最后

7. new_list = alist.split('value')    #将列表元素按value进行分离，所以得到的 new_list 将是一个列表  ， 这种方法常见于csv表格文件的读取，其每一行元素以 ' \n ' 划分，每一单元格元素以 ' , ' 划分

8. def 函数名（ a , b , ...参数列表 ) :

   ​    #函数体