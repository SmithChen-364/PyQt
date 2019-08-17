
'''

扩展的列表控件QListWidge

是QListview的子类

支持MVC模式 和 直接将数据添加到控件上

'''
 
import sys
from PyQt5.QtWidgets import *

from PyQt5.Qt import QMainWindow
from _pytest.main import Item

class ListWidget(QMainWindow):
    def __init__(self,parent=None):
        super(ListWidget,self).__init__(parent)
        self.setWindowTitle("QListWidget show")
        self.listwidget=QListWidget()
        self.listwidget.resize(300,270)
        self.listwidget.addItem("item1")
        self.listwidget.addItem("item2")
        self.listwidget.addItem("item3")
        
        
        self.listwidget.itemClicked.connect(self.clicked)
        
        self.setCentralWidget(self.listwidget)
        
    def clicked(self,index):
        QMessageBox.information(self, "QListWidget", "您选择了" + self.listwidget.item(self.listwidget.row(index)).text())
        
        
        
        

if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=ListWidget()
    win.show()
    sys.exit(app.exec())