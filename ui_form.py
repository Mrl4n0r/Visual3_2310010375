# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(800, 600)
        self.actionAbsensi = QAction(main)
        self.actionAbsensi.setObjectName(u"actionAbsensi")
        self.actionGaji = QAction(main)
        self.actionGaji.setObjectName(u"actionGaji")
        self.actionJabatan = QAction(main)
        self.actionJabatan.setObjectName(u"actionJabatan")
        self.actionKaryawan = QAction(main)
        self.actionKaryawan.setObjectName(u"actionKaryawan")
        self.actionMitra = QAction(main)
        self.actionMitra.setObjectName(u"actionMitra")
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main)
        self.statusbar.setObjectName(u"statusbar")
        main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionAbsensi)
        self.menuMenu.addAction(self.actionGaji)
        self.menuMenu.addAction(self.actionJabatan)
        self.menuMenu.addAction(self.actionKaryawan)
        self.menuMenu.addAction(self.actionMitra)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main", None))
        self.actionAbsensi.setText(QCoreApplication.translate("main", u"Absensi", None))
        self.actionGaji.setText(QCoreApplication.translate("main", u"Gaji", None))
        self.actionJabatan.setText(QCoreApplication.translate("main", u"Jabatan", None))
        self.actionKaryawan.setText(QCoreApplication.translate("main", u"Karyawan", None))
        self.actionMitra.setText(QCoreApplication.translate("main", u"Mitra", None))
        self.menuMenu.setTitle(QCoreApplication.translate("main", u"Menu", None))
    # retranslateUi

