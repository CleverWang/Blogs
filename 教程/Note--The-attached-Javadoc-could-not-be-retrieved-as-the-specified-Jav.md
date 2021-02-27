# Note: The attached Javadoc could not be retrieved as the specified Javadoc location is either wro

## 问题

最近升级了eclipse到oxygen版本，java升级到了9，然后打开原来的java项目，发现鼠标悬停后没有Javadoc提示了。

> 鼠标悬停后提示：
>
> Note: The attached Javadoc could not be retrieved as the specified Javadoc location is either wrong or currently not accessible.

翻译过来，大概意思是相应的Javadoc不能被获取，原因可能是特定的Javadoc位置要么错误要么目前不能获取。

## 解决办法

Window---preference---Java----Installed JREs---选中已经安装的JRE---edit---选中所有的JRE system libraries---Source Attachment....---选中External location---在path中输入自己安装的java所在的目录里面的lib目录下的src.zip的绝对路径

> 参考：<http://blog.csdn.net/chenhao0568/article/details/41956655>
