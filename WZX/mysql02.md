- Mysql数据库由后台线程和一个共享内存区组成。共享内存区可以被运行的后台线程所共享。数据库实例才是真正用于操作数据库文件的。

- Mysql被设计成一个单进程多线程的架构的数据库，也就是说，mysql数据库实例在系统中表现的就是一个进程。

- 从概念上来说，数据库是文件的集合，是依照某种数据模型组织起来并存放于二级存储器中的数据集合；数据库实例是程序，是位于用户和操作系统之间的一层数据管理软件，用户对数据库的任何操作，包括数据库定义、数据查询、数据维护、数据库运行控制等都是在数据库实例下运行的，应用程序只有通过数据库实例才能和数据库打交道。

- TCP/IP套接字方式是mysql数据库在任何平台下都提供的连接方式。

- InnoDB存储引擎有多个内存块，可以认为这些内存块组成一个大的线程池，负责以下工作：
1. 维护所有进程/线程需要访问的多个内部数据结构。
2. 缓存磁盘上的数据，方便快速地读取，同时在对磁盘文件的数据修改之前在这里进行缓存。
3. 重做日志缓存。

![](https://raw.githubusercontent.com/bananahab/text/master/docs/%E7%AC%AC%E4%B9%9D%E5%91%A8%E4%BD%9C%E4%B8%9A/image/201.png?token=AKNGWSP3AKU4OFYF6KG6UO25Y7NE4)

- 后台线程的主要作用是负责刷新内存池中的数据，保存内存池中的内存缓存是最近的数据。此外将已修改的数据文件刷新到磁盘文件中，同时保证在数据库发生异常的情况下InnoDB能恢复到正常运行的状态。

- InnoDB存储引擎是基于磁盘存储的，并将其中的方式按照页的方式进行管理。在数据库系统中，由于CPU速度和磁盘速度之间的鸿沟，基于磁盘的数据库系统通常使用缓存池技术来提高数据库的整体性能。

- 在数据库中进行读取页的操作，首先将从磁盘中读取的页存放在缓存池中，这个过程称之为页“FIX”在缓冲池中。下一次再读到相同的页时，首先判断该页是否在缓冲池中。
对于数据库中页的修改操作，则修改在缓冲池中的页，然后再以一定的频率刷新到磁盘中。

- 缓冲池中缓存的数据页类型有：索引页、数据页、undo页、插入缓冲（insert buffer）、自适应哈希索引（adaptive hash index）、InnoDB存储的锁信息（lock info）、数据字典信息（data dictionary）等。

![](https://raw.githubusercontent.com/bananahab/text/master/docs/%E7%AC%AC%E4%B9%9D%E5%91%A8%E4%BD%9C%E4%B8%9A/image/202.png?token=AKNGWSMDMUXF6UH5PRS3LGC5Y7MH2)

- 倘若每次一个页发生变化，就将新页的版本刷新到磁盘，那么这个开销是非常大的。若热点数据集中在某个几页中，那么数据库的性能就变得非常差。同时，如果在从缓冲池将页的新版本刷新到磁盘时发生了宕机，那么数据就不能恢复了。为了避免发生数据丢失的问题，当前事务数据库系统普遍都采用了Write Ahead Log策略，即当事务提交时，先写重做日志，再修改页。当由于发生宕机而导致数据丢失时，通过重做日志来完成数据的恢复。

- 宕机后数据库的恢复时间，当数据库运行了几个月甚至几年，这时发生宕机，重新应用重做日志的时间会非常久，此时恢复的代价也会非常大。
Checkpoint（检查点）技术的目的是解决以下几个问题：
1. 缩短数据库的恢复时间；
2. 缓冲池不够用，将脏页刷新到磁盘；
3. 重做日志不可用，刷新脏页。

- 当数据库发生宕机时，数据库不需要重做所有的日志，因为Checkpiont之前的页都已经刷新回磁盘。故数据库只需要对Checkpoint后的重做日志进行恢复。这样就大大缩短了恢复的时间。
- 此外，当缓冲池不够用时，根据LRU算法会一处最近最少使用的页，若此页为脏页，那么需要强制执行Checkpoint，将脏页也就是页的新版本刷新回磁盘。
重做日志出现不可用的情况是因为当前事务数据库系统对重做日志的设计都是循环使用的，并不是让其无限增大，这从成本及管理上都是比较困难的。重做日志可以被重用的部分是指这些重做日志已经不再需要，即当数据库发生宕机时，数据库恢复操作不需要这部分的重做日志，因此这部分就可以被覆盖重用。若此时重做日志还需要使用，那么必须强制产生Checkpoint，将缓冲池中的页至少刷新到当前重做日志的位置。

#### 索引组织表
- 在InnoDB存储引擎中，表都是根据主键顺序组织存放的，这种存储方式的表称为索引组织表。在InnoDB存储引擎表中，每张表都有个主键，如果在创建表时没有显式地定义主键，则InnoDB存储引擎会按如下方式选择或创建主键：
1. 首先判断表中是否有非空地唯一索引（Unique NOT NULL），如果有，则该列即为主键。
2. 如果不符合上述条件，InnoDB存储引擎自动创建一个6字节大小地指针。
当表中多个非空唯一索引时，InnoDB存储引擎将选择建表时第一个定义地非空唯一索引为主键。

- 从InnoDB存储引擎来看，所有数据都被逻辑地放在一个空间中，称为表空间。表空间又由段、区、页组成。
![](https://raw.githubusercontent.com/bananahab/text/master/docs/%E7%AC%AC%E4%B9%9D%E5%91%A8%E4%BD%9C%E4%B8%9A/image/203.png?token=AKNGWSLIXCRR2JJ5SGRG7YS5Y7NCS)

1. 表空间可以看做是InnoDB存储引擎逻辑结构的最高层，所有的数据都存放在表空间中。
2. 表空间是由各个段组成，常见的段有数据段、索引段、回滚段等；InnoDB存储引擎表是索引组织的，因此数据即索引，索引即数据。那么数据段即为B+树的叶子节点（Leaf node segment），索引段即为B+树的非索引节点。
3. 区是由连续页组成的空间，在任何情况下每个区的大小都为1MB。为了保证区中页的连续性，InnoDB存储引擎一次从磁盘申请4~5个区。在默认情况下，InnoDB存储引擎页的大小为16KB，即一个区中一个由64个连续的页。（在每一段开始时，先用32个页的碎片页来存放数据，在使用完这些页后才是64个连续页的申请）。
4. 页是InnoDB磁盘管理的最小单位，常见的页类型有：数据页、undo页、系统页、事务数据页、插入缓冲位图页、插入缓冲空闲列表页、未压缩的二进制大对象页、压缩的二进制大对象页。
5. InnoDB存储引擎是面向列的，也就是说按行进行存放。

- InnoDB行记录格式：InnoDB存储引擎和大多数数据库一样，记录是以行的形式存储的，这意味着页中保存着表的一行行的数据。

- Compact行记录格式（一个页中存放的行数据越多，其性能就越高）
- Compact行记录格式的首部是一个非NULL变长字段长度列表，若列的长度小于255字节，用1字节表示；若大于255个字节，用2字节表示。
NULL标志位指示了该行数据中是否有NULL值，有则用1表示。
头部信息固定占用5字节
NULL不占用该部分任何空间，即NULL除了占用NULL标志位，实际存储不占用任何空间，另外需要注意的是，每行数据除了用户定义的列外，还有两个隐藏列，事务ID列和回滚指针列，分别为6字节和7字节的大小。若IbboDB表没有定义主键，每行还会增加一个6字节的rowid列。

