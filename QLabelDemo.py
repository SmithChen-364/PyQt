'''QLabel控件：
setAlignment():设置文件的对齐方式
setIndent():设置文本缩进
text():获取文本内容
setBuddy():设置伙伴关系
setText():设置文本内容
selectedText()：返回所选择的字符
setWordWrap():设置是否允许换行

QLabel常用的信号（事件）:

1.鼠标滑过控件时触发：linkHovered
2.鼠标单击控件时触发:linkActivated
'''
import sys
from PyQt5.QtWidgets import QVBoxLayout,QMainWindow,QApplication,QLabel,QPushButton,QWidget
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        label1=QLabel(self)
        label2=QLabel(self)
        label3=QLabel(self)
        label4=QLabel(self)
        label1.setText("<font color=yellow>这是一个文本标签</font>")
        label.set
        palette=QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href ='#'>welcome</a>")
        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip("这是一个图片标签")
        layout=QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        label2.linkHovered.connect(self.linkHovered)
        label3.linkActivated.connect(self.linkClinked)

    
    def linkHovered(self):
        print("鼠标正在滑过")
    def linkClinked(self):
        print("鼠标正在点击")

if __name__ == "__main__":
    myapp=QApplication(sys.argv)
    main=QLabelDemo()
    main.show()
    sys.exit(myapp.exec_())