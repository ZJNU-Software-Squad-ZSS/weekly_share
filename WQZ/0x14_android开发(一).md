# MAD_5



## AlertDialog

**1.默认样式**

```java
        Button button1 = (Button)findViewById(R.id.btn_dialog1);
        button1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                AlertDialog.Builder builder = new AlertDialog.Builder(MainActivity.this);

                builder.setTitle("请回答").setMessage("你觉得我好看吗？").setPositiveButton("当然好看了！", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        Toast.makeText(MainActivity.this,"嘻嘻嘻",Toast.LENGTH_LONG).show();
                    }
                }).setNeutralButton("一般般", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        Toast.makeText(MainActivity.this,"你在瞅瞅",Toast.LENGTH_LONG).show();
                    }
                }).setNegativeButton("我觉得不好看", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        Toast.makeText(MainActivity.this,"嘤嘤嘤",Toast.LENGTH_LONG).show();
                    }
                }).show();
            }
        });
```

**2.单选弹出框**

```java
//单选弹出框
        Button button2 = (Button) findViewById(R.id.btn_dialog2);
        button2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                AlertDialog.Builder builder2 =new AlertDialog.Builder(MainActivity.this);
                final String[]gender = new  String[]{"帅哥","美女"};
                builder2.setTitle("请选择你的性别").setItems(gender, new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        Toast.makeText(MainActivity.this,gender[which],Toast.LENGTH_LONG).show();
                    }
                }).show();
            }
        });
```

**3.SingleChoiceItems单选框**

```java
        //SingleChoiceItems单选框
        Button button3 = (Button) findViewById(R.id.btn_dialog3);
        button3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                final String[] dish = new  String[]{"红烧牛肉","粉蒸排骨","油闷大虾","蒜蓉扇贝"};
                AlertDialog.Builder builder3 = new AlertDialog.Builder(MainActivity.this);

                builder3.setTitle("你最喜欢吃哪道菜？").setSingleChoiceItems(dish, -1, new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        Toast.makeText(MainActivity.this,dish[which],Toast.LENGTH_LONG).show();
                    }
                }).show();
                builder3.setCancelable(false);   //设置为false，按返回键不能退出。默认为true。
            }
        });
```

注：1.builder3.setCancelable(false); 设置为false，按返回键不能退出。默认为true。
        2.setSingleChoiceItems(dish, -1, new DialogInterface.OnClickListener() -1表示当前不选中任何选项，1表示当前默认选中dish[1]
**4.多选弹出框**

```java
       //多选弹出框
        final Button button4 = (Button) findViewById(R.id.btn_dialog4);
        button4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String[] dessert = new  String[]{"抹茶千层","芒果拿破仑","草莓雪梅娘","蓝莓慕斯"};
                boolean begin[] =new boolean[]{false,false,false,false};   //当前默认都未选中
                AlertDialog.Builder builder4 = new AlertDialog.Builder(MainActivity.this);

                builder4.setTitle("你想购买以下哪些甜点？").setMultiChoiceItems(dessert, begin, new DialogInterface.OnMultiChoiceClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which, boolean isChecked) {

                    }
                }).setPositiveButton("确认", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {

                    }
                }).setNegativeButton("取消", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {

                    }
                }).show();
            }
        });
```

注：boolean begin[] =new boolean[]{false,false,false,false};  当前默认都未选中
setMultiChoiceItems(dessert, begin, new DialogInterface.OnMultiChoiceClickListener()
**5.自定义弹出框**

**在使用AlertDialog类生成对话框时，常用的方法如下所示:**
setTitle ：为对话框设置标题
*setIcon ：为对话框设置图标
setMessage：为对话框设置内容
setButton：用于为提示对话框添加按钮，可以是取消按钮、中立按钮和确定按钮。setPositiveButton，setNeutralButton，setNegativeButton。
show ：显示对话框

setItems ：设置对话框要显示的一个list，一般用于显示几个命令时
setSingleChoiceItems ：用来设置对话框显示一系列的单选框
setMultiChoiceItems ：用来设置对话框显示一系列的复选框

自己编写了：AlertDialog_4types

*****

## Toast

<u>对于操作提供一个简单反馈信息。</u>在屏幕下方浮现出一个窗口，显示一段时间后又消失，这个可视化组件叫做 Toast，它主要用于提示用户某种事件发生了。

#### 如何在添加Toast

①定义一个Toast，用makeText（）设置要浮现的文本和浮现时间的长短

第一个参数为当前的上下文环境。可用getApplicationContext()或者getContext()或this
第二个参数为你要浮现的内容
第三个参数设置浮现时间的长短，Toast.LENGTH_SHORT和Toast.LENGTH_LONG

LENGTH_LONG   显示稍微长点的时间，大概在5秒左右
LENGTH_SHORT    显示稍微短点的时候，大概在3秒左右

```java
Toast toast = Toast.makeText(MainActivity.this,'要显示的内容',Toast.LENGTH_SHORT);
```

②将Toast显示出来

```java
toast.show()
```

#### 修改Toast的显示位置

Toast 显示的位置可通过如下有两个方法进行更改：
1、通过setGravity (int gravity, int xOffset, int yOffset)方法，

参数一：gravity，可以使用Gravity类的常量，比如：Gravity.CENTER,Gravity.BOTTOM,Gravity.LEFT,Gravity.RIGHT,Gravity.TOP等

参数二：toast位于屏幕X轴的位移，大于0表示往屏幕右边移动，小于0表示往屏幕左边移动。

参数三：与参数二一样， 不过是在屏幕Y轴的位移，大于0表示往屏幕下方移动，小于0表示往屏幕上方移动。

2、setMargin

```java
setMargin (float horizontalMargin, float verticalMargin) 
```

以横向和纵向的百分比设置显示位置，参数均为 float 类型(水平位移正右负左，竖直位移正上负下)。

#### 修改Toast的外观

1、修改Toast的背景颜色

LinearLayout layout = (LinearLayout) toast.getView();
                layout.setBackgroundColor(Color.parseColor("#F5F5F5"));  //设置toast的背景颜色
2、修改Toast的字体

 TextView v = (TextView) toast.getView().findViewById(android.R.id.message); //toast显示的文本内容
                v.setTextColor(Color.RED);   //设置toast的字体颜色
                v.setTextSize(20);           //设置toast的字体大小

#### 给Toast设置图片

需要用的setView (View view)方法

参数：设置一个view，可以是layout，也可以是imageview等，只要是view或者子类都可以，看需求定义即可



**Toast的3种例子**

1.默认效果

```java
 Toast.makeText(getApplicationContext(), "默认Toast样式",Toast.LENGTH_SHORT).show();
```

2.自定义显示位置效果

```java
1 toast = Toast.makeText(getApplicationContext(), "自定义位置Toast", Toast.LENGTH_LONG);
2 toast.setGravity(Gravity.CENTER, 0, 0);
3 toast.show();
```

3.带图片效果

```java
1 toast = Toast.makeText(getApplicationContext(),"带图片的Toast",Toast.LENGTH_LONG);
2 toast.setGravity(Gravity.CENTER, 0, 0);
3 LinearLayout toastView = (LinearLayout) toast.getView();
4 ImageView imageCodeProject = new ImageView(getApplicationContext());
5 imageCodeProject.setImageResource(R.drawable.icon);
6 toastView.addView(imageCodeProject, 0);
7 toast.show();
```

作业：lab5

******

## Radio Buttons

RadioButton是单个的圆形单选框，而RadioGroup是可以容纳多个RadioButton存在的容器，因此RadioButton和RadioGroup往往都配合使用。

每个已经放入RadioGroup中的RadioButton只能有一个被选中，不放入RadioGroup中的RadioButton可以多选，和checkbox无异。

**RadioGroup基本属性：**

　　（1）     orientation：排列方式

　　　　　　若值为horizontal，则为横向，水平排列：

　　　　　　**android:orientation="horizontal"**

​                       若值为vertical，则为纵向，垂直排列。

　　　　　　**android:orientation="vertical"**

**RadioButton基本属性：**

　　　　（1）、checked：选中状态

　　　　　　若为true则默认被选中，false则默认不被选中。

　　　　（2）、text等相关属性：

　　　　　　text是按钮的文本内容；

　　　　　　textSize是文本字体大小；

　　　　　　textColor是文本字体颜色······

　　　　　　这些属性和TextView一致。

　　　　（3）、button：按钮属性

　　　　　　若button的值设为“@null”则不显示前面的圆形按钮，只显示文本内容本身

　　　　　　**android:button="@null"**

**修改圆圈、波纹、文字效果**

布局文件

```java
<RadioButton
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:background="@drawable/radiobtn_ripplecolor"
        android:buttonTint="@drawable/radiobtn_circlecolor"
        android:text="语文"
        android:textColor="@drawable/radiobtn_textcolor" />
```

1、设置选中时圆圈的颜色为蓝色，radiobtn_circlecolor.xml

```java
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:state_checked="true"
        android:color="@color/blue"/>

    <item android:state_checked="false"
        android:color="@color/gray"/>
</selector>

```

设置`android:buttonTint="@drawable/radiobtn_circlecolor"`属性后，选中时圆圈已经变成了蓝色，但是点击时的波纹还是粉色。

2、设置点击时的波纹颜色为蓝色，`radiobtn_ripplecolor.xml`

```java
<?xml version="1.0" encoding="utf-8"?>
<ripple xmlns:android="http://schemas.android.com/apk/res/android"
    android:color="@color/blue">
</ripple>
```

设置`android:background="@drawable/radiobtn_ripplecolor"`属性后，点击时会出现蓝色波纹。

3、设置选中时文字的颜色为橙色，`radiobtn_textcolor.xml`

```java
<?xml version="1.0" encoding="utf-8"?>
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:state_checked="true"
        android:color="@color/blue"/>

    <item android:state_checked="false"
        android:color="@color/gray"/>
</selector>

```

设置`android:textColor="@drawable/radiobtn_textcolor"`属性后，选中时文字为橙色。

https://developer.android.google.cn/reference/android/widget/RadioButton.html

作业：lab5

************



## Spinner

实现下拉框功能

Spinner是一个列表选择框。相当于弹出一个菜单供用户进行选择。

Spinner继承AdapterView

```
        Spinner spin = (Spinner)findViewById(R.id.spinner);
     
       String[] subjects = {"Computer Engineering","Mathematics","Physics","Law","Electronics Engineering"};
       
        ArrayAdapter aa= new ArrayAdapter(this,android.R.layout.simple_spinner_item,subjects);
        aa.setDropDownViewResource(android.R.layout.simple_spinner_item);

        spin.setAdapter(aa);
```

1.获取界面布局文件里的Spinner组件

2.创建ArrayAdapter对象

3.为Spinner设置Adapter