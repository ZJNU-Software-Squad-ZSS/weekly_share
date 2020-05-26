# Gluoncv_ssd

使用框架：mxnet。训练平台：google colab。

### pip包

colab上没有mxnet和opencv包，需要下载

`!pip install mxnet-cu101`
`!pip install --upgrade mxnet-cu101 gluoncv`
`!pip install opencv-python`

### 导包

```
import time
import numpy as np
import mxnet as mx
from mxnet import nd
from mxnet import gluon
from mxnet import autograd
import gluoncv
from gluoncv import utils
from gluoncv import model_zoo
from gluoncv.model_zoo.ssd.vgg_atrous import vgg16_atrous_512
# gcv.utils.check_version('0.6.0')
from gluoncv.data.batchify import Tuple, Stack, Pad
from gluoncv.data.transforms.presets.ssd import SSDDefaultTrainTransform
from gluoncv.data.transforms.presets.ssd import SSDDefaultValTransform

from gluoncv.utils.metrics.voc_detection import VOCMApMetric
```

### 装载Google云盘

```
from google.colab import drive

drive.mount('/content/drive')
```

### 导入数据集并解压

```
!unzip '/content/drive/My Drive/VOC2028/VOC2028.zip'
```

### 获取dataloader

读取trainvalue和testvalue，拆分数据集，并生成可供迭代的dataloader，以便直接按batch随机读取数据。

需要根据数据集格式和训练需求作调整，一般目标检测的数据集会需要三个文件（xml、jpg、txt），txt文件用来指定拆分训练集和测试集。

### 导入ssd模型

```python
net = model_zoo.get_ssd('vgg16_atrous', 512, features=vgg16_atrous_512, filters=None,
                  sizes=[51.2, 76.8, 153.6, 230.4, 307.2, 384.0, 460.8, 537.6],
                  ratios=[[1, 2, 0.5]] + [[1, 2, 0.5, 3, 1.0/3]] * 4 + [[1, 2, 0.5]] * 2,
                  steps=[8, 16, 32, 64, 128, 256, 512],
                  classes=classes, dataset='voc', pretrained=False,
                  pretrained_base=True)
net.initialize(init=mx.initializer.Xavier())
net.collect_params().reset_ctx(ctx)
```

### 存储模型参数和测试精度

### 训练配置

```python
# 参数设定
epochs, lr, wd, momentum = 100, 0.0005, 0.0005, 0.9

# 在lr_steps个epoch时，进行一次lr decay
lr_steps = (60, 80)
lr_decay = 0.1
# log：以batch为单位汇报损失； val：以epoch为单位测试并汇报精度； save：保存模型参数
log_interval, val_interval, save_interval = 5, 5, 50
# 记录最好的map
best_map = [0]
# 保存参数时的前缀
save_prefix = "ssd_helmet"

# 将模型参数置于gpu
net.collect_params().reset_ctx(ctx)

# 训练器
trainer = gluon.Trainer(
      net.collect_params(), 'sgd',
      {'learning_rate': lr, 'wd': wd, 'momentum': momentum})

# 损失定义
mbox_loss = gluoncv.loss.SSDMultiBoxLoss()
ce_metric = mx.metric.Loss('CrossEntropy')
smoothl1_metric = mx.metric.Loss('SmoothL1')
```

### 训练

```python
def train(net, trainer, train_data, val_data, eval_metric, ctx):
  for epoch in range(0, epochs):
    while lr_steps and epoch >= lr_steps[0]:
      new_lr = trainer.learning_rate * lr_decay
      lr_steps.pop(0)
      trainer.set_learning_rate(new_lr)
      print("[Epoch {}] Set learning rate to {}".format(epoch, new_lr))
    # 重置损失与时间
    ce_metric.reset()
    smoothl1_metric.reset()
    tic = time.time()
    btic = time.time()
    net.hybridize(static_alloc=True, static_shape=True)

    for i, batch in enumerate(train_data):
      # 取得数据与标准（target，对每个anchor预算出的cls与box偏移量）
      # cls_targets和box_targets并不唯一确定，每次对同一张图取都不一定一样
      data = gluon.utils.split_and_load(batch[0], ctx_list=ctx, batch_axis=0)
      cls_targets = gluon.utils.split_and_load(batch[1], ctx_list=ctx, batch_axis=0)
      box_targets = gluon.utils.split_and_load(batch[2], ctx_list=ctx, batch_axis=0)

      with autograd.record():
        cls_preds = []
        box_preds = []
        # 这因为data是list类型，所以取data[0]，x仍是batch_size张图片
        for x in data:
          cls_pred, box_pred, _ = net(x)
          cls_preds.append(cls_pred)
          box_preds.append(box_pred)
        sum_loss, cls_loss, box_loss = mbox_loss(
            cls_preds, box_preds, cls_targets, box_targets)
        
        autograd.backward(sum_loss)
      # since we have already normalized the loss, we don't want to normalize
      # by batch-size anymore
      trainer.step(1)

      # 更新loss并输出当前结果
      ce_metric.update(0, [l * batch_size for l in cls_loss])
      smoothl1_metric.update(0, [l * batch_size for l in box_loss])
      if log_interval and not (i + 1) % log_interval:
        name1, loss1 = ce_metric.get()
        name2, loss2 = smoothl1_metric.get()
        print('[Epoch {}][Batch {}], Speed: {:.3f} samples/sec, {}={:.3f}, {}={:.3f}'.format(
            epoch, i, batch_size/(time.time()-btic), name1, loss1, name2, loss2))
      btic = time.time()

    # 输出一个epoch时间消耗与loss
    name1, loss1 = ce_metric.get()
    name2, loss2 = smoothl1_metric.get()
    print('[Epoch {}] Training cost: {:.3f}, {}={:.3f}, {}={:.3f}'.format(
        epoch, (time.time()-tic), name1, loss1, name2, loss2))
    # 输出当前精度并对最好精度进行参数保存
    if (epoch % val_interval == 0) or (save_interval and epoch % save_interval == 0):
      # consider reduce the frequency of validation to save time
      map_name, mean_ap = validate(net, val_data, ctx, eval_metric)
      val_msg = '\n'.join(['{}={}'.format(k, v) for k, v in zip(map_name, mean_ap)])
      print('[Epoch {}] Validation: \n{}'.format(epoch, val_msg))
      current_map = float(mean_ap[-1])
    else:
      current_map = 0.
    save_params(net, best_map, current_map, epoch, save_interval, save_prefix)
train(net, trainer, train_data, val_data, val_metric, ctx)
```

### 测试和锚框绘制

### 小结

文档只记录了训练过程需要的主要代码，其他部分的代码其实是很耗时间的（如果还没熟练使用框架的话），但是不同的数据集格式、不同的训练需求下，写出来的代码不同，只能是依样画葫芦。

关于lr和batch，因为colab的内存限制，只能跑8个batch，如果有条件，其实可以跑16或者32甚至更多的batch，并且把lr设置稍大些（如0.001），当然这些只是个人“感觉”。