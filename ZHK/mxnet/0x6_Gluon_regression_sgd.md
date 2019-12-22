## 0x6_Gluon_regression_sgd

代码分为两个，regression-scratch   和   用gluon实现的 regression_gluon ，代码在jupyter notebook上实现 ，所以这次就直接传了两个 ipynb 上来。。。。。

主要的区别是在定义模型上，gluon不用管输入shape的特点在层数多的时候有很好的效益 。

两个代码的基本思想是一致的。在Gluon中，data模块提供了有关数据处理的工具，nn模块定义了大量神经网络的层，loss模块定义了各种损失函数。详情见代码~