#coding:utf-8
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout() #创建水平布局对象
        hbox.addStretch(1)  #在第一个元素之前添加伸缩，元素会显示在右侧
        hbox.addWidget(okButton) #添加元素
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout() #创建垂直布局对象
        vbox.addStretch(1)  #在第一元素之前添加伸缩，元素会显示在下面
        vbox.addLayout(hbox) #添加元素

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())