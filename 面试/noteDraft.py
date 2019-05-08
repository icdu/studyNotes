(https://www.cnblogs.com/koubeisi/p/10751035.html)

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
          (https://www.cnblogs.com/123hll/p/5805040.html)(https://blog.csdn.net/hezh1994/article/details/78899683)
      空间占用：
      基本数据结构：
      自动转型和强制转型：
      封箱和拆箱：
      
    b.常用集合：掌握集合类如何实现(https://www.cnblogs.com/skywang12345/p/3323085.html)
      HashMap：散列表(非线程安全)(https://www.cnblogs.com/chengxiao/p/6059914.html)(https://segmentfault.com/a/1190000012926722)
        数组加链表的实现方式(http://www.importnew.com/31278.html)
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
      注解处理机制:
 
三、深入浅出JVM  (https://segmentfault.com/a/1190000014395186)(https://blog.csdn.net/qq_41701956/article/details/81664921)
  1.内存模型:运行时的数据区(作用和保存哪些数据)  HotSpot  (https://www.cnblogs.com/qingshanli/p/9256387.html)
    a.程序计数器(Program Counter Register):指向当前线程正在执行的字节码指令。
      线程私有   
    b.方法区(Method Area):用于存储已被虚拟机加载的类信息、常量、静态变量、即时编译后的代码等数据。
      线程共享
    c.堆(Heap): Java对象存储的地方。超出时OOM
      线程共享          
    d.虚拟机栈(VM Stack):Java执行方法的内存模型。每个方法被执行的时候，都会创建一个栈帧，把栈帧压人栈，当方法正常返回或者抛出未捕获的异常时，栈帧就会出栈。  
      线程私有 
    e.本地方法栈(Native Method Stack):调用本地native的内存模型
      线程私有
      
    JMM(Java Memory Model)和内存可见性：
      原子性：基本数据类型读或写(long、double除外)、synchronized
      可见性：synchronized、volatile
      有序性：volatile、happens-before原则
    
  2.类加载：(https://mp.weixin.qq.com/s/CrLdjROqKSe3iv-YZ751Ug)
    a.概念：类加载器把class文件中的二进制数据读入到内存中，存放在方法区，然后在堆区创建一个java.lang.Class对象，用来封装类在方法区内的数据结构。
      加载-》连接-》初始化-》使用-》卸载
             ||
      验证-》准备-》解析
    b.双亲委派模式:
      Bootstrap类加载器:启动类加载器 <JAVA_HOME>/lib
      Extension类加载器:扩展类加载器 <JAVA_HOME>/lib/ext
      System类加载器:系统/应用加载   java - classpath
      自定义类加载器:Custom ClassLoader
  
  3.GC   (https://baijiahao.baidu.com/s?id=1605937053950156833&wfr=spider&for=pc)
    a.分代回收:
      年轻代: Eden + Survivor1 + Survivor2
      老年代: Tenured
      持久代: PermGen/Metaspace     保存类信息等内容
      
      Minor GC:当Eden区满时，触发Minor GC。
      Major GC/Full GC：
            (1)调用System.gc时，系统建议执行Full GC，但是不必然执行
            (2)老年代空间不足
            (3)方法去空间不足
            (4)通过Minor GC后进入老年代的平均大小大于老年代的可用内存
            (5)由Eden区、From Space区向To Space区复制时，对象大小大于To Space可用内存，
              则把该对象转存到老年代，且老年代的可用内存小于该对象大小
        
    b.回收器实现：(思路和适合场景)
      串型回收器:
      并行回收器:
      CMS算法:属于标记清除算法，JDK1.7以前的主流算法，并发收集，停顿小
      G1算法：年轻代回收(并行复制STW)+老年代回收(初始标记STW、并发标记、最终标记STW、复制/清除STW)   逻辑分代
      GC:
      ZGC:针对大内存堆的低延迟垃圾回收算法(着色指针、读屏障、并发处理、基于Region、内存压缩[整理])
    
    Mark-Sweep（标记-清除算法）：
          思想：标记清除算法分为两个阶段，标记阶段和清除阶段。标记阶段任务是标记出所有需要回收的对象，清除阶段就是清除被标记对象的空间。
           优缺点：实现简单，容易产生内存碎片。
    Copying（复制清除算法）：
          思想：将可用内存划分为大小相等的两块，每次只使用其中的一块。当进行垃圾回收的时候了，把其中存活对象全部复制到另外一块中，然后把已使用的内存空间一次清空掉。
          优缺点：不容易产生内存碎片；可用内存空间少；存活对象多的话，效率低下。
    Mark-Compact（标记-整理算法）：
          思想：先标记存活对象，然后把存活对象向一边移动，然后清理掉端边界以外的内存。
          优缺点：不容易产生内存碎片；内存利用率高；存活对象多并且分散的时候，移动次数多，效率低下。
    分代收集算法：（目前大部分JVM的垃圾收集器所采用的算法）：    
          思想：把堆分成新生代和老年代。（永久代指的是方法区）
        （1）因为新生代每次垃圾回收都要回收大部分对象，所以新生代采用Copying算法。新生代里面分成一份较大的Eden空间和两份较小的Survivor空间。
            每次只使用Eden和其中一块Survivor空间，然后垃圾回收的时候，把存活对象放到未使用的Survivor（划分出from、to）空间中，清空Eden和刚才使用过的Survivor空间。
        （2）由于老年代每次只回收少量的对象，因此采用mark-compact算法。
        （3）在堆区外有一个永久代。对永久代的回收主要是无效的类和常量
  4.性能调优
    a.JVM参数:
    b.性能分析工具
      MAT:
      JMC:
      JStack:
      JStat:
        
  5.执行模式
    a.解释模式:
    b.编译模式:
    c.混合模式:
  
  6.编译器优化
    a.公共子表达式的消除:
    b.指令重排:
    c.内联:
    d.逃逸分析:
      方法逃逸:
      线程逃逸:
    e.栈上分配:
    f.同步消除:
  
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
 数据结构：
  1.队列：先进先出
  2.栈：先进后出
  3.表
    a.数组
    b.单链表
    c.双链表
    d.循环链表
    e.散列表
  4.图:适用于路由算法  掌握深度遍历、广度遍历
    a.有向图
    b.无向图
    c.带权图
  5.多叉树
    a.B、B+树:  适合用于文件检索
    b.字典树: 适合用于字符串的多模匹配
  6.二叉树：适合用于数据的查找和排序  要求了解二叉树的构建、删除、插入操作的实现，前中后遍历(https://www.cnblogs.com/manji/p/4903990.html)
    a.平衡二叉树
    b.红黑树
    c.哈夫曼树
    d.堆

  算法：
  1.常见算法思路：
    a.分治
    b.动态规划
    c.贪心
    d.回溯
    e.分支界定
  2.复杂度：
    a.时间复杂度
    b.空间复杂度
  3.排序
    a.插入
      希尔排序：
      直插排序：
    b.交换
      冒泡排序：
      快速排序△：
    c.选择
      简单选择排序：
      堆排序△：
    d.归并
    e.基数
  4.查找:
    a.二分查找：适合小数量集内存查找
    b.二叉排序树：
    c.B树：适合文件索引
    d.Hash：常数级的时间复杂度，更适合查找效率更高的场合
    e.BloomFilter：适合对大数据集进行数据存在性过滤
  5.字符串匹配
    a.BF算法
    b.BM算法
    c.Sunday算法
    d.KMP算法
    e.Tire算法
                       
六、常用工具类：
                  
七、必会框架：
  1.Spring
    a.Spring Framework：IOC、AOP、依赖注入、Context上下文、Bean管理、SpringMVC
    b.Spring Boot：简化Spring应用的创建、开发与部署， 简化配置文件，使用嵌入式web服务，还有诸多开箱即用的微服务功能，可以与SpringCloud联合部署。
        核心思想是约定大于配置，应用只需要极少的配置即可，简化了应用开发模式。               
    c.Spring Data：是数据访问和操作的工具集。封装了对多种数据源的操作能力，包括JDBC、Redis、MongoDB等。
    d.Spring Cloud：是完整的微服务解决方案，是一系列不同功能微服务的集合。基于SpringBoot，简化了分布式系统的开发，集成了服务发现、配置管理、
         消息总线、负载均衡、断路器、数据监控等各种服务治理能力。
      1).Sleuth：提供了全链路追踪能力
      2).Netflix：提供了熔断器、作用网关等众多的治理组件
      3).Config：提供了动态配置能力
      4).Bus：支持了RabbitMQ、Kafka、ActiveMq消息队列，实现分布式服务之间的事件通信
      5).Security：用于快速的构建安全的应用程序和服务    
   
    Spring Boot+Cloud可以实现常见安全模型，比如单点登录、令牌中继、令牌交换等
    
    SpringMVC工作原理详解：(https://mp.weixin.qq.com/s/_uPJiTdgd1sIlHvhBfcQcg)
    
    详解：
    1）Spring IOC与AOP:Dependecy Injection/Inversion of Control(https://www.cnblogs.com/xdp-gacl/p/4249939.html)(https://www.cnblogs.com/superjt/p/4275462.html)
      Java 反射：说的是在运行状态中，对于任何一个类，我们都能够知道这个类有哪些方法和属性。(https://baijiahao.baidu.com/s?id=1619748187138646880&wfr=spider&for=pc)
      AOP:  
          静态代理：在编译时进行织入，或者类加载时进行织入，比如aspectJ。
          动态代理：运行时增强，比如JDK代理
      PlaceHolder动态替换：PropertyPlaceholderConfigurer/PropertySourcesPlaceholderConfigurer(https://www.cnblogs.com/leftthen/p/5615066.html)  
      事物：(https://mp.weixin.qq.com/s/5KUo4CpizFZsirsInSn5Jw)
          隔离级别：事物的隔离级别是由具体数据库实现的
          传播类型：PROPAGATION_REQUEST、PROPAGATION_SUPPORTS(https://blog.csdn.net/weixin_38070406/article/details/78157603)
      核心借口/类：
          ApplicaationContext:保存IOC整个应用上下文，通过其中的beanfactory获得任意bean
          BeanFactory:主要作用是通过bean的描述来创建具体的bean
          BeanWrapper:是对bean的包装，一般情况下是在SpringIOC的内部使用，提供了访问bean的属性值、属性编辑器注册、类型转换等功能，方便IOC容器用统一的方式访问bean的属性。
          FactoryBean:通过getObject()方法返回实际的bean对象
      scope作用域:Singleton(默认)、Prototype、Request、Seesion、Global-Session、Application、Websockert(https://www.cnblogs.com/dyppp/p/7397290.html)
      事件机制：ContextRefreshEvent、ContextStartedEvent、ContextStoppedEvent、ContextCloseEvent、RequestHandledEvent
      
      阅读源码： 
      Spring Context初始化流程：(https://blog.csdn.net/u010209217/article/details/80828067)
           AbstractAC.refresh()<---ClassPathXmlAC、SpringAC、WebAC
           1).prepareRefresh():对刷新进行准备，包括设置开始时间、激活状态、初始化Context环境中的占位符。这个动作根据子类需求由子类执行，然后
                    验证是否确实必要的prepareRefresh。
           2).ConfigurableListableBeabFactory beanfactory = obtainFreshBeanFactory():刷新并获取内部的beanfactory
           3).prepareBeanFactory(beanfactory):对beanfactory进行准备工作，比如设置类加载器和后置处理器，配置不能自动装配的数据类型，注册
                    默认的环境bean。
           4).postProcessBeanFactory(beanfactory):为context的子类提供后置处理beanfactory的扩展能力，如果子类想要在bean定义加载完成后，
                    开始初始化上下文之前做一些特殊逻辑，写覆写这个方法。
           5).invokeBeanFactoryPostProcess(beanfactory):执行context中注册的beanfactory后置处理器。有两种后置处理器，一种可注册bean
                    的后置处理器，另一种是针对beanfactory进行处理的后置处理器。执行的顺序是先按优先级执行可注册bean的处理器，然后再按优先级
                    执行针对beanfactory进行处理的后置处理器。
                  对于SpringBoot来说，这一步会进行注解BeanDefinitions的解析，流程如下：
                    ConfigurationClassPostProcessor触发->ConfigurationClassParser->ClassPathBeanDefinitionScanner解析
           6).registerBeanPostProssors(beanfactory): 按优先级顺序在beanfactory中注册bean的后置处理器，bean的后置处理器可以再bean初始化
                    的前后进行处理。
           7).initMesageSource(): 初始化消息源，消息源用来支持消息的国际化。
           8).initApplicationEventMulticaster():初始化应用事件广播器，用来向ApplicationListener通知各种应用产生的事件，是一个标准的
                    观察者模式。
           9).onRefresh():是留给子类的扩展步骤。用来特定的Context子类初始化其他的bean
           10).registerListeners():把实现ApplicationListener的bean注册到事件广播器，并对广播器中早期没有广播的事件进行通知。
           11).finishBeanFactorynitialization(beanfatory):冻结所有bean描述信息的修改，实例化非延迟加载的单例bean。
           12).finishRefresh():完成上下文的刷新工作，调用LifecycleProcessor的onFresh()方法以及发布ContextRefreshedEvent事件。
           13).resetCommonCaches():在finally中执行13步，重置公用的缓存，比较典型的如： ReflectionUtils, ResolvableType
            以及CachedIntrospectionResults的缓存
      Spring中的bean的生命周期： 
           首先调用bean的构造方法创建bean，然后通过反射调用set方法进行属性的依赖注入。第三步，如果实现了BeanNameAware接口，会设置bean的name,
        第四步，如果实现了BeanFactoryAware接口，会把beanFactory设置给bean。第五步，如果实现ApplicationContextAware接口，会给bean设置ApplicationContext。
        第六步，如果实现了BeanPostProcessor接口，则执行前置的处理方法。第七步，实现了InitializingBean接口的话，会执行afterProPertiesSet()方法。
        第八步，执行自定义的init()方法。第九步，执行BeanPostProcessor的后置方法。这时就完成了bean的创建工作。那么在使用完bean需要销毁的时候，会先
        执行DisposableBean接口的destroy()方法，然后再执行自定义的destroy方法。
      
      Spring应用
      常用注解：(https://www.jianshu.com/p/71e8971d2bc5?utm_campaign=maleskine&utm_content=note&utm_medium=seo_notes&utm_source=recommendation)
           类型类：  +add PIC
           设置类：
           Web类：
           功能类：
     配置方式：XML、注解、API 
     自动装配：byType、byName、constructor、autodetect
     集合属性注入：
     内部bean：
     
  2.Struts：MVC控制层  和SpringMVC区别(SSM)
      Strus采用filter实现，根据类进行拦截，每次请求就会创建一个action，  
    
  3.ORM:简单来说就是把关系数据库的数据转化成面向程序中的对象。
    a.Hibernate：对数据库结构提供了完整的封装，实现了pojo对象与数据库表之间的映射，能自动生成和执行sql语句。
    b.Mybatis： 通过映射配置文件，将sql所需要的参数和返回结果映射到指定对象，mybatis不会自动生成sql，需要自己定义sql语句，自己实现sql优化。
    
    Mybatis详解：
      a.特点
          1)优点：原生sql、sql语句与代码解耦、简单易学、sql调优灵活
          2)缺点：半自动ORM、数据库移植性差
      b.缓存：
          1)一级缓存：作用域是session、hashMap实现、默认开启
          2)二级缓存：作用域是Mapping(maneSpace)、支持ehcache等缓存实现、可配置剔除策略，刷新间隔，缓存数量等
      c.应用相关：
          1)防止sql注入:#{}
          2)获得自增Id:keyProperty配置和selectKey两种方式实现
          3)动态sql标签:<foreach><choose><if><selectKey>
      d.执行流程：
      e.主要对象：(https://www.cnblogs.com/jian0110/p/9452592.html)
          1)SqlSessionFactory：用来创建SQLSession的工厂类，一个SqlSessionFactory对应一个数据库配置
                    对数据库的操作必须在SqlSession中进行
          2)SqlSession:非线程安全，每一次操作完成之后都要调用close()进行关闭
          3)Executor:SqlSession通过内部的Executor进行增删改查操作。
          4)StatementHandler：用来处理sql语句的预编译。   原生JDBC预编译，#占位符防止sql注入
          5)ParamterHandler：用来设置预编译参数。
          6)ResultSetHandler：用来处理结果集。
          7)TypeHandler：进行数据库类型和java Bean类型的互相映射。
      f.插件机制：
          1)拦截器链：
          2)作用点：Executor、StatementHandler、ParamterHandler、ResultSetHandler
          3)常见插件：mybatis-pagehelper
            
  4.Netty：是一个高性能的异步事件驱动的网络框架，对JDK原生的ORO进行封装，简化了网络服务的开发。
  5.RPC(https://www.jianshu.com/p/5b90a4e70783)
    RPC是Remote Procedure Call即远程过程调用。像调用本地方法一样调用远程过程。
    
    a.Motan   +add Pic
    b.Dubbo
    c.Grpc  
  6.其他框架
    a.Jersey
    b.RESTEasy
    c.Shiro                  
                       
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
      被动删除：
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
                       
                       
九、消息队列Kafka架构与原理和MySql调优与最佳实践
                

                       
