# PySide2下利用QThread实现后台线程

## PySide2简介

PySide2是Qt官方的[Qt for Python Project](http://wiki.qt.io/Qt_for_Python)的实现，支持Qt 5.12+。
安装方式：

```bash
pip3 install PySide2
```

同时还会安装：

- pyside2-designer：设计师工具
- pyside2-lupdate：国际化工具
- pyside2-rcc：资源工具
- pyside2-uic：ui文件编译成python工具

上述命令可以直接在命令行下执行。

## 界面

使用pyside2-designer设计界面：

![设计界面](https://upload-images.jianshu.io/upload_images/6411513-d81334057c05943c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

保存为：ui_widget.ui

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Widget</class>
 <widget class="QWidget" name="Widget">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>350</width>
    <height>250</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Widget</string>
  </property>
  <layout class="QVBoxLayout" name="verticalLayout_2">
   <item>
    <widget class="QLCDNumber" name="lcdNumber"/>
   </item>
   <item>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QProgressBar" name="progressBar">
       <property name="value">
        <number>0</number>
       </property>
       <property name="textVisible">
        <bool>true</bool>
       </property>
       <property name="invertedAppearance">
        <bool>false</bool>
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
        <widget class="QPushButton" name="btnCancel">
         <property name="text">
          <string>cancel</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
    </layout>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
```

执行命令：

```bash
pyside2-uic -o ui_widget.py ui_widget.ui
```

生成对应的python文件ui_widget.py：

```python
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(350, 250)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lcdNumber = QLCDNumber(Widget)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.verticalLayout_2.addWidget(self.lcdNumber)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progressBar = QProgressBar(Widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)

        self.verticalLayout.addWidget(self.progressBar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnStart = QPushButton(Widget)
        self.btnStart.setObjectName(u"btnStart")

        self.horizontalLayout.addWidget(self.btnStart)

        self.btnCancel = QPushButton(Widget)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.btnStart.setText(QCoreApplication.translate("Widget", u"start", None))
        self.btnCancel.setText(QCoreApplication.translate("Widget", u"cancel", None))
    # retranslateUi
```

## 逻辑

编写文件backgroundworker.py：

```python
# -*- coding: utf-8 -*-

from PySide2.QtCore import QObject, Signal, qDebug, QThread, Slot


class BackgroundWorker(QObject):
    report_progress = Signal(int)
    finished = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_cancelled_ = False
        self.progress_ = 0

    @Slot()
    def run(self):
        qDebug('start...thread id: '+str(QThread.currentThread()))
        for _ in range(10):
            if (self.is_cancelled_):
                break

            QThread.msleep(1000)

            self.progress_ += 10
            self.report_progress.emit(self.progress_)

        self.finished.emit(self.progress_)
        self.reset()

    def cancel(self):
        self.is_cancelled_ = True
        qDebug('cancelled...thread id: '+str(QThread.currentThread()))

    def reset(self):
        self.is_cancelled_ = False
        self.progress_ = 0
```

编写文件widget.py：

```python
# -*- coding: utf-8 -*-

from PySide2.QtCore import QThread, QTime, Signal, Slot, qDebug, QTimer
from PySide2.QtWidgets import QMessageBox, QWidget

from ui_widget import Ui_Widget
from backgroundworker import BackgroundWorker


class Widget(QWidget):
    start_background_work = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.btnCancel.setDisabled(True)
        self.ui.progressBar.setRange(0, 100)
        self.ui.progressBar.setValue(0)
        self.ui.lcdNumber.setDigitCount(8)

        self.background_worker_thread_ = QThread()
        self.background_worker_ = BackgroundWorker()
        self.background_worker_.moveToThread(self.background_worker_thread_)
        self.timer_ = QTimer()

        self.start_background_work.connect(self.background_worker_.run)
        self.background_worker_.report_progress.connect(self.show_progress)
        self.background_worker_.finished.connect(self.show_result)
        self.timer_.timeout.connect(lambda: self.ui.lcdNumber.display(
            QTime.currentTime().toString('hh:mm:ss')))

        self.timer_.start(1000)

    @Slot()
    def on_btnStart_clicked(self):
        if not self.background_worker_thread_.isRunning():
            self.background_worker_thread_.start()

        self.ui.btnStart.setDisabled(True)
        self.ui.btnCancel.setDisabled(False)
        self.start_background_work.emit()
        qDebug('start button was clicked! thread id: ' +
               str(QThread.currentThread()))

    @Slot()
    def on_btnCancel_clicked(self):
        qDebug('cancel button was clicked! thread id: ' +
               str(QThread.currentThread()))
        self.background_worker_.cancel()

    @Slot()
    def show_progress(self, progress):
        qDebug('show progress. thread id: '+str(QThread.currentThread()))
        self.ui.progressBar.setValue(progress)

    @Slot()
    def show_result(self, complete_progress):
        qDebug('show result. thread id: '+str(QThread.currentThread()))
        QMessageBox.information(
            self, 'result', '%d%% completed!' % complete_progress)
        self.ui.btnStart.setDisabled(False)
        self.ui.btnCancel.setDisabled(True)
        self.ui.progressBar.setValue(0)

    def closeEvent(self, event):
        qDebug('close')
        if self.background_worker_thread_.isRunning():
            self.background_worker_.cancel()
            self.background_worker_thread_.quit()
            self.background_worker_thread_.wait()
        if self.timer_.isActive():
            self.timer_.stop()

        return super().closeEvent(event)
```

编写文件main.py：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QApplication
from widget import Widget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = Widget()
    widget.show()

    sys.exit(app.exec_())
```

运行：`python3 main.py`

## 结果

![开始](https://upload-images.jianshu.io/upload_images/6411513-c0803646a0c0007e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![正常结束](https://upload-images.jianshu.io/upload_images/6411513-bf40bcda070ba580.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![中途结束](https://upload-images.jianshu.io/upload_images/6411513-3e3d5bb68c79e8b0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
