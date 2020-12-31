1. 参考我的上一篇文章[Windows Terminal添加Git Bash支持](https://www.jianshu.com/p/4540f00a82a3)
2. 在`settings.json`的`profiles`的`list`中增加一项命令行配置：
```json
{
    "guid" : "{7FC439DF-70CB-0588-5417-276C84E36B88}",
    "name" : "VsDevCmd",
    "commandline" : "cmd.exe %comspec% /k \"E:\\Microsoft Visual Studio\\2019\\Community\\Common7\\Tools\\VsDevCmd.bat\"",
    "icon" : "F:\\Pictures\\vs.png"
},
```
**注意，E:\\Microsoft Visual Studio\\2019\\Community\\Common7\\Tools\\VsDevCmd.bat需要设置为你自己的路径。**
这里给大家提供一个icon：

![vs.png](https://upload-images.jianshu.io/upload_images/6411513-ed03f11279837e16.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

3. 效果

![效果](https://upload-images.jianshu.io/upload_images/6411513-f95762a24659c695.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

VS命令行环境就起来了，可以愉快地运行msbuild、dotnet等命令啦~
