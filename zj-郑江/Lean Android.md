# Lean Android

## 知识点

1. 为控件加上ID

   ```
   android:id="@+id/tv"
   
   @ 符号告诉工具不要将引号里的内容视为字符串文本，而是寻找Android资源里的内容
   + 告诉工具如果id步不存在就创建一个
   id 告诉工具我们是在创建id，而并非引用任何东西，比方说style样式，string字符串，
      image drawable可绘制图像
      
   ```

2. FrameLayout布局控件

   ```
   最简单的布局控件，默认放到左上角。
   当你向他添加多个视图项，他们会重叠，有点像css 里面的浮动
   ```

3. LinearLayout

   ```
   适用于线性布局（水平或垂直）
   具有按比例拆分显示的强大功能
   ```

4. ConstraintLayout

   ```
   
   ```

5. 日志

   ```
   格式：Log.{一些字母}(String TAG,String message);
   TAG可以是任意的字符串，但最好豪是以当前的类名为TAG，这样会比较容易查找
   
   Log.e(String TAG,String MSG) ERROR级别  用户记录明显错误
   
   Log.w(String TAG,String MSG) WARN级别 
   	例如提醒用户媒体应用将会导致磁盘控件不足
   	可以用来诊断用户无法下载视频的问题
   	
   Log.i(String TAG,String MSG) info级别 
   
   Log.d(String TAG,String MSG) 输出自己一些调试信息
   
   Log.v(String TAG,String MSG) 
   
   最高级别错误 WTF=>What a Terrible Failure 哈哈
    						
   ```

6. EditText

   ```
   <EditText
           android:id="@+id/et_search_box"
           android:textSize="22sp"
           android:hint="Entry a query and then click search" 	//初始值
           android:layout_width="match_parent"
           android:layout_height="wrap_content" />
   ```

7. 引用资源

   1. res/values/string.xml

      ```xml
      	<string name="today">Today</string>
      
          <!-- For labelling tomorrow's forecast [CHAR LIMIT=15] -->
          <string name="tomorrow">Tomorrow</string>
      
          <!-- Date format [CHAR LIMIT=NONE] -->
          <string name="format_full_friendly_date">
              <xliff:g id="month">%1$s</xliff:g>, <xliff:g id="day">%2$s</xliff:g>
          </string>
      
      java文件中：
      String today=getString(R.string.today)
      
      xml文件中
      <TextView text=”@string/today”/>
      ```

8. 菜单

   ```xml
   1. 菜单的样式不能在一般的xml文件中写，要创建一个 Android Resource Directory，且value为menu
   
   <item
           android:id="@+id/action_search"  //指定id
           android:orderInCategory="1"	//指定这个菜单项的序号，为1 表示在最左边
           android:title="@string/search"	//指定item的title
           app:showAsAction="ifRoom"	//指定防止方式，ifRoom表示有空间就把item放在menu中
           />
   ```

   ```java
   MainActivity，注意menu的用法
   重写 onCreateOptionsMenu
   	onOptionsItemSelected
   
   package com.example.android.datafrominternet;
   
   import android.content.Context;
   import android.os.Bundle;
   import android.support.v7.app.AppCompatActivity;
   import android.view.Menu;
   import android.view.MenuItem;
   import android.widget.EditText;
   import android.widget.TextView;
   import android.widget.Toast;
   
   public class MainActivity extends AppCompatActivity {
   
       private EditText mSearchBoxEditText;
   
       private TextView mUrlDisplayTextView;
   
       private TextView mSearchResultsTextView;
   
       @Override
       protected void onCreate(Bundle savedInstanceState) {
           super.onCreate(savedInstanceState);
           setContentView(R.layout.activity_main);
   
           mSearchBoxEditText = (EditText) findViewById(R.id.et_search_box);
   
           mUrlDisplayTextView = (TextView) findViewById(R.id.tv_url_display);
           mSearchResultsTextView = (TextView) findViewById(R.id.tv_github_search_results_json);
       }
   
   
   
   
    
   
       @Override
       //在页面创建时，同时创建menu，并指定该menu的样式文件来源
       public boolean onCreateOptionsMenu(Menu menu) {
   //        表示在这个activity的创建时，创建一个menu
   //        getMenuInflater().inflate(R.menu.main,menu)：指定当前Activity中的menu所用到的xml样式是R.menu.main
           getMenuInflater().inflate(R.menu.main,menu);
           return true;
       }
   
   
   
   
       @Override
       //当菜单选项被点击时，触发这个事件
       public boolean onOptionsItemSelected(MenuItem item) {
           //获取所选择的item的id
           int menuItemThatWasSelected=item.getItemId();
           if(menuItemThatWasSelected==R.id.action_search){
               //如果是点击了id为action_search的item控件
   
               //获得上下文对象
               Context context=MainActivity.this;
               //指定Toast所要显示的message
               String message="Search clicked";
               //显示Toast
               Toast.makeText(context,message,Toast.LENGTH_SHORT).show();
           }
           return true;
       }
   }
   
   ```

9. Context 上下文

   ```
   资料：http://liuguoquan727.github.io/2016/06/02/Android%20Context%E8%AF%A6%E8%A7%A3/
   ```

10. 创建Url，使用Uri类来实现

    ```java
     //功能：使用Uri类根据基础的API地址，拼接成完整的URL地址
    //很方便，能够自动转换URL中的编码问题
    public static URL buildUrl(String githubSearchQuery){
        //基于基础URL创建（添加参数）
        Uri builtUri=Uri.parse(GITHUB_BASE_URL).buildUpon()
            .appendQueryParameter(PARAM_QUERY,githubSearchQuery)
            .appendQueryParameter(PARAM_SORT,sortBy)
            .build();
        //将Uri对象转换为URL，便于输出
         URL url=null;
            try{
                url=new URL(builtUri.toString());
            }catch (MalformedURLException e){
                e.printStackTrace();
            }
            return url;
    }
    
    
    MainActivity中的代码实现，从EditText中获取输入内容，输出到Textview中
       public void makeGithubSearchQuery(){
            // TODO (3) Within this method, build the URL with the text from the EditText and set the built URL to the TextView
            String githubQuery=mSearchBoxEditText.getText().toString();
            URL githubSearchUrl= NetworkUtils.buildUrl(githubQuery);
            mUrlDisplayTextView.setText(githubSearchUrl.toString());
        }
        
    public void makeGithubSearchQuery(){
        //获取EditText中的输入内容
        String githubQuery=mSearchBoxEdit.getText().toString();
        //根据输入的查询内容，生成Url对象
        Url githubSearchUrl=NetworkYtils.buildUrl(githubQuery);
        //将Url对象.toString()的字符串设置到TextView中
        mUrlDisplayTextView.setText(githubSearchUrl.toString());
    }
    ```

11. permission，安卓的权限问题

    ```xml
    1. 添加网络授权
       在AndroidManifest.xml文件中添加授权代码，与Application同级
       <uses-permission android:name="android.permission.INTERNET"/>
    
    ```

12. 访问网络

    ```java
    //从指定的URL处访问数据
    public static String getResponseFromHttpUrl(URL url) throws IOException {
        //URL对象的openConnection方法，请求指定URL资源，返回HttpURLConnection对象
            HttpURLConnection urlConnection = (HttpURLConnection) url.openConnection();
            try {
                //HttpURLConnection对象调用GetInputStream方法获取请求返回的内容（字符流）
                InputStream in = urlConnection.getInputStream();
    
                Scanner scanner = new Scanner(in);
                scanner.useDelimiter("\\A");
    
                boolean hasInput = scanner.hasNext();
                if (hasInput) {
                    return scanner.next();
                } else {
                    return null;
                }
            } finally {
                urlConnection.disconnect();
            }
        }
    
    ==========================
    但是在本例中，当在主线程中访问网络爆出一个异常 NetworkOnMainThreadException
    由于安卓应用的主线程是用来保证页面渲染正常的，所以要尽可能的减少在主线程上的工作量；但是当要访问网络时，这回导致几秒钟的事件来等待，使得应用页面无法正常加载，于是就报错；
    解决方案：在辅助线程中进行网络访问功能。
    
    ======================================
    AsyncTask：
    
    public abstract class AsyncTask<Params, Progress, Result> {
    三种泛型类型分别代表“启动任务执行的输入参数”、“后台任务执行的进度”、“后台计算结果的类型”。在特定场合下，并不是所有类型都被使用，如果没有被使用，可以用java.lang.Void类型代替。
    
    AsyncTask语序你在后台线程上运行任务，同时将结果发布到UI线程中，就是渲染页面的线程
    
    UI线程由于各消息队列 Message Queue，允许你发送和处理来自其他线程的
    可运行对象的消息和处理程序
    
    函数：
    doInBackground
    onProgressUpdate
    onPostExecute
    onPrecute
    
    =====================
    在Mainactivity类中，添加一个内置类，继承AsyncTask，这样在实例化该类的时候，就是创建一个线程来做任务了
    
    //内部类 
    public class GithubQueryTask extends AsyncTask<URL,Void,String>{
            @Override
            protected String doInBackground(URL... urls) {
                URL url=urls[0];
                String githubSearchResult=null;
                try {
                    githubSearchResult=NetworkUtils.getResponseFromHttpUrl(url);
                } catch (IOException e) {
                    e.printStackTrace();
                }
                return githubSearchResult;
            }
    
            @Override
            protected void onPostExecute(String s) {
                //这个参数String s，就是doInBackground方法的返回数据
                if(s!=null&&s.equals("")){
                    //前台页面显示
                    mSearchResultsTextView.setText(s);
                }
            }
        }
        
    在其他地方调用：
    点击menu中的item时，调用makeGithubSearchQuery方法
    并在该方法里面new 一个内部类
      private void makeGithubSearchQuery() {
            String githubQuery = mSearchBoxEditText.getText().toString();
            URL githubSearchUrl = NetworkUtils.buildUrl(githubQuery);
            mUrlDisplayTextView.setText(githubSearchUrl.toString());
            String githubSearchResults = null;
            //新建一个内部类
            new GithubQueryTask().execute(githubSearchUrl);
            // TODO (4) Create a new GithubQueryTask and call its execute method, passing in the url to query
        }
    
    ```

13. JSON数据处理

    ```json
    {
        "student":{
            "name":"Ocaen",
            "age":"20"
        },
        "teacher":{
            "name":"吕大师",
            "age":"30"
        }
    }
    
    json处理流程
    1. Initialize JSONObject from JSON string 
    	JSONObject contact = new JSONObject(contactJSONString);
    2. 获得json对象中的Student对象
    	JSONObject Student=contact.getJSONObject("student");
    3. 从Student对象中获取底层字符串数据
    	String name=Student.getString("name");
    	String age=Student.getString("age");
    ```

    

## 一些接口

1. api接口

   ```
   github接口，q参数表示要取github上所搜索的关键词
   https://api.github.com/search/repositories?q=android&sort=stars
   ```




## 组件

1. ProgressBar 相当于一个Loading，一直转圈圈，通过设置是否可视来进行程序阶段的过渡

## 功能流程

1. 从github接口获取查询数据

   ```java
   1. 在res下创建一个menu包，里面创建一个main.xml的文件，用来在主页面显示menu
   
   2. 在MainActivity文件中重写onCreateOptionsMenu方法，在其中绑定要在主页面上显示的菜单视图对象，就是上面创建的
   	  public boolean onCreateOptionsMenu(Menu menu) {
   	  //Inflate，主要是用来获取视图资源，这里就是把R.menu.main资源赋值给menu，页面上就能显示menu了
           getMenuInflater().inflate(R.menu.main, menu);
           return true;
         }
         
   3. 同时在MainActivity中绑定menu中的item被点击的触发事件，重写onOptionsItemSelected方法
   	@Override
       public boolean onOptionsItemSelected(MenuItem item) {
       	//获得选中的item的id
           int itemThatWasClickedId = item.getItemId();
           //如果这个id==我所绑定的视图组件的id
           if (itemThatWasClickedId == R.id.action_search) {
           	//指定查询操作，访问接口
               makeGithubSearchQuery();
               return true;
           }
           return super.onOptionsItemSelected(item);
       }
   
   ==========================================
   查询数据功能实现
   	1. 获取用户输入的查询关键词 
   		String githubQuery = mSearchBoxEditText.getText().toString();
   	2. 通过关键词组装URL，注意这里的的URL是对象，不是简单的字符串了
   		 public static URL buildUrl(String githubSearchQuery) {
                   Uri builtUri = Uri.parse(GITHUB_BASE_URL).buildUpon()
                           //添加查询字段
                           .appendQueryParameter(PARAM_QUERY, githubSearchQuery)
                           .appendQueryParameter(PARAM_SORT, sortBy)
                           .build();
   
                   URL url = null;
                   try {
                       url = new URL(builtUri.toString());
                   } catch (MalformedURLException e) {
                       e.printStackTrace();
                   }
   
                   return url;
               }
              
   	3. 使用AsyncTask，创建线程来进行数据查询
   	   实现方法，MainActivity的内部类，需要创建线程并执行查询的时候，直接new 一个该内部类对象，就自动进行查询了，传入的参数为要进行访问的url
       	 public class GithubQueryTask extends AsyncTask<URL, Void, String> {
   
           // COMPLETED (26) Override onPreExecute to set the loading indicator to visible
           @Override
           protected void onPreExecute() {
               super.onPreExecute();
               //当刚进行查询请求的时候，先把ProgressBar变成可视状态
               //转圈圈状态
               mLoadingIndicator.setVisibility(View.VISIBLE);
           }
   
           @Override
           protected String doInBackground(URL... params) {
               //获取穿过来的url
               URL searchUrl = params[0];
               String githubSearchResults = null;
               try {
                   githubSearchResults = NetworkUtils.getResponseFromHttpUrl(searchUrl);
               } catch (IOException e) {
                   e.printStackTrace();
               }
               return githubSearchResults;
           }
   
           @Override
           //请求完成时
           protected void onPostExecute(String githubSearchResults) {
               // COMPLETED (27) As soon as the loading is complete, hide the loading indicator
               mLoadingIndicator.setVisibility(View.INVISIBLE);
               if (githubSearchResults != null && !githubSearchResults.equals("")) {
                   // COMPLETED (17) Call showJsonDataView if we have valid, non-null results
   
                   //当获取到数据，将ProgressBar关闭，开启result显示的TextView
                   showJsonDataView();
                   //往ResultTextView里注入数据
                   mSearchResultsTextView.setText(githubSearchResults);
               } else {
                   // COMPLETED (16) Call showErrorMessage if the result is null in onPostExecute
                   //当没获取到数据，则显示错误信息
                   showErrorMessage();
               }
           }
       }
   	
   	
   ```

   