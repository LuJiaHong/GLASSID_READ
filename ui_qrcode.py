# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_qrcode.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(958, 530)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_label = QtWidgets.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(4, 30, 409, 345))
        self.image_label.setFrameShape(QtWidgets.QFrame.Box)
        self.image_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_label.setLineWidth(0)
        self.image_label.setMidLineWidth(13)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.TEXT = QtWidgets.QTextBrowser(self.centralwidget)
        self.TEXT.setGeometry(QtCore.QRect(10, 660, 1411, 57))
        self.TEXT.setObjectName("TEXT")
        self.SHOW = QtWidgets.QPushButton(self.centralwidget)
        self.SHOW.setGeometry(QtCore.QRect(844, 24, 103, 53))
        self.SHOW.setObjectName("SHOW")
        self.CAPTURE = QtWidgets.QPushButton(self.centralwidget)
        self.CAPTURE.setGeometry(QtCore.QRect(844, 82, 105, 53))
        self.CAPTURE.setObjectName("CAPTURE")
        self.capture_label = QtWidgets.QLabel(self.centralwidget)
        self.capture_label.setGeometry(QtCore.QRect(420, 28, 407, 347))
        self.capture_label.setFrameShape(QtWidgets.QFrame.Box)
        self.capture_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.capture_label.setLineWidth(0)
        self.capture_label.setMidLineWidth(13)
        self.capture_label.setAlignment(QtCore.Qt.AlignCenter)
        self.capture_label.setObjectName("capture_label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 414, 571, 34))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Capture_result = QtWidgets.QLabel(self.centralwidget)
        self.Capture_result.setGeometry(QtCore.QRect(104, 380, 171, 32))
        self.Capture_result.setObjectName("Capture_result")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(16, 378, 89, 32))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.CAPTURE_2 = QtWidgets.QPushButton(self.centralwidget)
        self.CAPTURE_2.setGeometry(QtCore.QRect(6, 2, 40, 23))
        self.CAPTURE_2.setAutoFillBackground(False)
        self.CAPTURE_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.CAPTURE_2.setText("")
        self.CAPTURE_2.setDefault(False)
        self.CAPTURE_2.setFlat(True)
        self.CAPTURE_2.setObjectName("CAPTURE_2")
        self.CAPTURE_2.raise_()
        self.image_label.raise_()
        self.TEXT.raise_()
        self.SHOW.raise_()
        self.CAPTURE.raise_()
        self.capture_label.raise_()
        self.layoutWidget.raise_()
        self.Capture_result.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 958, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.CAPTURE_2.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.image_label.setText(_translate("MainWindow", "Live Stream"))
        self.TEXT.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Message </p></body></html>"))
        self.SHOW.setText(_translate("MainWindow", "SHOW"))
        self.CAPTURE.setText(_translate("MainWindow", "Capture Image"))
        self.capture_label.setText(_translate("MainWindow", "Capture Image"))
        self.Capture_result.setText(_translate("MainWindow", "Capture_result"))
        self.label.setText(_translate("MainWindow", "Read Result"))
