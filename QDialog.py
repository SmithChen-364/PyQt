'''
QDialog(对话框）

有哪些对话框：

1.QMessageBox(消息对话框）
2.QColorDialog(颜色）
3.QFileDialog
4.QFontDialog
5.QInputDialog

'''
 
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QDialog Demo")
        self.resize(300,200)
        
        self.button=QPushButton(self)
        self.button.setText("弹出对话框")
        self.button.move(50,50)
        self.button.clicked.connect(self.showDialog)
        
    def showDialog(self):
        dialog=QDialog()
        button=QPushButton("yes",dialog)
        button.clicked.connect(dialog.close)
        button.move(50,50)
        dialog.setWindowTitle("对话框")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()
        
        
        
if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=QDialogDemo()
    win.show()
    sys.exit(app.exec())