# StudyJava——Stream

### Stream流

- 元素序列：Stream 以序列的形式提供了特定类型的元素的集合。根据需求，它可以获得和计算元素，但不会储存任何元素。
- 源：Stream 可以将集合、数组和 I/O 资源作为输入源。
- 聚集操作：Stream 支持诸如`filter`、`map`、`limit`、`reduce`等的聚集操作。
- 流水技术：许多 Stream 操作返回了流本身，故它们的返回值可以以流水的行式存在。这些操作称之为中间操作，并且它们的功能就是负责输入、处理和向目标输出。`collect()`方法是一个终结操作，通常存在于流水线操作的末端，来标记流的结束。
- 自动迭代：Stream 的操作可以基于已提供的源元素进行内部的迭代，而集合则需要显式的迭代。

集合的接口有两个方法来产生流：

- `stream()`：该方法返回一个将集合视为源的连续流。
- `parallelStream()`：该方法返回一个将集合视为源的并行流。

> 大家可以把Stream当成一个高级版本的Iterator。原始版本的Iterator，用户只能一个一个的遍历元素并对其执行某些操作；高级版本的Stream，用户只要给出需要对其包含的元素执行什么操作，比如“过滤掉长度大于10的字符串”、“获取每个字符串的首字母”等，具体这些操作如何应用到每个元素上，就给Stream就好了！

1. #### 通用语法

   ![img](http://img04.taobaocdn.com/imgextra/i4/90219132/T2ycFgXQ8XXXXXXXXX_!!90219132.jpg)

   使用Stream的基本步骤：

   1. 创建Stream；
   2. 转换Stream，每次转换原有Stream对象不改变，返回一个新的Stream对象（**可以有多次转换**）；
   3. 对Stream进行聚合（Reduce）操作，获取想要的结果；

2. #### 创建Stream

   1. 通过Stream接口的静态工厂方法（注意：Java8里接口可以带静态方法）；

      - of方法：有两个overload方法，一个接受变长参数，一个接口单一值

        ```java
        Stream<Integer> integerStream = Stream.of(1, 2, 3, 5);
        Stream<String> stringStream = Stream.of("taobao");
        ```

      - generator方法：生成一个无限长度的Stream，其元素的生成是通过给定的Supplier（这个接口可以看成一个对象的工厂，每次调用返回一个给定类型的对象）

        ```java
        Stream.generate(new Supplier<Double>() {
            @Override
            public Double get() {
                return Math.random();
            }
        });
        Stream.generate(() -> Math.random());
        Stream.generate(Math::random);
        ```

        `每条语句其实都是生成一个无限长度的Stream，其中值是随机的。这个无限长度Stream是懒加载，一般这种无限长度的Stream都会配合Stream的limit()方法来用。`

      - iterate方法：也是生成无限长度的Stream，和generator不同的是，其元素的生成是重复对给定的种子值(seed)调用用户指定函数来生成的。其中包含的元素可以认为是：seed，f(seed),f(f(seed))无限循环

        ```java
        Stream.iterate(1, item -> item + 1).limit(10).forEach(System.out::println);
        ```

        `获取一个无限长度的正整数集合的Stream，然后取出前10个打印`

   2. 通过Collection接口的默认方法（默认方法：Default method，也是Java8中的一个新特性，就是接口中的一个带有实现的方法）–stream()，把一个Collection对象转换成Stream

3. #### 转换Stream

   1. forEach：该方法用于对 Stream 中的每个元素进行迭代操作。

      ```java
      // 使用 forEach 方法输出 10 个随机数
      Random random = new Random();
      random.ints().limit(10).forEach(System.out::println);
      ```

   2. distinct: 对于Stream中包含的元素进行去重操作（去重逻辑依赖元素的equals方法），新生成的Stream中没有重复的元素；

      ![img](http://img04.taobaocdn.com/imgextra/i4/90219132/T2K0lnXPRXXXXXXXXX_!!90219132.jpg)

   3. filter: 对于Stream中包含的元素使用给定的过滤函数进行过滤操作，新生成的Stream只包含符合条件的元素；

      ![img](http://img03.taobaocdn.com/imgextra/i3/90219132/T2OxXnXPlXXXXXXXXX_!!90219132.jpg)

   4. map: 对于Stream中包含的元素使用给定的转换函数进行转换操作，新生成的Stream只包含转换生成的元素。这个方法有三个对于原始类型的变种方法，分别是：mapToInt，mapToLong和mapToDouble。这三个方法也比较好理解，比如mapToInt就是把原始Stream转换成一个新的Stream，这个新生成的Stream中的元素都是int类型。之所以会有这样三个变种方法，可以免除自动装箱/拆箱的额外消耗；

      ![img](http://img03.taobaocdn.com/imgextra/i3/90219132/T2PQJnXOJXXXXXXXXX_!!90219132.jpg)

   5. flatMap：和map类似，不同的是其每个元素转换得到的是Stream对象，会把子Stream中的元素压缩到父集合中；

      ![img](http://img01.taobaocdn.com/imgextra/i1/90219132/T2mBXnXQhXXXXXXXXX_!!90219132.jpg)

   6. peek: 生成一个包含原Stream的所有元素的新Stream，同时会提供一个消费函数（Consumer实例），新Stream每个元素被消费的时候都会执行给定的消费函数；

      ![img](http://img03.taobaocdn.com/imgextra/i3/90219132/T2DrFmXHtaXXXXXXXX_!!90219132.jpg)

   7.  limit: 对一个Stream进行截断操作，获取其前N个元素，如果原Stream中包含的元素个数小于N，那就获取其所有的元素；

      ![img](http://img02.taobaocdn.com/imgextra/i2/90219132/T2QAXlXJBaXXXXXXXX_!!90219132.jpg)

   8. skip: 返回一个丢弃原Stream的前N个元素后剩下元素组成的新Stream，如果原Stream中包含的元素个数小于N，那么返回空Stream；

      ![img](http://img04.taobaocdn.com/imgextra/i4/90219132/T24A8mXUJXXXXXXXXX_!!90219132.jpg)

   9. sorted：该方法用于对 Stream 排序。

      ```java
      // 以有序的形式输出 10 个随机数
      Random random = new Random();
      random.ints().limit(10).sorted().forEach(System.out::println);
      ```

4. #### 汇聚（Reduce）Stream

   1. 可变汇聚collect

      Java8给我们提供了Collector的工具类–[Collectors]，其中已经定义了一些静态工厂方法，比如：Collectors.toCollection()收集到Collection中, Collectors.toList()收集到List中和Collectors.toSet()收集到Set中。

      ```java
      List<Integer> numsWithoutNull = nums.stream()
          .filter(num -> num != null)
          .collect(Collectors.toList());
      ```

   2. reduce: 接受一个BinaryOperator类型的参数，在使用的时候我们可以用lambda表达式来

      ```java
      List<Integer> ints = Lists.newArrayList(1,2,3,4,5,6,7,8,9,10);
      
      // Optional<T> reduce(BinaryOperator<T> accumulator);
      // reduce方法接受一个函数，这个函数有两个参数，第一个参数是上次函数执行的返回值（也称为中间结果），第二个参数是stream中的元素，这个函数把这两个值相加，得到的和会被赋值给下次执行这个函数的第一个参数。要注意的是：第一次执行的时候第一个参数的值是Stream的第一个元素，第二个参数是Stream的第二个元素。
      System.out.println("ints sum is:" + ints.stream()
                         .reduce((sum, item) -> sum + item).get());
      
      // 变种
      // T reduce(T identity, BinaryOperator<T> accumulator);
      // 提供一个循环计算的初始值，如果Stream为空，就直接返回该值。
      System.out.println("ints sum is:" + ints.stream()
                         .reduce(0, (sum, item) -> sum + item));
      ```

      ![img](http://img03.taobaocdn.com/imgextra/i3/90219132/T28rVAXJlaXXXXXXXX_!!90219132.jpg)

   3. count: 获取Stream中元素的个数

      ```java
      System.out.println("ints sum is:" + ints.stream().count());
      ```

   4. sum: 将Stream的元素求和

   5. allMatch：是不是Stream中的所有元素都满足给定的匹配条件

   6. anyMatch：Stream中是否存在任何一个元素满足匹配条件

   7. findFirst: 返回Stream中的第一个元素，如果Stream为空，返回空Optional

   8. noneMatch：是不是Stream中的所有元素都不满足给定的匹配条件

   9. max和min：使用给定的比较器（Operator），返回Stream中的最大|最小值

5. #### Example1

   ```java
   import java.util.ArrayList;
   import java.util.Arrays;
   import java.util.IntSummaryStatistics;
   import java.util.List;
   import java.util.Random;
   import java.util.stream.Collectors;
   import java.util.Map;
   
   public class StreamTest {
      public static void main(String args[]){
   
          // 使用Java 8的新特性
         System.out.println("Using Java 8: ");
          
         // 统计空字符串的数量
         List<String> strings = Arrays.asList("efg", "", "abc", "bc", "ghij","", "lmn");
         System.out.println("List: " +strings);
   
         long count = strings.stream()
             .filter(string->string.isEmpty())
             .count();
         System.out.println("Empty Strings: " + count);
   
         count = strings.stream()
             .filter(string -> string.length() == 3)
             .count();
         System.out.println("Strings of length 3: " + count);
   
         // 消除空字符串
         List<String> filtered = strings.stream()
             .filter(string ->!string.isEmpty())
             .collect(Collectors.toList());
         System.out.println("Filtered List: " + filtered);
   
         // 消除空字符串，同时使用逗号来连接
         String mergedString = strings.stream()
             .filter(string ->!string.isEmpty())
             .collect(Collectors.joining(", "));
         System.out.println("Merged String: " + mergedString);
   
         // 获得不同数字的平方的列表
         List<Integer> numbers = Arrays.asList(2, 3, 3, 2, 5, 2, 7);
         List<Integer> squaresList = numbers.stream()
             .map( i ->i*i)
             .distinct()
             .collect(Collectors.toList());
         System.out.println("Squares List: " + squaresList);
          
         List<Integer> integers = Arrays.asList(1,2,13,4,15,6,17,8,19);
         System.out.println("List: " +integers);
         IntSummaryStatistics stats = integers.stream()
             .mapToInt((x) ->x)
             .summaryStatistics();
   
         // 输出结果
         System.out.println("Highest number in List : " + stats.getMax());
         System.out.println("Lowest number in List : " + stats.getMin());
         System.out.println("Sum of all numbers : " + stats.getSum());
         System.out.println("Average of all numbers : " + stats.getAverage());
         System.out.println("Random Numbers: ");
   
         // 输出10个随机数
         // ints是IntStream
         random.ints().limit(10).sorted().forEach(System.out::println);
   
         // 并行处理
         count = strings.parallelStream()
             .filter(string -> string.isEmpty())
             .count();
         System.out.println("Empty Strings: " + count);
      }
   ```

   ```
   $ javac StreamTest.java
   $ java StreamTest
   Using Java 8: 
   List: [efg, , abc, bc, ghij, , lmn]
   Empty Strings: 2
   Strings of length 3: 3
   Filtered List: [efg, abc, bc, ghij, lmn]
   Merged String: efg, abc, bc, ghij, lmn
   Squares List: [4, 9, 25, 49]
   List: [1, 2, 13, 4, 15, 6, 17, 8, 19]
   Highest number in List : 19
   Lowest number in List : 1
   Sum of all numbers : 85
   Average of all numbers : 9.444444444444445
   Random Numbers: 
   -1052491869
   -695737956
   105656001
   824662023
   1009911812
   1146499324
   1472638998
   1635609241
   1787308002
   1870383313
   Empty Strings: 2
   ```

6. #### Example2

   【要求】

   - 建立一个数组`1, 23, 4, 4, 22, 34, 45, 11, 33`
   - 求出数组中的最小数
   - 将数组去重，并将去重后数组的每个元素乘以 2，再求出乘以 2 后的数组的和。

   【代码】

   ```java
   import java.util.Arrays;
   
   public class Test {
       public static void main(String[] args) {
           int[] arr = {1, 23, 4, 4, 22, 34, 45, 11, 33};
           System.out.println("最小数："+Arrays.stream(arr).min());
           System.out.println("数组去重乘2求和：" + Arrays.stream(arr).distinct().map((i) -> i * 2).sum());
       }
   }
   ```

7. #### FlatMap

   FlatMap 用于将多个流合并为一个流，使用 FlatMap 时，表达式的返回值必须是 Stream 类型。而 Map 用于将一种流转化为另外一个流。

   【例1】考虑以下场景，有三个字符串("shi yan", "shi yan lou","lou yan shi")，我们希望将字符串使用空格分割，提取出单个单词。

   ```java
   import java.util.Arrays;
   import java.util.stream.Stream;
   
   public class FlatMapTest {
       public static void main(String[] args) {
           Stream<String> stringStream1 = Stream.of("shi yan", "shi yan lou","lou yan shi");
           Stream<String> stringStream2 = Stream.of("shi yan", "shi yan lou","lou yan shi");
           Stream<String[]> mapStream = stringStream1
                   //map将一种类型的流 转换为另外一个类型的流  这里转换成了String[]流 
                   //这并不是我们想要的，我们想要的是Stream<String>,而不是Stream<String[]>
                   .map(v -> v.split(" "));
           Stream<String> flatMapStream = stringStream2
                   //Arrays.stream将数组转换成了流 这里将分割后的String[]，转换成了Stream<String>，但是我们前面定义了三个字符串
                   //所以这里将产生三个Stream<String>，flatMap用于将三个流合并成一个流
                   .flatMap(v -> Arrays.stream(v.split(" ")));
           System.out.println("mapStream打印：");
           mapStream.peek(System.out::println).count();
           System.out.println("flatMapStream打印：");
           flatMapStream.peek(System.out::println).count();
   
       }
   }
   ```

   ```
   $ javac FlatMapTest.java
   $ java FlatMapTest
   mapStream打印：
   [Ljava.lang.String;@2d98a335
   [Ljava.lang.String;@16b98e56
   [Ljava.lang.String;@7ef20235
   flatMapStream打印：
   shi
   yan
   shi
   yan
   lou
   lou
   yan
   shi
   ```

   【例2】

   - 新建多个流，如：

     Stream<Integer> stream1 = Stream.of(1, 2, 3);

     Stream<Integer> stream2 = Stream.of(4, 5, 6);

     Stream<Integer> stream3 = Stream.of(7, 8, 9);

   - 使用 flatMap 合并多个流为一个流

   ```java
   import java.util.stream.Stream;
   
   public class MergerStream {
       public static void main(String[] args) {
           Stream<Integer> stream1 = Stream.of(1, 2, 3);
           Stream<Integer> stream2 = Stream.of(4, 5, 6);
           Stream<Integer> stream3 = Stream.of(7, 8, 9);
           Stream<Integer> mergerStream = Stream.of(stream1, stream2, stream3).flatMap((i) -> i);
           mergerStream.forEach(System.out::print);
       }
   }
   ```

   