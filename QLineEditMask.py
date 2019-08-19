'''
QLineEdit控件的输入的限制（用掩码）
Pyqt5支持的掩码见官方手册


'''
 
import sys
from PyQt5.QtWidgets import *


class QLineEditMask(QWidget):
    def __init__(self,parent=None):
        super(QLineEditMask,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QLineEdit的掩码")
        
        #表单布局
        formLayout=QFormLayout()
        
        
        ipLineEdit=QLineEdit()
        MacLineEdit=QLineEdit()
        dateLineEdit=QLineEdit()
        licenseLineEdit=QLineEdit()
        
        #设置ip掩码：192.168.0.100
        ipLineEdit.setInputMask("000.000.000.000;_")
        
        #设置MAC地址
        MacLineEdit.setInputMask("HH:HH:HH:HH:HH:HH;_")
        
        #设置日期
        dateLineEdit.setInputMask("0000-00-00")
        
        #设置验证码
        licenseLineEdit.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")
   
        formLayout.addRow("数字掩码 ", ipLineEdit)
        formLayout.addRow("MAC掩码",MacLineEdit)
        formLayout.addRow("日期掩码",dateLineEdit)
        formLayout.addRow("验证码",licenseLineEdit)
        
        self.setLayout(formLayout)
        
        
if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=QLineEditMask()
    win.show()
    sys.exit(app.exec())