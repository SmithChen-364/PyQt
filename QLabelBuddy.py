'''
QLabel与伙伴控件

'''
 
import sys
from PyQt5.QtWidgets import *


class QLabelBuddy(QDialog):
    def __init__(self,parent=None):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("设置伙伴")
        
        #热键是N
        nameLabel=QLabel("&Name",self)
        nameLineEdit=QLineEdit()
        
        #设置伙伴关系
        nameLabel.setBuddy(nameLineEdit)
        
        passwordLabel=QLabel("&Password",self)
        passwordLineEdit=QLineEdit()
        
        #设置伙伴关系
        passwordLabel.setBuddy(passwordLineEdit)
        
        btnOK=QPushButton("&OK")
        btnCancel=QPushButton("&Cancel")
        
        mainlayout=QGridLayout(self)
        mainlayout.addWidget(nameLabel,0,0)
        mainlayout.addWidget(nameLineEdit,0,1,1,2)
        mainlayout.addWidget(passwordLabel,1,0)
        mainlayout.addWidget(passwordLineEdit,1,1,1,2)
        
        mainlayout.addWidget(btnOK,2,1)
        mainlayout.addWidget(btnCancel,2,2)
   

if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=QLabelBuddy()
    win.show()
    sys.exit(app.exec())