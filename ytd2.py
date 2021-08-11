# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerusUtBQ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                          QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                         QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                         QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from functions import *
import threading
from pathlib import Path


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(897, 562)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.link_text = QLineEdit(self.centralwidget)
        self.link_text.setObjectName(u"link_text")
        self.link_text.setGeometry(QRect(270, 280, 321, 31))
        self.link_text.setStyleSheet(u"")
        self.audi_only = QCheckBox(self.centralwidget)
        self.audi_only.setObjectName(u"audi_only")
        self.audi_only.setGeometry(QRect(270, 330, 161, 31))
        self.audi_only.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")
        self.download_button = QPushButton(self.centralwidget)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setGeometry(QRect(150, 400, 611, 61))
        self.download_button.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")
        self.link_label = QLabel(self.centralwidget)
        self.link_label.setObjectName(u"link_label")
        self.link_label.setGeometry(QRect(160, 280, 91, 31))
        self.link_label.setStyleSheet(u"font: 75 14pt \"MS Shell Dlg 2\";")
        self.location_explore = QPushButton(self.centralwidget)
        self.location_explore.setObjectName(u"location_explore")
        self.location_explore.setGeometry(QRect(600, 280, 161, 31))
        self.location_explore.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
                                            "")
        self.location_explore.clicked.connect(self.files_io)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 60, 311, 171))
        self.label.setPixmap(QPixmap(u"E:/Youtube Downloader 2/download.png"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 897, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        # self.downloads_path = str(Path.home() / "Downloads")
        self.downloads_path = None
        if self.audi_only.isChecked():
            self.download_button.clicked.connect(self.aud_download)
            print('aud')
        else:
            self.download_button.clicked.connect(self.vid_download)
            print('vid')
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.audi_only.setText(QCoreApplication.translate("MainWindow", u"Audio only", None))
        self.download_button.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.link_label.setText(QCoreApplication.translate("MainWindow", u"Video link:", None))
        self.location_explore.setText(QCoreApplication.translate("MainWindow", u"Browse download location", None))
        self.label.setText("")

    # retranslateUi

    def files_io(self):
        path = QFileDialog.getExistingDirectory()
        path = str(path)
        self.downloads_path = path

    def vid_download(self):
        print('here_vid')
        link = self.link_text.text()
        location = self.downloads_path
        threading.Thread(target=download_video, args=(link, location),daemon=True).start()

    def aud_download(self):
        print('here_aud')
        link = self.link_text.text()
        location = self.downloads_path
        threading.Thread(target=download_audio, args=(link, location),daemon=True).start()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
