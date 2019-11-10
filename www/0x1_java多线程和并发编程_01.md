### java多线程和并发编程

#### Java并发框架Executor

**并行编程（较困难）：**通过编码方式利用多核或多处理器称为并行编程，多线程概念的一个子集。

任务分配和执行过程高度耦合

控制粒度，切割任务

**任务问题，线程执行过程的监督问题**

串行编程 （较简单）

-单个CPU计算核一直在下降，计算核一直在增加



并行模式：

-主从模式（主线程指挥工作）

-Worker（P2P）

java并发编程

-thread/runnable/thread组管理

-executor

-fork-join框架



线程组管理

-线程的集合

-树形结构，大线程组可包括小的线程组

-低层次管理（能管理但管理效率低）

-任务分配和执行过程高度耦合

-线程和线程组内的线程，都是new产生出来的，start一次后不可载使用--性价比低



*一、耦合*

*1、耦合是指两个或两个以上的体系或两种运动形式间通过相互作用而彼此影响以至联合起来的现象。*

*2、在软件工程中，对象之间的耦合度就是对象之间的依赖性。对象之间的耦合越高，维护成本越高，因此对象的设计应使类和构件之间的耦合最小。*

*3、分类：有软硬件之间的耦合，还有软件各模块之间的耦合。耦合性是程序结构中各个模块之间相互关联的度量。它取决于各个模块之间的接口的复杂程度、调用模块的方式以及哪些信息通过接口。*

*二、解耦*

*1、解耦，字面意思就是解除耦合关系。*

*2、在软件工程中，降低耦合度即可以理解为解耦，模块间有依赖关系必然存在耦合，理论上的绝对零耦合是做不到的，但可以通过一些现有的方法将耦合度降至最低。*

*3、设计的核心思想：尽可能减少代码耦合，如果发现代码耦合，就要采取解耦技术。让数据模型，业务逻辑和视图显示三层之间彼此降低耦合，把关联依赖降到最低，而不至于牵一发而动全身。原则就是A功能的代码不要写在B的功能代码中，如果两者之间需要交互，可以通过接口，通过消息，甚至可以引入框架，但总之就是不要直接交叉写。*



###### Executor

-分离任务的创建和执行者的创建

-线程重复利用

（共享线程池：预设好多个Thread，多次执行多个小任务，任务创建和执行过程解耦，无需考虑线程池的执行过程）

主要类：

-executors.newCachedThreadPool/newFixedThreadPool 创建线程池

-ExecutorService 线程服务

-Callable 具体的逻辑对象（线程类）*【注意】 Runnable的run方法没有返回值，而Callable的call方法可以有返回值*

-Future 返回结果

代码示例一：

```java
package executor.example1;

public class Main {

	public static void main(String[] args) throws InterruptedException {
		// 创建一个执行服务器
		Server server=new Server();
		
		// 创建100个任务，并发给执行器，等待完成
		for (int i=0; i<100; i++){
			Task task=new Task("Task "+i);
			Thread.sleep(10);
			server.submitTask(task);//提交任务给线程池
		}		
		server.endServer();
	}
}

```

```java
package executor.example1;

import java.util.concurrent.Executors;
import java.util.concurrent.ThreadPoolExecutor;

/**
 * 执行服务器
 *
 */
public class Server {
	
	//线程池
	private ThreadPoolExecutor executor;
	
	public Server(){
		executor=(ThreadPoolExecutor)Executors.newCachedThreadPool();//容量随着任务的量增长（默认线程池）
		//executor=(ThreadPoolExecutor)Executors.newFixedThreadPool(5);
	}
	
	//向线程池提交任务
	public void submitTask(Task task){
		System.out.printf("Server: A new task has arrived\n");
		executor.execute(task); //执行  无返回值
		
		System.out.printf("Server: Pool Size: %d\n",executor.getPoolSize());
		System.out.printf("Server: Active Count: %d\n",executor.getActiveCount());
		System.out.printf("Server: Completed Tasks: %d\n",executor.getCompletedTaskCount());
	}

	public void endServer() {//关闭
		executor.shutdown();
	}
}

```

```java
package executor.example1;

import java.util.Date;
import java.util.concurrent.TimeUnit;
/**
 * Task 任务类
 * @author Tom
 *
 */
public class Task implements Runnable {

	private String name;
	
	public Task(String name){
		this.name=name;
	}
	
	public void run() {
		try {
			Long duration=(long)(Math.random()*1000);
			System.out.printf("%s: Task %s: Doing a task during %d seconds\n",Thread.currentThread().getName(),name,duration);
			Thread.sleep(duration);			
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		
		System.out.printf("%s: Task %s: Finished on: %s\n",Thread.currentThread().getName(),name,new Date());
	}

}

```

代码示例二：

```java
package executor.example2;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.ThreadPoolExecutor;


public class SumTest {

	public static void main(String[] args) {
		
		// 执行线程池
		ThreadPoolExecutor executor=(ThreadPoolExecutor)Executors.newFixedThreadPool(4);//固定线程池，
		//线程越多，计算机负担越大（线程数最好为CPU核的两倍到四倍
		
		List<Future<Integer>> resultList=new ArrayList<>();//future 存放结果

		//统计1-1000总和，分成10个任务计算，提交任务
		for (int i=0; i<10; i++){
			SumTask calculator=new SumTask(i*100+1, (i+1)*100);
			Future<Integer> result=executor.submit(calculator);
			resultList.add(result);
		}
		
		// 每隔50毫秒，轮询等待10个任务结束
		do {
			System.out.printf("Main: 已经完成多少个任务: %d\n",executor.getCompletedTaskCount());
			for (int i=0; i<resultList.size(); i++) {
				Future<Integer> result=resultList.get(i);
				System.out.printf("Main: Task %d: %s\n",i,result.isDone());
			}
			try {
				Thread.sleep(50);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		} while (executor.getCompletedTaskCount()<resultList.size());
		
		// 所有任务都已经结束了，综合计算结果		
		int total = 0;
		for (int i=0; i<resultList.size(); i++) {
			Future<Integer> result=resultList.get(i);
			Integer sum=null;
			try {
				sum=result.get();
				total = total + sum;
			} catch (InterruptedException e) {
				e.printStackTrace();
			} catch (ExecutionException e) {
				e.printStackTrace();
			}
		}
		System.out.printf("1-1000的总和:" + total);
		
		// 关闭线程池
		executor.shutdown();
	}
}

```

```java
package executor.example2;

import java.util.Random;
import java.util.concurrent.Callable;

public class SumTask implements Callable<Integer> {
	//定义每个线程计算的区间
	private int startNumber;
	private int endNumber;
	
	public SumTask(int startNumber, int endNumber){
		this.startNumber=startNumber;
		this.endNumber=endNumber;
	}
	
	@Override
	public Integer call() throws Exception {
		int sum = 0;
		for(int i=startNumber; i<=endNumber; i++)
		{
			sum = sum + i;
		}
		
		Thread.sleep(new Random().nextInt(1000));
		
		System.out.printf("%s: %d\n",Thread.currentThread().getName(),sum);
		return sum;
	}
}

```

##### java并发框架Fork-join

java7提出，分治编程，适用于整体计算量不好确定的场合。

二分法

关键类：

-ForkJoinPool 任务池

-RecursiveAction

-RecursiveTask

示例代码：

```java
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.ForkJoinTask;

//分任务求和
public class SumTest {
    
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        //创建执行线程池
    	ForkJoinPool pool = new ForkJoinPool();
    	//ForkJoinPool pool = new ForkJoinPool(4);
    	
    	//创建任务
        SumTask task = new SumTask(1, 10000000);
        
        //提交任务
        ForkJoinTask<Long> result = pool.submit(task);
        
        //等待结果
        do {
			System.out.printf("Main: Thread Count: %d\n",pool.getActiveThreadCount());
			System.out.printf("Main: Paralelism: %d\n",pool.getParallelism());
			try {
				Thread.sleep(50);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		} while (!task.isDone());
        
        //输出结果
        System.out.println(result.get().toString());
    }
}

```

```java
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.ForkJoinTask;

//分任务求和
public class SumTest {
    
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        //创建执行线程池
    	ForkJoinPool pool = new ForkJoinPool();
    	//ForkJoinPool pool = new ForkJoinPool(4);
    	
    	//创建任务
        SumTask task = new SumTask(1, 10000000);
        
        //提交任务
        ForkJoinTask<Long> result = pool.submit(task);
        
        //等待结果
        do {
			System.out.printf("Main: Thread Count: %d\n",pool.getActiveThreadCount());
			System.out.printf("Main: Paralelism: %d\n",pool.getParallelism());
			try {
				Thread.sleep(50);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		} while (!task.isDone());
        
        //输出结果
        System.out.println(result.get().toString());
    }
}
```

##### Java并发数据结构

常用的数据结构试线程不安全的

-ArrayList，HashMap，HashSet 是非同步的

-多个线程同时读写，可能抛出异常或数据错误

传统Vector，Hashtable等同步集合性能稍差

并发数据结构：

-阻塞式集合：当集合为空或满时，等待

-非阻塞式集合：当集合为空或满时，不等待，返回null或异常

数据结构：

###### List

-Vector 同步安全，写多读少（大量修改操作，读时比较少）

-ArrayList 不安全

-Collections.sychronized(List list) 基于sychronized，效率低

-CopyOnWriteArrayList 读多写少，非阻塞式，基于复制机制

```java
package list;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;

public class ListTest {    
 
    public static void main(String[] args) throws InterruptedException{

        //线程不安全
        List<String> unsafeList = new ArrayList<String>();
        //线程安全
        List<String> safeList1 = Collections.synchronizedList(new ArrayList<String>());
        //线程安全
        CopyOnWriteArrayList<String> safeList2 = new CopyOnWriteArrayList<String>();

        ListThread t1 = new ListThread(unsafeList);
        ListThread t2 = new ListThread(safeList1);
        ListThread t3 = new ListThread(safeList2);

        for(int i = 0; i < 10; i++){
            Thread t = new Thread(t1, String.valueOf(i));//相当于十个线程启动
            t.start();
        }
        for(int i = 0; i < 10; i++) {
            Thread t = new Thread(t2, String.valueOf(i));
            t.start();
        }
        for(int i = 0; i < 10; i++) {
            Thread t = new Thread(t3, String.valueOf(i));
            t.start();
        }

        //等待子线程执行完
        Thread.sleep(2000);
 
        System.out.println("listThread1.list.size() = " + t1.list.size());
        System.out.println("listThread2.list.size() = " + t2.list.size());
        System.out.println("listThread3.list.size() = " + t3.list.size());

        //输出list中的值
        System.out.println("unsafeList：");
        for(String s : t1.list){
            if(s == null){
            	System.out.print("null  ");
            }
            else
            {
            	System.out.print(s + "  ");
            }
        }
        System.out.println();
        System.out.println("safeList1：");
        for(String s : t2.list){
        	if(s == null){
            	System.out.print("null  ");
            }
            else
            {
            	System.out.print(s + "  ");
            }
        }
        System.out.println();
        System.out.println("safeList2：");
        for(String s : t3.list){
        	if(s == null){
            	System.out.print("null  ");
            }
            else
            {
            	System.out.print(s + "  ");
            }
        }
    }
}

class ListThread implements Runnable{
	public List<String> list;

    public ListThread(List<String> list){
        this.list = list;
    }

    @Override
    public void run() {
    	int i = 0;
    	while(i<10)
    	{
    		try {
                Thread.sleep(10);
            }catch (InterruptedException e){
                e.printStackTrace();
            }
            //把当前线程名称加入list中
            list.add(Thread.currentThread().getName());
            i++;
    	}        
    }
}
```

###### Set

-HashSet 不安全

-Collections.sychronized(Set set) 基于sychronized，效率低

-CopyOnWriteArraySet （基于CopyOnWriteArrayList实现） 读多写少，非阻塞

```java
package set;

import java.util.*;
import java.util.concurrent.CopyOnWriteArraySet;

public class SetTest{  
 
    public static void main(String[] args) throws InterruptedException{

        //线程不安全
        Set<String> unsafeSet = new HashSet<String>();
        //线程安全
        Set<String> safeSet1 = Collections.synchronizedSet(new HashSet<String>());
        //线程安全
        CopyOnWriteArraySet<String> safeSet2 = new CopyOnWriteArraySet<String>();

        SetThread t1 = new SetThread(unsafeSet);
        SetThread t2 = new SetThread(safeSet1);
        SetThread t3 = new SetThread(safeSet2);

        //unsafeSet的运行测试
        for(int i = 0; i < 10; i++){
        	Thread t = new Thread(t1, String.valueOf(i));
        	t.start();
        }
        for(int i = 0; i < 10; i++) {
        	Thread t = new Thread(t2, String.valueOf(i));
            t.start();
        }
        for(int i = 0; i < 10; i++) {
        	Thread t = new Thread(t3, String.valueOf(i));
            t.start();
        }

        //等待子线程执行完
        Thread.sleep(2000);
 
        System.out.println("setThread1.set.size() = " + t1.set.size());
        System.out.println("setThread2.set.size() = " + t2.set.size());
        System.out.println("setThread3.set.size() = " + t3.set.size());

        //输出set中的值
        System.out.println("unsafeSet：");
        for(String element:t1.set){
            if(element == null){
            	System.out.print("null  ");
            }
            else
            {
            	System.out.print(element + "  ");
            }
        }
        System.out.println();
        System.out.println("safeSet1：");
        for(String element:t2.set){
        	if(element == null){
            	System.out.print("null  ");
            }
            else
            {
            	System.out.print(element + "  ");
            }
        }
        System.out.println();
        System.out.println("safeSet2：");
        for(String element:t3.set){
        	if(element == null){
            	System.out.print("null  ");
            }
            else
            {
            	System.out.print(element + "  ");
            }
        }
    }
}

class SetThread implements Runnable{
	public Set<String> set;

    public SetThread(Set<String> set){
        this.set = set;
    }

    @Override
    public void run() {
    	int i = 0;
    	while(i<10)
    	{
    		i++;
    		try {
                Thread.sleep(10);
            }catch (InterruptedException e){
                e.printStackTrace();
            }
            //把当前线程名称加入list中
            set.add(Thread.currentThread().getName() + i);
    	}        
    }
}
```

###### Map

-Hashtable 同步安全

-HashMap 不安全

-Collections.sychronized(Map map) 基于sychronized，效率低

-ConcurrentHashMap 读多写少，非阻塞

```java
package map;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

public class MapTest{    
 
    public static void main(String[] args) throws InterruptedException{

        //线程不安全
        Map<Integer,String> unsafeMap = new HashMap<Integer,String>();
        //线程安全
        Map<Integer,String> safeMap1 = Collections.synchronizedMap(new HashMap<Integer,String>());
        //线程安全
        ConcurrentHashMap<Integer,String> safeMap2 = new ConcurrentHashMap<Integer,String>();

        MapThread t1 = new MapThread(unsafeMap);
        MapThread t2 = new MapThread(safeMap1);
        MapThread t3 = new MapThread(safeMap2);

        //unsafeMap的运行测试
        for(int i = 0; i < 10; i++){
        	Thread t = new Thread(t1);
        	t.start();
        }       
        for(int i = 0; i < 10; i++) {
        	Thread t = new Thread(t2);
            t.start();
        }
        for(int i = 0; i < 10; i++) {
        	Thread t = new Thread(t3);
            t.start();
        }

        //等待子线程执行完
        Thread.sleep(2000);
 
        System.out.println("mapThread1.map.size() = " + t1.map.size());
        System.out.println("mapThread2.map.size() = " + t2.map.size());
        System.out.println("mapThread3.map.size() = " + t3.map.size());

        //输出set中的值
        System.out.println("unsafeMap：");
        Iterator iter = t1.map.entrySet().iterator();
        while(iter.hasNext()) {
            Map.Entry<Integer,String> entry = (Map.Entry<Integer,String>)iter.next();
            // 获取key
            System.out.print(entry.getKey() + ":");
            // 获取value
            System.out.print(entry.getValue() + " ");
        }
        System.out.println();
        
        System.out.println("safeMap1：");
        iter = t2.map.entrySet().iterator();
        while(iter.hasNext()) {
            Map.Entry<Integer,String> entry = (Map.Entry<Integer,String>)iter.next();
            // 获取key
            System.out.print(entry.getKey() + ":");
            // 获取value
            System.out.print(entry.getValue() + " ");
        }

        System.out.println();
        System.out.println("safeMap2：");
        iter = t3.map.entrySet().iterator();
        while(iter.hasNext()) {
            Map.Entry<Integer,String> entry = (Map.Entry<Integer,String>)iter.next();
            // 获取key
            System.out.print(entry.getKey() + ":");
            // 获取value
            System.out.print(entry.getValue() + " ");
        }
        System.out.println();
        System.out.println("mapThread1.map.size() = " + t1.map.size());
        System.out.println("mapThread2.map.size() = " + t2.map.size());
        System.out.println("mapThread3.map.size() = " + t3.map.size());
    }
}

class MapThread implements Runnable
{
	public Map<Integer,String> map;

    public MapThread(Map<Integer,String> map){
        this.map = map;
    }

    @Override
    public void run() {
        int i=0;
        
        while(i<100)
        {
        	//把当前线程名称加入map中
            map.put(i++,Thread.currentThread().getName());
            try {
                Thread.sleep(10);
            }catch (InterruptedException e){
                e.printStackTrace();
            }
        }        
    }
}
```

###### Queue & Deque

-ConcurrentLinkedQueue 非阻塞

-ArrayBlockingQueue/LinkedBlockingQueue 阻塞

```java
package queue;

import java.util.*;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.ConcurrentLinkedDeque;

public class QueueTest {

    public static void main(String[] args) throws InterruptedException{

        //线程不安全
        Deque<String> unsafeQueue = new ArrayDeque<String>();
        //线程安全
        ConcurrentLinkedDeque<String> safeQueue1 = new ConcurrentLinkedDeque<String>();

        ArrayBlockingQueue<String> safeQueue2 = new ArrayBlockingQueue<String>(100);

        QueueThread t1 = new QueueThread(unsafeQueue);
        QueueThread t2 = new QueueThread(safeQueue1);
        QueueThread t3 = new QueueThread(safeQueue2);

        for(int i = 0; i < 10; i++){
            Thread thread1 = new Thread(t1, String.valueOf(i));
            thread1.start();
        }
        for(int i = 0; i < 10; i++) {
            Thread thread2 = new Thread(t2, String.valueOf(i));
            thread2.start();
        }
        for(int i = 0; i < 10; i++) {
            Thread thread3 = new Thread(t3, String.valueOf(i));
            thread3.start();
        }

        //等待子线程执行完
        Thread.sleep(2000);
 
        System.out.println("queueThread1.queue.size() = " + t1.queue.size());
        System.out.println("queueThread2.queue.size() = " + t2.queue.size());
        System.out.println("queueThread3.queue.size() = " + t3.queue.size());

        //输出queue中的值
        System.out.println("unsafeQueue：");
        for(String s:t1.queue)
        {
        	System.out.print(s + " ");
        }
        System.out.println();
        System.out.println("safeQueue1：");
        for(String s:t2.queue)
        {
        	System.out.print(s + " ");
        }
        System.out.println();
        System.out.println("safeQueue2：");
        for(String s:t3.queue)
        {
        	System.out.print(s + " ");
        }
    }
}

class QueueThread implements Runnable{
	public Queue<String> queue;

    public QueueThread(Queue<String> queue){
        this.queue = queue;
    }

    @Override
    public void run() {
    	int i = 0;
    	while(i<10)
    	{
    		i++;
    		try {
                Thread.sleep(10);
            }catch (InterruptedException e){
                e.printStackTrace();
            }
            //把当前线程名称加入list中
            queue.add(Thread.currentThread().getName());
    	}        
    }
}
```

未完。。。

------

##### 作业：

给定一个int数组，假设有10000个长度，里面放满1-100的随机整数。需要用串行循环计算、Executors框架和Fork-Join框架三种方法，实现查找并输出该数组中50的出现个数。

预期执行结果如下(具体数量根据每个程序随机赋值决定)

串行搜索得到50的个数是5个。

Executors搜索得到50的个数是5个。

Fork-Join搜索得到50的个数是5个

mySearch.java

```java
package homework;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Executors;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.ForkJoinTask;
import java.util.concurrent.Future;
import java.util.concurrent.ThreadPoolExecutor;

public class mySearch {

	static int[] a = new int[10000];
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		for(int i = 0;i <10000;i++) {
			int t = (int) (Math.random()*100+1);
			a[i] = t;
		}
		Search1();
		Search2();
		Search3();
	}
	public static void Search1() {
		Arrays.sort(a);
		int c = 0;
		int b = Arrays.binarySearch(a, 50);
		for(int i = b; i <10000;i++) {
			if(a[i]==50) {
				c++;
				//System.out.println(a[i]+" "+c);
			}
			else
				break;
		}
		System.out.println(c);
		
		
	}
	public static void Search2() {
		ThreadPoolExecutor executor=(ThreadPoolExecutor)Executors.newFixedThreadPool(4);
		List<Future<Integer>> resultList=new ArrayList<>();
		for (int i=0; i<10; i++){
			SearchTask1 calculator=new SearchTask1(i*1000+1, (i+1)*1000,a);
			Future<Integer> result=executor.submit(calculator);
			resultList.add(result);
		}
		do {
			//System.out.printf("Main: 已经完成多少个任务: %d\n",executor.getCompletedTaskCount());
			for (int i=0; i<resultList.size(); i++) {
				Future<Integer> result =resultList.get(i);
				//System.out.printf("Main: Task %d: %s\n",i,result.isDone());
			}
			try {
				Thread.sleep(50);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		} while (executor.getCompletedTaskCount()<resultList.size());
		
		// 所有任务都已经结束了，综合计算结果		
		int total = 0;
		for (int i=0; i<resultList.size(); i++) {
			Future<Integer> result=resultList.get(i);
			Integer sum=null;
			try {
				sum=result.get();
				total = total + sum;
			} catch (InterruptedException e) {
				e.printStackTrace();
			} catch (ExecutionException e) {
				e.printStackTrace();
			}
		}
		System.out.printf("总共有:" + total+"个50");
		
		// 关闭线程池
		executor.shutdown();
	}
	public static void Search3() {
		ForkJoinPool pool = new ForkJoinPool();
    	//ForkJoinPool pool = new ForkJoinPool(4);
    	
    	//创建任务
        SearchTask2 task = new SearchTask2(0, 10000,a);
        
        //提交任务
        ForkJoinTask<Integer> result = pool.submit(task);
        do {
        	//System.out.println();
			//System.out.printf("Main: Thread Count: %d\n",pool.getActiveThreadCount());
			//System.out.printf("Main: Paralelism: %d\n",pool.getParallelism());
			try {
				Thread.sleep(50);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		} while (!task.isDone());
        if(task.isDone())
			try {
				System.out.println();
				System.out.println(result.get().toString());
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (ExecutionException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
        
		
	}
}
```

SearchTask1.java

```java
package homework;

import java.util.Arrays;
import java.util.Random;
import java.util.concurrent.Callable;

public class SearchTask1 implements Callable<Integer>{
	private int startNumber;
	private int endNumber;
	private int[] a;
	public SearchTask1(int startNumber, int endNumber,int[] a){
		this.startNumber=startNumber;
		this.endNumber=endNumber;
		this.a = a;
	}

	@Override
	public Integer call() throws Exception {
		Arrays.sort(a,startNumber,endNumber);
		int b;
		int c = 0;
		b = Arrays.binarySearch(a, startNumber, endNumber,50);
		if(b>startNumber) {
		System.out.println(b+" "+startNumber+" "+endNumber);
		
		for(int i = b; i < endNumber; i++) {
			if(a[i] == 50) {
				c++;
			}
			else
				break;
		}
		Thread.sleep(new Random().nextInt(1000));
		
		}
		
		return c;
	}
	

}

```

SearchTask2.java

```java
package homework;

import java.util.Arrays;
import java.util.concurrent.RecursiveTask;

public class SearchTask2 extends RecursiveTask<Integer> {
	private int startNumber;
	private int endNumber;
	private int[] a;
	
	public SearchTask2(int startNumber, int endNumber,int[] a){
		this.startNumber=startNumber;
		this.endNumber=endNumber;
		this.a = a;
	}

	public static final int threadhold = 1000;
	@Override
	protected Integer compute() {
		Integer sum = 0;
		boolean canCompute = (endNumber - startNumber) <= threadhold;
		if (canCompute) {
			//System.out.println("a");
			//Arrays.sort(a,startNumber,endNumber);
			int b;
			int c = 0;
			b = Arrays.binarySearch(a, startNumber, endNumber,50);
			//System.out.println(b);
			if(b > startNumber) {
			//System.out.println(b+" "+startNumber+" "+endNumber);
			
			for(int i = b; i < endNumber; i++) {
				if(a[i] == 50) {
					c++;
					//System.out.println(c);
				}
				else
					break;
			}
			sum = c;
		} 
		}
			else {
			// 任务大于阈值, 分裂为2个任务
			int middle = (startNumber + endNumber) / 2;
			SearchTask2 subTask1 = new SearchTask2(startNumber, middle,a);
			SearchTask2 subTask2 = new SearchTask2(middle + 1, endNumber,a);

			//System.out.println(middle);
			invokeAll(subTask1, subTask2);

			Integer sum1 = subTask1.join();
			Integer sum2 = subTask2.join();

			// 结果合并
			sum = sum1 + sum2;
		}
		
		
	
		return sum;
	}

}
```

reference

------

中国大学MOOC--java核心技术（陈育良--华东师范大学）