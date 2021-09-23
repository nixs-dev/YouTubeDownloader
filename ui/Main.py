# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(816, 703)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(210, 60, 391, 131))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/default/assets/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.link = QtWidgets.QLineEdit(self.centralwidget)
        self.link.setGeometry(QtCore.QRect(12, 240, 701, 31))
        self.link.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        self.link.setObjectName("link")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(720, 240, 61, 31))
        self.search.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.search.setObjectName("search")
        self.videoData = QtWidgets.QFrame(self.centralwidget)
        self.videoData.setGeometry(QtCore.QRect(100, 300, 581, 331))
        self.videoData.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.videoData.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.videoData.setFrameShadow(QtWidgets.QFrame.Raised)
        self.videoData.setObjectName("videoData")
        self.searchResult = QtWidgets.QLabel(self.videoData)
        self.searchResult.setGeometry(QtCore.QRect(10, 0, 751, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchResult.setFont(font)
        self.searchResult.setStyleSheet("color: rgb(255, 0, 0);")
        self.searchResult.setObjectName("searchResult")
        self.videoTitle = QtWidgets.QLabel(self.videoData)
        self.videoTitle.setGeometry(QtCore.QRect(340, 40, 761, 16))
        self.videoTitle.setObjectName("videoTitle")
        self.videoChannel = QtWidgets.QLabel(self.videoData)
        self.videoChannel.setGeometry(QtCore.QRect(340, 60, 761, 16))
        self.videoChannel.setObjectName("videoChannel")
        self.downloadSong = QtWidgets.QPushButton(self.videoData)
        self.downloadSong.setEnabled(False)
        self.downloadSong.setGeometry(QtCore.QRect(330, 200, 101, 51))
        self.downloadSong.setObjectName("downloadSong")
        self.downloadVideo = QtWidgets.QPushButton(self.videoData)
        self.downloadVideo.setEnabled(False)
        self.downloadVideo.setGeometry(QtCore.QRect(440, 200, 101, 51))
        self.downloadVideo.setObjectName("downloadVideo")
        self.videoThumbnail = QtWidgets.QLabel(self.videoData)
        self.videoThumbnail.setGeometry(QtCore.QRect(10, 40, 301, 211))
        self.videoThumbnail.setStyleSheet("")
        self.videoThumbnail.setText("")
        self.videoThumbnail.setPixmap(QtGui.QPixmap(":/default/assets/unavailable_video.jpg"))
        self.videoThumbnail.setScaledContents(True)
        self.videoThumbnail.setObjectName("videoThumbnail")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 670, 771, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.downloadStatus = QtWidgets.QLabel(self.centralwidget)
        self.downloadStatus.setGeometry(QtCore.QRect(10, 640, 771, 16))
        self.downloadStatus.setStyleSheet("color: rgb(85, 255, 0);")
        self.downloadStatus.setText("")
        self.downloadStatus.setObjectName("downloadStatus")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Downloader"))
        self.search.setText(_translate("MainWindow", "OK"))
        self.searchResult.setText(_translate("MainWindow", "Video não encontrado!"))
        self.videoTitle.setText(_translate("MainWindow", "Nome:"))
        self.videoChannel.setText(_translate("MainWindow", "Canal:"))
        self.downloadSong.setText(_translate("MainWindow", "Baixar música"))
        self.downloadVideo.setText(_translate("MainWindow", "Baixar video"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
