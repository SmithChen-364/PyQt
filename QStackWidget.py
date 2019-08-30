'''

选项卡控件：QStackedWidget

多页面控件


'''
 
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class stackwidgetDemo(QWidget):
    def __init__(self):
        super(stackwidgetDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("stackwidget控件示例")
        self.list=QListWidget()
        self.list.insertItem(0, "联系方式")
        self.list.insertItem(1,"家庭住址")
        
        self.stack1=QWidget()
        self.stack2=QWidget()
        
        self.tab1()
        
        self.stack=QStackedWidget()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        
        layout=QHBoxLayout()
        layout.addWidget(self.list)
        layout.addWidget(self.stack)
        
        
        self.setLayout(layout)
    
    def tab1(self):
        layout=QFormLayout()
        layout.addRow("name", QLineEdit())
        layout.addRow("address",QLineEdit())
        
        self.stack1.setLayout(layout)
        
        

if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=stackwidgetDemo()
    win.show()
    sys.exit(app.exec())