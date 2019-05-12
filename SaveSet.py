# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SaveSet.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_setDialog(object):
    def setupUi(self, setDialog):
        setDialog.setObjectName("setDialog")
        setDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        setDialog.resize(455, 352)
        self.layoutWidget = QtWidgets.QWidget(setDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 411, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 30, 311, 20))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SaveImage = QtWidgets.QCheckBox(self.layoutWidget1)
        self.SaveImage.setChecked(True)
        self.SaveImage.setObjectName("SaveImage")
        self.horizontalLayout.addWidget(self.SaveImage)
        self.SaveImage_gray = QtWidgets.QCheckBox(self.layoutWidget1)
        self.SaveImage_gray.setObjectName("SaveImage_gray")
        self.horizontalLayout.addWidget(self.SaveImage_gray)
        self.SaveImage_edge = QtWidgets.QCheckBox(self.layoutWidget1)
        self.SaveImage_edge.setObjectName("SaveImage_edge")
        self.horizontalLayout.addWidget(self.SaveImage_edge)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 80, 381, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelImage = QtWidgets.QLabel(self.layoutWidget2)
        self.labelImage.setObjectName("labelImage")
        self.horizontalLayout_2.addWidget(self.labelImage)
        self.ImageFile = QtWidgets.QLineEdit(self.layoutWidget2)
        self.ImageFile.setObjectName("ImageFile")
        self.horizontalLayout_2.addWidget(self.ImageFile)
        self.ImgFileButton = QtWidgets.QPushButton(self.layoutWidget2)
        self.ImgFileButton.setObjectName("ImgFileButton")
        self.horizontalLayout_2.addWidget(self.ImgFileButton)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 80, 381, 25))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelVideo = QtWidgets.QLabel(self.layoutWidget3)
        self.labelVideo.setObjectName("labelVideo")
        self.horizontalLayout_3.addWidget(self.labelVideo)
        self.VideoFile = QtWidgets.QLineEdit(self.layoutWidget3)
        self.VideoFile.setObjectName("VideoFile")
        self.horizontalLayout_3.addWidget(self.VideoFile)
        self.VideoFileButton = QtWidgets.QPushButton(self.layoutWidget3)
        self.VideoFileButton.setObjectName("VideoFileButton")
        self.horizontalLayout_3.addWidget(self.VideoFileButton)
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget4.setGeometry(QtCore.QRect(20, 40, 101, 22))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelFPS = QtWidgets.QLabel(self.layoutWidget4)
        self.labelFPS.setObjectName("labelFPS")
        self.horizontalLayout_4.addWidget(self.labelFPS)
        self.FPS = QtWidgets.QSpinBox(self.layoutWidget4)
        self.FPS.setProperty("value", 30)
        self.FPS.setObjectName("FPS")
        self.horizontalLayout_4.addWidget(self.FPS)
        self.verticalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(setDialog)
        QtCore.QMetaObject.connectSlotsByName(setDialog)

    def retranslateUi(self, setDialog):
        _translate = QtCore.QCoreApplication.translate
        setDialog.setWindowTitle(_translate("setDialog", "图像获取设置"))
        self.groupBox.setTitle(_translate("setDialog", "拍照设置"))
        self.SaveImage.setText(_translate("setDialog", "实时图像"))
        self.SaveImage_gray.setText(_translate("setDialog", "灰度图像"))
        self.SaveImage_edge.setText(_translate("setDialog", "边缘检测图像"))
        self.labelImage.setText(_translate("setDialog", "保存位置"))
        self.ImageFile.setText(_translate("setDialog", ".../Gallery/"))
        self.ImgFileButton.setText(_translate("setDialog", "浏览"))
        self.groupBox_2.setTitle(_translate("setDialog", "录像设置"))
        self.labelVideo.setText(_translate("setDialog", "保存位置"))
        self.VideoFile.setText(_translate("setDialog", ".../Gallery/"))
        self.VideoFileButton.setText(_translate("setDialog", "浏览"))
        self.labelFPS.setText(_translate("setDialog", "帧率设置"))

class SaveSet(QtWidgets.QDialog,Ui_setDialog):
    def __init__(self,parent=None):
        super(SaveSet,self).__init__(parent)
        self.setupUi(self)
        filename = os.getcwd()
        self.ImageFile.setText(filename+'\Gallery')
        self.VideoFile.setText(filename+'\Gallery')
        self.filenameImage = filename+'\Gallery'
        self.filenameVideo = filename+'\Gallery'
        self.ImgFileButton.clicked.connect(self.Img)
        self.VideoFileButton.clicked.connect(self.Video)

    def Img(self):
        self.filenameImage=QFileDialog.getExistingDirectory(self,None)
        self.ImageFile.setText(self.filenameImage)

    def Video(self):
        self.filenameVideo=QFileDialog.getExistingDirectory(self,None)
        self.VideoFile.setText(self.filenameVideo)