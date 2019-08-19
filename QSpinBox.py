'''
QSpinBox(计数器控件）

'''
 
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class QSpinBoxDemo(QWidget):
    def __init__(self,parent=None):
        super(QSpinBoxDemo,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QSpinBoxDemo Demo")
        self.resize(300,100)
        
        #选择垂直布局
        layout=QVBoxLayout()
        self.label=QLabel("当前值")
        self.label.setAlignment(Qt.AlignCenter)
        
        self.sb=QSpinBox()
       
        layout.addWidget(self.label)
        layout.addWidget(self.sb)
        
        self.sb.valueChanged.connect(self.valueChange)
        self.setLayout(layout)
        
        
    def valueChange(self):
        self.label.setText("当前值 "+str(self.sb.value()))
        
        
        
if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=QSpinBoxDemo()
    win.show()
    sys.exit(app.exec())