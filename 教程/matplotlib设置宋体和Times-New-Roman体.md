# matplotlib设置宋体和Times New Roman体

写论文时，要求图中的中文字体为宋体，英文字体为Times New Roman体。

matplotlib默认是英文字体，如果设置中文的xlabel、ylabel或者title，显示时会乱码或者变成方块，需要进行设置。

## 配置matplotlib

```python
from matplotlib import rcParams

config = {
    "font.family": 'serif', # 衬线字体
    "font.size": 12, # 相当于小四大小
    "font.serif": ['SimSun'], # 宋体
    "mathtext.fontset": 'stix', # matplotlib渲染数学字体时使用的字体，和Times New Roman差别不大
    'axes.unicode_minus': False # 处理负号，即-号
}
rcParams.update(config)
```

## Ubuntu下的matplotlib添加中文支持

Windows环境下自带宋体，而Ubuntu默认无中文字体支持，需要自己添加。

1. 在Windows中找到SimSun字体文件，默认在`C:\Windows\Fonts\simsun.tcc`
2. 将该文件拷贝到Ubuntu的`/usr/share/matplotlib/mpl-data/fonts/ttf`目录下（可能需要root权限）
3. 删除当前用户的matplotlib缓存：`cd ~/.cache/matplotlib && rm -rf *.*`
4. 关闭已打开的python解释器，重新import matplotlib并按上面介绍的方法配置matplotlib即可

> 参考：
>
> <https://zhuanlan.zhihu.com/p/118601703>
>
> <https://blog.csdn.net/jeff_liu_sky_/article/details/54023745>
