#USB摄像头图像获取及处理软件

#刘阳
#2018.06.06 尝试加入人脸检测
#2018.06.12 加入人脸识别

import sys
import time

import numpy as np
from PyQt5.QtCore import QThread, QTimer, pyqtSignal
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

import CIAP_GUI
import cv2
import SaveSet
import setProperty


class CIAP(QMainWindow,CIAP_GUI.Ui_MainWindow):                 #GUI实例化
    def __init__(self,parent=None):
        super(CIAP,self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        #主界面初始化
        QApplication.setStyle('Fusion')
        self.ChooseCameraAction.triggered.connect(self.ChooseCamera)    #菜单-设置-切换摄像头
        self.setPropertyAction.triggered.connect(self.setProperty)      #菜单-设置-摄像头设置
        self.SaveSetAction.triggered.connect(self.setSave)              #菜单-设置-获取图像设置
        self.DefaultAction.triggered.connect(self.DefaultProperty)      #菜单-设置-恢复默认值
        self.ModelTraining.triggered.connect(self.TrainModel)             #菜单-人脸识别-模型训练
        self.AboutAction.triggered.connect(self.helpAbout)              #菜单-帮助-关于
        self.HelpAction.triggered.connect(self.helpHelp)                #菜单-帮助-帮助
        self.ButtonSet.clicked.connect(self.setProperty)                #按钮-参数设置
        self.buttonChoose.clicked.connect(self.ChooseCamera)            #按钮-切换摄像头
        self.ButtonStop.clicked.connect(self.timeStop)                  #按钮-暂停
        self.buttoncamera.clicked.connect(self.SavePicture)             #按钮-拍照
        self.buttonvideo.clicked.connect(self.SaveVideo)                #按钮-录像
        self.Threshold1.valueChanged.connect(self.CannylowThreshold)    #计数器-阈值1
        self.Threshold2.valueChanged.connect(self.CannyhighThreshold)   #计数器-阈值2

        self.face_patterns = cv2.CascadeClassifier('source/haarcascade_frontalface_default.xml')     #加载人脸检测分类器
        self.model = cv2.face.LBPHFaceRecognizer_create()                   #加载我自己训练的分类器
        self.model.read("source/liuyang.xml")
        #self.face_patterns = cv2.CascadeClassifier("haarcascades/liuyang.xml")
        
        self.faceCaptureFlag=1

        #获取摄像头
        self.cameraID = 0                                       
        self.camera=cv2.VideoCapture(self.cameraID)
        if(self.camera.isOpened()):
            self.initProperty()                                 #摄像头属性参数初始化
            self.changeFirst=1                                  #一个标识，用于属性参数调整     
            self.SaveSet = SaveSet.SaveSet()                    #实例化图像获取设置对话框
            self.timer = QTimer(self)                           #初始化一个定时器
            self.timer.timeout.connect(self.CameraPicture)      #定时读取帧，用于界面显示
            self.timer.start(50)                                #按照帧率设置定时
            self.timerVideo = QTimer(self)                      #初始化第二个个定时器
            self.timerVideo.timeout.connect(self.VideoFrame)    #定时读取帧，用于录像
        else:
            reply = QMessageBox.critical(self,"错误","获取摄像头失败",QMessageBox.Ok)
            if reply == QMessageBox.Ok:
                close()

    def CameraPicture(self):  
        #摄像头视频图像获取及处理函数      
        ret,self.frame=self.camera.read()                            #获取摄像头帧
        self.image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)          #实时图像变换彩色空间顺序
        self.image_gray = cv2.cvtColor(self.frame,cv2.COLOR_BGR2GRAY)     #变换色彩空间得到灰度图像
        self.image_edge = cv2.Canny(self.image_gray,self.lowThreshold,self.highThreshold)             #canny边缘检测 
        self.face()      #人脸检测
        Q_image = QImage(self.image.data, self.image.shape[1], self.image.shape[0],QImage.Format_RGB888)                           #转换为QImage对象
        Q_image_gray = QImage(self.image_gray.data,self.image_gray.shape[1], self.image_gray.shape[0],QImage.Format_Grayscale8)    #灰度图转换为QImage对象
        Q_image_edge = QImage(self.image_edge.data,self.image_edge.shape[1], self.image_edge.shape[0],QImage.Format_Grayscale8)
        self.imagelabel.setPixmap(QPixmap.fromImage(Q_image))                    #设置imagelabel显示实时图像
        self.imageLabel_gray.setPixmap(QPixmap.fromImage(Q_image_gray))          #设置imageLabel_gray显示灰度图像
        self.imageLabel_edge.setPixmap(QPixmap.fromImage(Q_image_edge))
        self.hist = cv2.calcHist([self.image_gray],[0],None,[256],[0,256])      #计算直方图参数
        self.histWidget.histMP.plot(self.hist)                                  #在GUI上显示直方图
    
    def face(self):
        #人脸检测与识别函数
        self.FaceCapture.setEnabled(False)
        self.FaceRecognition.setEnabled(False)
        if(self.FaceDetection.isChecked()):         #人脸检测
            self.FaceCapture.setEnabled(True)
            self.FaceRecognition.setEnabled(True)
            faces = self.face_patterns.detectMultiScale(self.image_gray,scaleFactor=1.1,minNeighbors=5,minSize=(50, 50))
            if(self.FaceCapture.isChecked()):           #人脸数据收集
                self.ModelTraining.setEnabled(True)
                for (x, y, w, h) in faces:
                    faceImage = self.image_gray[y:y+h,x:x+w]
                    faceImage = cv2.resize(faceImage,(200,200))
                    #fileName = "FaceCapture/Face_"+time.strftime("%Y%m%d%H%M%S", time.localtime())+str(self.faceCaptureFlag)+".jpg"
                    fileName = "FaceCapture/Face"+str(self.faceCaptureFlag)+".png"
                    cv2.imwrite(fileName,faceImage)
                    self.faceCaptureFlag+=1
                    Message="已采集"+str(self.faceCaptureFlag)+"张人脸图像"
                    self.status.showMessage(Message,2000)
            if(self.FaceRecognition.isChecked()):       #人脸识别
                for (x, y, w, h) in faces:
                    face = self.image_gray[y:y+h,x:x+w]
                    face = cv2.resize(face,(200,200))
                    result = self.model.predict(face)
                    if(result[1]<50):
                        text='most beautiful '+str(result[1])
                        cv2.putText(self.image,text,(x, y),cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
                    else:
                        text=str(result[1])
                        cv2.putText(self.image,text,(x, y),cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
            for (x, y, w, h) in faces:
                cv2.rectangle(self.image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    def TrainModel(self):
        #人脸识别模型训练函数
        self.status.showMessage("正在训练模型")
        tr_image=[]
        tr_flag=[]
        for fileNum in range(1,self.faceCaptureFlag):
            fileName = "FaceCapture/Face"+str(fileNum)+".png"
            image = cv2.imread(fileName,cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image,(200,200))
            tr_image.append(np.asarray(image,dtype=np.uint8))
            tr_flag.append(1)

        tr_image = np.asarray(tr_image)
        tr_flag = np.asarray(tr_flag,dtype=np.int32)
     
        self.model = cv2.face.LBPHFaceRecognizer_create()
        self.model.train(tr_image,tr_flag)
        QMessageBox.information(self,"提示","模型训练已完成",QMessageBox.Yes)
        self.status.showMessage("模型训练已完成",3000)


    def initProperty(self):
        #摄像头初始化函数
        self.FPS = 20                       #帧率默认值
        self.lowThreshold = 50              #边缘检测阈值一默认值
        self.highThreshold = 100            #边缘检测阈值二默认值
        self.PropertyValue={}           
        self.PropertyValue['bright'] = self.camera.get(cv2.CAP_PROP_BRIGHTNESS)             #亮度值
        self.PropertyValue['contrast'] = self.camera.get(cv2.CAP_PROP_CONTRAST)             #对比度值
        self.PropertyValue['saturation'] = self.camera.get(cv2.CAP_PROP_SATURATION)         #饱和度值
        self.PropertyValue['hue'] = self.camera.get(cv2.CAP_PROP_HUE)                       #色调值
        self.PropertyValue['sharpness'] = self.camera.get(cv2.CAP_PROP_SHARPNESS)           #锐度值
        self.PropertyValue['gamma'] = self.camera.get(cv2.CAP_PROP_GAMMA)                   #灰度系数值
        self.PropertyValue['gain'] = self.camera.get(cv2.CAP_PROP_GAIN)                     #增益值
        self.width = self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)                             #帧宽度
        self.height = self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)                           #帧高度

        #保存摄像头参数初始值，用于初始化等
        self.brightDefault = self.PropertyValue['bright']
        self.contrastDefault = self.PropertyValue['contrast']
        self.saturationDefault = self.PropertyValue['saturation']
        self.hueDefault = self.PropertyValue['hue']
        self.sharpnessDefault = self.PropertyValue['sharpness']
        self.gammaDefault = self.PropertyValue['gamma']
        self.gainDefault = self.PropertyValue['gain']
        self.Size = (int(self.width),int(self.height))
        #在主界面当前参数区域显示当前摄像头参数
        self.Threshold1.setValue(self.lowThreshold)
        self.Threshold2.setValue(self.highThreshold)
        self.Label_briV.setText(str(self.PropertyValue['bright']))
        self.Label_conV.setText(str(self.PropertyValue['contrast']))
        self.Label_satV.setText(str(self.PropertyValue['saturation']))
        self.Label_hueV.setText(str(self.PropertyValue['hue']))
        self.Label_shaV.setText(str(self.PropertyValue['sharpness']))
        self.Label_gamV.setText(str(self.PropertyValue['gamma']))
        self.Label_gaiV.setText(str(self.PropertyValue['gain']))
        self.Label_FPSV.setText(str(self.FPS))
        self.status.showMessage("摄像头初始化完毕",3000)

    def DefaultProperty(self):
        #恢复默认值函数
        self.camera.set(cv2.CAP_PROP_BRIGHTNESS,self.brightDefault)            #亮度  ，初始值为0  ，范围-10-+10          
        self.camera.set(cv2.CAP_PROP_CONTRAST,self.contrastDefault)            #对比度，初始值为10 ，范围0-20
        self.camera.set(cv2.CAP_PROP_SATURATION,self.saturationDefault)        #饱和度，初始值为5  ，范围0-10
        self.camera.set(cv2.CAP_PROP_HUE,self.hueDefault)                      #色调  ，初始值为0  ，范围-5-+5
        self.camera.set(cv2.CAP_PROP_SHARPNESS,self.sharpnessDefault)          #锐度  ，范围0-10
        self.camera.set(cv2.CAP_PROP_GAMMA,self.gammaDefault)                  #灰度系数，范围100-200
        self.camera.set(cv2.CAP_PROP_GAIN,self.gainDefault)                    #增益  ，初始值32   ，范围32—48
        #self.camera.set(cv2.CAP_PROP_FRAME_WIDTH,self.widthDefault)            #帧宽度，初始值为640
        #self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT,self.heightDefault)          #帧高度，初始值为480
        self.Threshold1.setValue(50)
        self.Threshold2.setValue(100)
        self.initProperty()                             #初始化
        self.status.showMessage("已重置为默认值",3000)

    def ChooseCamera(self):
        #切换摄像头函数
        self.DefaultProperty()                #当前摄像头初始化
        cameraIDD = self.cameraID      #当前摄像头ID
        for i in range(0,8):
            self.cameraID = self.cameraID + 1
            if(self.cameraID >=5):
                self.cameraID = 0
            self.camera = cv2.VideoCapture(self.cameraID)       #打开摄像头
            if(self.camera.isOpened()):
                if(self.cameraID == cameraIDD):                  #若未切换
                    self.initProperty()                                 #摄像头属性参数初始化
                    QMessageBox.information(self,"切换摄像头","未找到其它摄像头",QMessageBox.Ok,QMessageBox.Ok)
                    self.status.showMessage("无其它可用摄像头",3000)
                else:
                    self.initProperty()                                 #摄像头属性参数初始化
                    self.changeFirst=1                                  #刚刚切换过摄像头的标志置1
                    self.status.showMessage("已切换摄像头",3000)
                break
        
    def setProperty(self):
        #菜单-设置-摄像头设置 槽函数对话框
        self.PropertyDialog=setProperty.PropertyDialog()            #参数调整对话框类实例化
        if(self.changeFirst):            #如果是切换摄像头后初次调用
            self.PropertyInit()         #则初始化参数调整对话框
            self.changeFirst=0          #刚刚切换过摄像头的标志置0
        self.PropertyDialog.setupUi(self.PropertyDialog,self.PropertyValue,self.PropertyRange)
        self.PropertyDialog.Brightness.valueChanged.connect(self.BrightnessValueChanged)
        self.PropertyDialog.Contrast.valueChanged.connect(self.ContrastValueChanged)
        self.PropertyDialog.Saturation.valueChanged.connect(self.SaturationValueChanged)
        self.PropertyDialog.Hue.valueChanged.connect(self.HueValueChanged)
        self.PropertyDialog.Sharpness.valueChanged.connect(self.SharpnessValueChanged)
        self.PropertyDialog.Gain.valueChanged.connect(self.GainValueChanged)
        self.PropertyDialog.Gamma.valueChanged.connect(self.GammaValueChanged)
        self.PropertyDialog.exec_()

    def setSave(self):
        #菜单-设置-图像获取设置 槽函数对话框
        self.SaveSet.FPS.valueChanged.connect(self.setFPS)      
        self.SaveSet.exec_()                #进入图像获取设置对话框循环

    def timeStop(self):
        #按钮-暂停/继续 槽函数对话框
        if(self.ButtonStop.isChecked()):                       #检查开关状态
            self.ButtonStop.setText("继续")
            self.timer.stop()                                   #停止计数器
            if(self.buttonvideo.isChecked()):                       #检查 录像 开关状态
                self.timerVideo.stop()
            else:                                                   
                self.buttonvideo.setEnabled(False)
            self.status.showMessage("暂停")                                                       
        else:                                                   #若开光状态为
            self.ButtonStop.setText("暂停")
            self.timer.start(30)                                   #启动第一个定时器
            if(self.buttonvideo.isChecked()):                       #检查 录像 开关状态
                self.timerVideo.start(1000/self.FPS)                #启动第二个定时器
                self.status.showMessage("正在录像……") 
            else:
                self.buttonvideo.setEnabled(True)                                                
                self.status.showMessage("继续",3000)

    def SavePicture(self):
        #按钮-拍照 槽函数
        fileName1=self.SaveSet.filenameImage+"\PHOTO_"+time.strftime("%Y%m%d%H%M%S", time.localtime())+".jpg"           #组合字符串
        fileName2=self.SaveSet.filenameImage+"\PHOTO_"+time.strftime("%Y%m%d%H%M%S", time.localtime())+"Gray.jpg"       #按照实时时间
        fileName3=self.SaveSet.filenameImage+"\PHOTO_"+time.strftime("%Y%m%d%H%M%S", time.localtime())+"Edge.jpg"       #得到文件名  
        if(self.ButtonStop.isChecked()):                                #判断暂停按钮状态
            if(self.SaveSet.SaveImage.isChecked()):                         #判断是否保存实时图像
                cv2.imencode('.jpg',self.frame)[1].tofile(fileName1)        #若是，则保存
            if(self.SaveSet.SaveImage_gray.isChecked()):                    #判断是否保存灰度图像
                cv2.imencode('.jpg',self.image_gray)[1].tofile(fileName2)   #若是，则保存
            if(self.SaveSet.SaveImage_edge.isChecked()):                    #判断是否保存边缘检测图像
                cv2.imencode('.jpg',self.image_edge)[1].tofile(fileName3)   #若是，则保存
        else:  
            self.timer.stop()                                               #定时器暂停一会儿、来模拟镜头拍照的感觉
            if(self.SaveSet.SaveImage.isChecked()):                         #判断是否保存实时图像
                cv2.imencode('.jpg',self.frame)[1].tofile(fileName1)        #若是，则保存
                self.imagelabel.setPixmap(QPixmap("image/black.png"))           #屏幕黑一下
            if(self.SaveSet.SaveImage_gray.isChecked()):                    #判断是否保存灰度图像
                cv2.imencode('.jpg',self.image_gray)[1].tofile(fileName2)   #若是，则保存
                self.imageLabel_gray.setPixmap(QPixmap("image/black.png"))      #屏幕黑一下
            if(self.SaveSet.SaveImage_edge.isChecked()):                    #判断是否保存边缘检测图像
                cv2.imencode('.jpg',self.image_edge)[1].tofile(fileName3)   #若是，则保存
                self.imageLabel_edge.setPixmap(QPixmap("image/black.png"))      #屏幕黑一下
            time.sleep(0.1)                                                 #延时一下
            self.timer.start(1000/self.FPS)                                 #恢复定时器1
        photomessage = "图像已成功保存至"+self.SaveSet.filenameImage        
        self.status.showMessage(photomessage,3000)                      #更新状态栏    

    def SaveVideo(self):
        #按钮-录像 开始录像槽函数
        if(self.buttonvideo.isChecked()):                       #检查开关状态，若“录像”
            self.fourcc = cv2.VideoWriter_fourcc(*'XVID')       #创建一个cv2.VideoWriter类
            fileNameVideo=self.SaveSet.filenameVideo+"\VIDEO_"+time.strftime("%Y%m%d%H%M%S", time.localtime())+".avi"
            self.out = cv2.VideoWriter(fileNameVideo,self.fourcc,self.FPS,self.Size)        #创建视频输出文件
            self.timerVideo.start(1000/int(self.FPS))                #启动第二个定时器
            self.buttonvideo.setText("停止录像")
            self.status.showMessage("正在录像……")   
        else:                                                   #若开光状态为“停止录像”
            self.timerVideo.stop()                              #停止第二个计数器
            self.out.release()                                  #释放视频输出文件
            self.buttonvideo.setText("录像")
            videomessage = "录像结束，已成功保存至"+self.SaveSet.filenameVideo
            self.status.showMessage(videomessage,3000)

    def VideoFrame(self):
        #用于录像的定时器二的槽函数
        ret,frame=self.camera.read()
        self.out.write(frame)

    def helpAbout(self):            
        #菜单-帮助-关于 槽函数对话框
        QMessageBox.about(self, "关于","基于Python的图像获取与处理软件设计\n\n       哈尔滨工业大学(威海) 刘阳\n          毕业设计 2018-06-12   ")
    
    def helpHelp(self): 
        #菜单-帮助-帮助 槽函数对话框
        QMessageBox.information(self,"帮助","帮不了你",QMessageBox.Ok)

    def closeEvent(self,event):
        #关闭事件重写
        if(self.changeFirst):               #如果未调用摄像头参数设置函数
            event.accept()
        else:                               #若调用过摄像头参数设置，关闭前询问是否保存更改
            reply = QMessageBox.question(self, '关闭', '程序即将关闭\n是否保存对摄像头参数的更改？',
                                        QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            elif reply == QMessageBox.No:
                self.DefaultProperty()
                event.accept()
            else:
                event.ignore()

    def BrightnessValueChanged(self): 
        """亮度调节槽函数"""
        self.camera.set(cv2.CAP_PROP_BRIGHTNESS,self.PropertyDialog.Brightness.value())      #设置亮度值
        self.PropertyValue['bright'] = self.PropertyDialog.Brightness.value()
        #self.labelBriVal.setText(str(self.bright))
        self.Label_briV.setText(str(self.PropertyValue['bright']))
        self.status.showMessage("亮度调整完毕",2000)

    def ContrastValueChanged(self):  
        """对比度调节槽函数"""
        self.camera.set(cv2.CAP_PROP_CONTRAST,self.PropertyDialog.Contrast.value())          #设置对比度
        self.PropertyValue['contrast'] = self.PropertyDialog.Contrast.value()
        self.Label_conV.setText(str(self.PropertyValue['contrast']))
        self.status.showMessage("对比度调整完毕",2000)

    def SaturationValueChanged(self):
        """饱和度调节槽函数"""
        self.camera.set(cv2.CAP_PROP_SATURATION,self.PropertyDialog.Saturation.value())      #设置饱和度
        self.PropertyValue['saturation'] = self.PropertyDialog.Saturation.value()
        self.Label_satV.setText(str(self.PropertyValue['saturation']))
        self.status.showMessage("饱和度调整完毕",2000)

    def HueValueChanged(self):
        """色调调节槽函数"""
        self.camera.set(cv2.CAP_PROP_HUE,self.PropertyDialog.Hue.value())                    #设置色调
        self.PropertyValue['hue'] = self.PropertyDialog.Hue.value()
        self.Label_hueV.setText(str(self.PropertyValue['hue']))
        self.status.showMessage("色调调整完毕",2000)

    def SharpnessValueChanged(self):
        """锐度调节槽函数"""
        self.camera.set(cv2.CAP_PROP_SHARPNESS,self.PropertyDialog.Sharpness.value())        #设置锐度
        self.PropertyValue['sharpness'] = self.PropertyDialog.Sharpness.value()
        self.Label_shaV.setText(str(self.PropertyValue['sharpness']))
        self.status.showMessage("锐度调节完毕",2000)
    
    def GammaValueChanged(self):
        """#灰度系数调节槽函数"""
        self.camera.set(cv2.CAP_PROP_GAMMA,self.PropertyDialog.Gamma.value())                #设置灰度系数
        self.PropertyValue['gamma'] = self.PropertyDialog.Gamma.value()
        self.Label_gamV.setText(str(self.PropertyValue['gamma']))
        self.status.showMessage("灰度系数调节完毕",2000)

    def GainValueChanged(self):
        """增益调节槽函数"""
        self.camera.set(cv2.CAP_PROP_GAIN,self.PropertyDialog.Gain.value())                  #设置增益
        self.PropertyValue['gain'] = self.PropertyDialog.Gain.value()
        self.Label_gaiV.setText(str(self.PropertyValue['gain']))
        self.status.showMessage("增益调节完毕",2000)
    
    def CannylowThreshold(self):
        """边缘检测低阈一调节槽函数"""
        self.lowThreshold= self.Threshold1.value()
        self.status.showMessage("边缘检测阈值一调节完毕",2000)

    def CannyhighThreshold(self):
        """边缘检测阈值二调节槽函数"""
        self.highThreshold= self.Threshold2.value()
        self.status.showMessage("边缘检测阈值二调节完毕",2000)
    
    def setFPS(self):
        #录像FPS设置槽函数
        self.FPS = self.SaveSet.FPS.value()
        self.Label_FPSV.setText(str(self.FPS))
        self.status.showMessage("FPS调节完毕",2000)

    def PropertyInit(self):
        #属性参数调整对话框初始化（可调范围确定）
        self.status.showMessage("参数设置对话框初始化中……")
        self.PropertyRange={}
        #1-亮度值
        brightval = self.brightDefault
        flagbri=self.camera.set(cv2.CAP_PROP_BRIGHTNESS,brightval)
        if(-1024<self.brightDefault<1024 and flagbri==True):  #我认为的该参数可调的条件
            bright = self.camera.get(cv2.CAP_PROP_BRIGHTNESS)
            while(bright==brightval):
                brightval = bright+1
                self.camera.set(cv2.CAP_PROP_BRIGHTNESS,brightval)
                bright = self.camera.get(cv2.CAP_PROP_BRIGHTNESS)
            self.PropertyRange['brimax'] = bright            #亮度可调最大值

            brightval = self.brightDefault - 1
            flagbri=self.camera.set(cv2.CAP_PROP_BRIGHTNESS,brightval)
            bright = self.camera.get(cv2.CAP_PROP_BRIGHTNESS)
            while(bright==brightval):
                brightval = bright-1
                self.camera.set(cv2.CAP_PROP_BRIGHTNESS,brightval)
                bright = self.camera.get(cv2.CAP_PROP_BRIGHTNESS)
            self.PropertyRange['brimin'] = bright                #亮度可调最小值
            self.camera.set(cv2.CAP_PROP_BRIGHTNESS,self.brightDefault)
        else:                       #我觉得参数不可调的话
            self.PropertyRange['brimax'] = -1
            self.PropertyRange['brimin'] = -1
            self.Label_briV.setText("——")

        #2-对比度
        contrastval = self.contrastDefault
        flagcon=self.camera.set(cv2.CAP_PROP_CONTRAST,contrastval)
        if(-256< contrastval <256 and flagcon==True):  #我认为的该参数可调的条件
            #print(-256<self.brightDefault<256 and flagbri==True)
            contrast = self.camera.get(cv2.CAP_PROP_CONTRAST)
            while(contrast==contrastval):
                contrastval = contrast + 1
                self.camera.set(cv2.CAP_PROP_CONTRAST,contrastval)
                contrast = self.camera.get(cv2.CAP_PROP_CONTRAST)
            self.PropertyRange['conmax'] = contrast            #对比度可调最大值

            contrastval = self.contrastDefault
            flagcon=self.camera.set(cv2.CAP_PROP_CONTRAST,contrastval)
            contrast = self.camera.get(cv2.CAP_PROP_CONTRAST)
            while(contrast==contrastval):
                contrastval = contrast-1
                self.camera.set(cv2.CAP_PROP_CONTRAST,contrastval)
                contrast = self.camera.get(cv2.CAP_PROP_CONTRAST)
            self.PropertyRange['conmin'] = contrast                #对比度可调最小值
            self.camera.set(cv2.CAP_PROP_CONTRAST,self.contrastDefault)
        else:                       #我觉得参数不可调的话
            self.PropertyRange['conmin'] = -1
            self.PropertyRange['conmax'] = -1
            self.Label_conV.setText("——")

        #3-饱和度
        saturationval = self.saturationDefault
        flagsat = self.camera.set(cv2.CAP_PROP_SATURATION,saturationval)
        if(-1024< saturationval <1024 and flagsat==True):  #我认为的该参数可调的条件
            #print(-256<self.brightDefault<256 and flagbri==True)
            saturation = self.camera.get(cv2.CAP_PROP_SATURATION)
            while(saturation==saturationval):
                saturationval = saturation + 1
                self.camera.set(cv2.CAP_PROP_SATURATION,saturationval)
                saturation = self.camera.get(cv2.CAP_PROP_SATURATION)
            self.PropertyRange['satmax'] = saturation            #饱和度可调最大值

            saturationval = self.saturationDefault
            flagsat = self.camera.set(cv2.CAP_PROP_SATURATION,saturationval)
            saturation = self.camera.get(cv2.CAP_PROP_SATURATION)
            while(saturation == saturationval):
                saturationval = saturation - 1
                self.camera.set(cv2.CAP_PROP_SATURATION,saturationval)
                saturation = self.camera.get(cv2.CAP_PROP_SATURATION)
            self.PropertyRange['satmin'] = saturation                #饱和度可调最小值
            self.camera.set(cv2.CAP_PROP_SATURATION,self.saturationDefault)
            #print("max=",self.satmax,"min=",self.satmin)
        else:                       #我觉得参数不可调的话
            self.PropertyRange['satmin'] = -1
            self.PropertyRange['satmax'] = -1
            self.Label_satV.setText("——")

        #4-色调
        hueval = self.hueDefault
        flaghue = self.camera.set(cv2.CAP_PROP_HUE,hueval)
        if(-1024< hueval <1024 and flaghue==True):  #我认为的该参数可调的条件
            hue = self.camera.get(cv2.CAP_PROP_HUE)
            while(hue==hueval):
                hueval = hue + 1
                self.camera.set(cv2.CAP_PROP_HUE,hueval)
                hue = self.camera.get(cv2.CAP_PROP_HUE)
            self.PropertyRange['huemax'] = hue            #色调可调最大值

            hueval = self.hueDefault
            flaghue = self.camera.set(cv2.CAP_PROP_HUE,hueval)
            hue = self.camera.get(cv2.CAP_PROP_HUE)
            while(hue == hueval):
                hueval = hue - 1
                self.camera.set(cv2.CAP_PROP_HUE,hueval)
                hue = self.camera.get(cv2.CAP_PROP_HUE)
            self.PropertyRange['huemin'] = hue                #饱和度可调最小值
            self.camera.set(cv2.CAP_PROP_HUE,self.hueDefault)
            #print("max=",self.huemax,"min=",self.huemin)
        else:                       #我觉得参数不可调的话
            self.PropertyRange['huemin'] = -1
            self.PropertyRange['huemax'] = -1
            self.Label_hueV.setText("——")

        #5-锐度
        sharpnessval = self.sharpnessDefault
        flagsha = self.camera.set(cv2.CAP_PROP_SHARPNESS,sharpnessval)
        if(-1024< sharpnessval <1024 and flagsha==True):  #我认为的该参数可调的条件
            sharpness = self.camera.get(cv2.CAP_PROP_SHARPNESS)
            while(sharpness==sharpnessval):
                sharpnessval = sharpness + 1
                self.camera.set(cv2.CAP_PROP_SHARPNESS,sharpnessval)
                sharpness = self.camera.get(cv2.CAP_PROP_SHARPNESS)
            self.PropertyRange['shamax'] = sharpness            #锐度可调最大值

            sharpnessval = self.sharpnessDefault
            flagsha = self.camera.set(cv2.CAP_PROP_SHARPNESS,sharpnessval)
            sharpness = self.camera.get(cv2.CAP_PROP_SHARPNESS)
            while(sharpness == sharpnessval):
                sharpnessval = sharpness - 1
                self.camera.set(cv2.CAP_PROP_SHARPNESS,sharpnessval)
                sharpness = self.camera.get(cv2.CAP_PROP_SHARPNESS)
            self.PropertyRange['shamin'] = sharpness                #锐度可调最小值
            self.camera.set(cv2.CAP_PROP_SHARPNESS,self.sharpnessDefault)
            #print("max=",self.shamax,"min=",self.shamin)
        else:                       #我觉得参数不可调的话
            self.PropertyRange['shamin'] = -1
            self.PropertyRange['shamax'] = -1
            self.Label_shaV.setText("——")

        #6-灰度系数
        gammaval = self.gammaDefault
        flaggam = self.camera.set(cv2.CAP_PROP_GAMMA,gammaval)
        if(-1024< gammaval <1024 and flaggam==True):  #我认为的该参数可调的条件
            gamma = self.camera.get(cv2.CAP_PROP_GAMMA)
            while(gamma == gammaval):
                gammaval = gamma + 1
                self.camera.set(cv2.CAP_PROP_GAMMA,gammaval)
                gamma = self.camera.get(cv2.CAP_PROP_GAMMA)
            self.PropertyRange['gammax'] = gamma            #锐度可调最大值

            gammaval = self.gammaDefault
            flaggam = self.camera.set(cv2.CAP_PROP_GAMMA,gammaval)
            gamma = self.camera.get(cv2.CAP_PROP_GAMMA)
            while(gamma == gammaval):
                gammaval = gamma - 1
                self.camera.set(cv2.CAP_PROP_GAMMA,gammaval)
                gamma = self.camera.get(cv2.CAP_PROP_GAMMA)
            self.PropertyRange['gammin'] = gamma                #锐度可调最小值
            self.camera.set(cv2.CAP_PROP_GAMMA,self.gammaDefault)
            #print("max=",self.gammax,"min=",self.gammin)
        else:                       #我觉得参数不可调的话
            self.PropertyRange['gammin'] = -1
            self.PropertyRange['gammax'] = -1
            self.Label_gamV.setText("——")

        #7-增益
        gainval = self.gainDefault
        flaggai = self.camera.set(cv2.CAP_PROP_GAIN,gainval)
        if(-1024< gainval <1024 and flaggai==True):  #我认为的该参数可调的条件
            gain = self.camera.get(cv2.CAP_PROP_GAIN)
            while(gain == gainval):
                gainval = gain + 1
                self.camera.set(cv2.CAP_PROP_GAIN,gainval)
                gain = self.camera.get(cv2.CAP_PROP_GAIN)
            self.PropertyRange['gaimax'] = gain            #锐度可调最大值

            gainval = self.gainDefault
            flaggai = self.camera.set(cv2.CAP_PROP_GAIN,gainval)
            gain = self.camera.get(cv2.CAP_PROP_GAIN)
            while(gain == gainval):
                gainval = gain - 1
                self.camera.set(cv2.CAP_PROP_GAIN,gainval)
                gain = self.camera.get(cv2.CAP_PROP_GAIN)
            self.PropertyRange['gaimin'] = gain                #锐度可调最小值
            self.camera.set(cv2.CAP_PROP_GAIN,self.gainDefault)
            #print("max=",self.gaimax,"min=",self.gaimin)
        else:                       #我觉得参数不可调的话
            self.PropertyRange['gaimin'] = -1
            self.PropertyRange['gaimax'] = -1
            self.Label_gaiV.setText("——")

        #self.Loading.close()
        self.status.showMessage("参数设置对话框初始化已完成",1000)
    
    
if __name__ == "__main__":
    app=QApplication(sys.argv)                      #每一个PyQt5程序都需要一个QApplication对象，QApplication类包含在QTWidgets模块中。sys.argv是一个命令行参数列表。Python脚本可以从Shell中执行，比如双击.py脚本文件，通过参数来选择启动脚本的方式。
    app.setWindowIcon(QIcon("source/lena.ico"))       #设置图标
    mainUI=CIAP()                              #主窗口
    mainUI.show()                                  
    sys.exit(app.exec_())                           #进入该程序的主循环
