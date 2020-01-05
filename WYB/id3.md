主要内容
（1）ID3算法简介

（2）ID3算法节点分裂规则

（3）ID3算法实例

（4）剪枝

------

一、简介
1、信息熵Entropy

![H(S)=\sum p_{i}log(p_{i})](https://private.codecogs.com/gif.latex?H%28S%29%3D%5Csum%20p_%7Bi%7Dlog%28p_%7Bi%7D%29)

其中为第i个类别的概率，S是样例集合

信息熵越大，样本越混乱；信息熵越小，样本越纯净。

2、期望信息

设特征A具有v个不同的类别，其样本个数分别记为

![H(S|A) = \sum_{i} \frac{|c_{j}|}{|c|}p_{ij}log(p_{ij})](https://private.codecogs.com/gif.latex?H%28S%7CA%29%20%3D%20%5Csum_%7Bi%7D%20%5Cfrac%7B%7Cc_%7Bj%7D%7C%7D%7B%7Cc%7C%7Dp_%7Bij%7Dlog%28p_%7Bij%7D%29)

E(A)特征A的期望信息，为特征A的第j个类别的数量占特征A所有类别的概率，为特征A下第j个类别中占样例集合S不同类别的概率

3、信息增益

为特征A的信息增益

![G_{A}(S) = H(S) - H(S|A)](https://private.codecogs.com/gif.latex?G_%7BA%7D%28S%29%20%3D%20H%28S%29%20-%20H%28S%7CA%29)

信息熵越小，信息增益越大，样本越纯净

选择信息增益最大的特征作为分裂标准

二、实例
1、样本（特征必须离散变量，支持多特征、多分类）

1024个样本，4个特征，2个分类

计数	年龄	收入	学生	信誉	是否购买
64	青	高	否	良	否
64	青	高	否	优	否
128	中	高	否	良	买
60	老	中	否	良	买
64	老	低	是	良	买
64	老	低	是	优	否
64	中	低	是	优	买
128	青	中	否	良	否
64	青	低	是	良	买
132	老	中	是	良	买
64	青	中	是	优	买
32	中	中	否	优	买
32	中	高	是	良	买
64	老	中	否	优	否
2、计算信息熵

![H\left ( S \right ) =- \sum_{i}p_{i}log(p_{i}) = -\frac{384}{1024}*log\left ( \frac{384}{1024} \right )- \frac{1024-384}{1024}*log\left ( \frac{1024-384}{1024} \right ) =0.9544](https://private.codecogs.com/gif.latex?H%5Cleft%20%28%20S%20%5Cright%20%29%20%3D-%20%5Csum_%7Bi%7Dp_%7Bi%7Dlog%28p_%7Bi%7D%29%20%3D%20-%5Cfrac%7B384%7D%7B1024%7D*log%5Cleft%20%28%20%5Cfrac%7B384%7D%7B1024%7D%20%5Cright%20%29-%20%5Cfrac%7B1024-384%7D%7B1024%7D*log%5Cleft%20%28%20%5Cfrac%7B1024-384%7D%7B1024%7D%20%5Cright%20%29%20%3D0.9544)

3、计算特征A的信息熵

假设以年龄为例：

分为青年：384/0.375（样本/概率）、中年：256/0.25（样本/概率）、老年：384/0.375（样本/概率）

以年龄为特征的熵为：

![H(S|A) =0.375*H(S|A_{1})+0.25*H(S|A_{2})+0.375*H(S|A_{3})](https://private.codecogs.com/gif.latex?H%28S%7CA%29%20%3D0.375*H%28S%7CA_%7B1%7D%29&plus;0.25*H%28S%7CA_%7B2%7D%29&plus;0.375*H%28S%7CA_%7B3%7D%29)

青年：128/256（买/不买），概率为1/3和2/3（买/不买）

![H(S|A_{1})=-[\frac{1}{3}*log(\frac{1}{3})+\frac{2}{3}*log(\frac{2}{3})]=0.9149](https://private.codecogs.com/gif.latex?H%28S%7CA_%7B1%7D%29%3D-%5B%5Cfrac%7B1%7D%7B3%7D*log%28%5Cfrac%7B1%7D%7B3%7D%29&plus;%5Cfrac%7B2%7D%7B3%7D*log%28%5Cfrac%7B2%7D%7B3%7D%29%5D%3D0.9149)

中年：256/0（买/不买），概率为1和0（买/不买）

![H(S|A_{2})=-[0*log(0)+1*log(1)]=0](https://private.codecogs.com/gif.latex?H%28S%7CA_%7B2%7D%29%3D-%5B0*log%280%29&plus;1*log%281%29%5D%3D0)

老年：256/128（买/不买），概率为2/3和1/3（买/不买）

![H(S|A_{3})=-[\frac{2}{3}*log(\frac{2}{3})+\frac{1}{3}*log(\frac{1}{3})]=0.9149](https://private.codecogs.com/gif.latex?H%28S%7CA_%7B3%7D%29%3D-%5B%5Cfrac%7B2%7D%7B3%7D*log%28%5Cfrac%7B2%7D%7B3%7D%29&plus;%5Cfrac%7B1%7D%7B3%7D*log%28%5Cfrac%7B1%7D%7B3%7D%29%5D%3D0.9149)

故得到以年龄为特征的熵（平均信息期望/条件熵）为

![H(S|A) =0.375*H(S|A_{1})+0.25*H(S|A_{2})+0.375*H(S|A_{3})=0.6862](https://private.codecogs.com/gif.latex?H%28S%7CA%29%20%3D0.375*H%28S%7CA_%7B1%7D%29&plus;0.25*H%28S%7CA_%7B2%7D%29&plus;0.375*H%28S%7CA_%7B3%7D%29%3D0.6862)

年龄特征的信息增益为：

![G_{A}(S)=H(S)-H(S|A)=0.9544-0.6862=0.2628](https://private.codecogs.com/gif.latex?G_%7BA%7D%28S%29%3DH%28S%29-H%28S%7CA%29%3D0.9544-0.6862%3D0.2628)

同理可得

收入：![H(S|B)=0.7811,G_{B}(S)=0.1733](https://private.codecogs.com/gif.latex?H%28S%7CB%29%3D0.7811%2CG_%7BB%7D%28S%29%3D0.1733)

学生：![H(S|C)=0.9631,G_{C}(S)=0.0183](https://private.codecogs.com/gif.latex?H%28S%7CC%29%3D0.9631%2CG_%7BC%7D%28S%29%3D0.0183)

信誉：![H(S|D)=0.9048,G_{D}(S)=0.0496](https://private.codecogs.com/gif.latex?H%28S%7CD%29%3D0.9048%2CG_%7BD%7D%28S%29%3D0.0496)

可以看出，‘年龄’的信息增益最大，因此选择‘年龄’作为节点来划分。

按此方法，直至叶节点为’纯‘的结束。

三、剪枝
树的剪枝包括预剪枝和后剪枝，通过提前停止树的构造进行剪枝的方法称为预剪枝，后剪枝是首先构造完整的决策树，然后把置信度不够节点子树替代为叶子节点的过程。

预剪枝判断停止树的生长可以归纳为以下几种：

1、树的高度限制：设定树的高度最大值，当达到限定值时，停止树的生长；

2、训练样本限制：对一个拥有较少训练样本的节点进行分裂时容易出现过拟合现象，因此设定样本量阀值，当样本量少于阀值时停止生长；

3、系统性能增益：当属性的信息增益小于某个指定的阀值时停止增长。

相对而言预剪枝比较简单，在实际的运用中运用最广的还是后剪枝。

后剪枝算法主要有以下几类：

1、降低错误剪枝REP(Reduced Error Pruning)；

2、悲观错误剪枝PER(Pessimistic Error Pruning)；

3、基于错误剪枝EBP(Error-Based Pruning)；

4、代价-复杂度剪枝CCP(Cost-Complexity Pruning)；

5、最小错误剪枝MEP(Minimun Error Pruning)

以上算法的理论介绍详见：

http://wenku.baidu.com/view/415c3cc19ec3d5bbfd0a7464.html?re=view

四、总结
1、ID3算法的流程

（1）自上而下贪婪搜索

（2）遍历所有的属性，按照信息增益最大的属性进行分裂

（3）根据分裂属性划分样本

（4）重复上述流程，直至满足条件结束

2、ID3算法的特点

（1）上述过程可以看出，ID3算法倾向于选择属性值较多的属性，有些时候不能提供有价值的信息

（2）贪婪性以及奥姆剃刀原理（尽量用较少的东西做更多的事）

（3）不适用于连续变量

（4）只能用于分类
