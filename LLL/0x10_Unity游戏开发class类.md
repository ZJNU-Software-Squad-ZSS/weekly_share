# 0x10_Unity游戏开发class类

### Fundamental class in C# scripts

- [x] #### **•GameObject class**

  Gameobject是一个类型，所有的游戏物件都是这个类型的对象。

  gameobject是一个对象， 就跟java里面的this一样， 指的是这个脚本所附着的游戏物件

  ***GameObject.transform:*** The Transform attached to this GameObject.

  ***GameObject.tag:*** The tag of this game object.

  ***GameObject.GetComponent<>():*** Returns the component of Type type if the game object has one attached, null if it doesn't.

  ***GameObject.Find(string name):*** Finds a GameObject by name and returns it.

  ***GameObject.FindGameObjectsWithTag(string tag)***：Returns an array of active GameObjects tagged tag. Returns empty array if no GameObject was found.

  ***GameObject.findWithTag(string tag):*** Returns one active GameObject tagged tag. Returns null if no GameObject was found.

- [x] #### **•Transform class**

  Transform是一个类，用来描述物体的位置，大小，旋转等等信息

  transform是Transform类的对象，依附于每一个物体。也是当前游戏对象的一个组件(每个对象都会有这个组件)

  ***Transform.forward:*** Returns a normalized vector representing the blue axis of the transform in world space

  ***Transform.right:*** The red axis of the transform in world space

  ***Transform.up:*** The green axis of the transform in world space

  ***Transform.position:***The world space position of the Transform.

  ***Transform.rotation:***A Quaternion that stores the rotation of the Transform in world space.

  ***Transform.TransformDirection(Vector3 direction): Vector3*** 变换方向从局部坐标转换到世界坐标。这个操作不会受到变换的缩放和位置的影响。返回的向量与direction有同样的长度。

  > 如自身Z轴方向跟世界Z轴方向一致，目前我的位置是（0，0，0），我向前（相对自身）移动一个单位，我的位置变成（0，0，1），
  >
  > 即为：transform.postion += vector3(0,0,1);
  >
  > 当自身Z轴方向跟世界X轴方向一致时，我的位置还是（0，0，0），我向前（相对自身）移动一个单位，我的位置变成（1，0，0），
  >
  > 即为：transform.postion += transform.TransformDirection(vector3(0,0,1))的结果。

  ***Transform.TransformPoint(Vector3 position):Vector3*** 变换位置从局部坐标转换到世界坐标。这个操作不会受到变换的缩放的影响。相反的转换采用***Transform.InverseTransformPoint***.

  ***Transform.Rotate(Vector3 eulers, Space relativeTo= Space.Self):*** Use Transform.Rotate to rotate GameObjects in a variety of ways. The rotation is often provided as an Euler angle and not a Quaternion.

  ***Transform.Translate(Vector3 translation, Space relativeTo = Space.Self):***Moves the transform in the direction and distance of translation.

  ***Transform.LookAt(Transform target):***Rotates the transform so the forward vector points at /target/'s current position

- [x] #### **•Rigidbody class**

  ***Rigidbody.AddForce:*** Adds a force to the Rigidbody
  参数一：force vector;参数二：type of force,其中ForceMode有四种形式：***ForceMode.Acceleration:***给物体添加一个持续的加速度，但是忽略其质量
  ***ForceMode.Force:***给物体添加一个持续的力并使用其质量
  ***ForceMode.Impulse:***给物体添加一个瞬间的力并使用其质量
  ***ForceMode.VelocityChange***:给物体添加一个瞬间的加速度，但是忽略其质量
  刚体运动速度的计算公式是：f•t=m•v

  ```c#
  // this.GetComponent<Rigidbody>().AddForce(Vector3.up * force);
  this.GetComponent<Rigidbody>().AddForce(Vector3.up * force, ForceMode.Force);
  ```

  ***Rigidbody.MovePosition:*** Moves the kinematic Rigidbody towards position

  ```c#
  this.GetComponent<Rigidbody>().MovePosition(this.transform.position + Vector3.right * speed * Time.deltaTime);
  ```

  ***Rigidbody.MoveRotation:*** Rotates the rigidbody to rotation

  ```c#
  Quaternion deltaRotation = Quaternion.Euler(eulerAngleVelocity * Time.deltaTime);
  this.GetComponent<Rigidbody>().MoveRotation(this.transform.rotation * deltaRotation);
  ```

  ***Rigidbody.isKinematic***: Controls whether physics affects the rigidbody.

  If isKinematic is enabled, Forces, collisions or joints will not affect the rigidbody anymore. 

  ```c#
  this.GetComponent<Rigidbody>().isKinematic = true;   //make it not to follow physical laws and delete the cube’s all changes. 
  this.GetComponent<Rigidbody>().isKinematic = false;     //make it follow physical laws so that the rigibody function can affect the object 
  ```

  ***Rigidbody.velocity***: 获得刚体的速度

  ```c#
  this.GetComponent<Rigidbody>().velocity = new Vector3(-10.0f, 9.0f, 0.0f);
  ```

- [ ] #### **•Input class**

- [ ] #### **•Vector3 structure**

- [ ] #### **•Physics class**

- [x] #### **•Time class**

  (加粗为只读，不加粗为可读可写)

  ***Time.time*** 表示从游戏开发到现在的时间，会随着游戏的暂停而停止计算。

  ***Time.timeSinceLevelLoad*** 表示从当前Scene开始到目前为止的时间，也会随着暂停操作而停止。

  ***Time.deltaTime*** 表示从上一帧到当前帧时间，以秒为单位。

  ***Time.fixedTime*** 表示以秒计游戏开始的时间，固定时间以定期间隔更新（相当于fixedDeltaTime）直到达到time属性。

  *Time.fixedDeltaTime* 表示以秒计间隔，在物理和其他固定帧率进行更新，在Edit->ProjectSettings->Time的Fixed Timestep可以自行设置。

  ***Time.SmoothDeltaTime*** 表示一个平稳的deltaTime，根据前 
  N帧的时间加权平均的值。

  *Time.timeScale* 时间缩放，默认值为1，若设置<1，表示时间减慢，若设置>1,表示时间加快，可以用来加速和减速游戏，非常有用。

  ***Time.frameCount*** 总帧数

  ***Time.realtimeSinceStartup*** 表示自游戏开始后的总时间，即使暂停也会不断的增加。

  *Time.captureFramerate* 表示设置每秒的帧率，然后不考虑真实时间。

  ***Time.unscaledDeltaTime*** 不考虑timescale时候与deltaTime相同，若timescale被设置，则无效。

  ***Time.unscaledTime*** 不考虑timescale时候与time相同，若timescale被设置，则无效。