'''

QDockWidget(停靠控件）
                                                                                        


'''
import  sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DockwidgetDemo(QMainWindow):
    def __init__(self):
        super(DockwidgetDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("DockwidgetDemo")
        layout=QHBoxLayout()
        self.items=QDockWidget("Dockable",self)
        self.listwidget=QListWidget()
        self.listwidget.addItem("item1")
        self.listwidget.addItem("item2")
        self.listwidget.addItem("item3")
        
        self.items.setWidget(self.listwidget)
        self.setCentralWidget(QLineEdit())
        
        self.items.setFloating(True)
        
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)
        
          
        
     
   
if __name__ =="__main__":
     app=QApplication(sys.argv)
     win=DockwidgetDemo()
     win.show()
     sys.exit(app.exec())