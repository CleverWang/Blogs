# 为Elan触控板安装微软精确式触控板驱动

## 背景

电脑一直以来使用的ELAN触控板的驱动，是之前买电脑时给的驱动盘安装的普通驱动，后面更新了Windows 10，但驱动还是老样子，体验很差，只能进行基本操作。其实微软推出Windows 10后，提供了“精确式触摸板”，为触控板增加了新的手势操作，所以马上搞起来。

## 步骤

1. 在 [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/Search.aspx) 上搜索 **elan wdf**，一般选择最新发布的驱动（可以点击Last Updated按时间排序，然后选择最新的。如果你的Windows 10版本不是最新的，可能需要按照Products那一栏的描述选择符合自己Windows版本的驱动）**下载下来并解压缩**：

![elan wdf](https://upload-images.jianshu.io/upload_images/6411513-2b519746b56e635e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2. 安装：

* 打开```设备管理器->鼠标和其他指针设备->右击ELAN Input Device->选择更新驱动程序```

![设备管理器](https://upload-images.jianshu.io/upload_images/6411513-8ded3d34ff33975e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

* 接下来```浏览我的电脑以查找驱动程序->让我从计算机上的可用驱动程序列表中选取->从磁盘安装->浏览->找到刚才解压的目录->选择ETD.info打开->确定->选择ELAN Input Device For WDF->下一步->弹出警告框，选择是->开始安装驱动```
* 安装完毕后**重启电脑**生效

## 体验

打开```设置->设备->触控板```可以对精确式触控板进行设置：

![设置](https://upload-images.jianshu.io/upload_images/6411513-6a726356f124d4c5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

**常用操作：三指上划打开多任务视图，三指下滑立刻回到桌面，三指左右滑切换程序**
操作很丰富，有点Mac的味道了，感觉很棒。

> 参考：
>
> 1. <https://zhuanlan.zhihu.com/p/38252987>
> 2. <https://blog.csdn.net/ccgcccccc/article/details/89044621>
