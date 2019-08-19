'''
QComboBox(下拉列表控件）

'''
 
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class QComboBoxDemo(QWidget):
    def __init__(self,parent=None):
        super(QComboBoxDemo,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QComboBox Demo")
        self.resize(300,100)
        
        
        layout=QVBoxLayout()
        self.label=QLabel("请选择语言")
        self.cb=QComboBox()
        self.cb.addItem("C++")
        self.cb.addItems(["Java","Python","Ruby"])
        
        self.cb.currentIndexChanged.connect(self.selectionChange)
        layout.addWidget(self.label)
        layout.addWidget(self.cb)
        self.setLayout(layout)
        
        
    def selectionChange(self,i):
        self.label.setText(self.cb.currentText())
        self.label.adjustSize()
        
        for count in range(self.cb.count()):
            print("item" + str(count)+"="+self.cb.itemText(count))
            print("current index",i,"selection changed",self.cb.currentText())
        
        
        
        
if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=QComboBoxDemo()
    win.show()
    sys.exit(app.exec())