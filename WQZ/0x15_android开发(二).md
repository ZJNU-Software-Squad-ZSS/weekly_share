# MAD

ViewStub过程

```
<Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hide"
        android:id="@+id/hide"
        android:layout_marginRight="65dp"
        android:layout_marginEnd="65dp"
        android:layout_alignParentBottom="true"
        android:layout_alignParentRight="true"
        android:layout_alignParentEnd="true" />
```

android:layout_alignParentBottom="true"需要在<RelativeLayout>中才能使用



## R文件

​    当 Android 应用程序被编译，会自动生成一个 R 类，其中包含了所有 res/ 目录下资源的 ID，如布局文件，资源文件，图片（values下所有文件）的ID等。在写java代码需要用这些资源的时候，你可以使用 R 类，通过子类+资源名或者直接使用资源 ID 来访问资源。
​    R.java文件是活动的Java文件，如MainActivity.java的和资源如strings.xml之间的胶水。我们不要去修改R.java文件的内容。

####     我们将如何通过R文件来实现资源调用呢？使用情况有两种：Java代码中使用和XML代码中使用。

1.java代码中使用：

Java 文字：

> txtName.setText(getResources().getText(R.string.name));

图片：

> imgIcon.setBackgroundDrawableResource(R.drawable.icon);

颜色：

> txtName.setTextColor(getResouces().getColor(R.color.red));

布局：

> setContentView(R.layout.main);

控件：

> txtName = (TextView)findViewById(R.id.txt_name);

2.XML代码中使用：

通过@xxx即可得到，比如这里获取文本和图片:

> <TextViewandroid:text="@string/hello_world"  android:layout_width="wrap_content" android:layout_height="wrap_content"  android:background="@drawable/img_back"/>



## TextView

​    文本控件

**二、各项属性：**

|      **id**       | 设置一个组件id，通过findViewById()的方法获取到该对象，然后进行相关设置 |
| :---------------: | :----------------------------------------------------------: |
| **layout_width**  |                           组件宽度                           |
| **layout_height** |                           组件高度                           |
|     **text**      |                         设置文本内容                         |
|  **background**   |                    背景颜色（或背景图片）                    |
|   **textColor**   |                         设置字体颜色                         |
|   **textStyle**   |                         设置字体样式                         |
|   **textSize**    |                           字体大小                           |
|    **gravity**    |                        内容的对齐方向                        |
|   **autoLink**    | autoLink的属性可以将符合指定格式的文本转换为可单击的超链接形式 |
|  **drawableTop**  |                   TextView上部出现一个图片                   |

详细看博客：https://www.cnblogs.com/guobin-/p/10772463.html



## EditText用法

​    ED（EditText的简称）在开发中也是经常使用到而且比较重要的一个控件，它是用户跟应用进行数据传输的窗口，比如实现一个登陆界面， 需要用户输入账号和密码，然后我们开发者获取到用户输入的内容，提交给后台服务器进行判断再做相应的处理。

**二、EditText的基础属性**    

| hint          | 输入框显示的提示文本       |
| ------------- | -------------------------- |
| textColorHint | 输入框显示的提示文本的颜色 |
| inputType     | 限制用户的输入类型         |
| capitalize    | 英文大写设置               |
| minLines      | 最小行数                   |
| maxLines      | 最大行数                   |
| SingleLine    | 单行不换行                 |

https://www.cnblogs.com/guobin-/p/10778457.html

**三、EditText的其他功能**

 1、监听用户输入的内容. 
       例如，一个搜索框，只要用户输入了内容就去请求服务器，于是就要在Activity里面监听EditeText文本改变事件，具体实现如下所示：

```
editText = (EditText)findViewById(R.id.editText);
editText.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
                Toast.makeText(getApplicationContext(),"before text change",Toast.LENGTH_LONG).show();
            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {

                adapter.getFilter().filter(s);
            }

            @Override
            public void afterTextChanged(Editable s) {

                Toast.makeText(getApplicationContext(),"after text change",Toast.LENGTH_LONG).show();
            }
```

作业：lab7 搜索页面



## ListView

**1.ListView的简单使用**

首先建立一个新的项目，在xml文件中添加ListView控件，如下所示：

![1585364106855](C:\Users\86188\AppData\Roaming\Typora\typora-user-images\1585364106855.png)

接下来修改MainActivity中的代码：

![1585364172024](C:\Users\86188\AppData\Roaming\Typora\typora-user-images\1585364172024.png)

将数据存储在数组中，借助ArrayAdapter适配器传递数据给ListView，最后调用setAdapter()方法，将适配器对象传递出去，关联建立完成。

https://www.cnblogs.com/mqlblog/p/10566048.html



## ViewPager

ViewPager（**android.support.v4.view.ViewPager**）是android扩展包v4包中的类，这个类可以让用户左右切换当前的view，实现滑动切换的效果，在使用这个类之前，必须明白：

- ViewPager类直接继承了ViewGroup类，也就是说它和我们经常打交道的LinearLayout一样，都是一个容器，需要在里面添加我们想要显示的内容。
- ViewPager类需要一个PagerAdapter适配器类给它提供数据，这个和ListView类似。

**二、简单的ViewPaper使用**

使用方法其实与Listview和RecyclerView的方法类似

**1.布局文件使用Viewpager**

  1.<androidx.viewpager.widget.ViewPager

  2.<android.support.v4.view.ViewPager

2.定义一个适配器类使其继承PagerAdapter，复写其中的四个方法，分别是getCount，isViewFromObject，instantiateItem和destroyItem**

**3.findviewbyid方法找到viewpager**

**4.设置适配器**

https://www.cnblogs.com/stars-one/p/8400929.html

作业：lab7 多张图片滑动



## ScrollView

​    ScrollView称为滚动视图，是当在一个屏幕的像素显示不下的时候，可以采用滑动的方式，显示在UI上。

 **1.垂直滚动：Scroll**

改变这个布局文件的根布局：把根布局改成:ScrollView

注意：ScrollView的子元素只能有一个，所以得<u>增加一个LinearLayout布局</u>，<u>把其他按键放在这个LinearLayout中</u>，那么ScrollViewd的子元素就只有一个LinearLayout了，而LinearLayout的子元素不限制。

<LinearLayout

android:orientation="vertical"

**2.水平滚动：HorizontalScrollView**

在LinearLayout里新建一个HorizontalScrollView,同样他的子元素只能有一个

所以在HorizontalScrollView布局中再加一个子布局LinearLayout,且LinearLayout为水平方向： android:orientation="horizontal"

作业：lab7 ScrollView



## ViewStub

​    <u>ViewStub 是一个不可见的，零大小的视图，可用于在运行时延迟扩展布局资源。</u>当 ViewStub 可见时，或者调用 inflate() 时，布局资源会 inflate 。然后， ViewStub 会在其父级中使用 inflated 的视图替换自身。因此，直到调用 setVisibility() 或 inflate() 方法的时候， ViewStub 才会被添加到视图层次结构中。

​    使用`ViewStub`实现按需加载。

**定义ViewStub**

​    `ViewStub`是轻量级视图，不需要大小信息，不会在布局中绘制任何东西，每个 ViewStub 只需要设置`android:layout`属性来指定需要被 inflate 的 Layout 类型。

**加载ViewStub布局**

   要加载`ViewStub`引用的布局只需要调用`inlfate()`方法

​    注：ViewStub 只能inflate一次

ViewStub 本身是不可见，无大小的；使用inflate后，会加载出android:layout指定的视图文件.

**使用按钮将ViewStub视图可视和消失**

```
        show.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                viewStub.setVisibility(View.VISIBLE);
            }
        });
        hide.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                viewStub.setVisibility(View.GONE);
            }
        });
```

viewStub.setVisibility(View.VISIBLE);   可视

viewStub.setVisibility(View.GONE);     消失

作业：lab7



## ImageSwitcher

​    ImageSwitcher是一个图片切换器，它间接继承自FrameLayout类，和ImageView相比，多了一个功能，那就是它说显示的图片切换时，可以设置动画效果，类似于淡进淡出效果，以及左进右出滑动等效果。

**动画效果设定**

使用setInAnimation()和setOutAnimation()方法

        Animation in = AnimationUtils.loadAnimation(this,android.R.anim.slide_in_left);
        Animation out = AnimationUtils.loadAnimation(this,android.R.anim.slide_out_right);
    
        simpleImageSwitcher.setInAnimation(in);
        simpleImageSwitcher.setOutAnimation(out);
​    对于动画效果，一般定义在android.R.anim类中，它是一个final类，以一些int常量的形式，定义的样式，这里仅仅介绍两组样式，淡进淡出效果，以及左进右出滑动效果，如果需要其他效果，可以查阅官方文档。

fede_in：淡进。
fade_out:淡出
slide_in_left:从左滑进。
slide_out_right: 从右滑出。

**ViewFactory**

　　在使用ImageSwitcher的时候，有一点特别需要注意的，需要通过setFactory()方法为它设置一个ViewSwitcher.ViewFactory接口，设置这个ViewFactory接口时需要实现makeView()方法，该方法通常会返回一个ImageView，而ImageSwitcher则负责显示这个ImageView。如果不设定ViewFactory的话，ImageSwitcher将无法使用。通过官方文档了解到，setFactory()方法被声明在ViewSwitcher类中，而ImageSwitcher直接继承自ViewSwitcher类。ViewSwitcher的功能与ImageSwitcher类似，只是ImageSwitcher用于展示图片，而ViewSwitcher用于展示一些View视图。

　　可以这么理解，通过ViewFactory中的makeView()方法返回一个新的View视图，用来放入ViewSwitcher中展示，而对于ImageSwitcher而言，这里通常返回的是一个ImageView。

作业：lab7