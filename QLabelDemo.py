'''QLabel控件：
setAlignment():设置文件的对齐方式
setIndent():设置文本缩进
text():获取文本内容
setBuddy():设置伙伴关系
setText():设置文本内容
selectedText():返回所选择的字符
setWordWrap():设置是否换行
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette,QPixmap
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.initUI()
    def initUI(self):
        label1=QLabel(self)
        label2=QLabel(self)
        label3=QLabel(self)
        label4=QLabel(self)
        
        label1.setText("<font color =yellow>这是一个文本标签</font>")
        label1.setAutoFillBackground(True)
        palette=QPalette()
        #设置背景色
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)
        
        label2.setText("<a href = '#'>欢迎</a>")
        
        label3.setAlignment(Qt.AlignCenter)
        
        label3.setToolTip("picture")
        label3.setPixmap(QPixmap("./images/NewAI.jpg"))
        
        #设置打开外部链接
        label4.setOpenExternalLinks(True)
        label4.setText("<a href ='http://www.baidu.com'>百度</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip("这是一个链接")
        
        vbox=QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        
      
        
        label2.linkHovered.connect(self.linkHoverde)
        label4.linkActivated.connect(self.linkClicked)
        
        
        self.setLayout(vbox)
        self.setWindowTitle("QLabel控件演示")
        
        
        
    def linkHoverde(self):
        print("鼠标滑过")
    
    def linkClicked(self):
        print("鼠标单击")
        

if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=QLabelDemo()
    win.show()
    sys.exit(app.exec())