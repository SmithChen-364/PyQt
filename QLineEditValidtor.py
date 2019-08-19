'''
QLineEdit控件的输入的限制（校验器）

限制只能输入整数，浮点数或满足一定条件的字符串

'''
 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp
from astropy.io.votable.converters import Double



class QLineEditValidator(QWidget):
    def __init__(self,parent=None):
        super(QLineEditValidator,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QLineEdit的校验器")
        
        formLayout=QFormLayout()
        
        intLineEdit=QLineEdit()
        doubleLineEdit=QLineEdit()
        reLineEdit=QLineEdit()
        
        
        formLayout.addRow("int", intLineEdit)
        formLayout.addRow("double",doubleLineEdit)
        formLayout.addRow("数字和字母",reLineEdit)
        
        #文本输入框在没有输入时的默认显示
        
        intLineEdit.setPlaceholderText("整数")
        doubleLineEdit.setPlaceholderText("浮点数")
        reLineEdit.setPlaceholderText("数字和字母")
        
        #整数校验器
        intValidator=QIntValidator(self)
        intValidator.setRange(1,99)
        
        #浮点数检验
        doubleValidator=QDoubleValidator(self)
        doubleValidator.setRange(-360,360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        #设置精度，小数点2位
        doubleValidator.setDecimals(2)
        
        #字符和数字
        reg=QRegExp("[a-zA-Z0-9]+$")
        revalidator=QRegExpValidator(self)
        revalidator.setRegExp(reg)
        
        #设置校验器
        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        reLineEdit.setValidator(revalidator)
        
        self.setLayout(formLayout)
        
        
if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=QLineEditValidator()
    win.show()
    sys.exit(app.exec())