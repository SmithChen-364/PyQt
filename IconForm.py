#窗口的setWindowIcon方法用于设置窗口的图标，只有Windows可用
#QApplication中的setWindowIcon方法用于设置主窗口的图标
import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
class IconForm(QMainWindow):
    def __init__(self,parent=None):
        super(IconForm,self).__init__(parent)
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,250,250)
        self.setWindowTitle("设置窗口图标")
        self.setWindowIcon(QIcon("./images/music.ico"))

if __name__ == "__main__":
    myapp=QApplication(sys.argv)
    #myapp.setWindowIcon(QIcon("./images/music.ico"))
    main=IconForm()
    main.show()
    sys.exit(myapp.exec_())