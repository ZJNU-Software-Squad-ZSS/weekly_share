上学期无意点开LeetCode，发现脱离IDE很多代码都写不出来，于是乘着寒假刷几道题，重新看一下（预习）数据结构。

##### hashMap 

对应LeetCode第36题，有效的数独

简单粗暴用数组破题，然后看题解懵了，

```java
class Solution {
  public boolean isValidSudoku(char[][] board) {
    // init data
    HashMap<Integer, Integer> [] rows = new HashMap[9];
    HashMap<Integer, Integer> [] columns = new HashMap[9];
    HashMap<Integer, Integer> [] boxes = new HashMap[9];
    for (int i = 0; i < 9; i++) {
      rows[i] = new HashMap<Integer, Integer>();
      columns[i] = new HashMap<Integer, Integer>();
      boxes[i] = new HashMap<Integer, Integer>();
    }
// validate a board
for (int i = 0; i < 9; i++) {
  for (int j = 0; j < 9; j++) {
    char num = board[i][j];
    if (num != '.') {
      int n = (int)num;
      int box_index = (i / 3 ) * 3 + j / 3;

      // keep the current cell value
      rows[i].put(n, rows[i].getOrDefault(n, 0) + 1);
      columns[j].put(n, columns[j].getOrDefault(n, 0) + 1);
      boxes[box_index].put(n, boxes[box_index].getOrDefault(n, 0) + 1);

      // check if this value has been already seen before
      if (rows[i].get(n) > 1 || columns[j].get(n) > 1 || boxes[box_index].get(n) > 1)
        return false;
    }
  }
}

return true;
}}
```
 

###### hash，一种数据存储方式，散列表

散列函数的设计原则：计算简单，分布均匀

设计方法：

1、直接定址法

2、数据分析法（事先知道数据内容）

3、平方取中法：将数字平方运算后取中间的数字

4、取余法

散列冲突的解决方案：

-开放地址法：

1、线性探测法（一般）

2、二次探测法 序号的平方数

3、再哈希法：多个散列函数叠加

-链地址法：数组与链表结合（hashMap的底层原理）

###### hashMap源码

```java
class HashMap<K, V> extends AbstractMap<K, V> implements Map<K, V>, Cloneable, Serializable
```

源码大概是从来没读懂过，

此处以LeetCode给出的题解代码来对照源码理解，（我真的没看懂题解的代码在写什么）。

```java
public V getOrDefault(Object key, V defaultValue) {    
    HashMap.Node e;    
    return (e = this.getNode(hash(key), key)) == null ? defaultValue : e.value;
}
```

此处getNode方法不清楚

```java
final HashMap.Node<K, V> getNode(int hash, Object key) {    
    HashMap.Node[] tab;    
    HashMap.Node first;    
    int n;    
    if ((tab = this.table) != null && (n = tab.length) > 0 && (first = tab[n - 1 & hash]) != null) {        
        Object k;        
        if (first.hash == hash && ((k = first.key) == key || key != null && key.equals(k))) {            
            return first;        
        }        
        HashMap.Node e;        
        if ((e = first.next) != null) {            
            if (first instanceof HashMap.TreeNode) {                
                return ((HashMap.TreeNode)first).getTreeNode(hash, key);            
            }            
            do {                
                if (e.hash == hash && ((k = e.key) == key || key != null && key.equals(k))) {                    
                    return e;                
                }            
            } while((e = e.next) != null);        
        }    
    }    
    return null;
}
```

即查找是否已存在key值，若存在，则设为e.value,若不存在，则设置为给定的defaultValue。



反思 

java容器和数据结构都没学好，要加强学习（预习）。

题目没做几道，但是感觉做出来也用处不大，看官方题解怀疑自己做题没带脑子。

后悔大一没好好刷题。