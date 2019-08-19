'''
QSlider(滑块控件）

'''
 
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class QSliderDemo(QWidget):
    def __init__(self,parent=None):
        super(QSliderDemo,self).__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("QSliderDemo Demo")
        self.resize(300,100)
        
        #选择垂直布局
        layout=QVBoxLayout()
        self.label=QLabel("你好 Pyqt5")
        self.label.setAlignment(Qt.AlignCenter)
        
        self.slider=QSlider(Qt.Horizontal)
        #设置最小值和最大值
        self.slider.setMinimum(12)
        self.slider.setMaximum(49)
        
        #设置步长
        self.slider.setSingleStep(2)
        
        #设置当前值
        self.slider.setValue(18)
        
        #设置刻度的位置，刻度在下方
        self.slider.setTickPosition(QSlider.TicksBelow)
        
        #设置刻度的间隔
        self.slider.setTickInterval(5)
       
        #添加到布局上
        layout.addWidget(self.label)
        layout.addWidget(self.slider)
        
        #绑定信号与槽
        self.slider.valueChanged.connect(self.valueChange)
        
        #设置窗口布局
        self.setLayout(layout)
        
    def valueChange(self):
        print("当前值 :%s" %self.slider.value())
        size=self.slider.value()
        self.label.setFont(QFont("Arial",size))
        
        
        
if __name__ =="__main__":
    app=QApplication(sys.argv)
    win=QSliderDemo()
    win.show()
    sys.exit(app.exec())