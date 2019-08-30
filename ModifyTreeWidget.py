'''

添加，修改，删除树控件的结点
                                                                                        


'''
import  sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ModifyTree(QWidget):
    def __init__(self):
        super(ModifyTree,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("修改树结点")  
        
        layout=QHBoxLayout()
        addbtn=QPushButton("添加结点")
        modbtn=QPushButton("修改结点")
        delbtn=QPushButton("删除结点")
        
        layout.addWidget(addbtn)
        layout.addWidget(modbtn)
        layout.addWidget(delbtn)
        
        addbtn.clicked.connect(self.addNode)
        modbtn.clicked.connect(self.modNode)
        delbtn.clicked.connect(self.delNode)
        
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
        
        mainlayout=QVBoxLayout()
        mainlayout.addLayout(layout)
        mainlayout.addWidget(self.tree)
        self.setLayout(mainlayout)
        
        
        
    def addNode(self):
        print("添加结点")
        item=self.tree.currentItem()
        print(item)
        node=QTreeWidgetItem(item)
        node.setText(0,"新结点")
        node.setText(1,"新值")
    def modNode(self):
        print("修改结点")
        item=self.tree.currentItem()
        item.setText(0,"修改结点")
        item.setText(1,"修改值")
    def delNode(self):
        print("删除结点")
        item=self.tree.currentItem()
        root=self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)
            
    
        
        
    
    def onTreeClicked(self,index):
        item=self.tree.currentItem()
        print(index.row())
        print("key=%s,value=%s"%(item.text(0),item.text(1)))
      
              
        
  
if __name__ =="__main__":
     app=QApplication(sys.argv)
     win=ModifyTree()
     win.show()
     sys.exit(app.exec())