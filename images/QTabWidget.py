'''
选项卡控件：QTabWidget

多页面控件
'''
 
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class TabwidgetDemo(QTabWidget):
    def __init__(self):
        super(TabwidgetDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("选项卡控件示例")
        
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()
        
        self.addTab(self.tab1,"选项卡1")
        self.addTab(self.tab2, "选项卡2")
        self.addTab(self.tab3, "选项卡3")
        

if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=TabwidgetDemo()
    win.show()
    sys.exit(app.exec())