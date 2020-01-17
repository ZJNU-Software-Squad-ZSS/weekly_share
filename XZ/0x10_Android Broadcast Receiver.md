## 简介
+ 用于发送接收程序内外的广播信息
+ 标准广播：一种完全**异步**执行的广播，广播发出后，所有的广播接收器几乎都会在**同一时刻**收到这条广播消息
+ 有序广播：一种**同步**执行的广播，在广播发出后，**同一时刻**只会有一个广播接收器才能收到该条广播，且该条广播可被当前接收器截断。优先级高的
接收器先接收广播，可设置是否继续传递该广播。

## 接收广播（广播接收器）
+ 自定义接收器 + 监听的广播值
  - 自定义接收器：定义一个广播接收器，继承自BroadcastReceiver,并重写父类的onReceive()方法。当该接收器接收到广播时就执行onReceive()方法，该方
法中就是具体处理逻辑。
  - 监听的广播值：指明接收器可接收的广播。使用Intent Filter
+ 动态注册接收器
+ 静态注册接收器

## 动态注册接收器
+ 本例用于监听网络变化
+ 自定义接收器类：NetworkChangeReceiver
+ 在代码中使用**IntentFilter**类指明可接收广播值
+ 动态注册的广播接收器最后一定都要取消注册，使用unregisterReceiver()方法
+ 代码
  ```
  public class MainActivity extends AppCompatActivity {

    private IntentFilter intentFilter;
    private NetworkChangeReceiver networkChangeReceiver;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        init();
    }

    @Override//在onDestory()方法中取消广播注册
    protected void onDestroy() {
        super.onDestroy();
        unregisterReceiver(networkChangeReceiver);
    }

    //活动初始化
    private void init(){
        registerNetReceiver();
    }

    //注册广播接收器
    private void registerNetReceiver(){
        intentFilter = new IntentFilter();
        networkChangeReceiver = new NetworkChangeReceiver();
        intentFilter.addAction("android.net.conn.CONNECTIVITY_CHANGE");//用addAction方法设置可接收广播值
        registerReceiver(networkChangeReceiver,intentFilter);//注册广播接收器
    }

    //自定义广播接收器
    class NetworkChangeReceiver extends BroadcastReceiver {
    
        @Override//重写onReceive方法
        public void onReceive(Context context, Intent intent) {
            ConnectivityManager connectivityManager = (ConnectivityManager)getSystemService(Context.CONNECTIVITY_SERVICE);
            NetworkInfo networkInfo = connectivityManager.getActiveNetworkInfo();
            if(networkInfo != null && networkInfo.isConnected()){
                Toast.makeText(context,"network is avaliable",Toast.LENGTH_SHORT).show();
            } else {
                Toast.makeText(context,"network is unavaliable",Toast.LENGTH_SHORT).show();
            }
        }
    }
  }
  ```

## 静态注册接收器
+ 本例实现开机启动
+ 自定义广播接收器类BootCompleteReceiver
+ 在AndroidManifest.xml文件中注册并设置可接收广播值
+ 无需取消注册
+ 代码
  - BootCompleteReceiver.class
  
  ```
  public class BootCompleteReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(Context context, Intent intent) {
        Toast.makeText(context,"Boot Complete!",Toast.LENGTH_LONG).show();
    }
  }
  
  ```
  
  - AndroidManifest.xml
  
  ```
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.brt2">

    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED"/>
    //申请监听系统开机权限
    
    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">
        
        //注册广播接收器
        <receiver
            android:name=".BootCompleteReceiver"
            android:enabled="true"
            android:exported="true">
            <intent-filter>//指定接收器的可接收广播值
                <action android:name="android.intent.action.BOOT_COMPLETED"/>
            </intent-filter>
        </receiver>

        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

  </manifest>
  ```
  
## 发送广播
+ 标准广播
  - 使用**Intent**指明广播内容
  - 使用sendBroadcast()方法发送广播
  - 代码
    ```
    Intent intent = new Intent("com.example.BRT2.MY_BROADCAST");
    sendBroadcast(intent);
    ```
+ 有序广播
  - 在标准广播的基础上，使用sendOrderedBroadcast()方法发送广播
  - 代码
    ```
    Intent intent = new Intent("com.example.BRT2.MY_BROADCAST");
    sendOrderedBroadcast(intent,null);
    ```
