## Android权限

- [Reference](https://developer.android.google.cn/guide/topics/permissions/overview?hl=en)

- 应用程序必须通过**<uses-permission>**在应用程序清单中包含标签 来公开其所需的权限 

- 系统版本低于6.0(API  23)时，在程序的安装界面**提醒用户**该程序申请的权限，如果用户不批准则**退出安装**

  系统版本高于或等于6.0时，使得用户可以在**使用软件时**再给软件的权限进行批准

- **运行时权限**：系统版本高于**6.0**，用户不需要在**安装**软件时一次性授权**所有**申请的权限，而是可以在软件的使用过程中再对某一权限申请进行授权

- **权限类型**

  - 普通权限：不会直接影响用户隐私和安全，系统自动授权
  - 危险权限：可能触及用户隐私和安全，需要用户手动点击授权
  - 特殊权限:

- **权限组**

  - 每一个权限组包含一个或多个权限
  - 同意了一个权限的申请，同组的权限也被授权

- **运行时权限申请**

  1. 在应用程序清单**声明**权限

     ```java
     <uses-permission android:name="android.permission.CALL_PHONE"/>
     ```

  2. 在具体需要申请权限的地方查询该权限是否已经被授权，如果没有则进行申请

     ```java
     if(ContextCompat.checkSelfPermission(MainActivity.this, Manifest.permission.CALL_PHONE) != PackageManager.PERMISSION_GRANTED){
                         ActivityCompat.requestPermissions(MainActivity.this, new String[]{ Manifest.permission.CALL_PHONE},1);
                     } else {
                         call();
                     }
     ```

     - 通过ContextCompat.checkSelfPermission(context, permissionName)是否等于PackgeManager.PERMISSION_GRANTED来判定该权限是否已被授权
     - 若未被授权则调用ActivityCompatrequestPermissions()方法申请
     - new String[]数组中存放需要申请的权限名，参数1用于回调函数

  3. 同意或者拒绝后，系统作出后续响应

     ```java
     @Override
     public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
             switch (requestCode){
                 case 1:
                     if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED){
                         call();
                     } else {
                         Toast.makeText(this,"You chose deny",Toast.LENGTH_LONG).show();
                     }
                     break;
                 default:
             }
         }
     ```

     - 调用完requestPermissions()方法后，弹出权限申请对话框，用户选择后执行回调函数

     public void onRequestPermissionsResult()

     - 授权结果封装在grantResults参数当中
     - requestCode就是requestPermissions()方法中的第三个参数

     

  4. 完整代码

     ```java
     public class MainActivity extends AppCompatActivity {
     
         @Override
         protected void onCreate(Bundle savedInstanceState) {
             super.onCreate(savedInstanceState);
             setContentView(R.layout.activity_main);
             Button button = new Button(findViewById(R.id.button_1);
             button.setOnClickListener(new View.OnClickListener() {
                 @Override
                 public void onClick(View v) {
                     if(ContextCompat.checkSelfPermission(MainActivity.this, Manifest.permission.CALL_PHONE) != PackageManager.PERMISSION_GRANTED){
                         ActivityCompat.requestPermissions(MainActivity.this, new String[]{ Manifest.permission.CALL_PHONE},1);
                     } else {
                         call();
                     }
                 }
             });
         }
     
         private void call(){
             try {
                 Intent intent = new Intent(Intent.ACTION_CALL);
                 intent.setData(Uri.parse("tel:10086"));
                 startActivity(intent);
             } catch (SecurityException e) {
                 e.printStackTrace();
             }
         }
     
         @Override
         public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
             switch (requestCode){
                 case 1:
                     if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED){
                         call();
                     } else {
                         Toast.makeText(this,"You chose deny",Toast.LENGTH_LONG).show();
                     }
                     break;
                 default:
             }
         }
     }
     
     ```

     