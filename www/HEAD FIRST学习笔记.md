# HEAD FIRST学习笔记

why？

软件体系结构与设计模式的reading任务，且对oop理解不透

本书代码可从官网https://www.wickedlysmart.com/head-first-design-patterns/处下载。

## CHAPTER ONE

##### 鸭子模拟应用

问题一：部分父类中的行为并不适合子类（橡皮鸭不会飞）

:anchor:设计原则：独立出需要改变的部分，**让系统中某部分改变不会影响其他部分**

​	解决方案一：在子类中覆盖该方法

​		此方案存在问题：改动父类后要对所有的子类作出调整、同时覆盖该方法的代码冗余

​	解决方案二：应用接口（将父类中需要改动的方法抽取出来放进行为接口）

​		相关概念：interface仅允许创建一个类的形式（有方法名、参数列表和返回类型，**但无任何方法体**）

​		此方案存在问题：java接口不能实现代码，继承接口并未实现对代码的复用

:anchor:针对接口编程，而不是针对实现编程​

解决方案三：使用相对应的行为接口，并制造相应的类实现接口（行为类）

​	此方案优势：具体的“实现”不会绑定在子类中

​	相关概念：程序针对超类进行编程，依据实际情况执行到对应的行为

```java
//“针对实现编程”
Dog d = new Dog();
d.bark();
//“针对接口/超类型编程”
Animal animal = new Dog();
animal.makeSound();
//已知对象是狗，但是利用animal来进行多态的调用
```

​	实现方法：声明行为接口，并创建引用变量，父类在行为类中指定相应的方法（通过接口指定），而子类将会继承变量从而指定方法。并可以通过setter方法动态指定行为类型

:anchor:多用组合，少用继承

**可维护性和可扩展性**

#### 策略模式（Strategy Pattern）

定义了算法族，分别封装起来，让它们之间可以互相替换，此模式让算法的变化独立于使用算法的客户

设计模式可以把你的思考架构的层次提高到模式层面，而不是仅停留在琐碎的对象上。

使用专有名词，提高对话（会议）效率……

设计模式告诉我们如何组织类和对象以解决某种问题。

## CHAPTER TWO

#### 观察者模式（Observer Pattern）

定义了对象之间的一对多依赖，这样依赖，当一个对象改变状态时，它色所有依赖着都会收到通知并自动更新

:anchor:为了交互对象之间的松耦合设计而努力

其中UML类图出现得挺频繁

![](https://i.bmp.ovh/imgs/2020/04/6959d2490ebabb09.png)

1. association 关联关系 类之间互相影响

2. inheritance  泛化关系 “is a“

3. realization 实现关系 类实现接口

4. dependency 依赖关系 临时性的关联，耦合度最弱

5. aggregation  聚合关系 ”has a“ 没有整体时，局部也可以存在

6. composition 组合关系 ”contains a“ 部分不能脱离整体而存在

   

##### 气象站设计

再来看书本给出的观察者模式的定义，主题接口Subject 是一个 观察者Observer。一个具体的主题将实现主题接口，而具体的观察者将实现观察者接口并成为一个具体的主题。（一本正经看图说话哈哈哈哈）

具体看下图（书P52），

![](https://i.bmp.ovh/imgs/2020/04/c40f24cdf4b59877.png)

也就是说，一个观察者会去观察一个特定的内容（主题），并且准备好去更新内容。在具体的主题里，必须设置注册、撤销方法，而notifyObservers（）则是在状态改变时去更新当前的观察者（其实我时嫌弃翻译差、、）。

如何去设计气象站，思路当然是要去搞主题接口，观察者接口，然后有几个布告板就有几个具体的主题类，同时为每一个类都实现一个特定的观察者。

现有模式的弊端：

由主题subject一次性送出大量数据至观察Observers，其中数据可能不满足观察者的需要，并且功能扩展相对繁琐（当新增更多的状态时，需要更改对每位观察者的调用）

解决方案：Java api中有内置的观察者模式，java.util包内包含Observer接口和Observable类，极大的方便了开发者的使用，可以用推（push）或拉（pull）的方式来传递数据，如下图，

![](https://i.bmp.ovh/imgs/2020/04/76f4aea21395a90b.png)

结合之前的那张图来看，我们可以发现，Subject接口和具体类被包装成继承Observable的WeatherData(直接以具体的主题来命名而非ConcreteSubject了)，而具体的观察者仍然是继承Observer，但直接被分类成GeneralDispaly、StatisticsDisplay、ForecastDisplay来实现功能。

可观察者送出通知：

1、调用setChanged()方法，标记状态的改变

2、调用notifyObservers()；

## CHAPTER THREE

:anchor:类应该对扩展开放，对修改关闭。（开闭原则）

#### 装饰者模式

装饰者模式动态地将责任附加到对象上，若要扩展功能，装饰者提供了比继承更有弹性的替代方案。

![](https://i.bmp.ovh/imgs/2020/04/608195c6dadebdbe.png)

在子类中如何引用父类（被装饰者），去用一个实例变量记录父类（被装饰者），把父类的名称（或其他要引用的东西）当作构造器的参数，再由构造器记录在实例变量当中。

![](https://i.bmp.ovh/imgs/2020/04/69f756e2b6b83d6d.png)

看到这张图我震惊了，javaIO没好好学,嗯没看出什么名堂来

![](https://pic1.zhimg.com/80/v2-eb408ac849a679b09941be7ebd734768_1440w.jpg)

![](https://i.bmp.ovh/imgs/2020/04/0ed01dbc1a35fefa.png)

## CHAPTER FOUR

我们会去用接口来实例化具体对象，但是究竟具体到哪一个是根据运行时的具体情况，但在后续的变化或扩展中，容错性降低。

解决方案：封装创建对象的代码。也就是指，将会变化的那一部分封装成一个类。

不需要使用创建对象的方法来实例化对象时，可以用静态方法来定义一个简单的工厂。

事实上，简单工厂不是一个设计模式，更加接近一种编程习惯。

“实现一个接口并不一定表示”写一个类，并利用implement关键字来实现某个Java接口“，“实现一个接口”泛指“实现某个超类型（可以是类或接口）的某个方法”。

Pizza店例子，

1.第一个举例的简单工厂还是比较好理解的，简单过一遍，

实例化工厂，工厂能有制造piazza的方法，能够具体到具体哪一个piazza[Cheese/Pepperon/Veggie]，将这个新创建的工厂产品送至store（store完成pizza具体的制作过程），用户点单，选择要的pizza，在工厂生产的一系列产品中选择，得到pizza。

在这个过程中，piazza的类型可以很容易在工厂中修改与创建，即符合了第一条设计原则——将要变化的过程抽取出来。

2.第二个书上没有明说是否是抽象工厂，翻GoF看得昏昏欲睡，先不计较这个，来看实例代码干了什么。

第一件事是在各地开设门店，

```java
PizzaStore nyStore = new NYPizzaStore();
		PizzaStore chicagoStore = new ChicagoPizzaStore();
```

门店中实现了pizza的制作功能，客户前往各地商店[NewYork/Chicago]购买pizza，于是地方商店类根据客户需要创造对应的pizza对象（实例化过程被包装到地方商店类里）。所有的Piazza继承自Piazza抽象类，各个地方的PizzaStore继承自PizzaStore抽象类。

#### 工厂模式

所有的工厂模式都用来封装对象的创建。工厂方法模式（Factory Method Pattern）通过让子类决定该创建的对象是什么，来达到将对象创建的过程封装的目的。

![](https://i.bmp.ovh/imgs/2020/04/659cb1287e5080c3.png)

![](https://i.bmp.ovh/imgs/2020/04/01540abe1915c7b4.png)

![](https://i.bmp.ovh/imgs/2020/04/be3281c4a3a36130.png)

通过用户行为orderPiazza（），产品类与创建者相连通。

:anchor:工厂方法模式定义了一个创建对象的接口，但由子类决定要实例化的类是哪一个。工厂方法让类把实例化推迟到子类。

![](https://i.bmp.ovh/imgs/2020/04/1e68f384572e1dc0.png)

书上给出了直接嵌套if else来创建piazza对象的代码，

```java
public class DependentPizzaStore {
 
	public Pizza createPizza(String style, String type) {
		Pizza pizza = null;
		if (style.equals("NY")) {
			if (type.equals("cheese")) {
				pizza = new NYStyleCheesePizza();
			} else if (type.equals("veggie")) {
				pizza = new NYStyleVeggiePizza();
			} else if (type.equals("clam")) {
				pizza = new NYStyleClamPizza();
			} else if (type.equals("pepperoni")) {
				pizza = new NYStylePepperoniPizza();
			}
		} else if (style.equals("Chicago")) {
			if (type.equals("cheese")) {
				pizza = new ChicagoStyleCheesePizza();
			} else if (type.equals("veggie")) {
				pizza = new ChicagoStyleVeggiePizza();
			} else if (type.equals("clam")) {
				pizza = new ChicagoStyleClamPizza();
			} else if (type.equals("pepperoni")) {
				pizza = new ChicagoStylePepperoniPizza();
			}
		} else {
			System.out.println("Error: invalid type of pizza");
			return null;
		}
		pizza.prepare();
		pizza.bake();
		pizza.cut();
		pizza.box();
		return pizza;
	}
}

```

~~看完之后觉得上面这个很像是在互联网上订购pizza，而工厂方法则是模仿到店点餐的原始pizza店（毕竟乍看之下似乎是上面那个逻辑很直接，虽然实现、、繁琐）~~

:anchor:要依赖抽象，不要依赖具体类【依赖倒置原则】

:ear_of_rice:变量不可以持有具体类的引用 （改用工厂）

:ear_of_rice:不要让类派生自具体类 （派生自一个抽象[接口、抽象类]）

:ear_of_rice:不要覆盖子类中已实现的方法​

3.现有的pizza店内加入原料相关类

#### 抽象工厂模式

提供了一个接口，用于创建相关或依赖对象的家族，而不需要明确具体类

![](https://i.bmp.ovh/imgs/2020/04/c0be04ddde0ef9ff.png)

抽象工厂允许客户使用抽象的接口来迟创建一组相关的产品，而不需要知道实际产出的具体产品是什么。这样一来，客户就从具体的产品中被解耦。（而工厂方法里用的是包装到某一特定类中）

抽象工厂的任务是定义一个负责创建一组产品的接口。这个接口内每个方法都负责创建一个具体产品，同时我们利用实现抽象工厂的子类来提供这些具体的方法。

区分：

抽象工厂与工厂方法都是负责从子类中创建对象，将客户从具体类型从解耦，其中工厂方法采用继承，而抽象工厂使用对象的组合。“使用对象的组合”意指，抽象方法定义一个用来创建一个产品家族的抽象类型，这个类型的 子类去定义产品生产的方法。将这个工厂的实例化对象传入针对抽象类型的代码中，实现解耦。













