## 泛型

- 泛型类型必须是**引用类型**（String , Double)

  

- 定义泛型**类**和泛型**接口**

  - 当使用类**创建对象**时，或者使用**类**或**接口**来**声明引用变量**时，必须指定具体的类型

    ```java
  GenericStack<String> str = new GenericStick<>();
    ```

  - 使用泛型能提高软件的可靠性和可读性，因为**某些错误能在编译时而不是运行时被检测到**。

  - **泛型类**的构造方法不包含泛型类型

    ```java
    public GenericStick()
    ```

  - 泛型类或接口也可以作为父类**被继承**



- 泛型方法

  - 可以为**静态方法**定义泛型类型

  - 声明泛型方法：将泛型类型**<T>**置于方法头关键字static之后

    ```java
    public static <E> void print(E[] list)
    ```

  - 调用泛型方法：将**实际类型**放在尖括号内作为方法名的**前缀**

    ```java
    GenericMethodDemo.<Integer>print(integers);
    ```

  - **受限的泛型类型**

    将泛型类指定为另一种类型的子类型

    ```java
    public static <E extends GemetricObject> boolean equalArea(){}
    ```



- 通配泛型

  - ？非受限通配，等同于? Extends Object

  - ？ Extends  T 受限通配，表示**T**或**T的一个子类型**

  - ?   Super  T  下限通配，表示**T**或**T的一个父类型**

    ```java
    public static double max(GenericStack<? extends Number> stack){}
    ```

    此例使用了受限通配，所以方法参数类型可以选择如GenericStack<Integer> , GenericStack<Double>

    

- 使用泛型的限制
  - 不能使用new E()
  - 不能使用new E[]
  - 在静态上下文中不允许类的参数是泛型类型，包括方法，数据域
  - 异常类不能是泛型的