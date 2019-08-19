'''
QTextEdit控件
输入多行文本

'''
 
import sys
from PyQt5.QtWidgets import *


class QTextEditItem(QWidget):
    def __init__(self,parent=None):
        super(QTextEditItem,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QTextEdit的示例")
        
        self.resize(300,360)
        
        self.textEdit=QTextEdit()
        self.buttonText=QPushButton("显示文本")
        self.buttonHtml=QPushButton("显示HTML")
        self.getbuttonText=QPushButton("获取文本")
        self.getbuttonHtml=QPushButton("获取HTML")
        
        layout=QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHtml)
        layout.addWidget(self.getbuttonText)
        layout.addWidget(self.getbuttonHtml)
        
        self.setLayout(layout)
        self.buttonText.clicked.connect(self.onClink_ButtonText)
        self.buttonHtml.clicked.connect(self.onClink_ButtonHtml)
        self.getbuttonText.clicked.connect(self.getText)
        self.getbuttonHtml.clicked.connect(self.getHtml)
        
    def onClink_ButtonText(self):
        self.textEdit.setPlainText("世界你好，我喜欢爱酱")
    
    def onClink_ButtonHtml(self):
        self.textEdit.setHtml("<font color='blue' size='5'>世界你好</font>")
        
    def getText(self):
        print(self.textEdit.toPlainText())
        
    def getHtml(self):
        print(self.textEdit.toHtml())
    
        
if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=QTextEditItem()
    win.show()
    sys.exit(app.exec())