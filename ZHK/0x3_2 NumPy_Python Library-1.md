## 0x3_2 NumPy_Python Library-1 

1. numpy.genfromtxt(" ...   . txt" ,  delimiter = " , " , dtype = str , skip_header=1)   #读取txt的函数（不常用）， delimiter 选择分隔符 ， dtype 选择数据类型 ，skip_header 选择开头去掉的行数 。 读取的结果为一个矩阵。各数据可按数组方式访问，如 new_data = matrix_1 [ 1 , 1 ] 或 new_list = matrix_1 [ 1 ] [ 1 : 3 ] (取第二行二、三个元素)  或 new_list = matrix_1 [ : , 3 ] （取每行第四个元素）

2. print( help ( genfromtxt ) )   #可用类似方法输出函数说明

3. vector = numpy.array( [ ... ] )       #设立array类型n维数组对象

4. vector. shape     # 表示数组形状的元组

   输出（2，3）表示一个两行三列的数组

5. numpy不允许存储不同类型的元素

   会自行转化部分元素的数据类型以统一元素数据类型

6. 用==对numpy的array进行比较，会将array中的每一个元素都比较一次，最后得到一个布尔元素的矩阵。

7. matrix_1[ matrix_2 ]   #若matrix_2是一个布尔的矩阵，则返回1矩阵中true元素对应位置的元素。

8. vector=vector.astype( #数据类型 )  #数据类型转换

9. matrix.sum(axis=1)   #按行求和，axis=0按列求和

10. vector.min()  #求vector最小值 ，max同理

11. numpy.arange(n)     #造一个0到n-1的数组

12. matrix.reshape(m,n)   #把原本的array数组转化成为m*n的矩阵。

13. matrix.shape   #shape属性

14. matrix.ndim   #维度属性

15. matrix.dtype   #数据类型属性（输出时加上 . name ）

16. matrix.size   #元素个数属性

17. numpy.zeros((3,4))   #创建一个3*4的元素值都为0. 的（float类型）矩阵。（维度(3,4)以元组形式传入）

18. numpy.ones((2,3,4), dtype = numpy.int32)  #ones 用法同zeros。dtype可指定数据类型为numpy指定的numpy.int32 格式

19. numpy.arange( 10 , 30 ,  5)   #创建一个从10开始到30结束，步长为5的矩阵）

20. numpy.random.random((2,3))   #构造一个2*3的每个元素值在-1到1之间的随机矩阵，第一个random指的是random模块

21. numpy.linspace( 0 ,  2 * pi , 100 )    #在0到2pi间  平均的   取100个值

22. array的加减平方对应于矩阵的每一个元素（均加减乘除n直接对array加减乘除n即可，无须定义一个矩阵）

23. array矩阵，a*b表示求内积，对位相乘

24. 。。。。。，a.dot (b)   或  numpy.dot(a,b)    都表示矩阵相乘

25. numpy.exp(n)    #求e的n次方

26. numpy.sqrt(n)     #开根号

27. numpy.floor(n)     #向下取整

28. a.ravel()       #将矩阵转化为一维数组，并且之后可以直接用   a.shape=(m,n)   来新定义形状

29. a.T     #转置

30. numpy.vstack((a,b))    #按行拼接a和b矩阵

31. numpy.hstack((a,b))    #按列拼接

32. numpy.hsplit(a,3)       #将a按列平均地切成3份

33. numpy.hsplit(a,(3,4))      #将a在第三四列上切分

34. vsplit同理

35. a=b的操作相当于给了引用，id相同

36. c=a.view()       #把a复制给c，但是引用不同，即a和c的id不同（可用id(a)来查看a的id），但是数据更改是同步的！所以，不好用！

37. c=a.copy()        #这个复制相当于真正的复制，a和c完全独立！

38. a.argmax(axis=0)     #返回每列的最大值所对应的行号index，以矩阵形式返回

39. numpy.tile(a,(4,2))              #返回一个行为原来4倍，列为两倍的矩阵，以原数据填充

40. numpy.sort(a,axis=1)           #按行排序（由小到大）

41. numpy.argsort(a)            #将sort后的元素索引值按序返回



11/21