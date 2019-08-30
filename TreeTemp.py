
'''

QTreeWidget
                                                                                        


'''
import  sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TreeWidgetDemo(QMainWindow):
    def __init__(self):
        super(TreeWidgetDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("树控件示例")  
        self.tree=QTreeWidget()
        
        #指定列数
        self.tree.setColumnCount(2)
        #指定列标签
        self.tree.setHeaderLabels(["key","value"])
        
        #在第一列添加结点
        root=QTreeWidgetItem(self.tree)
        root.setText(0,"根节点")
        root.setIcon(0,QIcon("./NewAI.jpg"))
        self.tree.setColumnWidth(0,120)
        
        #添加子结点1
        child1=QTreeWidgetItem(root)
        child1.setText(0,"child1")
        child1.setText(1,"1")
        
        child2=QTreeWidgetItem(root)
        child2.setText(0,"child2")
        child2.setText(1,"2")
        
        child3=QTreeWidgetItem(child2)
        child3.setText(0,"child3")
        child3.setText(1,"3")
        
        
        
        
        self.tree.clicked.connect(self.onTreeClicked)
        
        self.setCentralWidget(self.tree)
    
    def onTreeClicked(self,index):
        item=self.tree.currentItem()
        btnWidget=QWidget()
        btnlayout=QHBoxLayout()
        btn1=QPushButton("世界")
        btn2=QPushButton("你好")
        btn3=QPushButton("再见")
        
        btnlayout.addWidget(btn1)
        btnlayout.addWidget(btn2)
        btnlayout.addWidget(btn3)
        btnWidget.setLayout(btnlayout)

        self.tree.setItemWidget(item,1,btnWidget)
        
        print(index.row())
        print("key=%s,value=%s"%(item.text(0),item.text(1)))
      
              
        
  
if __name__ =="__main__":
     app=QApplication(sys.argv)
     win=TreeWidgetDemo()
     win.show()
     sys.exit(app.exec())