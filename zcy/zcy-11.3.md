# Tensorflow数据类型

## Data Container
 - List:可添加任意类型的数据[1,1.2,"hello"],但是消耗内存大，读取慢
 - np.array：可以存储大量数据，存取方便[64,224,224,3]
 - tf.tensor
## What is tensor
 - scalar（标量）：1.1  维度=0
 - vector（向量）：[1,1]  维度=1
 - martrix（矩阵）：[[1.1,2.2],[3.3,4.4],[5.5,6.6]]
 - 以上都能称为tensor
 
## TF is a computing lib
 - int,float,double
 - bool
 - string

## Create tensor

```
In [2]: tf.constant(1)
Out[2]: <tf.Tensor 'Const:0' shape=() dtype=int32>

In [3]: tf.constant(1.)
Out[3]: <tf.Tensor 'Const_1:0' shape=() dtype=float32>

In [5]: tf.constant([True,False])
Out[5]: <tf.Tensor 'Const_2:0' shape=(2,) dtype=bool>

In [6]: tf.constant('hello world')
Out[6]: <tf.Tensor 'Const_3:0' shape=() dtype=string>
```
## Check Tensor Type

```
In [3]: a=tf.constant([1.])

In [4]: a.dtype
Out[4]: tf.float32

In [5]: b=tf.constant(1.)

In [6]: b.dtype
Out[6]: tf.float32

In [7]: isinstance(a,tf.Tensor)  ##不推荐这个方法，可能出错
Out[7]: True

In [8]: tf.is_tensor(b)
Out[8]: True

In [10]: a.dtype==tf.float32
Out[10]: True
```

## Convert

```
In [12]: import numpy as np

In [13]: n=np.arange(5)

In [14]: print(n)
[0 1 2 3 4]

In [15]: n.dtype
Out[15]: dtype('int32')
```
##转换为tensor
```
In [16]: nn = tf.convert_to_tensor(n)

In [17]: print(nn)
Tensor("Const_2:0", shape=(5,), dtype=int32)
```
##转换为int64
```
In [21]: nn = tf.convert_to_tensor(n,dtype=tf.int64)

In [22]: print(nn)
Tensor("Const_4:0", shape=(5,), dtype=int64)
```
##使用cast方法
```
In [24]: tf.cast(nn,dtype=tf.float32)
Out[24]: <tf.Tensor 'Cast:0' shape=(5,) dtype=float32>
```
##int转换为bool  1为true  0为false
```
In [30]: w= tf.constant([0,1])

In [31]: tf.cast(w,dtype=tf.bool)  反向同理
Out[31]: <tf.Tensor 'Cast_1:0' shape=(2,) dtype=bool>
```


## tf.Variable




# Create Tensor
#### From Numpy,list


##numpy
```
In [4]: tf.convert_to_tensor(np.ones([2,3]))
Out[4]: <tf.Tensor 'Const:0' shape=(2, 3) dtype=float64>
```
##list
```
In [6]: tf.convert_to_tensor([1,2.])
Out[6]: <tf.Tensor 'Const_1:0' shape=(2,) dtype=float32>
```

 

#### From tf.zeros

```
In [7]: tf.zeros([])
Out[7]: <tf.Tensor 'zeros:0' shape=() dtype=float32>
```


#### From tf.zeros_like

```

In [9]: tf.zeros_like(a)
Out[9]: <tf.Tensor 'zeros_like:0' shape=(2, 3, 3) dtype=float32>
```
#### From tf.ones

```
In [10]: tf.ones(1)
Out[10]: <tf.Tensor 'ones:0' shape=(1,) dtype=float32>
```
#### From Fill

```
In [11]: tf.fill([2,2],0)
Out[11]: <tf.Tensor 'Fill:0' shape=(2, 2) dtype=int32>
```

