### 基数排序

基数排序的排序原理不难理解，但是在算法设计上，个人感觉还是比那些常见的排序要难的，耐心慢慢一步步理解，还是比较容易看懂的，注意基数排序有两种，一种是高位优先，一种是低位优先，在这里我只讲低位优先，即先排个位，再排十位……….

- 时间复杂度:
基数排序的时间复杂度为O (nlog(r)m)，其中r为所采取的基数，而m为堆数

- 排序原理:
排序数字为16,21,5,49,33,456,327,56,65,234
这是我测试的实例数字，下面有源程序，最高位有三位（程序里max=3）,所以要进行三遍排序（下图只排了两次，第三遍也一样啦），第一遍，以个位数分桶，个位相同放在一个桶里，然后把桶里的数在依次拿出来，第一次拿出，顺序为21，33，234，5，65，16，456，56，327，49   同理第二遍以十位数字比较，把第一遍拿出的数字再放进桶中，三次循环得到结果。
![](https://raw.githubusercontent.com/bananahab/text/master/docs/%E7%AC%AC%E4%B9%9D%E5%91%A8%E4%BD%9C%E4%B8%9A/image/07.png?token=AKNGWSNFK52GQEZE7LBGK5C5X3GRO)

### 栈的链表实现
![](https://raw.githubusercontent.com/bananahab/text/master/docs/%E7%AC%AC%E4%B9%9D%E5%91%A8%E4%BD%9C%E4%B8%9A/image/08.png?token=AKNGWSI2X2AEFTLLDTVOVJ25X3GQK)


