## 有序广播、无序广播

1. 无序广播

   无序广播又叫标准广播，在广播发出之后，所有的广播接收器几乎都会在同一时刻接收到这条广播的信息，因此他们之间没有任何的先后顺序可言。

2. 有序广播

   有序广播接收器是有先后顺序的，而且前面的广播可以对后续的广播进行截断，以阻止让其继续广播。权限高者会先获取得到广播的信息。

   

## 静态广播、动态广播

1. 静态广播

   如果我们设置为静态注册的时候，我们的广播接收器就一个设置为 独立外部类 或者是 静态内部类 并且在AndroidManifest.xml 中进行注册。

2. 动态广播

   通过代码动态注册的广播， 如：

   ```
          IntentFilter filter=new IntentFilter("com.example.jie.Broad");
           receiver=new Demo2Receiver();
      registerReceiver(receiver,filter,"com.cn.customview.permissions.MY_BROADCAST",null);
   
   ```

   

## 本地广播LocalBroadcastManager

1. BroadcastReceiver用于应用之间的传递消息，LocalBroadcastManager用于内部传递消息。

2. LocalBroadcastManager用法

   1. LocalBroadcastManager对象的创建

      ```
      LocalBroadcastManager localBroadcastManager = LocalBroadcastManager.getInstance( this ) ;
      ```

   2. 注册广播接收器

      ```
      LocalBroadcastManager.registerReceiver( broadcastReceiver , intentFilter );
      ```

   3. 发送广播

      ```
      LocalBroadcastManager.sendBroadcast( intent ) ;
      ```

   4. 取消注册广播接收器

      ```
      LocalBroadcastManager.sendBroadcast( intent ) ;
      ```

      

## 系统广播

## 广播内部实现机制

 Android广播机制可以跨进程通讯，多处得到通知的效果。所以需要由AMS（Activity Manager Service）集中管理 