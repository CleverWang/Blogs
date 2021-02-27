# Sublime Text 3打开中文乱码问题解决

## 问题

在使用Sublime Text 3打开一些包含中文的文件的时候，经常会遇到乱码的问题。比如使用Windows自带的记事本编写文件，然后按`ANSI`格式保存，再使用Sublime Text 3打开就会乱码。

![记事本](https://upload-images.jianshu.io/upload_images/6411513-e9e45e007afb68ff.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![Sublime Text 3](https://upload-images.jianshu.io/upload_images/6411513-25800581b5593bf4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

主要是因为记事本实际是按`GB2312`的编码（`ANSI`映射的本地编码）进行保存的，而Sublime Text 3不支持`GB2312`。

## 解决办法

**安装`ConvertToUTF8`包**

1. 安装`Package Control`：

![Package Control](https://upload-images.jianshu.io/upload_images/6411513-6387852f5089d141.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2. 打开`Package Control`，选择`Install Package`：

![Package Control](https://upload-images.jianshu.io/upload_images/6411513-dcafe5b7937541af.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![Install Package](https://upload-images.jianshu.io/upload_images/6411513-22fd5d2bc03de815.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

3. 搜索`ConvertToUTF8`，点击安装：

![ConvertToUTF8](https://upload-images.jianshu.io/upload_images/6411513-93b4441e4768a7fd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

4. **重启**Sublime Text 3

## 效果

![效果](https://upload-images.jianshu.io/upload_images/6411513-c109f1971777b9dd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

注意图中的红圈，可以看到是`GB2312`转换成`UTF8`。

**`ConvertToUTF8`并不会实际修改原文件的编码方式，而是解析原文件的编码方式，然后转换成`UTF8`显示出来。对原文件的任何修改，依旧是按原来的编码方式保存。（也可以自己设置，参考文末的链接）**

`ConvertToUTF8`支持的编码：

```json
// supported encoding list, name & code in pair
"encoding_list" : [
 ["Chinese Simplified (GBK)", "GBK"],
 ["Chinese Simplified (GB2312)", "GB2312"],
 ["Chinese Simplified (GB18030)", "GB18030"],
 ["Chinese Traditional (BIG5)", "BIG5"],
 ["Korean (EUC-KR)", "EUC-KR"],
 ["Japanese (CP932)", "CP932"],
 ["Japanese (Shift_JIS)", "Shift_JIS"],
 ["Japanese (EUC-JP)", "EUC-JP"],
 ["UTF-8", "UTF-8"]
]
```

> 参考:
> <https://github.com/seanliang/ConvertToUTF8>
