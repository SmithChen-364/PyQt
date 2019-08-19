'''

QColorDialog(字体对话框）


'''
 
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QColorDialogDemo Demo")
       
        
        layout=QVBoxLayout()
        
        self.colorButton=QPushButton("选择文字颜色")
        self.colorButton.clicked.connect(self.getColor)
        layout.addWidget(self.colorButton)
        
        self.colorButton1=QPushButton("选择背景颜色")
        self.colorButton1.clicked.connect(self.setBGColor)
        layout.addWidget(self.colorButton1)
        
        self.colorLabel=QLabel("测试颜色")
        layout.addWidget(self.colorLabel)
        
        self.setLayout(layout)
        
        
    def getColor(self):
        color=QColorDialog.getColor()
        p=QPalette()
        p.setColor(QPalette.WindowText, color)
        #设置文字颜色
        self.colorLabel.setPalette(p)
    
    def setBGColor(self):
        color=QColorDialog.getColor()
        p=QPalette()
        p.setColor(QPalette.Window, color)
    
        self.colorLabel.setAutoFillBackground(True)
        self.colorLabel.setPalette(p)
        


if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=QColorDialogDemo()
    win.show()
    sys.exit(app.exec())