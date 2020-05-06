# PHP autoload机制详解

> PHP在魔术函数`__autoload()`方法出现以前，如果你要在一个程序文件中实例化100个对象，那么你必须用include或者require包含进来100个类文件，或者你把这100个类定义在同一个类文件中——相信这个文件一定会非常大。但是`__autoload()`方法出来了，以后就不必为此大伤脑筋了，这个类会在你实例化对象之前自动加载制定的文件。



## 1. autoload机制概述

---

在使用PHP的**OO模式**开发系统时，通常大家习惯上将**每个类的实现都存放在一个单独的文件**里，这样会很容易实现对类进行复用，同时将来维护时也很便利。这也是OO设计的基本思想之一。在PHP5之前，如果需要使用一个类，只需要直接使用include/require将其包含进来即可。下面是一个实际的例子：

```php
/* Person.class.php */
<?php
 class Person {
  var $name, $age;
  
  function __construct ($name, $age)
  {
   $this->name = $name;
   $this->age = $age;
  }
 }
?>

/* no_autoload.php */
<?php
 require_once (”Person.class.php”);
 
 $person = new Person(”Altair”, 6);
 var_dump ($person);
?>
```

在这个例子中，no-autoload.php文件需要使用Person类，它**使用了require_once将其包含**，然后就可以直接使用Person类来实例化一个对象。

但随着项目规模的不断扩大，使用这种方式会带来一些隐含的问题：如果一个PHP文件需要使用很多其它类，那么就需要很多的require/include语句，这样有可能会造成遗漏或者包含进不必要的类文件。如果大量的文件都需要使用其它的类，那么要保证每个文件都包含正确的类文件肯定是一个噩梦。

PHP5为这个问题提供了一个解决方案，这就是类的**自动装载(autoload)**机制。autoload机制可以使得PHP程序有可能在**使用类时**才自动包含类文件，而不是一开始就将所有的类文件include进来，这种机制也称为**lazy loading**。

下面是使用autoload机制加载Person类的例子：

```php
/* autoload.php */
<?php
 function __autoload($classname)
{
  $classpath="./".$classname.'.class.php';
  if(file_exists($classpath))
  {
      //当文件存在时，使用require_once加载该文件
    require_once($classpath);
  }
  else
  {
    echo 'class file'.$classpath.'not found!';
   }
}
 
 $person = new Person(”Altair”, 6);
 var_dump ($person);
 ?>
```

通常PHP5在使用一个类时，如果发现这个类没有加载，就会自动运行__autoload()函数，在这个函数中我们可以加载需要使用的类。在我们这个简单的例子中，我们直接将类名加上扩展名”.class.php”构成了类文件名，然后使用require_once将其加载。从这个例子中，我们可以看出autoload至少要做三件事情，

1. 第一件事是根据类名确定类文件名，
2. 第二件事是确定类文件所在的磁盘路径(在我们的例子是最简单的情况，类与调用它们的PHP程序文件在同一个文件夹下)，
3. 第三件事是将类从磁盘文件中加载到系统中。

第三步最简单，只需要使用include/require即可。要实现第一步，第二步的功能，必须在开发时约定类名与磁盘文件的映射方法，只有这样我们才能根据类名找到它对应的磁盘文件。

因此，当有大量的类文件要包含的时候，我们只要确定**相应的规则**，然后在`__autoload()`函数中，将类名与实际的磁盘文件对应起来，就可以实现lazy loading的效果。从这里我们也可以看出`__autoload()`函数的实现中最重要的是类名与实际的磁盘文件映射规则的实现。

但现在问题来了，如果在一个系统的实现中，如果需要使用很多其它的类库，这些类库可能是由不同的开发人员编写的，其类名与实际的磁盘文件的映射规则不尽相同。这时如果要实现类库文件的自动加载，就必须在`__autoload()`函数中将所有的映射规则全部实现，这样的话`__autoload()`函数有可能会非常复杂，甚至无法实现。最后可能会导致`__autoload()`函数**十分臃肿**，这时即便能够实现，也会给将来的维护和系统效率带来很大的负面影响。在这种情况下，难道就没有更简单清晰的解决办法了吧？答案当然是：NO! 在看进一步的解决方法之前，我们先来看一下PHP中的autoload机制是如何实现的。



## 2. PHP的autoload机制的实现

---

我们知道，PHP文件的执行分为两个独立的过程

1. 第一步是将PHP文件编译成普通称之为OPCODE的字节码序列（实际上是编译成一个叫做zend_op_array的字节数组）
2. 第二步是由一个虚拟机来执行这些OPCODE。

PHP的所有行为都是由这些OPCODE来实现的。因此，为了研究PHP中autoload的实现机制，我们将autoload.php文件编译成opcode，然后根据这些OPCODE来研究PHP在这过程中都做了些什么:

```php
 /* autoload.php 编译后的OPCODE列表，是使用作者开发的OPDUMP工具
     * 生成的结果，可以到网站 http://www.phpinternals.com/ 下载该软件。
     */
    1: <?php
    2:  // require_once (”Person.php”);
    3:  
    4:  function __autoload ($classname) {
            0  NOP                
            0  RECV                1
    5:   if (!class_exists($classname)) {
            1  SEND_VAR            !0
            2  DO_FCALL            ‘class_exists’ [extval:1]
            3  BOOL_NOT            $0 =>RES[~1]     
            4  JMPZ                ~1, ->8
    6:    require_once ($classname. “.class.php”);
            5  CONCAT              !0, ‘.class.php’ =>RES[~2]     
            6  INCLUDE_OR_EVAL     ~2, REQUIRE_ONCE
    7:   }
            7  JMP                 ->8
    8:  }
            8  RETURN              null
    9:  
   10:  $p = new Person(’Fred’, 35);
            1  FETCH_CLASS         ‘Person’ =>RES[:0]     
            2  NEW                 :0 =>RES[$1]     
            3  SEND_VAL            ‘Fred’
            4  SEND_VAL            35
            5  DO_FCALL_BY_NAME     [extval:2]
            6  ASSIGN              !0, $1
   11:  
   12:  var_dump ($p);
            7  SEND_VAR            !0
            8  DO_FCALL            ‘var_dump’ [extval:1]
   13: ?>
```

在autoload.php的第10行代码中我们需要为类Person实例化一个对象。因此autoload机制一定会在该行编译后的opcode中有所体现。从上面的第10行代码生成的OPCODE中我们知道，在实例化对象Person时，首先要执行**FETCH_CLASS**指令。我们就从PHP对FETCH_CLASS指令的处理过程开始我们的探索之旅。



 通过查阅PHP的源代码(我使用的是PHP 5.3alpha2版本)可以发现如下的调用序列： 

```
ZEND_VM_HANDLER(109, ZEND_FETCH_CLASS, …) (zend_vm_def.h 1864行)
 => zend_fetch_class (zend_execute_API.c 1434行)
  =>zend_lookup_class_ex (zend_execute_API.c 964行)
   => zend_call_function(&fcall_info, &fcall_cache) (zend_execute_API.c 1040行)
```

 在最后一步的调用之前，我们先看一下调用时的关键参数： 

```
 /* 设置autoload_function变量值为”__autoload” */
 fcall_info.function_name = &autoload_function;  // Ooops, 终于发现”__autoload”了
 …
 fcall_cache.function_handler = EG(autoload_func); // autoload_func !
```

**Zend_call_function**是Zend Engine中最重要的函数直一，其主要功能式执行用户在PHP程序中自定义的函数或PHP本身的库函数。Zend_call_function有两个重要的指针型参数`fcall_info``fcall_cache`,它们分别指向两个重要的结构，一个是zend_fcall_info，另一个是zend_fcall_info_cache. 

zend_call_function的主要工作流程如下：

- 如果fcall_cache.function_handler指针为NULL，则尝试查找函数名为fcall_info.function_name的函数，如果函数存在，则执行之。
- 如果fcall_cache.function_handler不为NULL，则直接执行fcall_cache.function_handler指向的函数

> 在上面的opcode中，我们可以看到autoload_func()

现在我们清楚了，PHP在实例化一个对象时（实际上在实现接口、使用类常数或类中的静态变量、调用类中的静态方法时都会如此），首先会在系统（内存）中查找该类（或接口）是否存在，如果不存在，尝试使用autoload机制来加载该类。而autoload机制的主要执行过程为：

1. 检查执行器全局变量函数指针autoload_func是否为NULL

   - 如果**autoload_func==NULL**，则查找系统中是否定义有__autoload()函数，
     - 如果程序员没有定义__autoload()函数，则说明当前确实是执行到一个错误的代码，为定义的类被初始化了。
     - 如果定义了`__autoload()`函数，说明程序员可能是在写框架，就执行 `__autoload()`尝试加载类，并返回加载结果

   - 如果autoload_func不为NULL，则直接执行autoload_func指针指向的函数用来加载类。注意此时就不检查是否定义了`__autoload()`函数

     > 个人认为autoload_func其实就是被加载到内存中的某个类的信息结构。

   

真相终于大白，PHP提供了两种方法来实现自动装载机制

- 一种我们前面已经提到过，是使用用户定义的__autoload()函数，这通常在PHP源程序中来实现；
- 另外一种就是设计一个函数，将autoload_func指针指向它，这通常使用C语言在PHP扩展中实现。

如果既实现了__autoload()函数，又实现了autoload_func(将autoload_func指向某一PHP函数)，那么只执行autoload_func函数。



## 3. SPL autoload机制的实现

---

SPL是Standard PHP Library(标准PHP库)的缩写。它是PHP5引入的一个扩展库，其主要功能包括autoload机制的实现及包括各种Iterator接口或类。

SPL autoload机制的实现是通过**将函数指针autoload_func指向自己实现的具有自动装载功能的函数来实现的**。SPL有两个不同的函数spl_autoload, spl_autoload_call，通过将autoload_func指向这两个不同的函数地址来实现不同的自动加载机制。

spl_autoload时SPL实现的默认的自动加载函数，它的功能比较简单。它可以接受两个参数

- class_name，表示类名
- file_extensions 是可选的表示类文件的扩展名

可以在file_extensions中指定多个扩展名，扩展名之间使用分号隔开即可；如果不指定的话，它将使用默认的扩展名`.inc`或`.php`。

spl_autoload首先将class_name变为小写，然后在所有的include_path中搜索class_name.inc或class_name.php文件（如果不指定file_extensions参数的话），如果找到，就加载该类文件。

你可以使用spl_autoload("Person",".class.php")来加载Person类。实际上，它跟require/include差不多，不同的是它可以指定多个扩展名。

```php
//A.php
class A{
    public static function hello(){
        echo "Hello";
    }
}
   
//B.php
/*直接实例化A类，一定报错*/
$a=new A(); 

/*使用require或include将A.php引入；没问题*/
require "A.php";
$a=new A();

/*使用spl_autoload()加载A.php文件；没问题*/
//指定文件名+后缀
spl_autoload("A",".php")
$a=new A();
    
```

通过上面的说明我们知道，spl_autoload的功能比较简单（相当于就是个升级版本的require/include，还是要自己手动的引入文件）。而且它是在SPL扩展中实现的，我们无法扩充它的功能。如果想实现自己的更灵活的自动加载机制怎么办呢？这时，**spl_autoload_call**函数闪亮登场了。

我们先看一下spl_autoload_call的实现有何奇妙之处。在SPL模块内部，有一个全局变量autoload_functions，它**本质上是一个HashTable**，不过我们可以将其简单的看作一个链表，链表中的**每一个元素都是一个函数指针**,指向一个**具有自动加载类功能**的函数。spl_autoload_call本身的实现很简单，只是简单的按顺序执行这个链表中每个函数，在每个函数执行完成后都判断一次需要的类是否已经加载，如果加载成功就直接返回，不再继续执行链表中的其它函数。如果这个链表中所有的函数都执行完成后类还没有加载，spl_autoload_call就直接退出，并不向用户报告错误。因此，使用了autoload机制，并不能保证类就一定能正确的自动加载，关键还是要看你的自动加载函数如何实现。

> spl_autoload_call是个函数，由**autoload_func**指向。这个 **autoload_func**就是当实例化未引入的类时，被调用的函数。
>
> 原先来说，autoload_func指向的是`__autoload()`函数
>
> 但是现在变成指向spl_autoload_call() 函数了
>
> 该函数的主要功能是，在实例化未引入的类时，依次调用autoload_functions中的自动加载函数，直到该类被顺利引入。

那么自动加载函数链表autoload_functions是谁来维护呢？就是前面提到的spl_autoload_register函数。它可以将用户定义的自动加载函数注册到这个链表中，并将autoload_func函数指针指向spl_autoload_call函数（注意有一种情况例外，具体是哪种情况留给大家思考）。我们也可以通过spl_autoload_unregister函数将已经注册的函数从autoload_functions链表中删除。

> 就是说，使用spl_autoload_register函数，将自定义的自动加载函数注册到autoload_functions这个链表中。在实例化类对象时，如果从已有的内存中找不到该类（未使用require/include加载进来）spl_autoload_call会依次调用autoload_functions链表中的每个自定义自动加载函数，直到我所需要的类被加载进来。
>
> 注意优先级：如果要实例化的类已经在内存中了（已经引入了），就直接调用。不存在时，在进行自动加载工作。

上节说过，当autoload_func指针非空时，就不会自动执行`__autoload()`函数了，现在autoload_func已经指向了spl_autoload_call，如果我们还想让`__autoload()`函数起作用应该怎么办呢？当然还是使用`spl_autoload_register(__autoload)`调用将它注册到autoload_functions链表中。

```php
/*使用spl_autoload_register函数将一个函数注册为autoload函数*/
//自定义autoload函数
function auto(){
    include "A.php";
}
//将该自定义函数注册到spl_autoload_functions这个类似于链表中
//该链表由 spl_autoload_call()函数操作
//此时系统的 autoload_func就指向了sql_autoload_call()函数。当实例化未引入的类时，就调用spl_autoload_call()函数，一个个执行自定义的自动加载函数。
spl_autoload_register("auto")
$a=new A();
```

现在回到第一节最后的问题，我们有了解决方案：根据**每个类库不同的命名机制**实现各自的自动加载函数，然后使用spl_autoload_register分别将其注册到SPL自动加载函数队列中就可了。这样我们就不用维护一个非常复杂的__autoload函数了。



![](https://ocean-oss.oss-cn-beijing.aliyuncs.com/img/20200428212531.png)



## 4. autoload效率问题及其对策

---

使用autoload机制时，很多人的第一反应就是使用autoload会降低系统效率，甚至有人干脆提议为了效率不要使用autoload。在我们了解了autoload实现的原理后，我们知道**autoload机制本身并不是影响系统效率**的原因，甚至它还有可能提高系统效率，因为它不会将不需要的类加载到系统中。

那么为什么很多人都有一个使用autoload会降低系统效率的印象呢？实际上，影响autoload机制效率本身恰恰是用户设计的自动加载函数。如果它不能**高效的将类名与实际的磁盘文件**(注意，这里指实际的磁盘文件，而不仅仅是文件名)对应起来，**系统将不得不做大量的文件是否存在的判断**(需要在每个include path中包含的路径中去寻找)，而判断文件是否存在需要做磁盘I/O操作，众所周知磁盘I/O操作的效率很低，因此这才是使得autoload机制效率降低的罪魁祸首!

因此，我们在系统设计时，需要**定义一套清晰的将类名与实际磁盘文件映射的机制**。这个规则越简单越明确，autoload机制的效率就越高。



## 5.总结

---

```
__autoload实现自动加载;
但由于多类库的引入，__autoload维护会复杂，则引入spl_autoload,spl实现了一个自动加载函数列表的手动注册和移除
```

还有：如果一个类已经通过spl_autoload_register()所定义的自动加载函数被引入，下次再实例化该类时，就无需再重新调用自动加载函数了。所以本质上来说，自动加载函数其实就是实现了 include 效果。