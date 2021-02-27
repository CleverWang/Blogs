# PySide2下使用QtCharts

## 界面

使用pyside2-designer设计界面：

![界面](https://upload-images.jianshu.io/upload_images/6411513-3d438452a3069264.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

保存为：ui_chartswidget.ui

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>ChartsWidget</class>
 <widget class="QWidget" name="ChartsWidget">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>ChartsWidget</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout">
   <item>
    <widget class="QFrame" name="frameCharts">
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
pyside2-uic -o ui_chartswidget.py ui_chartswidget.ui
```

编译界面为python文件：ui_chartswidget.py

```python
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chartswidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ChartsWidget(object):
    def setupUi(self, ChartsWidget):
        if not ChartsWidget.objectName():
            ChartsWidget.setObjectName(u"ChartsWidget")
        ChartsWidget.resize(800, 600)
        self.verticalLayout = QVBoxLayout(ChartsWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frameCharts = QFrame(ChartsWidget)
        self.frameCharts.setObjectName(u"frameCharts")
        self.frameCharts.setFrameShape(QFrame.StyledPanel)
        self.frameCharts.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frameCharts)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnStart = QPushButton(ChartsWidget)
        self.btnStart.setObjectName(u"btnStart")

        self.horizontalLayout.addWidget(self.btnStart)

        self.btnStop = QPushButton(ChartsWidget)
        self.btnStop.setObjectName(u"btnStop")

        self.horizontalLayout.addWidget(self.btnStop)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ChartsWidget)

        QMetaObject.connectSlotsByName(ChartsWidget)
    # setupUi

    def retranslateUi(self, ChartsWidget):
        ChartsWidget.setWindowTitle(QCoreApplication.translate("ChartsWidget", u"ChartsWidget", None))
        self.btnStart.setText(QCoreApplication.translate("ChartsWidget", u"start", None))
        self.btnStop.setText(QCoreApplication.translate("ChartsWidget", u"stop", None))
    # retranslateUi
```

## 逻辑

编写文件chartswidget.py：

```python
#!E:/Python/Python38/python.exe
# -*- coding: utf-8 -*-

import numpy as np

from PySide2.QtCore import *
from PySide2.QtCharts import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from ui_chartswidget import Ui_ChartsWidget


class ChartsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ChartsWidget()
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
        self.series_sin = QtCharts.QLineSeries()
        self.series_cos = QtCharts.QLineSeries()
        self.series_sin.setName("y=sin(x)")
        self.series_cos.setName("y=cos(x)")
        x_start, x_stop = 0.0, 2*np.pi
        self.x_step = (x_stop-x_start)/(self.point_cnt-1)
        self.x_value = x_stop
        xs = np.linspace(x_start, x_stop, self.point_cnt)
        ys_sin, ys_cos = np.sin(xs), np.cos(xs)
        for i in range(self.point_cnt):
            self.series_sin.append(xs[i], ys_sin[i])
            self.series_cos.append(xs[i], ys_cos[i])
        # qDebug('init size of sin: %d' % self.series_sin.count())
        # qDebug('init size of cos: %d' % self.series_cos.count())

        self.chart = QtCharts.QChart()
        self.chart.addSeries(self.series_sin)
        self.chart.addSeries(self.series_cos)
        self.chart.setTitle('QtCharts Test')

        self.axis_x = QtCharts.QValueAxis()
        self.axis_x.setLabelFormat('%.1f')
        self.axis_x.setTitleText('X')
        self.axis_x.setTickCount(11)
        self.axis_x.setMinorTickCount(4)
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.series_sin.attachAxis(self.axis_x)
        self.series_cos.attachAxis(self.axis_x)

        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setLabelFormat('%.1f')
        self.axis_y.setTitleText('Y')
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.series_sin.attachAxis(self.axis_y)
        self.series_cos.attachAxis(self.axis_y)

        self.chart_view = QtCharts.QChartView(self.chart, self)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        self.horizontalLayout = QHBoxLayout(self.ui.frameCharts)
        self.horizontalLayout.addWidget(self.chart_view)

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
        self.series_sin.remove(0)
        self.series_cos.remove(0)
        self.x_value += self.x_step
        self.series_sin.append(self.x_value, np.sin(self.x_value))
        self.series_cos.append(self.x_value, np.cos(self.x_value))
        # qDebug('current size of sin: %d' % self.series_sin.count())
        # qDebug('current size of cos: %d' % self.series_cos.count())
        self.chart.scroll(self.chart.plotArea().width()/(self.point_cnt-1), 0)

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
from PySide2.QtWidgets import QApplication
from chartswidget import ChartsWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = ChartsWidget()
    widget.show()

    sys.exit(app.exec_())
```

## 结果

![初始界面](https://upload-images.jianshu.io/upload_images/6411513-ed644c9498750738.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![动态更新](https://upload-images.jianshu.io/upload_images/6411513-cf4213da833a654c.gif?imageMogr2/auto-orient/strip)
