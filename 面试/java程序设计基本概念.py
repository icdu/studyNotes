一.JVM
  JVM使用Unicode characters编码表示。
    所有编码转换只发生在边界的地方，JVM和OS的交界处，也就是各种输入/输出流(或者Reader,Writer类)起作用的地方。I/O分为两大阵营：面向字符的输入/输出流；
  面向字节的输入/输出流。..如果用到GBK编码以外的文件，就必须采用编码转换：一个字符与字节之间的转换。因此，java的I/O文件能够转换编码的地方，也就在字符
  与字节转换的地方，那就是InputStreamReader和OutputStreamWriter。这两个类是字节流和字符流之间的适配器类，他们承担编码转换的任务。
  
  ClassLoader：
