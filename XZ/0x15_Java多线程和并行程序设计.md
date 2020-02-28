## 什么是线程

- 一个程序可能包含多个可以同时运行的**任务**。**线程**是指一个任务**从头至尾执行流程**
- 为什么需要多线程：使程序反应更快、交互性更强、执行效率更高
- 在单处理器系统中，多个线程可**共享**CPU时间
- **可运行对象**：在Java中，每个任务都是**Runnable接口**的一个实例，也被称为可运行对象



## 创建任务和线程

- 一个**任务类**必须实现Runnable接口。**任务必须从线程运行**
- 任务就是对象
- 任务必须在线程中执行



- 创建任务

  - 为任务定义一个**实现Runnable**接口的类，并实现它唯一的方法run()

    ```java
    public class TaskClass implements Runnable {
    	
    	public TaskClass() {
    		
    	}
    
    	@Override
    	public void run() {
    		// Tell system how to run custom thread
    
    	}
    
    }
    ```

    

- 创建线程

  - 先创建一个任务，再将它作为参数创建线程，再启动线程

    ```java
    public class Client {
    	...
    	public void someMethod() {
    		...
    		//create an instant of TaskClass
    		TaskClass task = new TaskClass();
    		
    		//create a thread
    		Thread thread = new Thread(task);
    		
    		//start a thread
    		thread.start();
    		...
    	}
      ...
    }
    ```

    

- 训练

  ```java
  public class TaskThreadDemo {
  	
  	public TaskThreadDemo() {
  		
  	}
  	
  	public static void main(String[] args) {
  		TaskThreadDemo demo = new TaskThreadDemo();
  		//create tasks
  		PrintChar pc1 = demo.new PrintChar('a' , 100);
  		PrintChar pc2 = demo.new PrintChar('b' , 100);
  		PrintNum num = demo.new PrintNum(100);
  		
  		//create threads
  		Thread thread1 = new Thread(pc1);
  		Thread thread2 = new Thread(pc2);
  		Thread thread3 = new Thread(num);
  		
  		//start threads
  		thread1.start();
  		thread2.start();
  		thread3.start();
  	}
  	
  	class PrintChar implements Runnable {
  		private char charToPrint; //The character to print
  		private int times; //The number of times to repeat
  		
  		/**Construct a task with a specified character and number of 
  		 * times to print the character
  		 */
  		public PrintChar(char c, int t) {
  			charToPrint = c;
  			times = t;
  		}
  		
  		@Override
  		public void run() {
  			for(int i = 0 ; i < times ; i ++) {
  				System.out.print(charToPrint);
  			}
  		}
  	}
  	
  	class PrintNum implements Runnable {
  		private int lastNum;
  		
  		/** Construct a task for printing 1 to n for a given n */
  		public PrintNum(int n) {
  			lastNum = n ;
  		}
  		
  		@Override
  		public void run() {
  			for(int i = 1 ; i <= lastNum ; i ++) {
  				System.out.print(" " + i);
  			}
  		}
  	}
  
  }
  ```

  

## Thread类

- ```
  +Thread() //创建一个新的线程
  +Thread(task:Runnable) //为指定任务创建一个线程
  +start(): void //开始一个线程导致JVM调用Run()方法
  +isAlive(): boolean //测试线程是否在运行
  +setPriority(p: int): void //为线程指定优先级1<=p<=10
  +join(): void //等待线程结束
  +sleep(millis: long): void //以毫秒为单位让线程睡眠
  +yield(): void //暂停线程，并允许其他线程执行
  +interrupt(): void //终止线程
  ```

- 调用sleep()方法时，要将其放到try-catch块中

- 如果在一个循环中调用了sleep方法，应该将这个循环放在try-catch块中



## 线程池

- 仅需为**一个**任务创建线程，使用Thread。需为**多个**任务创建线程，使用线程池

- Executor接口

  ```java
  +execute(runnable object): void //执行可运行任务
  ```

- ExecutorService接口：Executor的子接口

  ```java
  +shutdown(): void //关闭执行器，允许任务完成，不再接受不了任务
  +shutdownNow(): void //关闭执行器，返回一个未完成任务列表
  +isShutdown(): boolean //执行器关闭，返回ture
  +isTerminated(): boolean //当所有任务终止，返回true
  ```

- Executors类

  ```java
  /**创建一个可以并行运行指定数目线程的线程池。一个线程完成一个任务后可以执行另一个任务*/
  +newFixedThreadPool(numberOfThreads: int): ExecutorService 
  /**创建一个线程池，在必要的时候创建新的线程，有可用线程就用可用线程*/
  +newCachedThreadool(): ExecutorService
  ```

- 练习

  ```java
  public class ExecutorDemo {
  	public static void main(String[] args) {
  		// Create a thread pool which have 3 thread
  		ExecutorService executor = Executors.newFixedThreadPool(3);
  		
  		// Execute tasks
  		TaskThreadDemo task = new TaskThreadDemo();
  		executor.execute(task.new PrintChar('a',100));
  		executor.execute(task.new PrintChar('b',100));
  		executor.execute(task.new PrintNum(100));;
  		
  		// Shut down executor
  		executor.shutdown();
  	}
  }
  ```

  



## 线程同步