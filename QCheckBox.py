'''
QCheckBox(复选框控件：同时选择多个）

三种状态：
1.未选中：0
2.半选中:1
3.选中：2

'''
 
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class QCheckButtonDemo(QWidget):
    def __init__(self,parent=None):
        super(QCheckButtonDemo,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("复选框的示例")
        
        layout=QHBoxLayout()
        
        self.checkbox1=QCheckBox("复选框控件1")
        self.checkbox1.setChecked(True)   
        self.checkbox1.stateChanged.connect(lambda:self.CheckboxState(self.checkbox1))
        layout.addWidget(self.checkbox1)
        
        self.checkbox2=QCheckBox("复选框控件2")
        self.checkbox2.stateChanged.connect(lambda:self.CheckboxState(self.checkbox2))
        layout.addWidget(self.checkbox2)

        self.checkbox3=QCheckBox("半选中")  
        self.checkbox3.stateChanged.connect(lambda:self.CheckboxState(self.checkbox3))
        #设置半选中属性
        self.checkbox3.setTristate(True)
        self.checkbox3.setCheckState(Qt.PartiallyChecked)
        layout.addWidget(self.checkbox3)
        
        self.setLayout(layout)
        
    def CheckboxState(self,cb):
        checkstate1=self.checkbox1.text()+",isChecked"+str(self.checkbox1.isChecked())+",checkState="+str(self.checkbox1.checkState())+"\n"
        checkstate2=self.checkbox2.text()+",isChecked"+str(self.checkbox2.isChecked())+",checkState="+str(self.checkbox2.checkState())+"\n"
        checkstate3=self.checkbox3.text()+",isChecked"+str(self.checkbox3.isChecked())+",checkState="+str(self.checkbox3.checkState())+"\n"
        
        print(checkstate1+checkstate2+checkstate3)
        
        
if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=QCheckButtonDemo()
    win.show()
    sys.exit(app.exec())