'''
QPushButton控件

所以按钮控件的父类：QAbstractButton

QPushButton
AToolButton
QRadioButton
QCheckBox

显示图像：
支持开关



'''
 
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class QPushButtonDemo(QDialog):
    def __init__(self,parent=None):
        super(QPushButtonDemo,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QPushButton的示例")
        
        self.resize(300,360)
        
        self.button1=QPushButton("第一个按钮")
        self.button2=QPushButton("图像按钮")
        self.button3=QPushButton("第三个按钮")
        self.button4=QPushButton("&MyButton")
        
        self.button1.setCheckable(True)
        self.button1.toggle()
        self.button2.setIcon(QIcon("./NewAI.jpg"))
        
        #设置按钮不可用（变成灰色不可用）
        self.button3.setEnabled(False)
        
        #设置默认按钮(即窗口打开时的 鼠标焦点自动在这个按钮上，直接回车即可选中）
        self.button4.setDefault(True)
        
        
        layout=QVBoxLayout()
        
        
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        
        self.button1.clicked.connect(lambda:self.whichButton(self.button1))
        self.button1.clicked.connect(self.buttonState)
        self.button2.clicked.connect(lambda:self.whichButton(self.button2))
        self.button3.clicked.connect(lambda:self.whichButton(self.button3))
        self.button4.clicked.connect(lambda:self.whichButton(self.button4))
        
        self.setLayout(layout)
        
    def buttonState(self):
        if self.button1.isChecked():
            print("按钮1已经被选中")
        else:
            print("按钮1未被选中")
        
    def whichButton(self,btn):
        print("被单击的按钮是："+btn.text())
        
        
        
        
if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=QPushButtonDemo()
    win.show()
    sys.exit(app.exec())