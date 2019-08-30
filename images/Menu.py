'''
创建和使用菜单
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Menu(QMainWindow):
    def __init__(self):
        super(Menu,self).__init__()
        #获取菜单栏
        bar=self.menuBar()
        
        file=bar.addMenu("文件")
        file.addAction("新建")
        
        save=QAction("保存",self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)
        
        save.triggered.connect(self.process)
        
    def process(self,a):
        print(self.sender().text())
    
if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=Menu()
    win.show()
    sys.exit(app.exec())