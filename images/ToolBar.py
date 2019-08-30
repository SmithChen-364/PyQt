'''

创建和使用工具栏


'''
 
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class ToolBar(QMainWindow):
    def __init__(self):
        super(ToolBar,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("工具栏例子")
        self.resize(300,300)
        
        #创建工具栏
        tb1=self.addToolBar("File")
        #添加按钮
        #默认是只显示图标，将文本作为悬停提示
        new=QAction(QIcon("./NewAI.jpg"),"new",self)
        tb1.addAction(new)

if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=ToolBar()
    win.show()
    sys.exit(app.exec())