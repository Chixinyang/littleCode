import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        #菜单元素
        exitAction = QAction(QIcon('web.jpg'), '&Exit', self) #创建元素，并添加图标，文字
        exitAction.setShortcut('Ctrl+Q') #添加快捷方式
        exitAction.setStatusTip('Exit application') #添加状态提示
        exitAction.triggered.connect(qApp.quit) #触发行为

        self.statusBar().showMessage("你好，小哥哥")

        # 创建一个菜单栏
        menubar = self.menuBar()
        # 添加菜单
        fileMenu = menubar.addMenu('&File')
        # 添加事件
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())