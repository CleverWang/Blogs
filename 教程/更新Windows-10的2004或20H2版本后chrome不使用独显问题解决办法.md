# 1. 问题
笔记本电脑的Windows 10更新20H2版本后，使用chrome看视频或者直播的时候，发现CPU利用率跑满（也可能是我的垃圾笔记本电脑太老了，CPU不行了，哈哈~），但是独显却在打酱油，截图如下：
![独显打酱油](https://upload-images.jianshu.io/upload_images/6411513-a0470932955eedbf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
这我不能忍啊，CPU忙的要死，独显却在围观。
于是我赶紧打开```NVIDIA控制面板```，看一下chrome是不是设置为了独显模式。发现之前早就设置过了：
![NVIDIA控制面板](https://upload-images.jianshu.io/upload_images/6411513-010b018d2dd9710c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
那问题出在哪里呢？
# 2. 解决
查阅资料，发现可以这样解决：
## 1. 步骤1
打开```设置->系统->显示->图形设置```
![步骤1](https://upload-images.jianshu.io/upload_images/6411513-8f31387838d51b9b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
## 2. 步骤2
选择```浏览```，在弹出的文件选择器中选择chrome的exe文件，路径一般在```C:\Program Files (x86)\Google\Chrome\Application```，单击```添加```
![步骤2](https://upload-images.jianshu.io/upload_images/6411513-101548510d41e74d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
## 3. 步骤3
添加好后单击```Google Chrome```，接着```选项->高性能->保存```，重启chrome
![步骤3](https://upload-images.jianshu.io/upload_images/6411513-d1966b711a545214.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
# 3. 结果
![结果](https://upload-images.jianshu.io/upload_images/6411513-d60fb6e0140ad71f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
独显终于跑起来了，不再打酱油了。
**如果发现其他本来可以调用独显的软件不再调用独显了，也可以使用本方法试试，但不保证有效哈。** 
问题解决，撒花~

**2021.1.2更新：**
感谢[JamesTt](https://www.jianshu.com/u/3e7929dbf483)提醒，NVIDIA控制面板中提供了直达“Windows图形设置”的入口：
![NVIDIA控制面板的图形设置入口](https://upload-images.jianshu.io/upload_images/6411513-906e5aad9c7abf86.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
点击可以直接转跳到图形设置中对每个程序进行单独的图形设置。


> 参考：https://www.bilibili.com/read/cv6266330/
