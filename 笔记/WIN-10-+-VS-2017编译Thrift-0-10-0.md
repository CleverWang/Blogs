# WIN 10 + VS 2017编译Thrift-0.10.0

## 一、准备工作

### 1.1 下载地址

1. 下载boost库：<http://www.boost.org/>
2. 下载openssl库：<https://www.openssl.org/source/>
3. 下载libevent库：<http://libevent.org/>
4. 下载thrift库：<http://thrift.apache.org/>

### 1.2 下载版本

| 库       | 版本                         |
| -------- | ---------------------------- |
| boost    | boost_1_66_0.tar.gz          |
| openssl  | openssl-1.1.0g.tar.gz        |
| libevent | libevent-2.1.8-stable.tar.gz |
| thrift   | thrift-0.10.0.tar.gz         |

## 二、编译boost

1. 解压 *boost_1_66_0.tar.gz* 。
2. 打开VS2017开发人员命令提示符，切换到 **[Boost解压目录]** ，运行：`bootstrap.bat`。
3. 然后运行：`.\b2`。
4. 在Boost解压目录下生成stage目录，存放编译好的lib，生成bin.v2，存放build，可以删除。

## 三、编译openssl

1. 下载并安装 Perl，地址：<http://www.perl.org/>，下载的版本是：*strawberry-perl-5.26.1.1-64bit.msi*。安装后确认 **[Perl安装目录]\perl\bin** 目录是否在环境变量中，如果不在则手动添加。
2. 下载并安装 NASM，地址：<http://www.nasm.us/>，下载的版本是：*nasm-2.13.03-installer-x64.exe*。安装后将 **[NASM安装目录]** 添加到环境变量中。
3. 解压 *openssl-1.1.0g.tar.gz* 。
4. 打开VS2017开发人员命令提示符，切换到 **[OpenSSL解压目录]** ，执行以下命令进行配置：`perl Configure VC-WIN32`， VC-WIN32表示编译成32位的库。然后执行：`nmake`，编译完成后执行如下指令进行测试：`nmake test`，然后执行`nmake install`安装。

## 四、编译libevent

1. 解压 *libevent-2.1.8-stable.tar.gz* 。
2. 打开 VS2017 开发人员命令提示符，切换到 **[libevent解压目录]** ，执行以下命令进行编译：`nmake /f Makefile.nmake`。
3. 注意编译过程中提示缺少 **print-winsock-errors.c** 文件，需要在test目录下加入该文件。参考：<http://blog.csdn.net/u013709254/article/details/77718693>。

## 五、编译thrift

1. 解压 *thrift-0.10.0.tar.gz* ，进入 **[Thrift源码]\lib\cpp** 目录。
2. 修改 **3rdparty.props** 文件中的各个第三方依赖库为之前编译好的各个库的绝对路径（各个库我都放在 **E:\compile_thrift_vs2017\\** 目录下）：

```xml
<BOOST_ROOT>E:\compile_thrift_vs2017\boost_1_66_0</BOOST_ROOT>

<OPENSSL_ROOT_DIR>E:\compile_thrift_vs2017\openssl-1.1.0g</OPENSSL_ROOT_DIR>

<LIBEVENT_ROOT>E:\compile_thrift_vs2017\libevent-2.1.8-stable</LIBEVENT_ROOT>
```

1. 用VS2017打开 **thrift.sln** ，如果提示升级编译器和库，则进行升级。
2. 切换到解决方案页签，展开libthrift工程，在server目录右键->添加->现有项，将 **[Thrift源代码目录]\lib\cpp\src\thrift\server\\** 目录下的以下四个文件加入到工程中（如果已经在工程中则忽略）：
   `TServerFramework.cpp`
   `TServerFramework.h`
   `TConnectedClient.cpp`
   `TConnectedClient.h`
3. 编译libthrift工程。
4. 编译libthriftnb工程。编译过程中报错，提示无法找到 **event-config.h** 文件，解决办法：将**E:\thrift\libevent-2.1.8-stable\WIN32-Code\nmake\event2** 目录下的 **event-config.h** 文件拷贝到 **E:\thrift\libevent-2.1.8-stable\include\event2** 中。
5. 编译完成后在Debug目录下生成如下两个lib即为编译完成：
   `libthrift.lib`
   `libshriftnb.lib`
