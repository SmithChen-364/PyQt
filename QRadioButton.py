'''
QRadioButton（单选按钮，同时只能选中一个）



'''
 
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from msilib.schema import RadioButton


class QRadioButtonDemo(QWidget):
    def __init__(self,parent=None):
        super(QRadioButtonDemo,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("单选按钮的示例")
        
        layout=QHBoxLayout()
        self.button1=QRadioButton("单选按钮1")
        self.button1.setChecked(True)
        
        self.button1.toggled.connect(self.buttonState)
        
        layout.addWidget(self.button1)
        
        self.button2=QRadioButton("单选按钮2")
        self.button2.toggled.connect(self.buttonState)
        layout.addWidget(self.button2)
        
        self.setLayout(layout)
        
        
    def buttonState(self):
        radioButton=self.sender()
        if(radioButton.isChecked()==True):
            print(radioButton.text()+"被选中")
        else:                
            print(radioButton.text()+"取消选中")
       
if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=QRadioButtonDemo()
    win.show()
    sys.exit(app.exec())