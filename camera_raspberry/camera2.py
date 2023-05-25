from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from camera_ui import *
import cv2
from time import *

class MyThread(QThread):
    mySignal = Signal(QPixmap)

    def __init__(self):
        super().__init__()
        self.cam = cv2.VideoCapture(0)
        self.cam.set(3, 480)
        self.cam.set(4, 320)

    def run(self):
        while True:
            ret, self.img = self.cam.read()
            if ret:
                self.printImage(self.img)
            sleep(0.1)

    def printImage(self, imgBGR):
        imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
        imgRGB=cv2.flip(imgRGB,0)
        imgRGB=cv2.flip(imgRGB,1)
        h, w, byte = imgRGB.shape
        img = QImage(imgRGB, w, h, byte * w, QImage.Format_RGB888).scaled(700,500)
        
        pix_img = QPixmap(img)

        self.mySignal.emit(pix_img)



class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.main()

    def main(self):
        self.th = MyThread()
        self.th.mySignal.connect(self.setImage)
        self.pic1.setGeometry(QRect(60,0,700,500))
        self.plyBtn.setGeometry(QRect(150,520,500,40))
    def setImage(self, img):
        self.pic1.setPixmap(img)

    def paly(self):
        self.th.start()

    def closeEvent(self, event):
        self.th.terminate()
        self.th.wait(3000)
        self.close()

app = QApplication()
win = MyApp()
win.show()
app.exec_()