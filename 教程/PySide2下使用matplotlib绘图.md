# PySide2下使用matplotlib绘图

## 界面

使用pyside2-designer设计界面：

![设计界面](https://upload-images.jianshu.io/upload_images/6411513-1e9ef3732f8538cd.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

保存为ui_matplotlibwidget.ui：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MatplotlibWidget</class>
 <widget class="QWidget" name="MatplotlibWidget">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MatplotlibWidget</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="QFrame" name="frameMatplotlib">
     <property name="frameShape">
      <enum>QFrame::StyledPanel</enum>
     </property>
     <property name="frameShadow">
      <enum>QFrame::Raised</enum>
     </property>
    </widget>
   </item>
   <item>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QPushButton" name="btnStart">
       <property name="text">
        <string>start</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="btnStop">
       <property name="text">
        <string>stop</string>
       </property>
      </widget>
     </item>
    </layout>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
```

输入命令：

```bash
pyside2-uic -o ui_matplotlibwidget.py ui_matplotlibwidget.ui
```

编译界面为python文件ui_matplotlibwidget.py：

```python
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_matplotlibwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MatplotlibWidget(object):
    def setupUi(self, MatplotlibWidget):
        if not MatplotlibWidget.objectName():
            MatplotlibWidget.setObjectName(u"MatplotlibWidget")
        MatplotlibWidget.resize(800, 600)
        self.verticalLayout = QVBoxLayout(MatplotlibWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frameMatplotlib = QFrame(MatplotlibWidget)
        self.frameMatplotlib.setObjectName(u"frameMatplotlib")
        self.frameMatplotlib.setFrameShape(QFrame.StyledPanel)
        self.frameMatplotlib.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frameMatplotlib)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnStart = QPushButton(MatplotlibWidget)
        self.btnStart.setObjectName(u"btnStart")

        self.horizontalLayout.addWidget(self.btnStart)

        self.btnStop = QPushButton(MatplotlibWidget)
        self.btnStop.setObjectName(u"btnStop")

        self.horizontalLayout.addWidget(self.btnStop)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(MatplotlibWidget)

        QMetaObject.connectSlotsByName(MatplotlibWidget)
    # setupUi

    def retranslateUi(self, MatplotlibWidget):
        MatplotlibWidget.setWindowTitle(QCoreApplication.translate("MatplotlibWidget", u"MatplotlibWidget", None))
        self.btnStart.setText(QCoreApplication.translate("MatplotlibWidget", u"start", None))
        self.btnStop.setText(QCoreApplication.translate("MatplotlibWidget", u"stop", None))
    # retranslateUi
```

## 逻辑

编写文件chartswidget.py：

```python
# -*- coding: utf-8 -*-

import numpy as np

from PySide2.QtCore import *
from PySide2.QtCharts import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

from ui_matplotlibwidget import Ui_MatplotlibWidget


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MatplotlibWidget()
        self.ui.setupUi(self)

        self.x_value = 0
        self.x_step = 0
        self.point_cnt = 100

        self.init_charts()

        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_charts)

        self.ui.btnStart.setDisabled(False)
        self.ui.btnStop.setDisabled(True)
        self.ui.btnStart.clicked.connect(self.start)
        self.ui.btnStop.clicked.connect(self.stop)

    def init_charts(self):
        x_start, x_stop = 0.0, 2*np.pi
        self.x_step = (x_stop-x_start)/(self.point_cnt-1)
        self.xs = np.linspace(x_start, x_stop, self.point_cnt)
        self.x_value = x_stop
        self.series_sin, self.series_cos = np.sin(self.xs), np.cos(self.xs)

        self.canvas = FigureCanvas(Figure())
        self.verticalLayout = QVBoxLayout(self.ui.frameMatplotlib)
        self.verticalLayout.addWidget(self.canvas)
        self.verticalLayout.addWidget(NavigationToolbar(self.canvas, self))

        self.ax = self.canvas.figure.subplots()
        self.draw_charts()

    @Slot()
    def start(self):
        self.ui.btnStart.setDisabled(True)
        self.ui.btnStop.setDisabled(False)
        self.timer.start()

    @Slot()
    def stop(self):
        self.ui.btnStart.setDisabled(False)
        self.ui.btnStop.setDisabled(True)
        self.timer.stop()

    @Slot()
    def update_charts(self):
        self.xs = np.delete(self.xs, 0)
        self.series_sin = np.delete(self.series_sin, 0)
        self.series_cos = np.delete(self.series_cos, 0)
        self.x_value += self.x_step
        self.xs = np.append(self.xs, self.x_value)
        self.series_sin = np.append(self.series_sin, np.sin(self.x_value))
        self.series_cos = np.append(self.series_cos, np.cos(self.x_value))
        self.ax.cla()
        self.draw_charts()
        self.canvas.draw()

    def draw_charts(self):
        self.ax.plot(self.xs, self.series_sin, label=r'$y=sin(x)$')
        self.ax.plot(self.xs, self.series_cos, label=r'$y=cos(x)$')
        self.ax.xaxis.set_major_locator(MultipleLocator(1))
        # self.ax.xaxis.set_minor_locator(MultipleLocator(0.2))
        self.ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        self.ax.yaxis.set_major_locator(MultipleLocator(1))
        self.ax.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
        self.ax.set_title('Matplotlib in PySide2 demo')
        self.ax.set_xlabel(r'$x$')
        self.ax.set_ylabel(r'$y$')
        self.ax.legend()
        self.ax.grid()
        self.ax.axis('equal')

    def closeEvent(self, event):
        if (self.timer.isActive()):
            self.timer.stop()
        return super().closeEvent(event)
```

编写文件main.py：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PySide2.QtWidgets import *

from matplotlibwidget import MatplotlibWidget

if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    widget = MatplotlibWidget()
    widget.show()

    sys.exit(app.exec_())
```

## 结果

![初始界面](https://upload-images.jianshu.io/upload_images/6411513-2f99061564dc6f25.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![动态更新](https://upload-images.jianshu.io/upload_images/6411513-07d1c3749a4fb166.gif?imageMogr2/auto-orient/strip)

> 参考：<https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_qt_sgskip.html>
