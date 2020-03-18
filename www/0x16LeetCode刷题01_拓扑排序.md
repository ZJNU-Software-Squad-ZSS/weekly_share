```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map.Entry;

public class HashMapTest {

	public static void main(String[] args) {
		HashMap<String, String> map = new HashMap<>();
		map.put("zhang", "31");//存放键值对

		System.out.println(map.containsKey("zhang"));//键中是否包含这个数据
		System.out.println(map.containsKey("daniu"));
		System.out.println("=========================");

		System.out.println(map.get("zhang"));//通过键拿值
		System.out.println(map.get("daniu"));
		System.out.println("=========================");

		System.out.println(map.isEmpty());//判空
		System.out.println(map.size());
		System.out.println("=========================");

		System.out.println(map.remove("zhang"));//从键值中删除
		System.out.println(map.containsKey("zhang"));
		System.out.println(map.get("zhang"));//获取值
		System.out.println(map.isEmpty());
		System.out.println(map.size());
		System.out.println("=========================");

		map.put("zhang", "31");
		System.out.println(map.get("zhang"));
		map.put("zhang", "32");
		System.out.println(map.get("zhang"));
		System.out.println("=========================");

		map.put("zhang", "31");
		map.put("cheng", "32");
		map.put("yun", "33");

		for (String key : map.keySet()) {
			System.out.println(key);
		}
		System.out.println("=========================");

		for (String values : map.values()) {
			System.out.println(values);
		}
		System.out.println("=========================");

		map.clear();
		map.put("A", "1");
		map.put("B", "2");
		map.put("C", "3");
		map.put("D", "1");
		map.put("E", "2");
		map.put("F", "3");
		map.put("G", "1");
		map.put("H", "2");
		map.put("I", "3");
		for (Entry<String, String> entry : map.entrySet()) {
			String key = entry.getKey();
			String value = entry.getValue();
			System.out.println(key + "," + value);
		}
		System.out.println("=========================");

		// you can not remove item in map when you use the iterator of map
		// for(Entry<String,String> entry : map.entrySet()){
		// if(!entry.getValue().equals("1")){
		// map.remove(entry.getKey());
		// }
		// }

		// if you want to remove items, collect them first, then remove them by
		// this way.
		List<String> removeKeys = new ArrayList<String>();
		for (Entry<String, String> entry : map.entrySet()) {
			if (!entry.getValue().equals("1")) {
				removeKeys.add(entry.getKey());
			}
		}
		for (String removeKey : removeKeys) {
			map.remove(removeKey);
		}
		for (Entry<String, String> entry : map.entrySet()) {
			String key = entry.getKey();
			String value = entry.getValue();
			System.out.println(key + "," + value);
		}
		System.out.println("=========================");

	}

}
```

```java
import java.util.Map;
import java.util.Random;
import java.util.Iterator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map.Entry;
import java.util.Collection;

/*
 * @desc HashMap测试程序
 *        
 * @author skywang
 */
public class HashMapTest {

    public static void main(String[] args) {
        testHashMapAPIs();
    }
    
    private static void testHashMapAPIs() {
        // 初始化随机种子
        Random r = new Random();
        // 新建HashMap
        HashMap map = new HashMap();
        // 添加操作
        map.put("one", r.nextInt(10));
        map.put("two", r.nextInt(10));
        map.put("three", r.nextInt(10));

        // 打印出map
        System.out.println("map:"+map );

        // 通过Iterator遍历key-value
        Iterator iter = map.entrySet().iterator();
        while(iter.hasNext()) {
            Map.Entry entry = (Map.Entry)iter.next();
            System.out.println("next : "+ entry.getKey() +" - "+entry.getValue());
        }

        // HashMap的键值对个数        
        System.out.println("size:"+map.size());

        // containsKey(Object key) :是否包含键key
        System.out.println("contains key two : "+map.containsKey("two"));
        System.out.println("contains key five : "+map.containsKey("five"));

        // containsValue(Object value) :是否包含值value
        System.out.println("contains value 0 : "+map.containsValue(new Integer(0)));

        // remove(Object key) ： 删除键key对应的键值对
        map.remove("three");

        System.out.println("map:"+map );

        // clear() ： 清空HashMap
        map.clear();

        // isEmpty() : HashMap是否为空
        System.out.println((map.isEmpty()?"map is empty":"map is not empty") );
    }
}
```

第一道关于图的题目：

入度：有向图的某个顶点作为终点的次数和。

出度：有向图的某个顶点作为起点的次数和。

```java
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
      	int[] indegrees = new int[numCourses];
        //新建indegrees数组        
        List<List<Integer>> adjacency = new ArrayList<>();//邻接表
        Queue<Integer> queue = new LinkedList<>();
        for(int i = 0; i < numCourses; i++)
            adjacency.add(new ArrayList<>());
        // Get the indegree and adjacency of every course.入度表
        for(int[] cp : prerequisites) {
            indegrees[cp[0]]++;//统计度数，以cp[0]为下标，巧妙地利用题目条件，课程编号从0开始
            adjacency.get(cp[1]).add(cp[0]);//在cp[1]处的邻接表加上cp[0]
        }
        // Get all the courses with the indegree of 0.
        for(int i = 0; i < numCourses; i++)
            if(indegrees[i] == 0) queue.add(i);//将入度数为0的推入栈
        // BFS TopSort.
        while(!queue.isEmpty()) {
            int pre = queue.poll();
            numCourses--;
            for(int cur : adjacency.get(pre))
                if(--indegrees[cur] == 0) queue.add(cur);
        }
        return numCourses == 0;
    }
}

```

拓扑排序，对一个有向无环图（Directed Acyclic Graph 简称DAG）进行拓扑排序，将G中所有顶点排成一个线性序列，使得图中任意一对顶点u和v，若边（u，v）-》E（G），则u在线性序列中出现在v之前。这样的线性序列称为满足拓扑排序（Topological Order）的序列，简称拓扑排序。由某个集合上的一个偏序得到该集合上的一个全序。

在实现上，从有向图中选一个没有前驱的顶点并且输出

从图中删除该顶点和所有出边，当顶点被删去，后继点的入度减零，实现循环直至完全删除

用于判断一张图是否能成环