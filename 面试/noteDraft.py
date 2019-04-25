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
      软引用：内存空间不
