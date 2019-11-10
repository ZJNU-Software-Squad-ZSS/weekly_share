## Redis服务器安装、配置、使用

#### 安装命令：

```
$ wget http://download.redis.io/releases/redis-2.8.17.tar.gz 下载源码安装包
$ tar xzf redis-2.8.17.tar.gz		解压安装包
$ cd redis-2.8.17	进入安装包
$ make	开始安装
$ ll src/redis* 查看redis安装好的二进制文件（主要是redis-cli和redis-server ）
$ make install 把生成的二进制文件放到/usr/local/bin下，相当于放进了环境变量中。
$ which redis-server 查看redis-server的位置
```

#### 启动服务：

```
1. 通常redis-server 后面要加上redis.conf配置文件来启动服务。例如：redis-server {配置文件的位置}
2. 在解压好的文件夹里有个默认的配置文件样板 redis.conf 。vim redis.conf。修改 daemonize 为yes 表示后台启动。修改port 为其他端口号（7200）隐藏默认的6379端口，增加安全性
3. 启动：redis-server redis.conf
4. 确定一下redis-server是否启动 ps aus|grep redis-server
可以看到正常启动且端口号为7200。
```

#### 使用redis-cli来操作Redis

```
1. which redis-cli 看一下机器上redis-cli在哪儿，是否已安装
2. 登陆：redis-cli  发现登陆不了，原来redis-cli默认登陆的是本机6379端口，而前面我们已经进行了修改。
3. redis-cli --help  发现登陆远程的服务要用到-h(host) -p(port)。于是就直接 redis-cli -h 127.0.0.1 -p 7200。就成功登陆了。127.0.0.1:7200> 
4. 登陆后 info命令 查看redis-server的当前状态。可以看到redis-server的版本、端口号、使用的配置信息···
```

![1538989228023](C:\Users\郑江\AppData\Local\Temp\1538989228023.png)

#### String类型操作

```
1. 设置字符串：set string1 zhengjiang //把string1赋值为zhengjiang 。
2. 取出字符串：get string1 //获取string1 中储存的字符串
3. 对整数操作：set string2 4 //string2 赋值为4
4. 自增操作：incr string2 //把string2所对应的整数自增
    get string2  => "5"  //就变成5了
5. 减2操作：deceby string2 2  //把string2对应的值减少2
   get string2  =>"3"  //变成3了
6. 加2操作：incrby string2 2 //把String2对应的值加2
   get string2 => "5"  //变成5了
7. 删除：del {key}
  
重点：设置失效时间 setex {key} {失效时间/秒} {value}
      setex ocean 12 "海洋"  //设置ocean的值为“海洋” ，从命令生效起12秒内有效，超过12秒，get ocean  就get不到了
```

#### list类型操作

```
就是队列了，有push（压入） pop（抛出），单数这里有左右之分。不要求集合内的元素唯一。
左：lpush lpop 
右：rpush rpop
像一根管子一样，左面先压入的，右边就先弹出

lpush list1 12   //往列表list1中左压入12
lpush list1 13   //再次左压入
rpop list1 =>"12"  //右面弹出为先压入的 12

llen list1 =>"1"  //列出list1中的元素个数，现在只剩下一个了
```

#### set类型操作

```

提供了无序的方式来存储多个不同的元素（注意：有唯一性，要求不同的元素）

1. 往set中插入元素：sadd set1 12  //插入一个12 到集合set1中
2. 查看集合元素个数：scard set1 =>(interger)1  
3. 查看某个值是否在集合里面：sismember set1 13 =>(interger) 0 //看13在不在set1里面，返回0 表示不在。返回 1 表示在。
4. 从集合中删除某个元素：srem set1 12 
```

#### hash类型操作

```
哈希是个散列类型，让用户能多个键值对存储到一个Redis键里面去
键值对的键不一样那就是不同的条数

1.往hash结构里面插入键值对：hset hash1 key1 12 //往hash1结构中插入键位 key1 值为 12 的一个键值对
2. 获取某个hash结构里面的键所对应的值：hget hash1 key1 =>"12" //在hash1 里面获取键为 key1 的键值对的值
3. 获取结构中的元素个数：hlen hash1 =>(integer) 1 
4. 根据键修改其值：hset hash1 key1 14  //把hash1 中的key1对应的值修改为14,感觉就是重新赋值了
5. 一次性获取多个key所对应的值：hmget jash1 key1 key2
```

#### sort set类型操作

```
这个类型hash 类型其实很相似,都是存储映射关系。不同的是，在这个类型中，储存的是 分数（score）->值(value) ,这个分数是浮点型的。这个类型主要是用来排序，依照分数sore，排序rank。需要注意的是，这里的value和集合类型一样是全局唯一的。
eg:zadd zset 10.1 val1
   zadd zset 9.1 val1  //这边val1的score先为10.1 ，第二次有又值为9.1，那么前一条10.1 的数据就不存在了。
但是可以有两条数据的score是一样的，这样排序就按照value的字典顺序来排序。
这个数据类型，感觉就是集合类型加上了个score，来进行排序。

1.添加元素 zadd zset1 10.1 val1
2.获取元素个数 zcard zset1
3.排序：zrange zset1 0 10 WITHSCORES //取前十个数据出来，下标0-10，后面的withscores表示把数据的scores也取出来。这个排名，scores越小的排在越上面
4. 获取某个值的具体排名：zrank zset val2 //获取在zset中val2的排名
```

## PHP操作Redis

#### PHP Redis扩展安装

```
1. php -m 查看有没有安装php Redis扩展
2. yum install php-devel 安装php扩展开发包（包括了phpize和php-config Redis所需要的扩展包）
3. which phpize ;which php-config;查看扩展包的安装位置

[安装教程]{https://segmentfault.com/a/1190000009422920}
```



```php
<?php
$redis=new \Redis();
$redis->connect('127.0.0.1',6379);

$redis->delete('set1');

$redis->sadd('set1',"A");
$redis->sadd('set1',"B");
$redis->sadd('set1',"C");
//集合的元素唯一性，两次插入C 只存入一次
$redis->sadd('set1',"C");

//获取集合中元素个数
$num=$redis->sCard("set1");
echo $num;

//获取集合中所有的元素（数组的格式）
//要是不存在就返回false
var_dump($redis->sMembers("set1"));

?>

```

