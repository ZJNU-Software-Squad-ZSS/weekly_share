# 简单的介绍安卓开发

**简单介绍下一些坑和控件**



（又是时间不够复习来水太难了）

- 所有的activity都需要在AMainf.xml里面注册

- LinearLayout适合团队协作的布局

- 位置**android**:gravity:?;

```xml
 android:layout_weight="1"权重可以用来设计如何平分空间（把剩余内容来按权值平分） 
android:layout_alignParentBottom="true"在父的底部
android:layout_toRightOf="@+id/view_1"在id为view_1的右边
```

## RadioButton

1）默认选择但是必须先设id

**android**:checked="true"

## ImageView

` <**ImageView**

**android**:layout_width=****"300dp"**

**android**:layout_height=****"200dp"**

**android**:background=****"#FF9900"**

**android**:src=****""**

**android**:scaleType=""**/> `

src理解为内容 scaleType为填充效果可选

## 弹幕（走马灯）

`

<**TextView**

**android**:id="@+id/tv_7"**

**android**:layout_width="200dp"**

**android**:layout_height="wrap_content"**

**android**:text="咕咕-+咕咕-+咕咕-+咕咕-+咕咕-+咕咕-+咕咕-+咕咕-+咕咕-+"**

**android**:textColor="#000000"**

**android**:textSize="24sp"**

**android**:layout_marginTop="10dp"**

**android**:singleLine="true"**

**android**:ellipsize="marquee"**

**android**:marqueeRepeatLimit="marquee_forever"**

**android**:focusable="true"**

**android**:focusableInTouchMode="true"**/>



最后放个唯一有用的5大布局科普的网址

> [https://www.qifeiye.com/%E4%BB%80%E4%B9%88%E6%98%AF%E5%93%8D%E5%BA%94%E5%BC%8F%E7%BD%91%E9%A1%B5%E5%B8%83%E5%B1%80-%E7%BB%99%E4%BD%A0%E4%BA%94%E4%B8%AA%E6%9C%80%E7%BB%8F%E5%85%B8%E7%9A%84%E4%BE%8B%E5%AD%90/](https://www.qifeiye.com/什么是响应式网页布局-给你五个最经典的例子/)





下周一定好好学习(T ^ T)

