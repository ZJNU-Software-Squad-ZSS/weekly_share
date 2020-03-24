# StudyJava——常用类

1. #### Arrays类：包含用于操作数组的各种方法（例如排序和搜索）。还包含一个静态工厂，允许将数组转为 List。

   | 方法                                     | 描述                             |
   | ---------------------------------------- | -------------------------------- |
   | `<T>` List`<T>` asList(T... a)           | 返回由指定数组构造的List         |
   | void sort(Object[] a)                    | 对数组进行排序                   |
   | void fill(Object[] a, Object val)        | 为数组的所有元素都赋上相同的值   |
   | boolean equals(Object[] a, Object[] a2)  | 检查两个数组是否相等             |
   | int binarySearch(Object[] a, Object key) | 对排序后的数组使用二分法查找数据 |

   ```java
   import java.util.Arrays;
   import java.util.Random;
   
   public class ArraysDemo {
       public static void main(String[] args) {
           int[] arr = new int[10];
           //将数组元素都设为9
           Arrays.fill(arr, 9);
           System.out.println("fill:" + Arrays.toString(arr));
           Random random = new Random();
           for (int i = 0; i < arr.length; i++) {
               //使用100以内的随机数赋值数组
               arr[i] = random.nextInt(101);
           }
           //重新赋值后的数组
           System.out.println("重新赋值：" + Arrays.toString(arr));
           //将索引为5的元素设为50
           arr[5] = 50;
           //排序
           Arrays.sort(arr);
           //排序后的数组
           System.out.println("sort排序后：" + Arrays.toString(arr));
           //查找50的位置
           int i = Arrays.binarySearch(arr, 50);
           System.out.println("值为50的元素索引："+i);
           //复制一份新数组
           int[] newArr = Arrays.copyOf(arr, arr.length);
           //比较
           System.out.println("equals:"+Arrays.equals(arr, newArr));
       }
   }
   ```

2. #### StringBuilder类：可变的。它是 String 的对等类，它可以增加和编写字符的可变序列，并且能够将字符插入到字符串中间或附加到字符串末尾（当然是不用创建其他对象的）

   | 构造方法                        | 说明                                                         |
   | ------------------------------- | ------------------------------------------------------------ |
   | StringBuilder()                 | 构造一个其中不带字符的 StringBuilder，其初始容量为 16 个字符 |
   | StringBuilder(CharSequence seq) | 构造一个 StringBuilder，它包含与指定的 CharSequence 相同的字符 |
   | StringBuilder(int capacity)     | 构造一个具有指定初始容量的 StringBuilder                     |
   | StringBuilder(String str)       | 并将其内容初始化为指定的字符串内容                           |

   | 方法                                    | 返回值        | 功能描述                                                     |
   | --------------------------------------- | ------------- | ------------------------------------------------------------ |
   | insert(int offsetm,Object obj)          | StringBuilder | 在 offsetm 的位置插入字符串 obj                              |
   | append(Object obj)                      | StringBuilder | 在字符串末尾追加字符串 obj                                   |
   | length()                                | int           | 确定 StringBuilder 对象的长度                                |
   | setCharAt(int index,char ch)            | void          | 使用 ch 指定的新值设置 index 指定的位置上的字符              |
   | toString()                              | String        | 转换为字符串形式                                             |
   | reverse()                               | StringBuilder | 反转字符串                                                   |
   | delete(int start, int end)              | StringBuilder | 删除调用对象中从 start 位置开始直到 end 指定的索引（end-1）位置的字符序列 |
   | replace(int start, int end, String str) | StringBuilder | 使用一组字符替换另一组字符。将用替换字符串从 start 指定的位置开始替换，直到 end 指定的位置结束 |

   ```java
   public class StringBuilderTest {
   
       public static void main(String[] args){
           //定义和初始化一个StringBuilder类的字串s
           StringBuilder s = new StringBuilder("I");
           //在s后面添加字串" java"
           s.append(" java");
           //在s[1]的位置插入字串
           s.insert(1, " love");
           String t = s.toString(); //转为字符串
           System.out.println(t);
       }
   }
   ```

3. #### Calendar类；子类GregorianCalendar类：实现了世界上普遍使用的公历系统

   ```java
   import java.text.DateFormat;
   import java.text.SimpleDateFormat;
   import java.util.Calendar;
   import java.util.Date;
   
   public class CalendarDemo {
       public static void main(String[] args) {
           System.out.println("完整显示日期时间：");
           // 字符串转换日期格式
           DateFormat fdate = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
           String str = fdate.format(new Date());
           System.out.println(str);
   
           // 创建 Calendar 对象
           Calendar calendar = Calendar.getInstance();
           // 初始化 Calendar 对象，但并不必要，除非需要重置时间
           calendar.setTime(new Date());
   
           // 显示年份
           System.out.println("年： " + calendar.get(Calendar.YEAR));
   
           // 显示月份 (从0开始, 实际显示要加一)
           System.out.println("月： " + calendar.get(Calendar.MONTH));
   
   
           // 当前分钟数
           System.out.println("分钟： " + calendar.get(Calendar.MINUTE));
   
           // 今年的第 N 天
           System.out.println("今年的第 " + calendar.get(Calendar.DAY_OF_YEAR) + "天");
   
           // 本月第 N 天
           System.out.println("本月的第 " + calendar.get(Calendar.DAY_OF_MONTH) + "天");
   
           // 3小时以后
           calendar.add(Calendar.HOUR_OF_DAY, 3);
           System.out.println("三小时以后的时间： " + calendar.getTime());
           // 格式化显示
           str = (new SimpleDateFormat("yyyy-MM-dd HH:mm:ss:SS")).format(calendar.getTime());
           System.out.println(str);
   
           // 重置 Calendar 显示当前时间
           calendar.setTime(new Date());
           str = (new SimpleDateFormat("yyyy-MM-dd HH:mm:ss:SS")).format(calendar.getTime());
           System.out.println(str);
   
           // 创建一个 Calendar 用于比较时间
           Calendar calendarNew = Calendar.getInstance();
   
           // 设定为 5 小时以前，后者大，显示 -1
           calendarNew.add(Calendar.HOUR, -5);
           System.out.println("时间比较：" + calendarNew.compareTo(calendar));
   
           // 设定7小时以后，前者大，显示 1
           calendarNew.add(Calendar.HOUR, +7);
           System.out.println("时间比较：" + calendarNew.compareTo(calendar));
   
           // 退回 2 小时，时间相同，显示0
           //有时是 0 ，有时是 1，在这里会涉及到 calendarNew 与 calendar 的创建时间点,最终比较的是谁先创建好，时间点靠后的大一些
           calendarNew.add(Calendar.HOUR, -2);
           System.out.println("时间比较：" + calendarNew.compareTo(calendar));
   
           // calendarNew创建时间点
           System.out.println((new SimpleDateFormat("yyyy-MM-dd HH:mm:ss:SS")).format(calendarNew.getTime()));
           // calendar创建时间点
           System.out.println((new SimpleDateFormat("yyyy-MM-dd HH:mm:ss:SS")).format(calendar.getTime()));
           System.out.println("时间比较：" + calendarNew.compareTo(calendar));
       }
   }
   ```

   ```
   $ javac CalendarDemo.java
   $ java CalendarDemo
   完整显示日期时间：
   2018-12-12 15:50:49
   年： 2018
   月： 11
   分钟： 50
   今年的第 346天
   本月的第 12天
   三小时以后的时间： Wed Dec 12 18:50:49 CST 2018
   2018-12-12 18:50:49:449
   2018-12-12 15:50:49:455
   时间比较：-1
   时间比较：1
   时间比较：1
   2018-12-12 15:50:49:456
   2018-12-12 15:50:49:455
   时间比较：1
   ```

   > month 的含义与 Date 类相同，0 代表 1 月，11 代表 12 月。

4. #### Date类

   | 构造方法        | 说明                                                         |
   | --------------- | ------------------------------------------------------------ |
   | Date()          | 构造一个 Date 对象并对其进行初始化以反映当前时间             |
   | Date(long date) | 构造一个 Date 对象，并根据相对于 GMT 1970 年 1 月 1 日 00:00:00 的毫秒数对其进行初始化 |

   ```java
   import java.text.SimpleDateFormat;
   import java.util.Date;
   
   public class DateDemo {
       public static void main(String[] args) {
           String strDate, strTime;
           Date objDate = new Date();
           System.out.println("今天的日期是：" + objDate);
           long time = objDate.getTime();
           System.out.println("自1970年1月1日起以毫秒为单位的时间（GMT）：" + time);
           strDate = objDate.toString();
           //提取 GMT 时间
           strTime = strDate.substring(11, (strDate.length() - 4));
           //按小时、分钟和秒提取时间
           strTime = "时间：" + strTime.substring(0, 8);
           System.out.println(strTime);
           //格式化时间
           SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
           System.out.println(formatter.format(objDate));
       }
   }
   ```

   ```
   $ javac DateDemo.java
   $ java DateDemo
   今天的日期是：Wed Dec 12 14:43:15 CST 2018
   自1970年1月1日起以毫秒为单位的时间（GMT）：1544596995669
   时间：14:43:15
   2018-12-12 14:43:15
   ```

5. #### Math类

   | 方法                    | 返回值                                         | 功能描述                                                     |
   | ----------------------- | ---------------------------------------------- | ------------------------------------------------------------ |
   | sin(double numvalue)    | double                                         | 计算角 numvalue 的正弦值                                     |
   | cos(double numvalue)    | double                                         | 计算角 numvalue 的余弦值                                     |
   | acos(double numvalue)   | double                                         | 计算 numvalue 的反余弦                                       |
   | asin(double numvalue)   | double                                         | 计算 numvalue 的反正弦                                       |
   | atan(double numvalue)   | double                                         | 计算 numvalue 的反正切                                       |
   | pow(double a, double b) | double                                         | 计算 a 的 b 次方                                             |
   | sqrt(double numvalue)   | double                                         | 计算给定值的正平方根                                         |
   | abs(int numvalue)       | int                                            | 计算 int 类型值 numvalue 的绝对值，也接收 long、float 和 double 类型的参数 |
   | ceil(double numvalue)   | double                                         | 返回大于等于 numvalue 的最小整数值                           |
   | floor(double numvalue)  | double                                         | 返回小于等于 numvalue 的最大整数值                           |
   | max(int a, int b)       | int                                            | 返回 int 型 a 和 b 中的较大值，也接收 long、float 和 double 类型的参数 |
   | min(int a, int b)       | int                                            | 返回 a 和 b 中的较小值，也可接受 long、float 和 double 类型的参数 |
   | rint(double numvalue)   | double                                         | 返回最接近 numvalue 的整数值                                 |
   | round(T arg)            | arg 为 double 时返回 long，为 float 时返回 int | 返回最接近arg的整数值                                        |
   | random()                | double                                         | 返回带正号的 double 值，该值大于等于 0.0 且小于 1.0          |

6. #### System类

   - 标准输入，标准输出和错误输出流;
   - 访问外部定义的属性和环境变量;
   - 加载文件和库的方法;
   - 以及用于快速复制数组的实用方法。

   > System 不可以被实例化，只可以使用其静态方法

   ```java
   import java.util.Arrays;
   public class SystemDemo {
       public static void main(String[] args) {
           int[] a = {7, 8, 9, 10, 11};
           int[] b = {1, 2, 3, 4, 5, 6};
           //从数组a的第二个元素开始，复制到b数组的第三个位置 复制的元素长度为3
           System.arraycopy(a, 1, b, 2, 3);
           //输出结果
           System.out.println(Arrays.toString(b));
           System.out.println("当前时间：" + System.currentTimeMillis());
           System.out.println("java版本信息：" + System.getProperty("java.version"));
           //运行垃圾收集器
           System.gc();
           //退出
           System.exit(0);
       }
   }
   ```

7. #### Random类：生成伪随机数流，在java.util包下

   ```java
   import java.util.Random;
   
   public class RandomDemo {
       public static void main(String[] args) {
           Random random = new Random();
           //随机生成一个整数 int范围
           System.out.println(random.nextInt());
           //生成 [0,n] 范围的整数  设n=100
           System.out.println(random.nextInt(100 + 1));
           //生成 [0,n) 范围的整数  设n=100
           System.out.println(random.nextInt(100));
           //生成 [m,n] 范围的整数  设n=100 m=40
           System.out.println((random.nextInt(100 - 40 + 1) + 40));
           //随机生成一个整数 long范围
           System.out.print(random.nextLong());
           //生成[0,1.0)范围的float型小数
           System.out.println(random.nextFloat());
           //生成[0,1.0)范围的double型小数
           System.out.println(random.nextDouble());
       }
   }
   ```

   

