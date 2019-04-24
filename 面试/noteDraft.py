一、操作系统与计算机网络
  1.进程与线程：
    a.进程是系统资源分配的最小单位，线程是程序执行的最小单位。进程使用独立的数据空间，而线程共享进程的数据空间。
    b.线程调度：时间片轮转调度、先来先服务调度、优先级调度、多级反馈队列调度、高响应比优先调度
    c.线程切换的步骤：线程上下文切换，以及线程切换的代价(增加资源消耗https://www.cnblogs.com/binyue/p/4484783.html)
    *d.中间件相关：进程间通信IPC
    
  2.Linux常用命令：线上问题排查
    awk、top、netstat、grep、less、tail(https://www.cnblogs.com/ginvip/p/6352157.html)
    
  3.拓展知识点：
    内存屏障、指令乱码、分支预测、CPU亲和性(affinity)、Netfilter与iptables
    
  4.网络知识：
    a.4/7层网络模型(https://blog.csdn.net/qq_21508727/article/details/81074763)
      OSI七层网络模型：物理层、数据链路层、网络层、传输层、会话层、表示层、应用层
      TCP/IP四层网络模型：网络接口层、网间层、传输层、应用层
    b.TCP协议:基于链接(点对点)、双工通信、可靠传输、阻塞控制、基于字节流而非报文
      △三次握手建连、四次握手断连：(https://www.cnblogs.com/cy568searchx/p/4211124.html)三次握手为了建立双向链接、
            洪水攻击(SYN_RCVD):设置linux的TCP参数retry=0，或者加大back
      报文状态标志与链接状态:
      Nagel算法与ACK延迟：产生的背景，解决小包问题提高数据再核比；延迟比较敏感且发送数据频率比较低的情况，可以关闭Nagel算法
      Keepalive：长时间没有数据发送到场景下，TCP保持链接可用的机制。知道开启和设置方式
      滑动窗口与流量控制：如何通过滑动窗口机制进行流量控制的
    c.HTTP协议
      协议：Method、Header、Cookies
      UmEncode
      状态码：200(请求成功)、301(资源/网页等被永久转移到其它URL)、404(请求的资源/网页等不存在)、500(内部服务器错误)
      HTTPS：
      HTTP2：多路复用、Stream、流量控制、服务端推送、头部压缩
    d.UDP：非链接、非可靠性传输、效率高
    e.QUIC(HTTP3):基于UDP，但是提供了类似TCP的可靠性保障和流量控制；
      避免前序包阻塞(HQL阻塞)、零RTT链接、FEC前向纠错
      
二、Java语言特性和设计模式
  1.设计模式：在什么场景下是用什么模式(https://www.cnblogs.com/geek6/p/3951677.html)(https://www.jianshu.com/p/77fcd3e8f9f7)
    单例模式：1.静态初始化(饿汉式)2.双重检查(懒汉式)3.单例注册表
    工厂模式：Spring如何创建Bean
    代理模式：Motan服务的动态代理(https://www.jianshu.com/p/c06a686dae39)
    构造者模式：PB序列化中的Builder
    责任链模式：Neety消息处理方式
    适配器模式：SLF4如何支持Log4J
    观察者模式：GRPC是如何支持流式请求的
    其他模式：
    
  2.java语言特性
    a.数据类型：byte(1字节)、short(2字节)、int(4字节)、long(8字节)、char(2字节[C语言中是1字节]可以存储一个汉字) 
               float(4字节)、double(8字节)、boolean(false/true[理论上占用1bit,1/8字节，实际处理按1byte处理])                     
      空间占用：
      基本数据结构：
      自动转型和强制转型：
      封箱和拆箱：
      
    b.常用集合：掌握集合类如何实现(https://www.cnblogs.com/skywang12345/p/3323085.html)
      HashMap：散列表(非线程安全)(https://www.cnblogs.com/chengxiao/p/6059914.html)(https://segmentfault.com/a/1190000012926722)
        数组加链表的实现方式
        容量大小是2的幂次方的原因、并发读写会有什么风险
        --Map的实现能够考察到数据结构，Java基础实现，以及对并发问题处理思路的掌握程度
        Java的HashMap就是数组加链表实现的，数组中的每一项是一个链表，通过计算存入对象的HashCode来计算对象在数组中要存入的位置，用链表来解决散列冲突，
        链表中的节点存储的是键值对。除了实现的方式，我们还要知道填充因子的作用，与扩容是的rehash机制，需要知道map容量大小是2的幂次方的原因，因为通过
        按位与操作来计算余数，比求模要快。另外HashMap是非线程安全的，在多线程put的情况下，有可能在容量超过填充因子时，进行rehash，因为HashMap为了
        避免尾部遍历，在链表的插入时使用的是头插法，多线程场景下可能会产生死循环。
        rehash:(https://www.jianshu.com/p/13c650a25ed3)
      ConcurrentHashMap：(线程安全)(https://www.cnblogs.com/chengxiao/p/6842045.html)
        并发控制与分段锁思想:降低并发场景下锁定发生频率，1.7和1.8中实现方式比较大
        1.8中的CAS自旋锁(并发量大时效率一般)
      ArrayList:是可以动态增长和缩减的索引序列，是基于数组实现的List类(https://www.cnblogs.com/xujian2014/p/4625346.html)  capacity  iterator
      LinkedList：是一种可以在任意位置高效地插入和移除操作的有序序列，基于双向链表实现的(https://www.cnblogs.com/xujian2014/p/4630785.html)
      HashSet：一个没有重复元素的集合，由HashMap实现的，不保证元素的顺序，允许使用null元素(https://www.cnblogs.com/skywang12345/p/3311252.html)
      HashTree：
      CopyOnWriteArrayList和CopyOnWriteArraySet:CopyOnWrite容器(https://www.cnblogs.com/dolphin0520/p/3938914.html)
      
    c.JUC：(多线程)
      ConcurrentXXX：
      AtomicXXX：
      Executor：
      Caller&&Future：
      Queue：
      Loacks：
      
    d.对象引用：(https://www.cnblogs.com/dolphin0520/p/3592498.html)这些引用在JC的处理策略不同
      (https://blog.csdn.net/sinat_21118695/article/details/82392028)
      强引用：不会被JC回收    强应用使用不当有可能造成内存泄漏(https://cloud.tencent.com/developer/article/1362804)
      软引用：内存空间不足时会被JC回收(https://www.cnblogs.com/dolphin0520/p/3784171.html)
      弱引用：每次JC时都会被回收(https://www.jianshu.com/p/dde92ec37bd1)(http://www.importnew.com/21206.html)(https://www.jianshu.com/p/964fbc30151a)
      虚引用：必须和引用队列ReferenceQueue联合使用，主要用于跟踪一个对象被垃圾回收的过程
      
    e.动态代理与反射：掌握使用场景，ORM框架中大量使用代理类，RPC调用时会使用反射机制，调用实现类的方法；   大量使用会造成性能影响
      JAVA不可变类(immutable)机制与String的不可变性(https://www.cnblogs.com/jaylon/p/5721571.html)
      
      
    f.异常机制：try catch finally机制，需要知道error和Exception的区别 
    
    g.版本差异新特性：
      V1.8：Lambda表达式、Stream API、方法引用、接口默认方法(简化掉简单的抽象类)、
            Metaspace替换PermGem   M不在虚拟机中使用的是本地内存，替换的原因是提升对原数据的处理，提高GC效率，另一方面方便后续合并
      V1.9：模块系统、默认G1回收器、接口私有方法、局部变量推断、Graal编译器
      V1.11：ZGC(大内存堆设置的新的垃圾回收器)、字符串API增强、内建HTTP Client
      
    k.拓展知识点：
      SPI机制：
      注解处理机制
 
三、深入浅出JVM
  1.
  
  
  
四、并发与多线程 (https://www.cnblogs.com/skywang12345/p/java_threads_category.html)
  线程实现：实现Runnable接口、实现Callable接口(返回值通过FutureTask进行封装)、继承Thread类
  
  1.死锁：
    竞争条件与临界区(https://blog.csdn.net/shfqbluestone/article/details/46059879)(https://blog.csdn.net/u010715440/article/details/79503472)
  两个线程访问同一个资源而且与线程访问资源时的顺序有关的这样一种情形就叫竞争条件。(当两个线程访问同一资源时，如果对资源的访问顺序敏感，就称存在竞争条件) 
  导致竞争条件发生的代码片段就叫临界区。在前面的例子中，add() 方法导致了竞争条件的发生，它就是临界区。在临界区中可以通过适当的线程同步来消除竞争条件。
    死锁检测与防止:(https://www.cnblogs.com/lrhya/p/10644506.html)
    产生条件：互斥、请求并持有、非剥夺、循环等待
    
  2.线程通信：主要指线程之间的协作机制，比如wait、notify、notifyAll
  
  3.线程状态转化：new、runnanle、bloacked、time_waiting、waiting、terminated(https://blog.csdn.net/qq_41665476/article/details/80225592)
 
  4.常用工具类(JUC)：
  
  5.机制：java为多线程提供的机制
    a.ThreadLocal:用来保存线程独享的数据(https://www.jianshu.com/p/98b68c97df9b)(https://www.cnblogs.com/dolphin0520/p/3920407.html)
      (https://www.jianshu.com/p/dde92ec37bd1)(https://blog.csdn.net/yezis/article/details/57513130)
    b.Fork/Join:用于大任务的分割与汇总(http://ifeve.com/talk-concurrency-forkjoin/)
    c.Volatile:对多线程数据可见性的保障(https://www.cnblogs.com/dolphin0520/p/3920373.html)
      “观察加入volatile关键字和没有加入volatile关键字时所生成的汇编代码发现，加入volatile关键字时，会多出一个lock前缀指令”
　　  lock前缀指令实际上相当于一个内存屏障（也成内存栅栏），内存屏障会提供3个功能：
　　  1）它确保指令重排序时不会把其后面的指令排到内存屏障之前的位置，也不会把前面的指令排到内存屏障的后面；即在执行到内存屏障这句指令时，
        在它前面的操作已经全部完成；
　　  2）它会强制将对缓存的修改操作立即写入主存；
　　  3）如果是写操作，它会导致其他CPU中对应的缓存行无效。
    d.Interrupt:(https://www.cnblogs.com/skywang12345/p/3479949.html)isInterrupted()、添加标记
      
  6.同步与互斥：
    解决同步与互斥方法： 
      a.CAS CompareAndSwap即比较交换(https://blog.csdn.net/mmoren/article/details/79185862) AtomicStampedReference原子类是一个带有时间戳的对象引用
      b.Synchronized  (https://blog.csdn.net/javazejian/article/details/72828483#synchronized的三种应用方式) synchronized的可重入性
       JVM   Java6后，引入偏向锁和轻量锁自旋锁，性能与Lock持平
      c.Lock(AQS AbstractQueuedSynchronizer)  JDK  带高级功能  
        tryLock()/lockinterruptibly()、RenntrantReadWriteLock()、ReentrantLock()
        (https://www.cnblogs.com/aishangJava/p/6555291.html)(https://blog.csdn.net/qpzkobe/article/details/78586619)
      区别：(1) Lock是一个接口，是JDK层面的实现；而synchronized是Java中的关键字，是Java的内置特性，是JVM层面的实现；
           (2) synchronized 在发生异常时，会自动释放线程占有的锁，因此不会导致死锁现象发生；而Lock在发生异常时，如果没有主动通过unLock()去释放锁，则很可能造成死锁现象，因此使用Lock时需要在finally块中释放锁；
           (3) Lock 可以让等待锁的线程响应中断，而使用synchronized时，等待的线程会一直等待下去，不能够响应中断；
           (4) 通过Lock可以知道有没有成功获取锁，而synchronized却无法办到；
           (5) Lock可以提高多个线程进行读操作的效率。
           在性能上来说，如果竞争资源不激烈，两者的性能是差不多的。而当竞争资源非常激烈时（即有大量线程同时竞争），
           此时Lock的性能要远远优于synchronized。所以说，在具体使用时要根据适当情况选择。
                       
  7.线程池：Executors(https://www.cnblogs.com/dolphin0520/p/3932921.html)
    a.newFixedThreadPool:固定线程数，无界序列，适用于任务数量不均匀的场景、对内存压力不敏感，但系统负载比较敏感的场景   LinkedBlockingQueue(无界队列)
    b.newCacheThreadPool:无限线程数，适用于要求低延迟的短期任务场景                                                SynchronousQueue
    c.newSingleThreadExecutor:单个线程的固定线程池，适用于保证异步执行顺序的场景                                       
    d.newScheduledThreadPool:适用于定期执行任务场景，支持固定频率和固定延迟                                        DelayedWorkQueue
    e.newWorkStealingPool:使用ForkJoinPool，多任务队列的固定并行度，适合任务执行时长不均匀的场景
    THreadPoolExecutor(int corePoolSize,int maximumPoolSize,long keepAliveTime,TimeUnit unit,
                      BlockingQueue<Runnable> workQueue,ThreadFactory threadFactory,RejectedExecutorHandler handler)
    拒绝策略：Abort：丢弃任务并抛出RejectedExecutionException异常。(默认)
             DisCard：也是丢弃任务，但是不抛出异常。
             CallerRuns：丢弃队列最前面的任务，然后重新尝试执行任务（重复此过程）
             DisneycardOldest：由调用线程处理该任务      
                       
五、数据结构与算法 (https://www.cnblogs.com/skywang12345/p/3603935.html)

六、常用工具类
                  
七、必会框架
                       
八、高并发架构的基石-缓存
  缓存是高并发场景下提高热点数据访问性能的有效手段。
  1.缓存的类型：
    a.本地缓存：在进程中的内存中进行缓存,比如JVM堆中。最简单的可以用LRUMap实现，也可以用ehcache工具实现。
                   本地缓存是内存访问，没有远程交互的开销，性能最好。单机容量有限，无法扩展。
    b.分布式缓存：容量可水平扩展
    c.多级缓存:
  2.淘汰策略：(https://www.cnblogs.com/s-b-b/p/6047954.html)
    a.FIFO(先进先出)
    b.LRU(最近最少使用)
    c.LFU(根据历史访问频率)
  3.缓存的问题
    a.缓存更新方式: 数据变更、缓存时效性     同步更新、失效更新，异步更新，定时更新
    b.缓存不一致： 同步更新失败、异步更新    增加重试、补偿任务，最终一致
    c.缓存穿透：   恶意攻击                空对象缓存，bloomFilter过滤器
    d.缓存击穿：   热点key失效             互斥更新、随机退避、差异失效时间
    e.缓存雪崩：   缓存挂掉                快速失败熔断、主从模式、集群模式
    (https://blog.csdn.net/haoxin963/article/details/83245113)
    (https://blog.csdn.net/fanrenxiang/article/details/80542580)
    (https://www.cnblogs.com/zhangweizhong/p/6258797.html)
  4.Memcache:
    a.特点：
       多线程：
       异步IO：
       KV储存：
       内存存储，没有持久化：
    b.内存结构：Slab = Chunk + Page(1M)    Slab初始化:Chunk大小的增长因子，Chunk大小初始值，Page大小
    c.钙化问题：(https://blog.csdn.net/weixin_34247032/article/details/87105559)LRU只会淘汰同一级别的Slab数据
    d.失效和删除机制：设置失效期，采用延迟失效删除
    f.限制：key小于250B、value小鱼1M、过期时间小于30天
 5.Redis:
    a.特点：  
       单线程异步IO：
       支持持久化：
       多数据结构：dictht = key + value + next;
            string:
            hash:
            list:
            set:
            zset:
       主从模式：
    b.功能
      bitmap：用setbit(bitmap)统计上亿访问量活跃用户，可实现bloomfilter
         (https://blog.csdn.net/u011489043/article/details/78990162)(https://www.cnblogs.com/devilwind/p/7374017.html)(https://www.jianshu.com/p/62cf39db5c2f)
      hyperLogLog：大规模数据去重统计，
      geospatial：保存地理位置,位置距离计算，或者根据半径计算位置
      pub/sub：订阅发布功能，用作简单的消息队列
      pipeline：批量执行一组指令，一次性返回全部结果，可减少频繁的请求应答
      lua脚本：
      事物:不是严格的事物，保证串行执行命令，失败不会回滚，继续执行下去
    c.数据持久化 (https://www.cnblogs.com/chenliangcl/p/7240350.html)(https://blog.csdn.net/A_BlackMoon/article/details/85246554)
      AOF:是以文本日志的形式记录redis处理的每一个写入或删除操作。
         AOF对日志文件的写入方式使用追加模式，有灵活的同步策略，支持每秒同步、每次修改同步和不同步；缺点是相同规模的数据集，AOF要大于RDB，AOF要运行效率上要慢与RDB。              
      RDB:在指定时间内将内存中的数据集以快照形式写入磁盘，实际操作是通过fork子进程执行的，采用二进制压缩存储。
         RDB把整个redis数据保存单一文件中，比较适合做灾备，缺点是快照保存完成之前宕机，这段时间的数据将会丢失；另外保存快照是可能会导致服务短时间不可用。
    d.△redis cluster（https://blog.csdn.net/fouy_yun/article/details/81590252）(https://www.cnblogs.com/huangfuyuan/p/9880379.html)
      Sentinel:通过Sentinel哨兵来监控Redis主服务器的状况(https://blog.csdn.net/angjunqiang/article/details/81190562)
               (https://arthur2014.iteye.com/blog/2368657)
      主从同步: 
      master选举:
    f:key失效机制
      主动删除：
      被动善春：
    g:淘汰策略
      voltile-lru:                  
      voltile-all:                 
      voltile-random:                 
      allkeys-lru:                  
      allkeys-all:                 
      allkeys-random: 
      no-eviction:                 
    f.4.0/5.0新特性                       
      Module:
      Stream:
      PSYNC 2.0:
      混合 RD      格式：
                       
                       
九、消息队列Kafka                       
                

                       
