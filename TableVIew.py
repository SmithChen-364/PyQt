'''

显示二维表数据（QTableView）

数据源：

Model

需要创建控件和数据源，将之关联

'''
 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class TableView(QWidget):
    def __init__(self,arg=None):
        super(TableView,self).__init__(arg)
        self.setWindowTitle("QTableView show")
        self.resize(500,300)
        self.model=QStandardItemModel(4,3)
        self.model.setHorizontalHeaderLabels(["id","name","age"])
        self.tableView=QTableView()
        #关联控件和数据模型
        self.tableView.setModel(self.model)
        
        
        #添加数据,每一个单元格是一个item
        item1=QStandardItem("10")
        item2=QStandardItem("小明")
        item3=QStandardItem("30")
        self.model.setItem(0, 0, item1)
        self.model.setItem(0, 1, item2)
        self.model.setItem(0, 2, item3)
        
        layout=QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)
        
        
        
if __name__ =="__main__":
    app=QApplication(sys.argv)
    w=TableView()
    w.move(300,300)
    w.show()
    sys.exit(app.exec())