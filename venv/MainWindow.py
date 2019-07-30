# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube
import threading
from venv.VideoListBox import Ui_WindwForVideos
from venv.AudioListBox import Ui_AudioListBox
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def Open_VideoWin(self):
        link = self.UrlEntry.text()
        print(link)
        video = YouTube(link)
        i = 0
        while i<=50:
            self.progressBar.setValue(i)
        streams = video.streams.filter(progressive=True).order_by('resolution').desc().all()
        for i in streams:
            print(i)
        self.Vidwindow = QtWidgets.QMainWindow()
        self.VideoBox = Ui_WindwForVideos()
        self.VideoBox.setupUi(self.Vidwindow)
        while i<=101:
            self.progressBar.setValue(100)
        self.Vidwindow.show()


    def Open_AudioWin(self):
            self.Audiowindow = QtWidgets.QMainWindow()
            self.AudioBox = Ui_AudioListBox()
            self.AudioBox.setupUi(self.Audiowindow)
            self.Audiowindow.show()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QtGui.QIcon("ytdIcon.ico"))
        MainWindow.resize(668, 306)
        MainWindow.setWindowTitle("Ytd ")
        MainWindow.setToolTipDuration(0)
        # self.setWindowIcon(QtGui.QIcon('ytd.ico'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(798, 683))
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.UrlEntry = QtWidgets.QLineEdit(self.frame)
        self.UrlEntry.setGeometry(QtCore.QRect(120, 10, 501, 21))
        self.UrlEntry.setObjectName("UrlEntry")
        self.EnterUrl = QtWidgets.QLabel(self.frame)
        self.EnterUrl.setGeometry(QtCore.QRect(20, 10, 81, 20))
        self.EnterUrl.setObjectName("EnterUrl")

        self.Location = QtWidgets.QLabel(self.frame)
        self.Location.setGeometry(QtCore.QRect(20, 50, 131, 16))
        self.Location.setObjectName("Location")
        self.Browse = QtWidgets.QPushButton(self.frame)
        self.Browse.setGeometry(QtCore.QRect(520, 50, 91, 23))
        self.Browse.setObjectName("Browse")
        self.Location_Entry = QtWidgets.QLineEdit(self.frame)
        self.Location_Entry.setGeometry(QtCore.QRect(160, 50, 350, 22))
        self.Location_Entry.setObjectName("Location_Entry")
        self.VideoSearch = QtWidgets.QPushButton(self.frame)
        self.VideoSearch.setGeometry(QtCore.QRect(130, 90, 171, 30))
        self.VideoSearch.setAcceptDrops(False)
        self.VideoSearch.setAutoFillBackground(False)
        self.VideoSearch.setAutoDefault(False)
        self.VideoSearch.setFlat(False)
        self.VideoSearch.setObjectName("VideoSearch")
        self.VideoSearch.clicked.connect(self.Open_VideoWin)
        self.AudioSearch = QtWidgets.QPushButton(self.frame)
        self.AudioSearch.setGeometry(QtCore.QRect(360, 90, 151, 30))
        self.AudioSearch.setObjectName("AudioSearch")
        self.AudioSearch.clicked.connect(self.Open_AudioWin)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(330, 90, 3, 61))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(110, 240, 521, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.EnterUrl.raise_()
        self.Location.raise_()
        self.Browse.raise_()
        self.Location_Entry.raise_()
        self.VideoSearch.raise_()
        self.AudioSearch.raise_()
        self.line.raise_()
        self.progressBar.raise_()
        self.UrlEntry.raise_()
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setWindowTitle("Youtube Downloader")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.EnterUrl.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#210101;\">Enter Url : </span></p></body></html>"))
        self.Location.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Download Locaton :</span></p></body></html>"))
        self.Browse.setText(_translate("MainWindow", "Browse"))
        self.VideoSearch.setText(_translate("MainWindow", "Search For Videos"))
        self.AudioSearch.setText(_translate("MainWindow", "Search For Audios"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

