# 0x9_Unity游戏开发基本方法

### Some important methods in C# scripts

- [x] #### **•Start()**

  Start is called on the frame when a script is enabled just before any of the Update methods is called the first time.

  初始化函数，在所有Awake函数运行完之后（一般是这样，但不一定），在所有Update函数前系统自动调用，一般用来给变量赋值。Start将在MonoBehavior创建后在该帧Update之前，在该Monobehavior.enabled == true的情况下执行

- [x] #### **•Update()**

  都是用来更新的，在每一帧被调用

  void FixedUpdate () 	固定更新: 每帧与每帧之间相差的时间是固定的,一些物理属性的更新操									   作,比如Force，Collider，Rigidbody等, 外设的操作也是，比如说键盘或									   者鼠标的输入输出Input应该在FixedUpdate中操作

  void Update ()        	  更新: 每一帧的时间不固定,受当前渲染的物体影响

  void LateUpdate()  	  晚于更新：是在所有Update函数（多个脚本均有Update）调用后被调										用，可用于调整脚本执行顺序

- [x] #### **•OnTriggerEnter()**

  OnTriggerEnter触发条件：

  1 碰撞双方都必须是碰撞体 
  2 碰撞双方其中一个碰撞体必须勾选IsTigger选项 
  3 碰撞双方其中一个必须是刚体 
  4 刚体的IsKinematic选项可以勾选也可以不勾选

  只要满足上面两个条件，不管谁主动都会触发,OnTriggerEnter方法的形参对象指的是碰撞双方中没有携带OnTriggerEnter方法的一方

- [x] #### **•OnCollisionEnter()**

  OnCollisionEnter触发条件：
      1 碰撞双方必须是碰撞体 
  	2 碰撞的主动方必须是刚体，注意我的用词是主动方，而不是被动方 
  	3 刚体不能勾选IsKinematic 
  	4 碰撞体不能够勾选IsTigger
      OnCollisionEnter方法的形参对象指的是碰撞双方中没有携带OnCollisionEnter方法的一方

- [x] #### **•Awake()**

  Awake is called when the script instance is being loaded.

  Awake()是在脚本对象实例化时被调用的

  初始化函数，Awake在MonoBehavior创建后就立刻调用，即在游戏开始时系统自动调用。一般用来创建变量之类的东西。

- [x] #### **•GetMouseButton()**

  GetButton				根据按钮名称返回true当对应的虚拟按钮被按住时

  GetButtonDown	  在给定名称的虚拟按钮被按下的那一帧返回true

  GetButtonUp	  	 在给定名称的虚拟按钮被释放的那一帧返回true

  ```c#
  if(Input.GetButton("Fire1")){//Fire1表示按下鼠标左键         
      print(“按下鼠标左键”); 
  }
  if(Input.GetMouseButton("0")){//0表示按下鼠标左键         
      print(“按下鼠标左键”); 
  }
  if(Input.GetMouseButton("1")){//1表示按下鼠标右键         
      print(“按下鼠标右键”); 
  }
  if(Input.GetButton("2")){//2表示按下鼠标中键         
      print(“按下鼠标中键”); 
  }
  ```

- [x] #### **•GetKey()**

  Input.GetKey()	当通过名称指定的按键被用户按住时，返回值为TRUE
  Input.GetKeyDown()	当用户按下指定名称的按键时的那一帧，返回值为TRUE
  Input.GetKeyUp()	当用户释放指定名称的按键时的那一帧，返回值为TRUE

  ```c#
  if(Input.GetKey(KeyCode.I))
  ```

  - KeyCode.A/B/.../Z
  - KeyCode.UpArrow/DownArrow/RightArrow/LeftArrow
  - KeyCode.Mouse0(left)/Mouse1(right)
  - KeyCode.space

- [x] #### **•GetAxis()**

  ```c#
  Input.GetAxis(string axisName)
  ```

  根据输入设备，参数分为两类： 
  	一、触屏类 
  　　	1、Mouse X 鼠标沿屏幕X移动时触发 
  　　	2、Mouse Y 鼠标沿屏幕Y移动时触发 
  　　	3、Mouse ScrollWheel 鼠标滚轮滚动是触发 
  	二、键盘类 
  　　	1、Vertical 键盘按上或下键时触发 
  　　	2、Horizontal 键盘按左或右键时触发 

  ​		（用方向键或WASD键来模拟-1到1的平滑输入）

  ​	返回值是输入设备在方法参数axisName所指定的轴上的位移量，正负代表方向

- [x] #### •**Translate()**

  ```c#
  Translate(translation : Vector3, relativeTo : Space = Space.Self)
  Translate (x : float, y : float, z : float, relativeTo : Space = Space.Self)
  ```

  ​	平移：移动transform在translation的方向和距离，即向某方向移动物体多少距离。
  ​	如果relativeTo留空或者设置为Space.Self，移动被应用相对于变换的自身轴。（当在场景视	图选择物体时，x、y和z轴显示）如果相对于Space.World 移动被应用相对于世界坐标系统。

- [x] #### **•Rotate()**

  旋转一个欧拉角度，它按照zxy的顺序进行旋转，默认情况下局部坐标系下Space.Self

  ```c#
  transform.Rotate(Vector3 eulers, Space relativeTo = Space.Self)
  transform.Rotate(float xAngle, float yAngle, float zAngle, Space relativeTo = Space.Self)
  ```

  绕axis轴旋转angle角度，默认情况下局部坐标系下Space.Self。

  ```c#
  Rotate(Vector3 axis, float angle, Space relativeTo = Space.Self)
  ```

- [x] #### **•Destroy()**

  ```c#
  Destroy(Object obj, float t = 0.0F)
  ```

  obj: The object to destroy.

  t: The optional amount of time to delay before destroying the object.

- [x] #### **•Instantiate()**

  ```c#
  public static Object Instantiate(Object original);
  public static Object Instantiate(Object original, Transform parent);
  public static Object Instantiate(Object original, Transform parent, bool instantiateInWorldSpace);
  public static Object Instantiate(Object original, Vector3 position, Quaternion rotation);
  public static Object Instantiate(Object original, Vector3 position, Quaternion rotation, Transform parent);
  ```

  Quaternion：四元组(x,y,z,w)表示rotations
  original：An existing object that you want to make a copy of.
  position：Position for the new object.
  rotation：Orientation of the new object.
  parent：Parent that will be assigned to the new object.
  instantiateInWorldSpace：When you assign a parent Object, pass true to position the new object directly in world space. Pass false to set the Object’s position relative to its new parent.