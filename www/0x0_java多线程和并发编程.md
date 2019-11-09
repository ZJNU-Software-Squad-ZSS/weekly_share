#### 多线程和多进程

###### 多线程

一个程序可以包含多个子任务，可串/并行

每个子任务可称为一个线程

想象打扫房间的阿姨在一个房间被锁住时打扫该楼的其他房间，而非去其他楼栋打扫。（CPU的利用率提高）

```java
public class ThreadDemo1
{
	public static void main(String args[]) throws Exception
	{
		new TestThread1().start();
		while(true)
		{
			System.out.println("main thread is running");
			Thread.sleep(1000);
		}
	}
}

class TestThread1 extends Thread
{
	public void run() 
	{
		while(true)
		{
			System.out.println(" TestThread1 is running");
			try {
				Thread.sleep(1000); //1000毫秒
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
} 

```

输出结果：同一程序两条语句交替不定时输出（只启动一个java.exe)

###### 多进程

当前的操作系统都是多任务OS

每个独立执行的任务都是一个进程

OS将时间划分为小的时间片段，每个时间片段内，CPU被分配给某个任务，在该时间结束后，CPU自动回收，执行其他任务。

在CPU上，任务按照串行一次运行（单核CPU）（多核CPU可以并行进程任务）

```java

public class ProcessDemo1 {

	public static void main(String[] args) {
		while(true)
		{
			int a = (int) (Math.random() * 100);
			System.out.println(" main thread is running " + a);
			try {
				Thread.sleep(5000); //5000毫秒
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}		
	}
}

```

多线程vs多进程

线程共享数据

线程通讯更高效

线程更轻量更易切换

多个线程更易管理

###### java多线程

*<!--java的四个主要接口*-->

<!--Colonable，用于对象克隆-->

<!--<!--Comparable，用于对象比较-->

<!--Serializable，用于对象序列化-->

<!--Runnable，用于对象线程化-->

创建：

```java

public class Thread2 implements Runnable{
	//通过实现runnable接口来创建线程
	public void run()
	{
		System.out.println("hello");
	}
	public static void main(String[] a)
	{
		new Thread(new Thread2()).start();
		//实现runnable的对象必须包装在thread类里面，才可以启动
		//通过start方法来启动线程中的run方法
	}
}
```

```java
public class Thread1 extends Thread{
	//通过继承thread类来创建线程
	public void run()
	{
		System.out.println("hello");
	}
	public static void main(String[] a)
	{
		new Thread1().start();//通过start方法来启动线程的run方法
	}
}
```

```java
//线程基本运行规则：
public class ThreadDemo0
{
	public static void main(String args[]) throws Exception
	{
		new TestThread0().run();//串行
		new TestThread1().start();//并行运行（1、通过start方法来启动run方法
		while(true)
		{
			System.out.println("main thread is running");//run（）时不输出
			Thread.sleep(10);
		}
	}
}
 class TestThread0  	
{
	public void run() 
	{
		while(true)
		{
			System.out.println(" TestThread1 is running");//run（）时仅输出该行
			try {
				Thread.sleep(1000); //1000毫秒
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackT/2race();
			}
		}
	}
} 
//2、main线程可能早于子线程结束，当main线程和子线程都结束时，整个程序才算终止
```

3、实现runnable的对象必须包装在thread类中，才可以启动

不能直接对runnable对象进行start方法。

```java
public class ThreadDemo3
{
	public static void main(String args[])
	{
		//new TestThread3().start();
		//Runnable对象必须放在一个Thread类中才能运行
		TestThread3 tt= new TestThread3();//创建TestThread类的一个实例
		Thread t= new Thread(tt);//创建一个Thread类的实例
		t.start();//使线程进入Runnable状态
		while(true)
		{
			System.out.println("main thread is running");
			try {
				Thread.sleep(1000); //1000毫秒
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
}
class TestThread3 implements Runnable //extends Thread
{
	//线程的代码段，当执行start()时，线程从此出开始执行
	public void run()
	{
		while(true)
		{
			System.out.println(Thread.currentThread().getName() +
			" is running");
			try {
				Thread.sleep(1000); //1000毫秒
			} catch (InterruptedException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
}
```

4、一个线程对象不能多次start，否则报异常

无法指定那个线程对象先执行，完全由JVM操作系统来主导。



**thread类 vs runnable接口**

**thread类占据了父类的名额（单根继承）**

**runnable启动时需要thread类的支持**

**thread类中必须使用static变量，才能实现变量共享**

**对比结论：建议使用runnable接口**

###### **多线程信息共享（细粒度编程模式）**

通过共享变量来达到信息共享

java并不支持点对点的发送消息

``MPI是一个跨语言的通讯协议，用于编写并行计算机。支持点对点和广播。MPI是一个信息传递应用程序接口，包括协议和和语义说明，他们指明其如何在各种实现中发挥其特性。MPI的目标是高性能，大规模性，和可移植性。``

i++，并非原子性操作

`读取主存i（正本）到工作缓存（副本）中`

`每个CPU执行（副本）i+1操作`

`CPU将结果写入缓存（副本）中`

`数据再从缓存（副本）中刷到主存（正本）中`

采用volatile关键字修饰变量

```java
public class ThreadDemo2
{
	public static void main(String args[]) throws Exception 
	{
		TestThread2 t = new TestThread2();
		t.start();
		Thread.sleep(2000);
		t.flag = false;
		System.out.println("main thread is exiting");
	}
}

class TestThread2 extends Thread
{
	//boolean flag = true;   //子线程不会停止
	volatile boolean flag = true;  //用volatile修饰的变量可以及时在各线程里面通知
	public void run() 
	{
		int i=0;
		while(flag)
		{
			i++;			
		}
		System.out.println("test thread3 is exiting");
	}	
} 

```

**关键步骤加锁限制**

互斥：某一个线程运行一个代码段（关键区），其他线程不能同时运行这个代码段 

synchronize（互斥的关键字），修饰代码块，仅允许一个线程进入

性能负担较大

同步：多个线程的运行，必须按照某一种规定的先后顺序来运行 

```java
public class ThreadDemo3 {
	public static void main(String[] args) {
		TestThread3 t = new TestThread3();
		new Thread(t, "Thread-0").start();
		new Thread(t, "Thread-1").start();
		new Thread(t, "Thread-2").start();
		new Thread(t, "Thread-3").start();
	}
}

class TestThread3 implements Runnable {
	private volatile int tickets = 100; // 多个 线程在共享的
	String str = new String("");

	public void run() {
		while (true) {
//			synchronized(str) { 必须用在某一对象上
//				sale();
//			}
			sale();
			try {
				Thread.sleep(100);
			} catch (Exception e) {
				System.out.println(e.getMessage());
			}
			if (tickets <= 0) {
				break;
			}
		}

	}	

	public synchronized void sale() { // 同步函数
		if (tickets > 0) {
			System.out.println(Thread.currentThread().getName() + " is saling ticket " + tickets--);
		}
	
	}
	
//	public void sale() { // 同步函数
//		if (tickets > 0) {
//			System.out.println(Thread.currentThread().getName() + " is saling ticket " + tickets--);
//		}
//	
//	}
	
}
```

###### 多线程管理

等待

通知/唤醒

终止

<img src="C:\Users\buzou\AppData\Roaming\Typora\typora-user-images\1572699857991.png" alt="1572699857991" style="zoom:80%;" />

线程阻塞/唤醒

-sleep

-wait/notify/notifyAll 处于等待阶段的线程需要唤醒

-join，等待另外一个线程结束

-interrupt，向另外一个线程发送中断信号，该线程收到信号后，做下一步处理



多线程死锁

每个线程互相持有别人需要的锁

示例：

```java
import java.util.concurrent.TimeUnit;

public class ThreadDemo5
{
	public static Integer r1 = 1;
	public static Integer r2 = 2;
	public static void main(String args[]) throws InterruptedException
	{
		TestThread51 t1 = new TestThread51();
		t1.start();
		TestThread52 t2 = new TestThread52();
		t2.start();
	}
}

class TestThread51 extends Thread
{
	public void run() 
	{
		//先要r1,再要r2
		synchronized(ThreadDemo5.r1)
		{
			try {
				TimeUnit.SECONDS.sleep(3);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			synchronized(ThreadDemo5.r2)
			{
				System.out.println("TestThread51 is running");
			}
		}
	}
} 
class TestThread52 extends Thread
{
	public void run() 
	{
		//先要r2,再要r1
		synchronized(ThreadDemo5.r2)
		{
			try {
				TimeUnit.SECONDS.sleep(3);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			synchronized(ThreadDemo5.r1)
			{
				System.out.println("TestThread52 is running");
			}
		}
	}
} 

```

`jvisualvm`  功能如下：

1、内存分析

VisualVM 通过检测 JVM 中加载的类和对象信息等帮助我们分析内存使用情况，我们可以通过 VisualVM 的监视标签和 Profiler 标签对应用程序进行内存分析。

在监视标签内，我们可以看到实时的应用程序内存堆以及永久保留区域的使用情况。

2、CPU 分析

VisualVM 能够监控应用程序在一段时间的 CPU 的使用情况，显示 CPU 的使用率、方法的执行效率和频率等相关数据帮助我们发现应用程序的性能瓶颈。我们可以通过 VisualVM 的监视标签和 Profiler 标签对应用程序进行 CPU 性能分析。

在监视标签内，我们可以查看 CPU 的使用率以及垃圾回收活动对性能的影响。过高的 CPU 使用率可能是由于我们的项目中存在低效的代码，可以通过 Profiler 标签的 CPU 性能分析功能进行详细的分析。如果垃圾回收活动过于频繁，占用了较高的 CPU 资源，可能是由内存不足或者是新生代和旧生代分配不合理导致的等。

[详见java visualvm](https://www.ibm.com/developerworks/cn/java/j-lo-visualvm/index.html)



守护线程：

守护线程的结束是run方法运行结束，**或main函数结束**

守护线程不可访问资源（文件或数据库），强制结束时无法释放占用的资源



作业：请分成6个线程，计算m到n的值(以1到100000000为例)的总和。要求每个线程计算的数字量之差不超过1. 

```java
package product;

import java.util.concurrent.CountDownLatch;

public class myThread implements Runnable  {
	int start;
	int end;
	CountDownLatch latch;  
	static int max = 1000000;
	volatile long m = 0;
	volatile long sum = 0 ;
	public static void main(String[] args) {
//		for (int i = 0; i < threads; i++) {
//            //边界条件
//            int fromInt=toMax*i/threads+1;
//            int toInt=toMax*(i+1)/threads;
//            sumThread[i]=new MultisSum(fromInt,toInt);
//            sumThread[i].start();
//        }

		CountDownLatch latch=new CountDownLatch(6);
		myThread t1 = new myThread(1,max*1/6, latch);
		myThread t2 = new myThread(max*1/6+1,max*2/6, latch);
		myThread t3 = new myThread(max*2/6+1,max*3/6, latch);
		myThread t4 = new myThread(max*3/6+1,max*4/6, latch);
		myThread t5 = new myThread(max*4/6+1,max*5/6, latch);
		myThread t6 = new myThread(max*5/6+1,max*6/6, latch);
		new Thread(t1).start();
		new Thread(t2).start();
		new Thread(t3).start();
		new Thread(t4).start();
		new Thread(t5).start();
		new Thread(t6).start();
		
		try {
			latch.await();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println(t1.sum+t2.sum+t3.sum+t5.sum+t4.sum+t6.sum);
		
		
	}
	public myThread(int start,int end,CountDownLatch latch) {
		this.end = end;
		this.start = start;
		this.latch = latch;
	}

	public void run() {
		
		
		for(int i = start;i <=end;i++) {
			m+=i;
		}
		System.out.println(" "+Thread.currentThread().getName()+"  "+m);
		sum();
		try {
			Thread.sleep(1000);
			latch.countDown();
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
	}
	public synchronized void sum() {
			sum += m;
		//System.out.println(sum);
	}
}

```



##### Reference

------

中国大学MOOC--java核心技术（陈育良--华东师范大学）

