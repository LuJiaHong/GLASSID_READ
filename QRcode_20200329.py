import sys
import datetime

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, Qt

import pyzbar.pyzbar as pyzbar
import cv2
import numpy as np
# import qdarkstyle
import qdarkstyle
from ui_qrcode import *



class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.iniUI()

    def iniUI(self):
        self.setupUi(self)
        self.logic = 0
        self.value = 1
        self.setWindowFlags(Qt.FramelessWindowHint )

        self.timer = QTimer()
        self.timer.timeout.connect(self.viewCam)
        self.TEXT.setText("To Start, click the SHOW to connect the webcam")
        self.SHOW.clicked.connect(self.onClick)
        self.CAPTURE.clicked.connect(self.CaptureClicked)

        self.show()

    def viewCam(self):
        ret, frame = self.cap.read()
        frame = cv2.flip(frame, 1, 0)

        self.displayImage(frame)

        if (self.logic == 2):
            self.value = self.value + 1
            cv2.imwrite(f"{self.value}.jpg", frame)
            capture_img = frame
            self.displayImage_capture(capture_img)

            self.logic = 1
            self.TEXT.setText("Save one image")

    def onClick(self):
        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(1)
            self.SHOW.setText("Stop")
        else:
            self.timer.stop()
            self.cap.release()
            self.SHOW.setText("Start")

    def CaptureClicked(self):
        self.logic = 2

    def displayImage(self, img):

        check_code_result = self.qrcode_detect(img)
        print(check_code_result )

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, channel = img.shape
        step = channel * width
        qImg = QImage(img.data, width, height, step, QtGui.QImage.Format_RGB888)

        self.image_label.setPixmap(QPixmap.fromImage(qImg))

    def displayImage_capture(self, img):

        check_code_result = self.qrcode_detect(img)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        height, width, channel = img.shape
        step = channel * width
        qImg = QImage(img.data, width, height, step, QtGui.QImage.Format_RGB888)

        self.capture_label.setPixmap(QPixmap.fromImage(qImg))

    def qrcode_detect(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        barcodes = pyzbar.decode(gray)

        if len(barcodes) != 0:
            self.CaptureClicked()

        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            barcodeData = str(barcode.data.decode("utf-8"))
            dateT = str(datetime.datetime.now())
            # print(barcodeData)
            cv2.putText(img, barcodeData, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255), 2)
            cv2.putText(img, dateT, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255), 2)
            self.Capture_result.setText(barcodeData)

            return barcodeData


def main():
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
