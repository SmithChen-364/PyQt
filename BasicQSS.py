
'''
QSS基础
                                                                        
'''
import  sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class BasicQSS(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("QSS示例")  
        btn1=QPushButton("按钮1",self)
        btn1.setProperty("name", "btn1")
        btn2=QPushButton("按钮2",self)
        
        vbox=QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        self.setLayout(vbox)
  
if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=BasicQSS()
    #选择器
    qssstyle="""
     
    QPushButton[name="btn1"]{
        background-color:orange;
        color:blue;
    }
     
     
     """
    win.setStyleSheet(qssstyle)
    win.show()
    sys.exit(app.exec())