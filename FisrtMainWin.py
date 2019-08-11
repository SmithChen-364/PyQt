import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon
class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWin,self).__init__(parent)

        self.setWindowTitle("第一个主窗口")
        self.resize(300,400)
        self.status=self.statusBar()

        self.status.showMessage("Hello world",5000)
if __name__ == "__main__":
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/music.ico"))
    main=FirstMainWin()
    main.show()
    sys.exit(app.exec_())