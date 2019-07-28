# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AudioListBox.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AudioListBox(object):
    def setupUi(self, AudioListBox):
        AudioListBox.setWindowIcon(QtGui.QIcon("ytdIcon.ico"))
        AudioListBox.setObjectName("AudioListBox")
        AudioListBox.resize(457, 453)
        self.centralwidget = QtWidgets.QWidget(AudioListBox)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.AvalaibleAudio = QtWidgets.QLabel(self.centralwidget)
        self.AvalaibleAudio.setObjectName("AvalaibleAudio")
        self.verticalLayout.addWidget(self.AvalaibleAudio)
        self.AudioListView = QtWidgets.QListView(self.centralwidget)
        self.AudioListView.setObjectName("AudioListView")
        self.verticalLayout.addWidget(self.AudioListView)
        self.DownloadAudio = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadAudio.setObjectName("DownloadAudio")
        self.verticalLayout.addWidget(self.DownloadAudio)
        self.AudioProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.AudioProgressBar.setProperty("value", 0)
        self.AudioProgressBar.setObjectName("AudioProgressBar")
        self.verticalLayout.addWidget(self.AudioProgressBar)
        AudioListBox.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AudioListBox)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 457, 18))
        self.menubar.setObjectName("menubar")
        AudioListBox.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AudioListBox)
        self.statusbar.setObjectName("statusbar")
        AudioListBox.setStatusBar(self.statusbar)

        self.retranslateUi(AudioListBox)
        QtCore.QMetaObject.connectSlotsByName(AudioListBox)
        AudioListBox.setWindowTitle("Youtube Downloader")
    def retranslateUi(self, AudioListBox):
        _translate = QtCore.QCoreApplication.translate
        AudioListBox.setWindowTitle(_translate("AudioListBox", "MainWindow"))
        self.AvalaibleAudio.setText(_translate("AudioListBox", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Avalaible Audio Qualities</span></p></body></html>"))
        self.DownloadAudio.setText(_translate("AudioListBox", "Download Selected"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AudioListBox = QtWidgets.QMainWindow()
    ui = Ui_AudioListBox()
    ui.setupUi(AudioListBox)
    AudioListBox.show()
    sys.exit(app.exec_())

