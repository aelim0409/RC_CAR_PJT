from PySide2.QtWidgets import *
from camera_ui import Ui_MainWindow
from PySide2.QtGui import *
from PySide2.QtCore import *
import cv2


class myapp(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.cam = cv2.VideoCapture(-1)
        self.cam.set(3,480)
        self.cam.set(4,320)
        self.tm = QBasicTimer()

    def mode(self):
        pass
        
    def timerEvent(self,event):
        ret,self.img = self.cam.read()
        self.printImage(self.img, self.pic1)

    def paly(self):
        self.img = cv2.imread('aelim.png')
       self.tm.start(100,self)
       
    def printImage(self,imgBGR,pic):
        imgRGB = cv2.cvtColor(imgBGR,cv2.COLOR_BGR2RGB)
        h,w,byte = imgRGB.shape
        img = QImage(imgRGB,w,h,byte*w,QImage.Format_RGB888)
        pic.setPixmap(QPixmap(img))

app = QApplication()
win = myapp()
win.show()
app.exec_()



