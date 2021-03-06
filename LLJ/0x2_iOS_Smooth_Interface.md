#  iOS开发之流畅界面的开发
- 界面卡顿产生原因及解决方案
- 开发流畅界面 - ASDK（AsyncDisplayKit）

## 卡顿产生的原因和解决方案

### 屏幕图像显示原理

屏幕由像素点阵组成。可以分割成有限多行的像素。

>
* 假设屏幕左上角坐标为（0，0）
* 水平方向向右为x轴正向，垂直方向向下为y轴正向
* 点阵的x，y轴坐标均从0到Max。

<P align=center>
 <img src="https://cdn.jsdelivr.net/gh/AppleisTasty/Materials/0x2_pic2.png" width="580">
</p>

1. 使得屏幕得以成像的电子枪会从（0，0）点开始
先以y轴不变，x轴从0至max扫描电子，完成一行像素的呈现。
2. 此时显示器会发出一个水平同步信号（HSync：Horizontal Synchronization）提示电子枪可跳转到新的一行，此时y轴值+1，x轴值归0.
3. 重复向右及向下跳转的过程，直到完成所有行的扫描。电子枪将接受一个垂直同步信号（VSync：Vertical Synchronization），电子枪复原到（0，0）位。此时完成整幅画面的一帧的呈现
4. 重复1-2-3步骤完成下一帧扫描。


>常听到的屏幕刷新率就是这里的`VSync`.

### 计算机系统中的图像显示原理

CPU计算好显示内容提交给GPU
GPU渲染后放入帧缓冲区
视频控制器按照VSync信号逐行读取帧缓冲区的数据
视频控制器通过数模转换传递给显示器显示

<P align=center>
 <img src="https://cdn.jsdelivr.net/gh/AppleisTasty/Materials/0x2_pic3.PNG" width="580">
</p>

因为单帧缓冲区都会有比较大的读取和刷新问题，
所以iOS设备始终使用的是双帧缓冲区并开启垂直同步。
双缓冲区即两个缓冲区交替使用；这样当视频控制器在其中一个缓冲区读取内容的时候，GPU可将新的一帧内容放在第二缓冲区，并调整视频控制器的指针到第二缓冲区。

> 为什么开启垂直同步

双缓冲区存在一个问题：
有时候GPU控制指针过快，会导致前一帧读取一半就被拉来读后一帧，因此会造成画面撕裂（如图）。


<P align=center>
 <img src="https://cdn.jsdelivr.net/gh/AppleisTasty/Materials/0x2_pic1.jpeg" width="580">
</p>


GPU中的机制：`垂直同步` 就可以解决这个问题，开启垂直同步以后，GPU会等待显示器的VSync信号发出以后才进行新的一帧的渲染和缓冲区更新。
这样能解决画面撕裂现象，也增加了画面流畅度，但需要消费更多的计算资源，带来延迟。

* 安卓系统是三缓存+垂直同步

### 卡顿产生原因

因为有垂直同步，如果CPU或GPU没有在一个同步时间单位内完成内容的提交，那一帧就会被丢弃，等待下一次机会再显示
此时显示屏会停留在之前的内容保持不变。这就是界面卡顿的原因。

解决方法就是对CPU和GPU压力进行评估和优化。

---
<br/><br/>

### CPU资源消耗原因和解决方案

* 对象创建

对象的创建会分配内存、调整属性、甚至还有读取文件等操作。比较消耗CPU资源。应尽量用轻量对象代替重量的对象，可以对性能有所优化。

比如`CALayer`比`UIView`要轻量许多，不需要响应触摸事件的控件，用`CALayer`显示会更加合适。

如果对象不涉及UI操作，则尽量放到后台线程去创建。（包含`CALayer`的控件都只能在主线程创建和操作）

通过`Storyboard`创建视图对象时，其资源消耗会比直接通过代码创建对象要大，在性能敏感界面，`Storyboard`并不是一个好的技术选择。

尽量推迟对象创建的时间，并把对象的创建分散到多个任务中去。

如果对象可以复用，并且复用的代价比释放、创建新对象要小，那么这类对象应当尽量放到一个缓存池里复用。

* 对象调整

对象的调整也经常是消耗 CPU 资源的地方。特别的 `CALayer：CALayer` 内部并没有属性，当调用属性方法时，它内部是通过运行时 `resolveInstanceMethod` 为对象临时添加一个方法，并把对应属性值保存到内部的一个 `Dictionary` 里，同时还会通知 `delegate`、创建动画等等，非常消耗资源。

`UIView` 的关于显示相关的属性（比如 frame/bounds/transform）等实际上都是 `CALayer` 属性映射来的，所以对 `UIView` 的这些属性进行调整时，消耗的资源要远大于一般的属性。在应用中，应该尽量减少不必要的属性修改。

当视图层次调整时，`UIView`、`CALayer` 之间会出现很多方法调用与通知，所以在优化性能时，应该尽量避免调整视图层次、添加和移除视图。

* 对象销毁

对象的销毁虽然消耗资源不多，但累积起来也是不容忽视的。

通常当容器类持有大量对象时，其销毁时的资源消耗就非常明显。

同样的，如果对象可以放到后台线程去释放，那就挪到后台线程去。

Tip：把对象捕获到 `block` 中，然后扔到后台队列去随便发送个消息以避免编译器警告，就可以让对象在后台线程销毁了。

    NSArray *tmp = self.array;
    self.array = nil;
    dispatch_async(queue, ^{
        [tmp class];
    });

* 布局计算

视图布局的计算是 App 中最为常见的消耗 CPU 资源的地方。如果能在后台线程提前计算好视图布局、并且对视图布局进行缓存，那么这个地方基本就不会产生性能问题。

不论通过何种技术对视图进行布局，其最终都会落到对 `UIView.frame/bounds/center` 等属性的调整上。对这些属性的调整非常消耗资源，所以尽量提前计算好布局，在需要时一次性调整好对应属性，而不要多次、频繁的计算和调整这些属性。

* AutoLayout

`Autolayout` 是苹果本身提倡的技术，在大部分情况下也能很好的提升开发效率，但是 `Autolayout` 对于复杂视图来说常常会产生严重的性能问题。

随着视图数量的增长，`Autolayout` 带来的 CPU 消耗会呈指数级上升。[具体数据可以看这个文章](http://pilky.me/36/)

如果不想手动调整 `frame` 等属性，可以用一些工具方法替代（比如常见的 `left/right/top/bottom/width/height` 快捷属性），或者使用 `ComponentKit`、`AsyncDisplayKit` 等框架。

* 文本计算

如果一个界面中包含大量文本（比如微博微信朋友圈等），文本的宽高计算会占用很大一部分资源，并且不可避免。如果对文本显示没有特殊要求，可以参考下 `UILabel` 内部的实现方式：用 `[NSAttributedString boundingRectWithSize:options:context:]` 来计算文本宽高，用 `[NSAttributedString drawWithRect:options:context:]` 来绘制文本。尽管这两个方法性能不错，但仍旧需要放到后台线程进行以避免阻塞主线程。

如果用 `CoreText` 绘制文本，那就可以先生成 `CoreText` 排版对象，然后自己计算了，并且 `CoreText` 对象还能保留以供稍后绘制使用。

* 文本渲染

屏幕上能看到的所有文本内容控件，包括 `UIWebView`，在底层都是通过 `CoreText` 排版、绘制为 `Bitmap` 显示的。

常见的文本控件`UILabel`、`UITextView` 等，其排版和绘制都是在主线程进行的，当显示大量文本时，CPU 的压力会非常大。

对此解决方案只有一个，那就是自定义文本控件，用 `TextKit` 或最底层的 `CoreText` 对文本异步绘制。

`CoreText` 对象创建好后，能直接获取文本的宽高等信息，避免了多次计算（调整 `UILabel` 大小时算一遍、`UILabel` 绘制时内部再算一遍）；`CoreText` 对象占用内存较少，可以缓存下来以备稍后多次渲染。

* 图片的解码

用 `UIImage` 或 `CGImageSource` 的那几个方法创建图片时，图片数据并不会立刻解码。图片设置到 `UIImageView` 或者 `CALayer.contents` 中去，并且 `CALayer` 被提交到 GPU 前，`CGImage` 中的数据才会得到解码。这一步是发生在主线程的，并且不可避免。如果想要绕开这个机制，常见的做法是在后台线程先把图片绘制到 `CGBitmapContext` 中，然后从 `Bitmap` 直接创建图片。目前常见的网络图片库都自带这个功能。

* 图像的绘制

图像的绘制通常是指用那些以 CG 开头的方法把图像绘制到画布中，然后从画布创建图片并显示这样一个过程。这个最常见的地方就是 `[UIView drawRect:]` 里面。

由于 `CoreGraphic` 方法通常都是线程安全的，所以图像的绘制可以很容易的放到后台线程进行。一个简单异步绘制的过程大致如下（实际情况会比这个复杂得多，但原理基本一致）：

    (void)display {
        dispatch_async(backgroundQueue, ^{
            CGContextRef ctx = CGBitmapContextCreate(...);
            // draw in context...
            CGImageRef img = CGBitmapContextCreateImage(ctx);
            CFRelease(ctx);
            dispatch_async(mainQueue, ^{
                layer.contents = img;
            });
        });
    }
    
---
<br/><br/>

### GPU 资源消耗原因和解决方案

GPU主要工作：`接收提交的纹理（Texture）和顶点描述（三角形`），`应用变换（transform）`、`混合并渲染`，然后`输出到屏幕上`。
通常所能看到的内容，主要就是纹理（图片）和形状（三角模拟的矢量图形）两类.

* 纹理的渲染

所有的 Bitmap，包括图片、文本、栅格化的内容，最终都要由内存提交到显存，绑定为 GPU Texture。不论是提交到显存的过程，还是 GPU 调整和渲染 Texture 的过程，都要消耗不少 GPU 资源。

当在较短时间显示大量图片时（比如 `TableView` 存在非常多的图片并且快速滑动时），CPU 占用率很低，GPU 占用非常高，界面仍然会掉帧。避免这种情况的方法只能是尽量减少在短时间内大量图片的显示，尽可能将多张图片合成为一张进行显示。

当图片过大，超过 GPU 的最大纹理尺寸时，图片需要先由 CPU 进行预处理，这对 CPU 和 GPU 都会带来额外的资源消耗。目前来说，iPhone 4S 以上机型，纹理尺寸上限都是 4096×4096，更详细的资料可以看：iosres.com。尽量不要让图片和视图的大小超过这个值。

* 视图的混合 (Composing)

当多个视图（或者说 `CALayer`）重叠在一起显示时，GPU 会首先把他们混合到一起。如果视图结构过于复杂，混合的过程也会消耗很多 GPU 资源。

减轻这种情况的 GPU 消耗，应用应当尽量减少视图数量和层次，并在不透明的视图里标明 `opaque` 属性以避免无用的 Alpha 通道合成。也可以用上面的方法，把多个视图预先渲染为一张图片来显示。

* 图形的生成

`CALayer` 的 border、圆角、阴影、遮罩（mask），`CASharpLayer` 的矢量图形显示，通常会触发离屏渲染（offscreen rendering），而离屏渲染通常发生在 GPU 中。

当一个列表视图中出现大量圆角的 `CALayer`，并且快速滑动时，GPU 资源容易占满，而 CPU 资源消耗很少。这时界面仍然能正常滑动，但平均帧数会降到很低。

避免这种情况，可以尝试开启 `CALayer.shouldRasterize` 属性，但这会把原本离屏渲染的操作转嫁到 CPU 上去。对于只需要圆角的某些场合，也可以用一张已经绘制好的圆角图片覆盖到原本视图上面来模拟相同的视觉效果。最彻底的解决办法，就是把需要显示的图形在后台线程绘制为图片，避免使用圆角、阴影、遮罩等属性。

## AsyncDisplayKit

> AsyncDisplayKit 是 Facebook 开源的一个用于保持 iOS 界面流畅的库

### 相关资料

ASDK原理和细节

[ASDK 的基本原理1](https://www.youtube.com/watch?v=-IPMNWqA638)

[ASDK 的基本原理2](https://www.youtube.com/watch?v=ZPL4Nse76oY)

[ASDK 2.0 新特性介绍](https://www.youtube.com/watch?v=RY_X7l1g79Q)

ASDK相关的讨论

[关于 Runloop Dispatch](https://github.com/facebook/AsyncDisplayKit/issues/42)

[关于 ComponentKit 和 ASDK 的区别](https://github.com/facebook/AsyncDisplayKit/issues/70)

[为什么不支持 Storyboard 和 Autolayout](https://github.com/facebook/AsyncDisplayKit/issues/132)

[如何评测界面的流畅度](https://github.com/facebook/AsyncDisplayKit/issues/204)

更多内容：
https://groups.google.com/forum/#!forum/asyncdisplaykit





