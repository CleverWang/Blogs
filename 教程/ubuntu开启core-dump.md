# ubuntu开启core dump

## 1. ubuntu默认core dump是关闭的

通过命令```$ ulimit -a```查看：

![$ ulimit -a](https://upload-images.jianshu.io/upload_images/6411513-45bfd351b9ec4e58.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> core file size这一项为0，说明不生成core dump文件。

## 2. 打开方法

通过命令```$ ulimit -c unlimited```设置生成的core文件大小不限，也可以按自己的需求设置大小，设置完成后：

![$ ulimit -a](https://upload-images.jianshu.io/upload_images/6411513-b651aa5bc42c27e1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

但是，这样设置会有一个问题，就是这个命令只在当前打开的shell中生效，关闭后就失效了。

## 3. 每次打开shell能够自动打开

可以在```~/.bashrc```（只对当前用户生效）文件末尾添加```ulimit -c unlimited```，这样每次打开shell都会生效，可以使用编辑器或者输入命令```$ echo 'ulimit -c unlimited' >> ~/.bashrc```进行添加。

## 4. 测试

源文件```test.cpp```：

```c++
#include <iostream>
using namespace std;

int main() {
    int *p = nullptr;
    *p = 0; // 给空指针指向的地址赋值，引发core dump
    return 0;
}
```

编译：```$ g++ -g test.cpp -o test```（-g添加调试信息）
运行：```$ ./test```
结果：
> Segmentation fault (core dumped)

在与源文件相同目录下会生成名为```core```的core dump文件，使用gdb查看调用栈```$ gdb test core```：

![$ gdb test core](https://upload-images.jianshu.io/upload_images/6411513-f8de0043f505e077.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

通过gdb可以定位到发生core dump的位置为test.cpp文件的main()函数，具体在源文件的第6行，符合预期。

**2021.1.11更新：**

默认生成的core dump文件的名称为core，不够直观，可通过以下命令修改：
```$ sudo sysctl -w kernel.core_pattern=core.%p.%s.%c.%d.%P.%E```
其中每个%开头的符号含义如下（来自man，命令:```man 5 core```）：

```shell
   Naming of core dump files
       By default, a core dump file is named core, but the /proc/sys/kernel/core_pattern file (since  Linux  2.6  and
       2.4.21)  can  be  set  to  define a template that is used to name core dump files.  The template can contain %
       specifiers which are substituted by the following values when a core file is created:

           %%  a single % character
           %c  core file size soft resource limit of crashing process (since Linux 2.6.24)
           %d  dump mode—same as value returned by prctl(2) PR_GET_DUMPABLE (since Linux 3.7)
           %e  executable filename (without path prefix)
           %E  pathname of executable, with slashes ('/') replaced by exclamation marks ('!') (since Linux 3.0).
           %g  (numeric) real GID of dumped process
           %h  hostname (same as nodename returned by uname(2))
           %i  TID of thread that triggered core dump, as seen in the PID  namespace  in  which  the  thread  resides
               (since Linux 3.18)
           %I  TID of thread that triggered core dump, as seen in the initial PID namespace (since Linux 3.18)
           %p  PID of dumped process, as seen in the PID namespace in which the process resides
           %P  PID of dumped process, as seen in the initial PID namespace (since Linux 3.12)
           %s  number of signal causing dump
           %t  time of dump, expressed as seconds since the Epoch, 1970-01-01 00:00:00 +0000 (UTC)
           %u  (numeric) real UID of dumped process
```

> 参考：<https://stackoverflow.com/questions/17965/how-to-generate-a-core-dump-in-linux-on-a-segmentation-fault>
