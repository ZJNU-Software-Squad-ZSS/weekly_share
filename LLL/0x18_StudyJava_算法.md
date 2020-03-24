# StudyJava——算法

## 排序算法

1. ### 插入排序

   > 插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，算法适用于少量数据的排序，时间复杂度为 O(n^2)。

   排序过程如下：

   1. 从第一个元素开始，该元素可以认为已经被排序
   2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
   3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
   4. 重复步骤 3，直到找到已排序的元素小于或者等于新元素的位置
   5. 将新元素插入到该位置后
   6. 重复步骤 2~5

   ![](https://doc.shiyanlou.com/document-uid441493labid9180timestamp1545641555708.png/wm)

   ```java
   import java.util.Arrays;
   
   public class InsertSort {
       public static void sort(int[] arr) {
           int temp;
           for (int i = 1; i < arr.length; i++) {
               for (int j = 0; j < i; j++) {
                   //对已经排序好的元素比较，找到一个比插入元素大的元素 交换位置
                   if (arr[i] < arr[j]) {
                       temp = arr[i];
                       arr[i] = arr[j];
                       arr[j] = temp;
                   }
               }
           }
       }
   
       public static void main(String[] args) {
           int[] ints = {5, 3, 4, 1, 2};
           sort(ints);
           System.out.println(Arrays.toString(ints));
       }
   }
   ```

2. ### 冒泡排序

   冒泡排序的运行过程如下：

   - 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
   - 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
   - 针对所有的元素重复以上的步骤，除了最后一个。
   - 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

   ```java
   import java.util.Arrays;
   
   public class BubbleSort {
       public static void sort(int[] arr) {
           for (int i = 0; i < arr.length-1; i++) {
               for (int j = 0; j < arr.length - i - 1; j++) {
                   //如果当前元素比后一位元素大 交换位置
                   if (arr[j] > arr[j + 1]) {
                       int temp = arr[j];
                       arr[j] = arr[j + 1];
                       arr[j + 1] = temp;
                   }
               }
           }
       }
   
       public static void main(String[] args) {
           int[] ints = {5, 3, 4, 1, 2};
           sort(ints);
           System.out.println(Arrays.toString(ints));
       }
   }
   ```

3. ### 归并排序

   排序过程：

   1. 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
   2. 设定两个指针，最初位置分别为两个已经排序序列的起始位置
   3. 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
   4. 重复步骤 3 直到某一指针到达序列尾
   5. 将另一序列剩下的所有元素直接复制到合并序列尾

   ![](https://doc.shiyanlou.com/document-uid441493labid9180timestamp1545641120494.png/wm)

   ```java
   import java.util.Arrays;
   
   public class MergeSort {
   
       public static void mergeSort(int[] arrays, int left, int right) {
   //        如果数组还可以拆分
           if (left < right) {
               //数组的中间位置
               int middle = (left + right) / 2;
               //拆分左边数组
               mergeSort(arrays, left, middle);
               //拆分右边数组
               mergeSort(arrays, middle + 1, right);
               //合并
               merge(arrays, left, middle, right);
   
           }
       }
   
       /**
        * 合并数组
        */
       public static void merge(int[] arr, int left, int middle, int right) {
           //申请合并空间 大小为两个已经排序序列之和
           int[] temp = new int[right - left + 1];
           //i 和 j为两个已经排好序的数组的起始位置
           int i = left;
           int j = middle + 1;
           int k = 0;
           //排序
           while (i <= middle && j <= right) {
               //将比较小的数组放入合并空间
               if (arr[i] < arr[j]) {
                   temp[k++] = arr[i++];
               } else {
                   temp[k++] = arr[j++];
               }
           }
           //将左边剩余元素写入合并空间
           while (i <= middle) {
               temp[k++] = arr[i++];
           }
           //将右边剩余的元素写入合并空间
           while (j <= right) {
               temp[k++] = arr[j++];
           }
           //将排序后的数组写回原来的数组
           for (int l = 0; l < temp.length; l++) {
               arr[l + left] = temp[l];
           }
   
       }
   
       public static void main(String[] args) {
           int[] ints = {5, 3, 4, 1, 2};
           mergeSort(ints,0,ints.length-1);
           System.out.println(Arrays.toString(ints));
       }
   }
   ```

4. ### 快速排序

   快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为两个子序列（sub-lists）。

   步骤为：

   1. 从数列中挑出一个元素，称为“基准”（pivot），
   2. 重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（相同的数可以到任何一边）。在这个分割结束之后，该基准就处于数列的中间位置。这个称为**分割（partition）**操作。
   3. 递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子数列排序。

   递归到最底部时，数列的大小是零或一，也就是已经排序好了。这个算法一定会结束，因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。

   ![](https://doc.shiyanlou.com/document-uid441493labid9180timestamp1545641831045.png/wm)

   ```java
   import java.util.Arrays;
   
   public class QuickSort {
       public static void sort(int[] arr, int head, int tail) {
           if (head >= tail || arr == null || arr.length <= 1) {
               return;
           }
           //设置数组的起始位置 i 结束位置j 基准 pivot 为数组的中间
           int i = head, j = tail, pivot = arr[(head + tail) / 2];
           while (i <= j) {
               //当数组小于基准 循环结束后 相当于i所处的位置的值为大于基准的元素
               while (arr[i] < pivot) {
                   ++i;
               }
               //当数组大于基准 循环结束后 相当于j所处的位置的值为小于于基准的元素
               while (arr[j] > pivot) {
                   --j;
               }
               //如果i<j 那么则将交互i j对应位置的值
               if (i < j) {
                   int t = arr[i];
                   arr[i] = arr[j];
                   arr[j] = t;
                   //将指针继续移动
                   ++i;
                   --j;
               } else if (i == j) {
   //如果i=j 那么说明本次排序已经结束 将i++ 如果这里不使用i++ 那么后面的sort(arr,i,tail)将改为arr(arr,i+1,tail)
                   ++i;
               }
           }
           //继续将数组分割  
           sort(arr, head, j);
           sort(arr, i, tail);
       }
   
       public static void main(String[] args) {
           int[] ints = {5, 3, 4, 1, 2};
           sort(ints, 0, ints.length - 1);
           System.out.println(Arrays.toString(ints));
       }
   }
   ```

## 搜索算法

1. ### 线性搜索

   > 线性搜索或顺序搜索是一种寻找某一特定值的搜索算法，指按一定的顺序检查数组中每一个元素，直到找到所要寻找的特定值为止。是最简单的一种搜索算法。

   ```java
   public class LinearSearch {
       public static void main(String[] args) {
           int[] ints = {5, 3, 4, 1, 2};
           System.out.println(search(ints, 4));
       }
   
       public static int search(int[] arr, int key) {
           //循环
           for (int i = 0; i < arr.length; i++) {
               //比较是否等于key
               if (arr[i] == key) {
                   return arr[i];
               }
           }
           //找不到就返回-1
           return -1;
       }
   }
   ```

2. ### 二分查找

   > 在计算机科学中，**二分搜索**（英语：binary search），也称**折半搜索**（英语：half-interval search）、**对数搜索**（英语：logarithmic search），是一种在有序数组中查找某一特定元素的搜索算法。搜索过程从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜索过程结束；如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。如果在某一步骤数组为空，则代表找不到。这种搜索算法每一次比较都使搜索范围缩小一半。

   ```java
   public class BinarySearch {
       public static int search(int[] arr, int key) {
           int low = 0;
           int high = arr.length - 1;
           while (low <= high) {
               int middle = (high + low) / 2;
               //如果相等 返回值
               if (key == arr[middle]) {
                   return key;
               } else if (key < arr[middle]) {
                   //如果key小于中间值，那么改变high，值可能在左边部（比较小的部分）
                   high = middle - 1;
               }else {
                   //如果key大于中间值，那么改变low，值可能在右边部（比较大的部分）
                   low = middle + 1;
               }
           }
           return -1;
       }
   
       public static void main(String[] args) {
           int[] ints = {1, 2, 3, 4, 5};
           System.out.println(search(ints, 4));
       }
   }
   ```

   