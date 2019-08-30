
'''
QSS子控件选择器
                                                                        
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
        self.setWindowTitle("QSS子控件选择器示例")  
        combo=QComboBox(self)
        combo.setObjectName("myCombox")
        combo.addItem("window")
        combo.addItem("Linux")
        combo.addItem("Mac")
        
        combo.move(50,50)
        
        self.setGeometry(350,350,300,300)
        
        
if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=BasicQSS()
    #选择器
    qssstyle="""
        
        QComboBox#myCombox::drop-down{
            
            image:url("./NewAI.png")
            
            }
    
     """
    win.setStyleSheet(qssstyle)
    win.show()
    sys.exit(app.exec())