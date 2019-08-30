'''

显示列表数据（QListView控件）

数据源：

Model

需要创建控件和数据源，将之关联

'''
 
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QListView,QMessageBox
from PyQt5.QtCore import QStringListModel

class ListView(QWidget):
    def __init__(self,parent=None):
        super(ListView,self).__init__(parent)
        self.setWindowTitle("QList show")
        self.resize(300,100)
        
        layout=QVBoxLayout()
        
        listview=QListView()
        
        listModel=QStringListModel()
        self.list=["列表1","列表2","列表3","列表4","列表5"]
        listModel.setStringList(self.list)
        listview.setModel(listModel)
        
        listview.clicked.connect(self.clicked)
        layout.addWidget(listview)
       
        self.setLayout(layout)
    
    def clicked(self,item):
        QMessageBox.information(self,"QListView","您选择了:" + self.list[item.row()])
     
        
if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=ListView()
    win.show()
    sys.exit(app.exec())