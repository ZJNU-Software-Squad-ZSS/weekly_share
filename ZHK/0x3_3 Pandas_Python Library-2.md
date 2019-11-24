## 0x3_3 Pandas_Python Library-2

1. 主要应用：数据预处理

2. pandas.read_csv(" 文件名 ")     #读取以逗号为分隔符的文件

3. read_csv读入的文件以DataFrame格式存储

4. a.dtypes            #返回数据格式

5. pandas提供float、int、object类型的数据类型，字符串视为object

6. a.head(n)          #显示前n行的数据，默认五行

7. a.tail(n)          #显示从后往前n行

8. a.columns      #每列列名

9. a.shape          #形状

10. a.loc[0]            #读取第0行数据 [2,3,5]  或 [ 2 : 7 ]  亦可

11. a["列名"," 列名",.... ]        #返回这几个列的数据

12. a.columns.tolist()            #返回列名的矩阵

13. ch.endswith(" 字符串 ")     #判断字符串ch是否 以某字符串结尾，返回布尔型

14. a.sort_values("列名", inplace= Ture)     #以某列元素的升序排序，Ture表示新生成一个DataFrame文件，不覆盖原文件

15. a.sort_values("列名", inplace= Ture ,ascending=False)        #降序

16. 缺失值查询：

    pandas.isnull(listName)        #是空返回True，返回一个一维矩阵

    list=a[一维Boolean矩阵]        #返回仅Ture元素的矩阵

    len(a)              #返回个数

17. 有缺失值时无法直接计算平均值

18. good_num = a[”列名“] [真值列==False]      #去掉真值为True的元素

19. a["列名"].mean()          #求忽略缺失值的平均值

20. ⚠a.pivot_table(index=" 主指标 （列名）"   ,    values = "目标指标（列名）" ,  aggfunc = numpy.mean )       #统计主指标对目标指标的影响，以numpy.mean为判断标准，numpy.mean也是默认标准，还有numpy.sum等。

21. 上述函数也可以同时指定多个目标函数，value=[" ... " , "   " , ... ]     即可

22. a.dropna(axis=0,subset=["Age","Sex"])      #去掉"Age","Sex"有缺失值的行

23. a.dropna(axis=1)       #去掉有缺失的列

24. a.loc[ 12  ,   "列名"  ]      #返回11行某列的对应元素

25. a.reset_index(drop=Ture)     #把索引值从零开始重新排列，用在排序后

26. a.apply(自定义函数名)               #调用函数

    ------

    

27. series结构：DataFrame的一个子结构，从DataFrame中取出一个列得到，结构类似numpy的array

28. Series(series1，index=series2)        #返回一个series结构，这个结构以series2 的元素作为索引，原索引仍可使用

29. series_x.index.tolist()      #返回一个index的列

30. sorted_index = sorted(series_x.index.tolist())         #返回一个index的排序（字母顺序）

    series_x.reindex(sorted_index)                 #返回一个新的按index排序的series

31. series_x.sort_index()           #返回排序后的series，相当于上述步骤

    series_x.sort_values()                 

32. series可以用numpy的函数计算

33. criteria_one  =  series_custom > 50       #取出大于50的值

    criteria_two  =  series_custom < 20

    series_x[criteria_one & criteria_two]          #返回符合这两个条件的一个series