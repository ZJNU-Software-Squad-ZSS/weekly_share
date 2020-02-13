# Machine Learning

### Steps：

**1.Import the Data**

**2.Clean the Data   去除重复和不相关数据**

**3.Split the Data into Training/Test Sets   训练/测试**

**4.Create a Model 根据问题类型选择算法**

**5.Train the Model**

**6.Make Predictions**

**7.Evaluation and improve**



###  Libraries and Tools

**Libraries 库：**

- Numpy 提供一个多维数组

- Pandas 数据分析库 提供一个称为数据帧的概念。数据帧是二维的

- MatPlotLib 二维绘图库

- Scikit-Learn  最流行的机器学习之一

**Tools：**

- Vscode或其他编译器不适合机器学习项目，我们经常要检查数据

- jupyter

- anavonda（Anaconda.com）

  安装完Anavonda后，在开始菜单中找到Anaconda Prompt 打开后输入jupyter notebook会自动打开一个浏览器窗口，指向本地主机



###  Importing a Data Set

**https://www.kaggle.com/**进入网站后先注册用户 

我用到是我的谷歌账号登录

```
import pandas as pd
df = pd.read_csv('vgsales.csv')
df.shape
```

导入vagsales.csv数据集

```
df.describe()
```

![166Fot.png](https://s2.ax1x.com/2020/02/06/166Fot.png)

在数据集中返回关于每一列的一些基本信息，我们有Rank ，Year等列，count是这一列中记录的数量，mean表示这一列所有数据的均值，std标准差

```
df.values
```

显示的是一个二维数组

![166uLj.png](https://s2.ax1x.com/2020/02/06/166uLj.png)

### Jupyter shortcuts

绿色左边框 表示单元格处于编辑模式

蓝色框  命令模式 按下H键 我们能看到所有Keyboard shortcuts

******

Jupyter笔记本有两种不同的键盘输入模式. **编辑模式**允许您将代码或文本输入到一个单元格中，并通过一个绿色的单元格来表示 **命令模式**将键盘与笔记本级命令绑定在一起，并通过一个灰色的单元格边界显示，该边框为蓝色的左边框。

```
a或b
```

在单元格之间插入一个单元格 ：A在选中单元格上面插入单元格，B在选中单元格下面插入单元格

```
连按两下d
```

删除选择选中的单元格



一个单元格只能执行那个单元格中的代码，即其他单元中的代码不会被执行

要想运行不止一个单元格点击上面cell进行选择



```
df.
```

长按Tab键会显示所有属性

![166dm9.png](https://s2.ax1x.com/2020/02/06/166dm9.png)

按下shift和tab键，查看这个属性的提示

按下ctrl+/将该行代码变为注释

Ctril+Enter运行当前单元格



### A Real Problem

一个音乐网站，根据注册用户的年龄和性别向他推荐不同的音乐

**1.Import the Data**

```
import pandas as pd
music_data = pd.read_csv('music.csv')
music_data
```

**2.Clean the Data   去除重复和不相关数据**

这个数据集没有重复和空值

另一件要做的事：将这个数据集分成两个独立的数据集，一个到输入集，一个到输出集

```
import pandas as pd
music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
X
```

music_data.drop(columns=['genre'])创建一个新的数据集没有genre这一列

```
import pandas as pd
music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']
y
```

music_data['genre']得到genre这一列 ，这个数据集里，我们只有答案或预测

**3.Learning and Predicting**

我们选择最简单的决策树算法

```
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']

model = DecisionTreeClassifier()            #建立模型，有了模型我们需要训练它
model.fit(X,y)                              #调用模型，参数是两个数据集（输入集和输出集）
predictions = model.predict([[21,1],[22,0]])#调用模型进行预测，在内数组内我们传入新的输入集
predictions                                 #输出预测结果
```

Out[12]:

```
array(['HipHop', 'Dance'], dtype=object)
```



**总结：**

  建立模型—>训练模型—>调用模型，进行预测新数据

  model = DecisionTreeClassifier()     
  model.fit(X,y)                              
  predictions = model.predict([[21,1],[22,0]])



### Calculating the Accuracy 测试算法的精确度

数据集分成两部分：一部分用于训练，一部分用于测试

70-80%的数据用于训练，还有20%-30%的数据用于测试



```
from sklearn.model_selection import train_test_split
```

使用这个函数train_test_split，我们可以很容易的将数据分成两组（训练和测试）

```
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)
```

X_train是训练输入集   在模型训练中用 取总数据集的80%(完全随机取的)

X_test是测试输入集  在预测时传递的参数 取总数据集的20%

y_train训练输出集   在模型训练中用 取总数据集的80%

y_test测试输出集  用于与预测值进行比较，计算精确度 取总数据集的20%



为了计算准确度在预测值和输出集中的实际值之间，我们导入新的函数，

```
from sklearn.metrics import accuracy_score
```

传递给它的参数包含预期值和实际值的预测，这个函数在0~1之间返回一个精确值

```
accuracy_score(y_test,predictions)
```



完整的代码：

```
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train,y_train)
predictions = model.predict(X_test)

score = accuracy_score(y_test,predictions)
score
```

我们每次运行获得的值不一样，因为每次用于训练和测试的数据是随机的



### Persisting Models 持久性模型

​    在实际应用中，我们会有成千上万个例子的数据集，需要训练很长时间，我们构建并训练我们的模型，然后将其保存到一个文件中，下次我们要做预测时，我们只需要从文件中加载模型，让它做预测，而不需要重新训练。

joblib函数有保存和加载模型的作用

```
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib

music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']

model = DecisionTreeClassifier()            
model.fit(X,y)       

joblib.dump(model,'music-recommender.joblib')
```

joblib.dump(model,'music-recommender.joblib')将model命名为music-recommender并以joblib形式保存在电脑中了

然后可以直接调用这个模型进行预测了

```
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib       

model = joblib.load('music-recommender.joblib')

predictions = model.predict([[21,1],[22,0]])
predictions
```

joblib.load('music-recommender.joblib')加载这个模型



**总结：**

- 1.在训练完模型后，用joblib.dump(model,'music-recommender.joblib')保存模型
- 2.要用到这个模型进行预测时，用model = joblib.load('music-recommender.joblib')，重新加载这个模型，可以直接预测了



### Visualizing a Decision Tree

  将决策图的算法以视图的方式展现出来

```
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['genre'])
y = music_data['genre']

model = DecisionTreeClassifier()            
model.fit(X,y)       

tree.export_graphviz(model,out_file='music-recommender.dot',
                     feature_names=['age','gender'],       #以年龄和性别作为特征
                     class_names=sorted(y.unique()),       #显示class的值
                     label='all',                          #每个标签可读
                     rounded=True,                        #将标签设为圆角
                     filled=True)                         #每一个盒子或节点都有颜色
```

运行后，将会生成music-recommender.dot文件，将文件拖入Vs编辑器里，下载dot插件在左上角点击Open Preview to the Side 打开视图