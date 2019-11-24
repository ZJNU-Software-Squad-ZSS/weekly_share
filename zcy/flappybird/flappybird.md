


1.1机器学习
现在获得更多技术，我们可以询问机器学习可以为我们做些什么或可以完成什么任务。任务通常分为两类：

有监督的学习：在此任务中，我们可以通过提供示例输入示例和所需输出的示例来训练机器。机器将尝试找到将输入映射到输出的功能。
无监督学习：这里我们的输入没有直接连接到预期的输出。当尝试发现数据中的隐藏模式时，这很有用。
如何分辨使用哪一个？这取决于我们是否有学习信号。

在以上这两类中，我们讨论的是如何为机器提供良好的输入，但是在输出方面，我们还有其他类型的任务。这些通常被称为“这是什么类型的问题？”，类别如下：

分类：通过为机器提供训练的输入和输出，我们可以使用数据来预测它是否属于一个类别或另一个类别。例如，我们可以创建一台机器，通过向机器提供猫和狗的样本图像作为输入，从而区分猫和狗，而输出是这些机器的分类。
回归：在回归任务中，我们旨在优化随时间推移而不是预定义值生成输出的函数。在跳过障碍物示例中，我们可以基于您与障碍物之间的距离及其高度来应用回归任务。换句话说，机器将基于输入优化告诉我们是否跳转的功能。
聚类，密度 估计和降维是我们可以应用的其他类型的任务，不如本文的前两类重要。

1.2深度学习
在特定于任务的算法中，输入将产生输出，该输出将告诉我们一些信息。在深度学习中，这些输出不会立即成为我们的反馈，而是将它们用作另一层功能的输入。

一种常见的体系结构是利用神经网络，其中每个隐藏层都将接收前一层的输入。

1.3人工神经网络
这个奇特的名字和概念来自组成人脑的生物神经网络。神经网络由相互连接的节点（神经元）组成，将一些知识应用于输入值。

神经元
想象一下，神经元是一个接受数字并将其乘以另一个值的实体。该值称为权重，可以初始进行随机化。为了从该神经元获得输出值，我们需要激活它，这意味着我们将应用激活函数来产生输出。


激活函数的另一点是bias ，即增加的值将移动我们的函数轴。例如，采用一个返回0到1之间的值的函数。我们可以期望我们的输出在该范围内，这意味着我们将在此基础上设计结论。但是我们的模式可以在另一个范围内工作，例如2到3之间。因此，我们可以添加偏置来移动轴并适应新的输出范围。

层数
单靠一个神经元是无法解决问题的，我们需要更多的神经元。神经元层的通用名称是隐藏层，您可以在其中确定许多神经元以及它们与前一层的连接方式。  

可以根据需要连接各层，但通常的方法是创建一个完全连接的神经网络，这意味着一层中的神经元连接到另一层的每个神经元。

根据我们的问题，我们将发现的其他层是输入和输出层，它们也由任意数量的神经元组成。

如果您想了解有关人工神经元网络的更多信息，请从3Blue1Brown频道观看此视频。

2.什么是TensorFlow.js
TensorFlow是一个广泛使用的开源机器学习框架，主要针对Python分发，但也可以为Java，Go和C安装。随着社区的广泛发展，多年来它得到了改进，在机器学习中得到了崇敬，甚至被使用由美国国家航空航天局。



值得一提的，但是，TensorFlow.js不是网络的唯一和绝对的机器学习库，我们可以提到Synpatic和Brain.js。

张量
张量是类似于矩阵或向量的数学结构，但更灵活，这意味着您可以具有多维结构。

在TensorFlow.js中，张量 API为我们提供了一种创建和操作张量的简单方法，例如：

tf.tensor2d([[1, 2], [3, 4]]).print();
 
//output
Tensor
    [[1, 2],
     [3, 4]]
3.创建我的第一个神经网络
因此，在学习了TensorFlow.js教程的基础知识之后，我觉得我想尝试创建自己的简单神经网络。

让我们开始创建一个隐藏层：

	const NEURONS = 8;
 
	const hiddenLayer = tf.layers.dense({
    units: NEURONS,
    inputShape: [3],
    activation: 'sigmoid',
	});
因此，这里的layers API非常方便，我们使用的是密集的，它描述了一个完全连接的网络。请注意，我们这里没有创建输入层，而是说我的隐藏层的输入形状为3，这意味着我们将为隐藏层传递3个值。

对于这个特定的层，我决定使用称为sigmoid的激活函数。此函数以S形闻名，并遵循以下公式：

乙状结肠激活功能

图片来源

这将表明我的输出将在0到1之间。

我们缺少输出层。因此，我们添加一个：

	const outputLayer = tf.layers.dense({
    units: 1,
	});
现在我们有了神经网络，对吗？好吧，不完全是。我们确实设置了变量，但是它们没有相互连接。我们需要一个模型！

	const model = tf.sequential();
 
	model.add(hiddenLayer);
	model.add(outputLayer);
现在我们将要编译模型，但是我们需要指定两件事：损失函数和优化器函数：

model.compile({ loss: 'meanSquaredError', optimizer: 'sgd' });
损失函数将告诉我们输出与所需输出之间的距离，优化器函数将吸收该损失并更新我们的权重和偏差。


4.我有工具，下一步是什么？
在为前端编码时，您始终必须意识到浏览器的性能限制，并且使用TensorFlow.js也不例外。该库经过优化，可以使用GPU处理计算，这意味着错误可能会导致FPS非常低。

幸运的是，API为我们提供了足够的工具来解决这一问题。每当您手动执行操作时，假设您想向张量添加一个值，就需要使用整齐的函数：

	return tf.tidy(() =>  {
    return tensor.add(tf.randomUniform(tensor.shape, min, max));
	});
为什么？完成所需的操作后，tidy将负责清理函数中使用的所有张量，但返回的张量除外。请注意，这用于处理同步操作，因此用整洁的包装Promise无效。

5.使用TensorFlow.js的飞扬的小鸟


如原始存储库中所述，作者使用的神经网络有2个输入，6个神经元隐藏层和1个输出。



因此，我将创建以下结构：

	const NEURONS = 6;
 
	const hiddenLayer = tf.layers.dense({
    units: NEURONS,
    inputShape: [2],
    activation: 'sigmoid',
    kernelInitializer: 'leCunNormal',
    useBias: true,
    biasInitializer: 'randomNormal',
	);
 
	const outputLayer = tf.layers.dense({
    units: 1,
	});
判断鸟是否应该拍打的逻辑是：

	if (output > 0.5) {
    bird.flap();
	}
这告诉我输出将在0到1之间（您还记得Sigmoid函数吗？）。听起来我们有激活功能！

我通过尝试并检查那些会使我的输出保持在0.5左右的值来选择内核初始化程序和偏差初始化程序。

好的，现在我们有了模型，可以开始使用遗传算法创建鸟类种群了。但是到底是什么呢？

5.1遗传算法
该算法使用种群的自然选择来根据最佳个体生成下一个种群。我们需要一种方法来判断哪些人是最好的人，对于我们的问题，我们可以说最好的人是最能干的人。

原始实现将此定义为适应度，计算方法如下：

适应性=总行驶距离–到最接近的距离的距离

我们将根据他们的健康状况选择前4名获胜者，然后创建一些交叉点。这是我们的实现开始与原始实现略有不同的地方。

	evolvePopulation: function() {
    const Winners = this.selection();
 
    const crossover1 = this.crossOver(Winners[0], Winners[1]);
    const crossover2 = this.crossOver(Winners[2], Winners[3]);
 
    const mutatedWinners = this.mutateBias(Winners);
 
    this.Population = [crossover1, ...Winners, crossover2, ...mutatedWinners];
	}


要创建分频器，我们使用以下功能：

	crossOver: function(a, b) {
    const biasA = a.layers[0].bias.read();
    const biasB = b.layers[0].bias.read();
 
    return this.setBias(a, this.exchangeBias(biasA, biasB));
	},
这将返回一个张量，其中包含该层的偏差值。

	const biasA = a.layers[0].bias.read();


	exchangeBias: function(tensorA, tensorB) {
    const size = Math.ceil(tensorA.size / 2);
    return tf.tidy(() => {
        const a = tensorA.slice([0], [size]);
        const b = tensorB.slice([size], [size]);
 
        return a.concat(b);
    });
	},
因为我不想更改原始偏差，所以正在复制它。注意TensforFlow.js的对象是不可变的，因此函数write将返回一个新的张量，而不是对其进行设置。

	setBias: function(model, bias) {
    const newModel = Object.assign({}, model);
    newModel.layers[0].bias = newModel.layers[0].bias.write(bias);
 
    return newModel;
	},
我想创建一个变异的个体，所以我的变异函数将返回一个带有随机偏差的新模型：

	mutateBias: function(population) {
    return population.map(bird => {
        const hiddenLayer = tf.layers.dense({
            units: NEURONS,
            inputShape: [2],
            activation: 'sigmoid',
            kernelInitializer: 'leCunNormal',
            useBias: true,
            biasInitializer: tf.initializers.constant({
                value: this.random(-2, 2),
            }),
        });
 
        return this.createModel(bird.index, hiddenLayer);
  	  });
	},
我们在这里将偏差随机化，但是可能会有更合乎逻辑的方式来实现，例如，鸟类走得越远，随机化的值就越小。但是，-2和2之间的随机值对我们来说效果很好。



5.2我们如何训练模型？

为了测试模型，我们必须使用fit API：

	trainPopulation: function(population) {
    return population.map(async model => {
        await model.fit(tf.tensor2d(model.history),                         
	 tf.tensor1d(model.outputHistory), {
            shuffle: true,
        });
    });
	},





