# iOS UIView Animation
## 登陆动画
> 如何抛开CALayer层使用UIKit动画接口

动画原理： 两个文本框从屏幕左边进入，下方的按钮从隐藏（alpha实现）到显示。
简单来说可以写成：

```swift
self.userName.center.x += offset;  // userName slide in
self.password.center.x += offset;  // password slide in
self.login.alpha = 1;  // login button reveal
```

使用UIKit动画API

```swift
// set original position of the textbox to the left of the screen
CGPoint accountCenter = self.userName.center;
CGPoint psdCenter = self.password.center;
accountCenter.x -= 200;
pasCenter.x -= 200;
self.userName.center = accountCenter;
self.password.center = psdCenter;

// reset the center position
accountCenter.x += 200;
psdCenter.x += 200;        
[UIView animateWithDuration: 0.5 animations: ^{
  self.userName.center = accountCenter;
  self.password.center = passwordCenter;
    self.login.alpha = 1;
} completion: nil];
```

* UIKit 中， animate开头的属于UIView的类方法，每一个这样的类方法提供了名为 animations 的 block 代码块，这些代码会在方法调用后立即或者延迟一段时间以动画的方式执行。所有这些API的第一个参数都是用来设置动画时长的。

> 接下来可以进一步让三个组件的动画错开，使得密码框在账户框出现一段时间后再出现，再来是按钮。

```swift
[UIView animateWithDuration: 0.5 delay: 0.35 options: UIViewAnimationOptionCurveEaseInOut animations: ^{
  self.password.center = passwordCenter;
} completion: ^(BOOL finished) {
  [UIView animateWithDuration: 0.2 animations: ^{
    self.login.alpha = 1;
  }];
}];
```

> 密码输入框在延迟0.35s后开始出现，动画持续0.5s后开始渐变显示按钮

几个参数：

`duration` 动画时长
`delay` 动画在延迟多久之后执行
`options` 动画的展示方式
`animations` 转化成动画表示的代码
`completion` 动画结束后执行的代码块



## 可实现动画的属性

> 不是所有修改属性的操作放到 animations 代码块中都变成动画实现
>> 例如不管如何修改一个视图的tag，或者是delegate。

> 可实现动画的属性必定会导致视图的重新渲染。

* 可以生成动画的属性大致分为三类：`坐标尺寸`、`视图显示`、`形态变化`

### 坐标尺寸类 属性

`bounds` 修改此属性会结合center属性重新计算frame。建议通过这个属性修改尺寸
`frame` 修改此属性通常会导致视图形变的同时也发生移动，然后会重新设置center跟bounds属性
`center` 设置后视图会移动到一个新位置，修改后会结合bounds重新计算frame

### 视图显示类 属性

`backgroundColor:` 修改此属性会产生颜色渐变过渡的效果，本质上是系统不断修改了tintColor来实现的
`alpha` 修改此属性会产生淡入淡出的效果
`hidden` 修改此属性可以制作翻页隐藏的效果

### 形态变化类 属性

`transform` 修改此属性可以实现旋转、形变、移动、翻转等动画效果，其通过矩阵运算的方式来实现，因此更加强大

## 动画参数

上面用到的动画方法中有一个重要的参数options，用于高度的自定义动画效果。

### 参数 options 的值集合

> 可通过结合不同的参数来实现自己的动画

#### Repeating

 `UIViewAnimationOptionRepeat`       //动画循环执行
 `UIViewAnimationOptionAutoreverse`  //动画在执行完毕后会反方向再执行一次

> 将这两个参数传入到上面密码框出现动画中（不同的参数使用|操作符一起传入）

```swift
    [UIView animateWithDuration: 0.5 delay: 0.35 options: UIViewAnimationOptionAutoreverse | UIViewAnimationOptionRepeat animations: ^{
      self.password.center = passwordCenter;
    } completion: ^(BOOL finished) {
      [UIView animateWithDuration: 0.2 animations: ^{
        self.login.alpha = 1;
      }];
    }];
```

效果是密码框不断的循环进入屏幕，反方向退出屏幕。登录按钮始终没有渐变出现。
`UIViewAnimationOptionRepeat` 参数不仅是让动画循环播放，并且使得completion的回调永远无法执行。

#### Easing
> 使得动画更符合认知的规则
>> 任何事物都不能突然间的开始移动和停下，例如车辆启动和停止都有一个加速和减速的过程。

 系统提供的类似的效果的参数

`UIViewAnimationOptionCurveEaseInOut`   //先加速后减速，默认
`UIViewAnimationOptionCurveEaseIn`      //由慢到快
`UIViewAnimationOptionCurveEaseOut`     //由快到慢
`UIViewAnimationOptionCurveLinear`      //匀速

小例子

> 创建四个橙色的UIView，分别传入这四个不同的参数，然后让这四个view在同一时间y轴上向上移动。

```swift
  [self animatedView: _view1];
  [self animatedView: _view2];
  [self animatedView: _view3];
  [self animatedView: _view4];

  //y轴上移动视图上升250
  - (void)animatedView: (UIView *)view
  {
      [UIView animateWithDuration: 0.5 delay: 0 options: UIViewAnimationOptionCurveLinear animations: ^{
          CGPoint center = view.center;
          center.y -= 250;
          view.center = center;
      } completion: nil];
  }
```

> 在模拟器运行状态下，点击上面的菜单栏 DEBUG -> Slow Animation 或者快捷键 command + T，来放慢app的动画运行速度（在iPhone11的模拟器上运行）。

四个view的速度变化：
1. 逐渐加速。EaseIn
2. 先加速，后减速。EaseInOut
3. 速度领先，然后减速。EaseOut
4. 匀速运动。Linear

运行最开始的登录动画，放慢模拟器的动画速度，能看到默认情况下使用的EaseInOut参数使得密码框在接近结束点的时候出现了明显的减速动画。

#### Transitioning
> 除了上面提到的效果，在视图、图片切换的时候，还能通过传入以下参数来实现一些特殊的动画效果。

`UIViewAnimationOptionTransitionNone` //没有效果，默认
`UIViewAnimationOptionTransitionFlipFromLeft` //从左翻转效果
`UIViewAnimationOptionTransitionFlipFromRight` //从右翻转效果
`UIViewAnimationOptionTransitionCurlUp` //从上往下翻页
`UIViewAnimationOptionTransitionCurlDown` //从下往上翻页
`UIViewAnimationOptionTransitionCrossDissolve` //旧视图溶解过渡到下一个视图
`UIViewAnimationOptionTransitionFlipFromTop` //从上翻转效果
`UIViewAnimationOptionTransitionFlipFromBottom` //从上翻转效果

使用示例

```swift
[UIView transitionWithView: firstPV duration: 0.5 options: UIViewAnimationOptionTransitionFlipFromLeft animations: ^{
[firstPV flipCard];
} completion: ^(BOOL finished) {
isAnimating = NO;
}];

- (void)flipCard
{
  if (isfliped) {
     self.image = [UIImage imageNamed: @"flipPicBG.png"];
     isfliped = NO;
     } else {
        self.image = [UIImage imageNamed: [NSString stringWithFormat: @"flipPic%d.png", type]];
        isfliped = YES; 
     }
}
```

这段代码中改变了一个UIImageView的图片显示，同样用了一个动画的方式表现。

这里用到了一个新的动画API方法：
`transitionWithView: duration: options: animations: completion:` 
这个方法跟上面的animateWithDuration系列方法相比多了一个UIView类型的参数，这个参数接收的对象作为动画的作用者。这段代码点击之后的动画效果如下：

> 模拟器下使用command+T放慢了动画的速度之后截取的翻转的四张图片：

在切换图片的时候，原有的图片会基于视图中心位置进行x轴上的翻转，为了达到更逼真的效果，系统会在切换中加上了阴影效果
> 要说明的是，transition的动画应该只用在视图的切换当中 —— 该动画不会在移动中产生任何transition效果的

## 弹簧动画

> 实现一个弹簧被压扁，当松开手的时候会反复弹动的动画
使用上面的方式可以实现这样的动画，但代码量复杂，也基本无复用性可言。

因此，系统提供了另一种动画供使用：

```swift
+ (void)animateWithDuration:(NSTimeInterval)duration delay:(NSTimeInterval)delay usingSpringWithDamping:(CGFloat)dampingRatio initialSpringVelocity:(CGFloat)velocity options:(UIViewAnimationOptions)options animations:(void (^)(void))animations completion:(void (^ __nullable)(BOOL finished))completion
```

`dampingRatio` 速度衰减比例。取值范围0 ~ 1，值越低震动越强
`velocity` 初始化速度，值越高则物品的速度越快

效果：

小球弹出的动画代码：

```swift
CGPoint center = cell.center;
CGPoint startCenter = center;
startCenter.y += LXD_SCREEN_HEIGHT;
cell.center = startCenter;

[UIView animateWithDuration: 0.5 delay: 0.35 * indexPath.item usingSpringWithDamping: 0.6 initialSpringVelocity: 0 options: UIViewAnimationOptionCurveLinear animations: ^{
    cell.center = center;
} completion: nil];
```

除了这段弹出的代码，在小球被点击的时候，还会产生一个弹到右下角的动画，然后从左侧弹出列表。这样的动画示能效果很好，用户学习使用软件的成本低。

## 总结

相比起PC端的粗糙，移动端的应用需要更加精致，精致复杂的动画都是源于一个个简单的动画组合而成的。最后吐槽一下今天网络很差。不管是实验室还是寝室还是手机热点，打开外网太慢了。


