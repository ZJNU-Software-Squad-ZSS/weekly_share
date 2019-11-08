## 安卓自带的dialog有三种： 

- AlertDialog—-普通的提示对话框
- ProgressDialog–进度条对话
- DatePickerDialog/TimePickerDialog–日期对话框/时间对话框



## 三个层次的dialog的使用：

- 简单的系统dialog调用//就是简单的系统dialog的调用
- 半自定义的dialog//就是改变一些基础属性
- 完全自定义dialog//自定义dialog类，自己写界面，点击事件



 ## 简单的系统dialog：

- 第一步：new个AlertDialog.Builder

- 第二步：设置dialog的图标，文字，提示信息

- 第三步：设置不同选择的点击事件

- 第四步：显示dialog

   

 代码：

```

 /**
     * 普通dialog
          */
        private void showAlterDialog(){
        final AlertDialog.Builder alterDiaglog = new AlertDialog.Builder(MainActivity.this);
        alterDiaglog.setIcon(R.drawable.icon);//图标
        alterDiaglog.setTitle("简单的dialog");//文字
        alterDiaglog.setMessage("生存还是死亡");//提示消息
        //积极的选择
        alterDiaglog.setPositiveButton("生存", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                Toast.makeText(MainActivity.this,"点击了生存",Toast.LENGTH_SHORT).show();
            }
        });
        //消极的选择
        alterDiaglog.setNegativeButton("死亡", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                Toast.makeText(MainActivity.this,"点击了死亡",Toast.LENGTH_SHORT).show();
            }
        });
       //中立的选择
        alterDiaglog.setNeutralButton("不生不死", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                Toast.makeText(MainActivity.this,"点击了不生不死",Toast.LENGTH_SHORT).show();
            }
        });

         //显示
        alterDiaglog.show();
        }

```

```

 /**
     * 列表Dialog
          */
        private void showListDialog(){
        final String[] items = {"我是1","我是2","我是3"};
        AlertDialog.Builder listDialog = new AlertDialog.Builder(MainActivity.this);
        listDialog.setIcon(R.drawable.icon);//图标
        listDialog.setTitle("我就是个列表Dialog");
        listDialog.setItems(items, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                Toast.makeText(MainActivity.this,"点击了"+items[which],Toast.LENGTH_SHORT).show();
            }
        });
        listDialog.show();
        }
    
    

 ```
 
 ```
 
 /**
     * 单选Dialog
          */
        int choice;
        private void showSingDialog(){
        final String[] items = {"我是1","我是2","我是3"};
        AlertDialog.Builder singleChoiceDialog = new AlertDialog.Builder(MainActivity.this);
        singleChoiceDialog.setIcon(R.drawable.icon);
        singleChoiceDialog.setTitle("我是单选Dialo");
        //第二个参数是默认的选项
        singleChoiceDialog.setSingleChoiceItems(items, 0, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                choice= which;
            }
        });
        singleChoiceDialog.setPositiveButton("确定", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                if (choice!=-1){
                    Toast.makeText(MainActivity.this,
                            "你选择了" + items[choice],
                            Toast.LENGTH_SHORT).show();
                }
            }
        });
        singleChoiceDialog.show();
        }
    
```

```

/**
     * 多选对话框
          */
        ArrayList<Integer> choices= new ArrayList<>();
        private void showMultiChoiceDialog(){
        final String[] items = {"我是1","我是2","我是3"};
        //设置默认选择都是false
        final boolean initchoices[] = {false,false,false};
        choices.clear();
        AlertDialog.Builder multChoiceDialog = new AlertDialog.Builder(MainActivity.this);
        multChoiceDialog.setIcon(R.drawable.icon);
        multChoiceDialog.setTitle("我是个多选Dialog");
        multChoiceDialog.setMultiChoiceItems(items, initchoices, new DialogInterface.OnMultiChoiceClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which, boolean isChecked) {
                if (isChecked){
                    choices.add(which);
                }else {
                    choices.remove(which);
                }
            }
        });
        multChoiceDialog.setPositiveButton("确定", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                int size = choices.size();
                String str = "";
                for(int i = 0;i<size;i++){
                    str+=items[choices.get(i)]+"";
                }
                Toast.makeText(MainActivity.this,
                        "你选中了" + str,
                        Toast.LENGTH_SHORT).show();
            }
        });
        multChoiceDialog.show();
        }
    
```

## 半自定义对话框
代码：

```

 /**
     * 自定义1 控制普通的dialog的位置，大小，透明度
          * 在普通的dialog.show下面添加东西
          */
        private void DiyDialog1(){
        AlertDialog.Builder alterDiaglog = new AlertDialog.Builder(MainActivity.this);
        alterDiaglog.setIcon(R.drawable.icon);//图标
        alterDiaglog.setTitle("简单的dialog");//文字
        alterDiaglog.setMessage("生存还是死亡");//提示消息
        //积极的选择
        alterDiaglog.setPositiveButton("生存", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                Toast.makeText(MainActivity.this,"点击了生存",Toast.LENGTH_SHORT).show();
            }
        });
        //消极的选择
        alterDiaglog.setNegativeButton("死亡", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                Toast.makeText(MainActivity.this,"点击了死亡",Toast.LENGTH_SHORT).show();
            }
        });

        alterDiaglog.setNeutralButton("不生不死", new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int which) {
                Toast.makeText(MainActivity.this,"点击了不生不死",Toast.LENGTH_SHORT).show();
            }
        });
        AlertDialog dialog = alterDiaglog.create();
    
        //显示
        dialog.show();
        //自定义的东西
       //放在show()之后，不然有些属性是没有效果的，比如height和width
        Window dialogWindow = dialog.getWindow();
        WindowManager m = getWindowManager();
        Display d = m.getDefaultDisplay(); // 获取屏幕宽、高用
        WindowManager.LayoutParams p = dialogWindow.getAttributes(); // 获取对话框当前的参数值
        // 设置高度和宽度
        p.height = (int) (d.getHeight() * 0.4); // 高度设置为屏幕的0.6
        p.width = (int) (d.getWidth() * 0.6); // 宽度设置为屏幕的0.65
    
        p.gravity = Gravity.TOP;//设置位置
    
        p.alpha = 0.8f;//设置透明度
        dialogWindow.setAttributes(p);
    }
    
    
```


## 完全自定义dialog

1.在values/styles.xml新建一个样式MyDialog

   代码：
   
   
```
   
   <style name="MyDialog" parent="android:Theme.Dialog">
    <!-- 背景颜色及透明程度 -->
    <item name="android:windowBackground">@android:color/transparent</item>
    <!-- 是否半透明 -->
    <item name="android:windowIsTranslucent">false</item>
    <!-- 是否没有标题 -->
    <item name="android:windowNoTitle">true</item>
    <!-- 是否浮现在activity之上 -->
    <item name="android:windowIsFloating">true</item>
    <!-- 是否背景模糊 -->
    <item name="android:backgroundDimEnabled">false</item>
    <!-- 设置背景模糊的透明度-->
    <item name="android:backgroundDimAmount">0.5</item>
</style>

```


 2.新建一个MyDialog继承Dialog类
    代码：
    
 ```
    
    public class MyDialog1 extends Dialog implements View.OnClickListener{
    //在构造方法里提前加载了样式
    private Context context;//上下文
    private int layoutResID;//布局文件id
    private int[] listenedItem;//监听的控件id
    public MyDialog1(Context context,int layoutResID,int[] listenedItem){
        super(context,R.style.MyDialog);//加载dialog的样式
        this.context = context;
        this.layoutResID = layoutResID;
        this.listenedItem = listenedItem;
    }
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //提前设置Dialog的一些样式
        Window dialogWindow = getWindow();
        dialogWindow.setGravity(Gravity.CENTER);//设置dialog显示居中
        //dialogWindow.setWindowAnimations();设置动画效果
        setContentView(layoutResID);


        WindowManager windowManager = ((Activity)context).getWindowManager();
        Display display = windowManager.getDefaultDisplay();
        WindowManager.LayoutParams lp = getWindow().getAttributes();
        lp.width = display.getWidth()*4/5;// 设置dialog宽度为屏幕的4/5
        getWindow().setAttributes(lp);
        setCanceledOnTouchOutside(true);//点击外部Dialog消失
        //遍历控件id添加点击注册
        for(int id:listenedItem){
            findViewById(id).setOnClickListener(this);
        }
    }
    private OnCenterItemClickListener listener;
    public interface OnCenterItemClickListener {
        void OnCenterItemClick(MyDialog1 dialog, View view);
    }
    //很明显我们要在这里面写个接口，然后添加一个方法
    public void setOnCenterItemClickListener(OnCenterItemClickListener listener) {
        this.listener = listener;
    }


    @Override
    public void onClick(View v) {
        dismiss();//注意：我在这里加了这句话，表示只要按任何一个控件的id,弹窗都会消失，不管是确定还是取消。
        listener.OnCenterItemClick(this,v);
    }
}


```


3.主活动继承自己写的dialog的接口,实现点击方法

   代码：


```

//定义一个自己的dialog
 private MyDialog1 myDialog1;
//实例化自定义的dialog
  myDialog1 = new MyDialog1(this,R.layout.dialog_2,new int[]{R.id.dialog_btn});
  //绑定点击事件
 myDialog1.setOnCenterItemClickListener((MyDialog1.OnCenterItemClickListener) this);
 //显示
  myDialog1.show();
 //调用点击函数
 @Override
    public void OnCenterItemClick(MyDialog1 dialog, View view) {
        switch (view.getId()){
            case R.id.dialog_btn:
                Toast.makeText(getApplicationContext(),"点击了",Toast.LENGTH_SHORT).show();
                break;
            default:
                break;
        }

    }  
    
    
```
