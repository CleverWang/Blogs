# matplotlib绘制动态图表

## 原理

主要是利用matplotlib的[“交互”模式](https://matplotlib.org/stable/tutorials/introductory/usage.html#what-is-interactive-mode)（interactive mode）。交互模式下，图表会实时绘制，对图表的操作会立即反映出来，不会阻塞代码。而非交互模式下，需要先完成对图表的操作，最后调用`show()`函数显示图表，并且会阻塞在调用`show()`的地方。交互模式相关函数：

- `ion()`：打开交互模式
- `ioff()`：关闭交互模式
- `pause()`：暂停指定时间
- `cla()`：清空Axes对象
- `clf()`：清空Figure对象

## 示例代码

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


def main():
    x_start, x_stop = 0, 2*np.pi
    point_cnt = 100
    x_step = (x_stop-x_start)/(point_cnt-1)
    xs = np.linspace(x_start, x_stop, point_cnt)
    x_value = x_stop
    series_sin, series_cos = np.sin(xs), np.cos(xs)

    # 打开交互模式（非阻塞，代码可以继续执行）
    plt.ion()
    fig, ax = plt.subplots()

    def draw():
        ax.plot(xs, series_sin, label=r'$y=sin(x)$')
        ax.plot(xs, series_cos, label=r'$y=cos(x)$')
        ax.xaxis.set_major_locator(MultipleLocator(1))
        ax.xaxis.set_minor_locator(MultipleLocator(0.2))
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        ax.yaxis.set_major_locator(MultipleLocator(1))
        ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        ax.set_title('Matplotlib in PySide2 demo')
        ax.set_xlabel(r'$x$')
        ax.set_ylabel(r'$y$')
        ax.legend()
        ax.grid()
        ax.axis('equal')

    # 第一次绘制
    draw()

    for _ in range(100):
        # 清除上一次的图表
        ax.cla()

        xs = np.delete(xs, 0)
        series_sin = np.delete(series_sin, 0)
        series_cos = np.delete(series_cos, 0)
        x_value += x_step
        xs = np.append(xs, x_value)
        series_sin = np.append(series_sin, np.sin(x_value))
        series_cos = np.append(series_cos, np.cos(x_value))

        # 重新绘制
        draw()

        # 暂停之前会更新和显示图表
        plt.pause(0.01)

    # 关闭交互模式
    plt.ioff()
    # 需要调用show，否则直接退出
    plt.show()


if __name__ == '__main__':
    main()
```

## 结果

![结果](https://upload-images.jianshu.io/upload_images/6411513-6fc29fbacd43bdc0.gif?imageMogr2/auto-orient/strip)

> 参考：<https://matplotlib.org/stable/tutorials/introductory/usage.html#what-is-interactive-mode>
