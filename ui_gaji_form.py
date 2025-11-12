# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gaji_form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_FormGaji(object):
    def setupUi(self, FormGaji):
        if not FormGaji.objectName():
            FormGaji.setObjectName(u"FormGaji")
        FormGaji.resize(475, 625)
        self.verticalLayoutWidget = QWidget(FormGaji)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(190, 50, 241, 231))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.kd_gaji = QLineEdit(self.verticalLayoutWidget)
        self.kd_gaji.setObjectName(u"kd_gaji")

        self.verticalLayout.addWidget(self.kd_gaji)

        self.nik = QLineEdit(self.verticalLayoutWidget)
        self.nik.setObjectName(u"nik")

        self.verticalLayout.addWidget(self.nik)

        self.tunjangan = QLineEdit(self.verticalLayoutWidget)
        self.tunjangan.setObjectName(u"tunjangan")

        self.verticalLayout.addWidget(self.tunjangan)

        self.total_lembur = QLineEdit(self.verticalLayoutWidget)
        self.total_lembur.setObjectName(u"total_lembur")

        self.verticalLayout.addWidget(self.total_lembur)

        self.total_gaji = QLineEdit(self.verticalLayoutWidget)
        self.total_gaji.setObjectName(u"total_gaji")

        self.verticalLayout.addWidget(self.total_gaji)

        self.horizontalLayoutWidget = QWidget(FormGaji)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(50, 280, 383, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnTambah = QPushButton(self.horizontalLayoutWidget)
        self.btnTambah.setObjectName(u"btnTambah")

        self.horizontalLayout_2.addWidget(self.btnTambah)

        self.btnEdit = QPushButton(self.horizontalLayoutWidget)
        self.btnEdit.setObjectName(u"btnEdit")

        self.horizontalLayout_2.addWidget(self.btnEdit)

        self.btnBersih = QPushButton(self.horizontalLayoutWidget)
        self.btnBersih.setObjectName(u"btnBersih")

        self.horizontalLayout_2.addWidget(self.btnBersih)

        self.btnHapus = QPushButton(self.horizontalLayoutWidget)
        self.btnHapus.setObjectName(u"btnHapus")

        self.horizontalLayout_2.addWidget(self.btnHapus)

        self.verticalLayoutWidget_2 = QWidget(FormGaji)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(50, 50, 160, 221))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(10)
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(FormGaji)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(130, 10, 301, 38))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_7.setFont(font1)
        self.tableGaji = QTableWidget(FormGaji)
        if (self.tableGaji.columnCount() < 5):
            self.tableGaji.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableGaji.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableGaji.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableGaji.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableGaji.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableGaji.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableGaji.setObjectName(u"tableGaji")
        self.tableGaji.setGeometry(QRect(50, 400, 381, 192))
        self.editcari = QLineEdit(FormGaji)
        self.editcari.setObjectName(u"editcari")
        self.editcari.setGeometry(QRect(190, 360, 239, 28))
        self.label_8 = QLabel(FormGaji)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 350, 158, 38))
        self.label_8.setFont(font)

        self.retranslateUi(FormGaji)

        QMetaObject.connectSlotsByName(FormGaji)
    # setupUi

    def retranslateUi(self, FormGaji):
        FormGaji.setWindowTitle(QCoreApplication.translate("FormGaji", u"Form", None))
        self.btnTambah.setText(QCoreApplication.translate("FormGaji", u"Tambah", None))
        self.btnEdit.setText(QCoreApplication.translate("FormGaji", u"Edit", None))
        self.btnBersih.setText(QCoreApplication.translate("FormGaji", u"BERSIH", None))
        self.btnHapus.setText(QCoreApplication.translate("FormGaji", u"Hapus", None))
        self.label_2.setText(QCoreApplication.translate("FormGaji", u"Kode Gaji", None))
        self.label_3.setText(QCoreApplication.translate("FormGaji", u"Nik", None))
        self.label_4.setText(QCoreApplication.translate("FormGaji", u"Tunjangan", None))
        self.label_5.setText(QCoreApplication.translate("FormGaji", u"Total Lembur", None))
        self.label_6.setText(QCoreApplication.translate("FormGaji", u"Total Gaji", None))
        self.label_7.setText(QCoreApplication.translate("FormGaji", u"GAJI KARYAWAN", None))
        ___qtablewidgetitem = self.tableGaji.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormGaji", u"kd_gaji", None));
        ___qtablewidgetitem1 = self.tableGaji.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormGaji", u"nik", None));
        ___qtablewidgetitem2 = self.tableGaji.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormGaji", u"tunjangan", None));
        ___qtablewidgetitem3 = self.tableGaji.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormGaji", u"total_lembur", None));
        ___qtablewidgetitem4 = self.tableGaji.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormGaji", u"total_gaji", None));
        self.label_8.setText(QCoreApplication.translate("FormGaji", u"Cari Gaji", None))
    # retranslateUi

