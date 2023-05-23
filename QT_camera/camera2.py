from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from cam_ui import *
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
        h, w, byte = imgRGB.shape
        img = QImage(imgRGB, w, h, byte * w, QImage.Format_RGB888)
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

    def setImage(self, img):
        self.pic.setPixmap(img)

    def play(self):
        self.th.start()

    def closeEvent(self, event):
        self.th.terminate()
        self.th.wait(3000)
        self.close()


app = QApplication()
win = MyApp()
win.show()
app.exec_()