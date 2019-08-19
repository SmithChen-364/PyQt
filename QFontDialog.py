'''

QFontDialog(字体对话框）


'''
 
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class QFontDialogDemo(QWidget):
    def __init__(self):
        super(QFontDialogDemo,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QFontDialogDemo Demo")
       
        
        layout=QVBoxLayout()
        
        self.fontButton=QPushButton("选择字体")
        self.fontButton.clicked.connect(self.getFont)
        layout.addWidget(self.fontButton)
        
        self.fontLabel=QLabel("测试字体")
        layout.addWidget(self.fontLabel)
        
        self.setLayout(layout)
        
        
    def getFont(self):
        font,ok=QFontDialog.getFont()
        if ok:
            self.fontLabel.setFont(font)
        
        


if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=QFontDialogDemo()
    win.show()
    sys.exit(app.exec())