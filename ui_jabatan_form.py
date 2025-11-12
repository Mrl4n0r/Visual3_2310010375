# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'jabatan_form.ui'
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

class Ui_FormJabatan(object):
    def setupUi(self, FormJabatan):
        if not FormJabatan.objectName():
            FormJabatan.setObjectName(u"FormJabatan")
        FormJabatan.resize(546, 578)
        self.verticalLayoutWidget = QWidget(FormJabatan)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(250, 40, 231, 211))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.kd_jabatan = QLineEdit(self.verticalLayoutWidget)
        self.kd_jabatan.setObjectName(u"kd_jabatan")

        self.verticalLayout.addWidget(self.kd_jabatan)

        self.nama_jabatan = QLineEdit(self.verticalLayoutWidget)
        self.nama_jabatan.setObjectName(u"nama_jabatan")

        self.verticalLayout.addWidget(self.nama_jabatan)

        self.tunjangan = QLineEdit(self.verticalLayoutWidget)
        self.tunjangan.setObjectName(u"tunjangan")

        self.verticalLayout.addWidget(self.tunjangan)

        self.gaji_pokok = QLineEdit(self.verticalLayoutWidget)
        self.gaji_pokok.setObjectName(u"gaji_pokok")

        self.verticalLayout.addWidget(self.gaji_pokok)

        self.deskripsi = QLineEdit(self.verticalLayoutWidget)
        self.deskripsi.setObjectName(u"deskripsi")

        self.verticalLayout.addWidget(self.deskripsi)

        self.horizontalLayoutWidget = QWidget(FormJabatan)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(90, 240, 383, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnTambah = QPushButton(self.horizontalLayoutWidget)
        self.btnTambah.setObjectName(u"btnTambah")

        self.horizontalLayout.addWidget(self.btnTambah)

        self.btnEdit = QPushButton(self.horizontalLayoutWidget)
        self.btnEdit.setObjectName(u"btnEdit")

        self.horizontalLayout.addWidget(self.btnEdit)

        self.btnBersih = QPushButton(self.horizontalLayoutWidget)
        self.btnBersih.setObjectName(u"btnBersih")

        self.horizontalLayout.addWidget(self.btnBersih)

        self.btnHapus = QPushButton(self.horizontalLayoutWidget)
        self.btnHapus.setObjectName(u"btnHapus")

        self.horizontalLayout.addWidget(self.btnHapus)

        self.verticalLayoutWidget_2 = QWidget(FormJabatan)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(90, 40, 160, 201))
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

        self.label_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_5 = QLabel(FormJabatan)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(140, 0, 291, 38))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_5.setFont(font1)
        self.tableJabatan = QTableWidget(FormJabatan)
        if (self.tableJabatan.columnCount() < 5):
            self.tableJabatan.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableJabatan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableJabatan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableJabatan.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableJabatan.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableJabatan.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableJabatan.setObjectName(u"tableJabatan")
        self.tableJabatan.setGeometry(QRect(90, 360, 381, 192))
        self.editcari = QLineEdit(FormJabatan)
        self.editcari.setObjectName(u"editcari")
        self.editcari.setGeometry(QRect(250, 320, 229, 28))
        self.label_8 = QLabel(FormJabatan)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(90, 310, 158, 34))
        self.label_8.setFont(font)

        self.retranslateUi(FormJabatan)

        QMetaObject.connectSlotsByName(FormJabatan)
    # setupUi

    def retranslateUi(self, FormJabatan):
        FormJabatan.setWindowTitle(QCoreApplication.translate("FormJabatan", u"Form", None))
        self.btnTambah.setText(QCoreApplication.translate("FormJabatan", u"Tambah", None))
        self.btnEdit.setText(QCoreApplication.translate("FormJabatan", u"Edit", None))
        self.btnBersih.setText(QCoreApplication.translate("FormJabatan", u"BERSIH", None))
        self.btnHapus.setText(QCoreApplication.translate("FormJabatan", u"Hapus", None))
        self.label_2.setText(QCoreApplication.translate("FormJabatan", u"Kode Jabatan", None))
        self.label_3.setText(QCoreApplication.translate("FormJabatan", u"Nama Jabatan", None))
        self.label_4.setText(QCoreApplication.translate("FormJabatan", u"Tunjangan", None))
        self.label_6.setText(QCoreApplication.translate("FormJabatan", u"Gaji Pokok", None))
        self.label_7.setText(QCoreApplication.translate("FormJabatan", u"Deskripsi", None))
        self.label_5.setText(QCoreApplication.translate("FormJabatan", u"JABATAN PERUSAHAAN", None))
        ___qtablewidgetitem = self.tableJabatan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormJabatan", u"kd_jabatan", None));
        ___qtablewidgetitem1 = self.tableJabatan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormJabatan", u"nama_jabatan", None));
        ___qtablewidgetitem2 = self.tableJabatan.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormJabatan", u"tunjukan", None));
        ___qtablewidgetitem3 = self.tableJabatan.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormJabatan", u"gaji_pokok", None));
        ___qtablewidgetitem4 = self.tableJabatan.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormJabatan", u"deskripsi", None));
        self.label_8.setText(QCoreApplication.translate("FormJabatan", u"Cari Jabatan", None))
    # retranslateUi

