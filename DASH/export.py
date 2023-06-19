# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 642)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 162, 741, 441))
        self.graphicsView.setStyleSheet("background-color:#fefefe;\n"
"border: 5px solid #4ba1df;")
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:black;\n"
"background-color: white;\n"
"border: 2px solid white; border-radius:10px;")
        self.label.setObjectName("label")
        self.textBrowser_98 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_98.setEnabled(True)
        self.textBrowser_98.setGeometry(QtCore.QRect(40, 210, 671, 281))
        self.textBrowser_98.setStyleSheet("border: 5px solid #4ba1df; border-radius:50px;\n"
"background-color:black;\n"
"color:white;")
        self.textBrowser_98.setFrameShape(QtWidgets.QFrame.Box)
        self.textBrowser_98.setObjectName("textBrowser_98")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 510, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"color: black;\n"
"background-color:#fefefe;\n"
"border: 2px solid #4ba1df; border-radius:20px;\n"
"font: 16pt \"Times New Roman\";\n"
"background-repeat:none;\n"
"}\n"
"QPushButton#pushButton_2:hover\n"
"{\n"
"    background-color:lightgreen;\n"
"    color:black;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(0, 0, 741, 161))
        self.graphicsView_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.543136, y1:0.074, x2:0.52, y2:1, stop:0.880682 rgba(75, 161, 223, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 10, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.create = QtWidgets.QPushButton(self.centralwidget)
        self.create.setGeometry(QtCore.QRect(10, 70, 171, 61))
        font = QtGui.QFont()
        font.setFamily("TImes New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.create.setFont(font)
        self.create.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.create.setStyleSheet("QPushButton#create{\n"
"padding-left:-40px;\n"
"color:black;\n"
"background-color:#fefefe;\n"
"border: 2px solid #58e870; border-radius:30px;\n"
"font: 12pt \"TImes New Roman\";\n"
"background-image:url(\"icons/create.png\");\n"
"background-repeat:none;\n"
"}\n"
"QPushButton#create:hover\n"
"{\n"
"   background-color:lightgreen;\n"
"    color:white;\n"
"}")
        self.create.setObjectName("create")
        self.scan_sen = QtWidgets.QPushButton(self.centralwidget)
        self.scan_sen.setGeometry(QtCore.QRect(370, 70, 171, 61))
        font = QtGui.QFont()
        font.setFamily("TImes New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.scan_sen.setFont(font)
        self.scan_sen.setStyleSheet("QPushButton#scan_sen{\n"
"padding-left:-40px;\n"
"color:black;\n"
"background-color:#fefefe;\n"
"border: 2px solid #58e870; border-radius:30px;\n"
"font: 12pt \"TImes New Roman\";\n"
"background-image:url(\"icons/sent.png\");\n"
"background-repeat:none;\n"
"}\n"
"QPushButton#scan_sen:hover\n"
"{\n"
"   background-color:lightgreen;\n"
"    color:white;\n"
"}")
        self.scan_sen.setObjectName("scan_sen")
        self.scan_sinlge = QtWidgets.QPushButton(self.centralwidget)
        self.scan_sinlge.setGeometry(QtCore.QRect(190, 70, 171, 61))
        font = QtGui.QFont()
        font.setFamily("TImes New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.scan_sinlge.setFont(font)
        self.scan_sinlge.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scan_sinlge.setAutoFillBackground(False)
        self.scan_sinlge.setStyleSheet("QPushButton#scan_sinlge{\n"
"padding-left:-40px;\n"
"color:black;\n"
"background-color:#fefefe;\n"
"border: 2px solid #58e870; border-radius:30px;\n"
"font: 12pt \"TImes New Roman\";\n"
"background-image:url(\"icons/scan.png\");\n"
"background-repeat:none;\n"
"}\n"
"QPushButton#scan_sinlge:hover\n"
"{\n"
"   background-color:lightgreen;\n"
"    color:white;\n"
"}")
        self.scan_sinlge.setObjectName("scan_sinlge")
        self.exp2 = QtWidgets.QPushButton(self.centralwidget)
        self.exp2.setGeometry(QtCore.QRect(560, 70, 171, 61))
        font = QtGui.QFont()
        font.setFamily("TImes New Roman")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.exp2.setFont(font)
        self.exp2.setStyleSheet("QPushButton#exp2{\n"
"padding-left:-40px;\n"
"color:black;\n"
"background-color:#fefefe;\n"
"border: 2px solid #58e870; border-radius:30px;\n"
"font: 12pt \"TImes New Roman\";\n"
"background-image:url(\"icons/export.png\");\n"
"background-repeat:none;\n"
"}\n"
"QPushButton#exp2:hover\n"
"{\n"
"   background-color:lightgreen;\n"
"    color:white;\n"
"}")
        self.exp2.setCheckable(False)
        self.exp2.setAutoRepeat(False)
        self.exp2.setAutoExclusive(False)
        self.exp2.setAutoDefault(False)
        self.exp2.setDefault(False)
        self.exp2.setFlat(False)
        self.exp2.setObjectName("exp2")
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(710, 2, 31, 31))
        self.exit_button.setStyleSheet("QPushButton#exit_button{\n"
"background-image:url(\"icons/quit.png\");\n"
"background-repeat:none;\n"
"}")
        self.exit_button.setText("")
        self.exit_button.setObjectName("exit_button")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 510, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3{\n"
"color: black;\n"
"background-color:#fefefe;\n"
"border: 2px solid #4ba1df; border-radius:20px;\n"
"font: 16pt \"Times New Roman\";\n"
"background-repeat:none;\n"
"}\n"
"QPushButton#pushButton_3:hover\n"
"{\n"
"    background-color:lightgreen;\n"
"    color:black;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 741, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Export To File"))
        self.textBrowser_98.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Export"))
        self.graphicsView_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Sign Language Recognition Using Hand Gestures"))
        self.create.setText(_translate("MainWindow", "   Create Gesture"))
        self.scan_sen.setText(_translate("MainWindow", "                          Scan Sentence "))
        self.scan_sinlge.setText(_translate("MainWindow", "                         Scan Gestures"))
        self.exp2.setText(_translate("MainWindow", "                       Export To File"))
        self.pushButton_3.setText(_translate("MainWindow", "Gesture Viewer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

