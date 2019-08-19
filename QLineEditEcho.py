'''
QLineEdit控件与回显模式
基本功能:输入单行的文本
EchoMode(回显模式）
4种回显模式

1.Normal
2.NoEcho(就是Linux输入密码时，用户看不到那种）
3.Password(回显为 .或*等）
4.PasswordEchoOnEdit(输入时能看到，马上就变成点或星号那种）

'''
 
import sys
from PyQt5.QtWidgets import *


class QLineEditEchoMode(QWidget):
    def __init__(self,parent=None):
        super(QLineEditEchoMode,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QLineEdit的回显模式")
        #表单布局 
        formLayout=QFormLayout()
        normalLineEdit=QLineEdit()
        noEchoLineEdit=QLineEdit()
        passwordLineEdit=QLineEdit()
        passwordEchoLineEdit=QLineEdit()
        
        formLayout.addRow("Normal", normalLineEdit)
        formLayout.addRow("NoEcho",noEchoLineEdit)
        formLayout.addRow("password", passwordLineEdit)
        formLayout.addRow("PasswordEcho", passwordEchoLineEdit)
        
        #文本输入框在没有输入时的默认显示
        
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoLineEdit.setPlaceholderText("PasswordEcho")
        
        #设置回显模式
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        
        self.setLayout(formLayout)
        
        
        
if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=QLineEditEchoMode()
    win.show()
    sys.exit(app.exec())