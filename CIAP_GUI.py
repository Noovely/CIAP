# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CIAP_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1306, 574)
        MainWindow.setMinimumSize(QtCore.QSize(10, 10))
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 1301, 523))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_pro = QtWidgets.QLabel(self.layoutWidget)
        self.label_pro.setMinimumSize(QtCore.QSize(100, 22))
        self.label_pro.setMaximumSize(QtCore.QSize(16777215, 23))
        self.label_pro.setObjectName("label_pro")
        self.verticalLayout_3.addWidget(self.label_pro)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Label_sat = QtWidgets.QLabel(self.layoutWidget)
        self.Label_sat.setMinimumSize(QtCore.QSize(0, 16))
        self.Label_sat.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_sat.setObjectName("Label_sat")
        self.gridLayout.addWidget(self.Label_sat, 1, 0, 1, 1)
        self.Label_sha = QtWidgets.QLabel(self.layoutWidget)
        self.Label_sha.setMinimumSize(QtCore.QSize(0, 16))
        self.Label_sha.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_sha.setObjectName("Label_sha")
        self.gridLayout.addWidget(self.Label_sha, 2, 0, 1, 1)
        self.Label_gaiV = QtWidgets.QLabel(self.layoutWidget)
        self.Label_gaiV.setObjectName("Label_gaiV")
        self.gridLayout.addWidget(self.Label_gaiV, 2, 3, 1, 1)
        self.Label_gamV = QtWidgets.QLabel(self.layoutWidget)
        self.Label_gamV.setObjectName("Label_gamV")
        self.gridLayout.addWidget(self.Label_gamV, 3, 1, 1, 1)
        self.Label_FPSV = QtWidgets.QLabel(self.layoutWidget)
        self.Label_FPSV.setObjectName("Label_FPSV")
        self.gridLayout.addWidget(self.Label_FPSV, 3, 3, 1, 1)
        self.Label_con = QtWidgets.QLabel(self.layoutWidget)
        self.Label_con.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_con.setObjectName("Label_con")
        self.gridLayout.addWidget(self.Label_con, 0, 2, 1, 1)
        self.Label_shaV = QtWidgets.QLabel(self.layoutWidget)
        self.Label_shaV.setObjectName("Label_shaV")
        self.gridLayout.addWidget(self.Label_shaV, 2, 1, 1, 1)
        self.Label_gai = QtWidgets.QLabel(self.layoutWidget)
        self.Label_gai.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_gai.setObjectName("Label_gai")
        self.gridLayout.addWidget(self.Label_gai, 2, 2, 1, 1)
        self.Label_hueV = QtWidgets.QLabel(self.layoutWidget)
        self.Label_hueV.setObjectName("Label_hueV")
        self.gridLayout.addWidget(self.Label_hueV, 1, 3, 1, 1)
        self.Label_gam = QtWidgets.QLabel(self.layoutWidget)
        self.Label_gam.setMinimumSize(QtCore.QSize(0, 16))
        self.Label_gam.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_gam.setObjectName("Label_gam")
        self.gridLayout.addWidget(self.Label_gam, 3, 0, 1, 1)
        self.Label_FPS = QtWidgets.QLabel(self.layoutWidget)
        self.Label_FPS.setMinimumSize(QtCore.QSize(0, 16))
        self.Label_FPS.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_FPS.setObjectName("Label_FPS")
        self.gridLayout.addWidget(self.Label_FPS, 3, 2, 1, 1)
        self.Label_briV = QtWidgets.QLabel(self.layoutWidget)
        self.Label_briV.setObjectName("Label_briV")
        self.gridLayout.addWidget(self.Label_briV, 0, 1, 1, 1)
        self.Label_bri = QtWidgets.QLabel(self.layoutWidget)
        self.Label_bri.setMinimumSize(QtCore.QSize(0, 16))
        self.Label_bri.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Label_bri.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_bri.setObjectName("Label_bri")
        self.gridLayout.addWidget(self.Label_bri, 0, 0, 1, 1)
        self.Label_conV = QtWidgets.QLabel(self.layoutWidget)
        self.Label_conV.setObjectName("Label_conV")
        self.gridLayout.addWidget(self.Label_conV, 0, 3, 1, 1)
        self.Label_satV = QtWidgets.QLabel(self.layoutWidget)
        self.Label_satV.setObjectName("Label_satV")
        self.gridLayout.addWidget(self.Label_satV, 1, 1, 1, 1)
        self.Label_hue = QtWidgets.QLabel(self.layoutWidget)
        self.Label_hue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_hue.setObjectName("Label_hue")
        self.gridLayout.addWidget(self.Label_hue, 1, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_hist = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_hist.sizePolicy().hasHeightForWidth())
        self.label_hist.setSizePolicy(sizePolicy)
        self.label_hist.setMinimumSize(QtCore.QSize(100, 20))
        self.label_hist.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_hist.setObjectName("label_hist")
        self.horizontalLayout_2.addWidget(self.label_hist)
        spacerItem = QtWidgets.QSpacerItem(138, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.ButtonSet = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonSet.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonSet.setObjectName("ButtonSet")
        self.horizontalLayout_2.addWidget(self.ButtonSet)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.histWidget = MatplotlibWidget(self.layoutWidget)
        self.histWidget.setMinimumSize(QtCore.QSize(378, 370))
        self.histWidget.setObjectName("histWidget")
        self.verticalLayout_3.addWidget(self.histWidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_cam = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_cam.sizePolicy().hasHeightForWidth())
        self.label_cam.setSizePolicy(sizePolicy)
        self.label_cam.setMinimumSize(QtCore.QSize(100, 24))
        self.label_cam.setObjectName("label_cam")
        self.verticalLayout.addWidget(self.label_cam)
        self.imagelabel = QtWidgets.QLabel(self.layoutWidget)
        self.imagelabel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imagelabel.sizePolicy().hasHeightForWidth())
        self.imagelabel.setSizePolicy(sizePolicy)
        self.imagelabel.setMinimumSize(QtCore.QSize(600, 450))
        self.imagelabel.setMaximumSize(QtCore.QSize(600, 450))
        self.imagelabel.setText("")
        self.imagelabel.setPixmap(QtGui.QPixmap("source/nonentity.png"))
        self.imagelabel.setScaledContents(True)
        self.imagelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imagelabel.setObjectName("imagelabel")
        self.verticalLayout.addWidget(self.imagelabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonChoose = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonChoose.sizePolicy().hasHeightForWidth())
        self.buttonChoose.setSizePolicy(sizePolicy)
        self.buttonChoose.setMinimumSize(QtCore.QSize(80, 23))
        self.buttonChoose.setMaximumSize(QtCore.QSize(1888, 223445))
        self.buttonChoose.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonChoose.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttonChoose.setObjectName("buttonChoose")
        self.horizontalLayout_3.addWidget(self.buttonChoose)
        spacerItem1 = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.ButtonStop = QtWidgets.QPushButton(self.layoutWidget)
        self.ButtonStop.setMinimumSize(QtCore.QSize(60, 26))
        self.ButtonStop.setMaximumSize(QtCore.QSize(50, 16777215))
        self.ButtonStop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonStop.setCheckable(True)
        self.ButtonStop.setObjectName("ButtonStop")
        self.horizontalLayout_3.addWidget(self.ButtonStop)
        self.buttonvideo = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonvideo.sizePolicy().hasHeightForWidth())
        self.buttonvideo.setSizePolicy(sizePolicy)
        self.buttonvideo.setMinimumSize(QtCore.QSize(60, 23))
        self.buttonvideo.setMaximumSize(QtCore.QSize(60, 30))
        self.buttonvideo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonvideo.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttonvideo.setCheckable(True)
        self.buttonvideo.setChecked(False)
        self.buttonvideo.setObjectName("buttonvideo")
        self.horizontalLayout_3.addWidget(self.buttonvideo)
        self.buttoncamera = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttoncamera.sizePolicy().hasHeightForWidth())
        self.buttoncamera.setSizePolicy(sizePolicy)
        self.buttoncamera.setMinimumSize(QtCore.QSize(60, 23))
        self.buttoncamera.setMaximumSize(QtCore.QSize(60, 30))
        self.buttoncamera.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttoncamera.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttoncamera.setObjectName("buttoncamera")
        self.horizontalLayout_3.addWidget(self.buttoncamera)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_gray = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(24)
        sizePolicy.setHeightForWidth(self.label_gray.sizePolicy().hasHeightForWidth())
        self.label_gray.setSizePolicy(sizePolicy)
        self.label_gray.setMinimumSize(QtCore.QSize(100, 22))
        self.label_gray.setMaximumSize(QtCore.QSize(16777215, 22))
        self.label_gray.setObjectName("label_gray")
        self.verticalLayout_2.addWidget(self.label_gray)
        self.imageLabel_gray = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel_gray.sizePolicy().hasHeightForWidth())
        self.imageLabel_gray.setSizePolicy(sizePolicy)
        self.imageLabel_gray.setMinimumSize(QtCore.QSize(300, 225))
        self.imageLabel_gray.setMaximumSize(QtCore.QSize(300, 225))
        self.imageLabel_gray.setText("")
        self.imageLabel_gray.setPixmap(QtGui.QPixmap("source/nonentity.png"))
        self.imageLabel_gray.setScaledContents(True)
        self.imageLabel_gray.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel_gray.setObjectName("imageLabel_gray")
        self.verticalLayout_2.addWidget(self.imageLabel_gray)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cannyLabel = QtWidgets.QLabel(self.layoutWidget)
        self.cannyLabel.setMinimumSize(QtCore.QSize(100, 22))
        self.cannyLabel.setMaximumSize(QtCore.QSize(16777215, 22))
        self.cannyLabel.setObjectName("cannyLabel")
        self.horizontalLayout.addWidget(self.cannyLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.lowThresholdLabel = QtWidgets.QLabel(self.layoutWidget)
        self.lowThresholdLabel.setObjectName("lowThresholdLabel")
        self.horizontalLayout.addWidget(self.lowThresholdLabel)
        self.Threshold1 = QtWidgets.QSpinBox(self.layoutWidget)
        self.Threshold1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Threshold1.setMaximum(500)
        self.Threshold1.setProperty("value", 20)
        self.Threshold1.setObjectName("Threshold1")
        self.horizontalLayout.addWidget(self.Threshold1)
        self.highThresholdLabel = QtWidgets.QLabel(self.layoutWidget)
        self.highThresholdLabel.setObjectName("highThresholdLabel")
        self.horizontalLayout.addWidget(self.highThresholdLabel)
        self.Threshold2 = QtWidgets.QSpinBox(self.layoutWidget)
        self.Threshold2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Threshold2.setMaximum(1000)
        self.Threshold2.setProperty("value", 50)
        self.Threshold2.setObjectName("Threshold2")
        self.horizontalLayout.addWidget(self.Threshold2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.imageLabel_edge = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel_edge.sizePolicy().hasHeightForWidth())
        self.imageLabel_edge.setSizePolicy(sizePolicy)
        self.imageLabel_edge.setMinimumSize(QtCore.QSize(300, 225))
        self.imageLabel_edge.setMaximumSize(QtCore.QSize(300, 225))
        self.imageLabel_edge.setText("")
        self.imageLabel_edge.setPixmap(QtGui.QPixmap("source/nonentity.png"))
        self.imageLabel_edge.setScaledContents(True)
        self.imageLabel_edge.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel_edge.setObjectName("imageLabel_edge")
        self.verticalLayout_2.addWidget(self.imageLabel_edge)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1306, 23))
        self.menubar.setObjectName("menubar")
        self.SettingMenu = QtWidgets.QMenu(self.menubar)
        self.SettingMenu.setObjectName("SettingMenu")
        self.HelpMenu = QtWidgets.QMenu(self.menubar)
        self.HelpMenu.setObjectName("HelpMenu")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.status = QtWidgets.QStatusBar(MainWindow)
        self.status.setObjectName("status")
        MainWindow.setStatusBar(self.status)
        self.setPropertyAction = QtWidgets.QAction(MainWindow)
        self.setPropertyAction.setObjectName("setPropertyAction")
        self.DefaultAction = QtWidgets.QAction(MainWindow)
        self.DefaultAction.setObjectName("DefaultAction")
        self.AboutAction = QtWidgets.QAction(MainWindow)
        self.AboutAction.setObjectName("AboutAction")
        self.HelpAction = QtWidgets.QAction(MainWindow)
        self.HelpAction.setObjectName("HelpAction")
        self.ChooseCameraAction = QtWidgets.QAction(MainWindow)
        self.ChooseCameraAction.setObjectName("ChooseCameraAction")
        self.SaveSetAction = QtWidgets.QAction(MainWindow)
        self.SaveSetAction.setObjectName("SaveSetAction")
        self.FaceDetection = QtWidgets.QAction(MainWindow)
        self.FaceDetection.setCheckable(True)
        self.FaceDetection.setChecked(False)
        self.FaceDetection.setEnabled(True)
        self.FaceDetection.setObjectName("FaceDetection")
        self.FaceRecognition = QtWidgets.QAction(MainWindow)
        self.FaceRecognition.setCheckable(True)
        self.FaceRecognition.setObjectName("FaceRecognition")
        self.FaceCapture = QtWidgets.QAction(MainWindow)
        self.FaceCapture.setCheckable(True)
        self.FaceCapture.setObjectName("FaceCapture")
        self.ModelTraining = QtWidgets.QAction(MainWindow)
        self.ModelTraining.setObjectName("ModelTraining")
        self.ModelTraining.setEnabled(False)
        self.SettingMenu.addAction(self.ChooseCameraAction)
        self.SettingMenu.addAction(self.setPropertyAction)
        self.SettingMenu.addAction(self.SaveSetAction)
        self.SettingMenu.addSeparator()
        self.SettingMenu.addAction(self.DefaultAction)
        self.HelpMenu.addAction(self.AboutAction)
        self.HelpMenu.addAction(self.HelpAction)
        self.menu.addAction(self.FaceDetection)
        self.menu.addAction(self.FaceRecognition)
        self.menu.addSeparator()
        self.menu.addAction(self.FaceCapture)
        self.menu.addAction(self.ModelTraining)
        self.menubar.addAction(self.SettingMenu.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.HelpMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "USB摄像头图像获取及处理软件"))
        self.label_pro.setText(_translate("MainWindow", " 当前参数"))
        self.Label_sat.setText(_translate("MainWindow", "饱和度值："))
        self.Label_sha.setText(_translate("MainWindow", "锐 度 值："))
        self.Label_gaiV.setText(_translate("MainWindow", "0"))
        self.Label_gamV.setText(_translate("MainWindow", "0"))
        self.Label_FPSV.setText(_translate("MainWindow", "30"))
        self.Label_con.setText(_translate("MainWindow", "对比度值："))
        self.Label_shaV.setText(_translate("MainWindow", "0"))
        self.Label_gai.setText(_translate("MainWindow", "增 益 值："))
        self.Label_hueV.setText(_translate("MainWindow", "0"))
        self.Label_gam.setText(_translate("MainWindow", "灰度系数："))
        self.Label_FPS.setText(_translate("MainWindow", "帧    率："))
        self.Label_briV.setText(_translate("MainWindow", "0"))
        self.Label_bri.setText(_translate("MainWindow", "           亮 度 值："))
        self.Label_conV.setText(_translate("MainWindow", "0    "))
        self.Label_satV.setText(_translate("MainWindow", "0"))
        self.Label_hue.setText(_translate("MainWindow", "色 调 值："))
        self.label_hist.setText(_translate("MainWindow", " 直方图"))
        self.ButtonSet.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>摄像头属性参数的设置</p></body></html>"))
        self.ButtonSet.setText(_translate("MainWindow", "参数设置"))
        self.label_cam.setText(_translate("MainWindow", "实时图像"))
        self.buttonChoose.setText(_translate("MainWindow", "切换摄像头"))
        self.ButtonStop.setText(_translate("MainWindow", "暂停"))
        self.buttonvideo.setText(_translate("MainWindow", "录像"))
        self.buttoncamera.setText(_translate("MainWindow", "拍照"))
        self.label_gray.setText(_translate("MainWindow", "灰度图像"))
        self.cannyLabel.setText(_translate("MainWindow", "边缘检测"))
        self.lowThresholdLabel.setText(_translate("MainWindow", "阈值1"))
        self.highThresholdLabel.setText(_translate("MainWindow", "阈值2"))
        self.SettingMenu.setTitle(_translate("MainWindow", "图像采集"))
        self.HelpMenu.setTitle(_translate("MainWindow", "帮助"))
        self.menu.setTitle(_translate("MainWindow", "人脸识别"))
        self.setPropertyAction.setText(_translate("MainWindow", "摄像头参数设置"))
        self.setPropertyAction.setShortcut(_translate("MainWindow", "Alt+P"))
        self.DefaultAction.setText(_translate("MainWindow", "恢复初始值"))
        self.DefaultAction.setToolTip(_translate("MainWindow", "恢复初始值"))
        self.DefaultAction.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.AboutAction.setText(_translate("MainWindow", "关于"))
        self.AboutAction.setShortcut(_translate("MainWindow", "Alt+A"))
        self.HelpAction.setText(_translate("MainWindow", "帮助"))
        self.HelpAction.setShortcut(_translate("MainWindow", "Alt+H"))
        self.ChooseCameraAction.setText(_translate("MainWindow", "切换摄像头"))
        self.ChooseCameraAction.setShortcut(_translate("MainWindow", "Alt+C"))
        self.SaveSetAction.setText(_translate("MainWindow", "图像获取设置"))
        self.SaveSetAction.setShortcut(_translate("MainWindow", "Alt+S"))
        self.FaceDetection.setText(_translate("MainWindow", "人脸检测"))
        self.FaceRecognition.setText(_translate("MainWindow", "人脸识别"))
        self.FaceCapture.setText(_translate("MainWindow", "人脸采集"))
        self.ModelTraining.setText(_translate("MainWindow", "模型训练"))

from MatplotlibWidget import MatplotlibWidget
