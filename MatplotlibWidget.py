#USB摄像头图像获取及处理软件

#刘阳
#使用Matplotlib绘制直方图

import sys
import matplotlib
import cv2

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

class MyMplCanvas(FigureCanvas):
    """FigureCanvas的最终的父类其实是QWidget。"""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

        self.fig = Figure(figsize=(width, height), dpi=dpi)  # 新建一个figure
        self.axes = self.fig.add_subplot(111)  # 建立一个子图，如果要建立复合图，可以在这里修改
        self.fig.subplots_adjust(left=0.180, bottom=0.110, right=0.990, top=0.990,wspace=None, hspace=None)

        #self.axes.hold(False)  # 每次绘图的时候不保留上一次绘图的结果

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        '''定义FigureCanvas的尺寸策略，这部分的意思是设置FigureCanvas，使之尽可能的向外填充空间。'''
        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)

        FigureCanvas.updateGeometry(self)

    '''绘图，可以在这里定义自己的绘图逻辑'''
    def plot(self,histr=[0]):
        
        self.axes.cla()
        self.axes.plot(histr)
        self.axes.set_ylabel('像素值数量')
        self.axes.set_xlabel('灰度级')
        self.axes.set_xlim((0,256))
        #self.axes.grid(True)
        self.draw()

class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.layout = QVBoxLayout(self)
        self.histMP = MyMplCanvas(self, width=3.78, height=3.86, dpi=100)
        #self.histMP.plot() # 如果你想要初始化的时候就呈现静态图，请把这行注释去掉
        self.layout.addWidget(self.histMP)

        #self.mpl_ntb = NavigationToolbar(self.histMP, self)  # 添加完整的 toolbar
        #self.layout.addWidget(self.mpl_ntb)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
    img = cv2.imread(r'image/lena.jpg')
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    histr = cv2.calcHist([img],[0],None,[256],[0,256])
    ui.histMP.plot(histr)     #测试静态图效果
    #ui.Tool()
    ui.show()
    sys.exit(app.exec_())