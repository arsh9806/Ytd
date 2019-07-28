# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VideoListBox.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WindwForVideos(object):
    def setupUi(self, WindwForVideos):
        WindwForVideos.setObjectName("WindwForVideos")
        WindwForVideos.setWindowIcon(QtGui.QIcon("ytdIcon.ico"))
        WindwForVideos.setEnabled(True)
        WindwForVideos.resize(458, 462)
        self.centralwidget = QtWidgets.QWidget(WindwForVideos)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.AvalaibleVideos = QtWidgets.QLabel(self.centralwidget)
        self.AvalaibleVideos.setObjectName("AvalaibleVideos")
        self.verticalLayout.addWidget(self.AvalaibleVideos)
        self.VideoListView = QtWidgets.QListView(self.centralwidget)
        self.VideoListView.setObjectName("VideoListView")
        self.verticalLayout.addWidget(self.VideoListView)
        self.DownloadVideo = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadVideo.setObjectName("DownloadVideo")
        self.verticalLayout.addWidget(self.DownloadVideo)
        self.VideoProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.VideoProgressBar.setProperty("value", 0)
        self.VideoProgressBar.setObjectName("VideoProgressBar")
        self.verticalLayout.addWidget(self.VideoProgressBar)
        WindwForVideos.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindwForVideos)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 458, 18))
        self.menubar.setObjectName("menubar")
        WindwForVideos.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindwForVideos)
        self.statusbar.setObjectName("statusbar")
        WindwForVideos.setStatusBar(self.statusbar)

        self.retranslateUi(WindwForVideos)
        QtCore.QMetaObject.connectSlotsByName(WindwForVideos)
        WindwForVideos.setWindowTitle("Youtube Downloader")

    def retranslateUi(self, WindwForVideos):
        _translate = QtCore.QCoreApplication.translate
        WindwForVideos.setWindowTitle(_translate("WindwForVideos", "MainWindow"))
        self.AvalaibleVideos.setText(_translate("WindwForVideos", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt; font-weight:600;\">Avalaible Video Qualities</span></p></body></html>"))
        self.DownloadVideo.setText(_translate("WindwForVideos", "DownLoad Selected"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WindwForVideos = QtWidgets.QMainWindow()
    ui = Ui_WindwForVideos()
    ui.setupUi(WindwForVideos)
    WindwForVideos.show()
    sys.exit(app.exec_())

