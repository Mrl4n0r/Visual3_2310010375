# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'absensi_form.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_FormAbsensi(object):
    def setupUi(self, FormAbsensi):
        if not FormAbsensi.objectName():
            FormAbsensi.setObjectName(u"FormAbsensi")
        FormAbsensi.resize(503, 659)
        self.label = QLabel(FormAbsensi)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 50, 201, 20))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.horizontalLayoutWidget = QWidget(FormAbsensi)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(90, 250, 341, 101))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.rHadir = QRadioButton(self.horizontalLayoutWidget)
        self.rHadir.setObjectName(u"rHadir")

        self.horizontalLayout_2.addWidget(self.rHadir)

        self.rIzin = QRadioButton(self.horizontalLayoutWidget)
        self.rIzin.setObjectName(u"rIzin")

        self.horizontalLayout_2.addWidget(self.rIzin)

        self.rSakit = QRadioButton(self.horizontalLayoutWidget)
        self.rSakit.setObjectName(u"rSakit")

        self.horizontalLayout_2.addWidget(self.rSakit)

        self.verticalLayoutWidget = QWidget(FormAbsensi)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(210, 100, 231, 171))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.kdAbsen = QLineEdit(self.verticalLayoutWidget)
        self.kdAbsen.setObjectName(u"kdAbsen")

        self.verticalLayout.addWidget(self.kdAbsen)

        self.nik = QLineEdit(self.verticalLayoutWidget)
        self.nik.setObjectName(u"nik")

        self.verticalLayout.addWidget(self.nik)

        self.namaKry = QLineEdit(self.verticalLayoutWidget)
        self.namaKry.setObjectName(u"namaKry")

        self.verticalLayout.addWidget(self.namaKry)

        self.tglrekap = QDateEdit(self.verticalLayoutWidget)
        self.tglrekap.setObjectName(u"tglrekap")

        self.verticalLayout.addWidget(self.tglrekap)

        self.verticalLayoutWidget_2 = QWidget(FormAbsensi)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(50, 100, 160, 171))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(10)
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_5)

        self.tableAbsen = QTableWidget(FormAbsensi)
        if (self.tableAbsen.columnCount() < 5):
            self.tableAbsen.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableAbsen.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableAbsen.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableAbsen.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableAbsen.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableAbsen.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableAbsen.setObjectName(u"tableAbsen")
        self.tableAbsen.setGeometry(QRect(40, 440, 411, 192))
        self.horizontalLayoutWidget_2 = QWidget(FormAbsensi)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(60, 330, 381, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnDone = QPushButton(self.horizontalLayoutWidget_2)
        self.btnDone.setObjectName(u"btnDone")

        self.horizontalLayout.addWidget(self.btnDone)

        self.btnEdit = QPushButton(self.horizontalLayoutWidget_2)
        self.btnEdit.setObjectName(u"btnEdit")

        self.horizontalLayout.addWidget(self.btnEdit)

        self.btnBersih = QPushButton(self.horizontalLayoutWidget_2)
        self.btnBersih.setObjectName(u"btnBersih")

        self.horizontalLayout.addWidget(self.btnBersih)

        self.btnHapus = QPushButton(self.horizontalLayoutWidget_2)
        self.btnHapus.setObjectName(u"btnHapus")

        self.horizontalLayout.addWidget(self.btnHapus)

        self.editcari = QLineEdit(FormAbsensi)
        self.editcari.setObjectName(u"editcari")
        self.editcari.setGeometry(QRect(210, 410, 229, 28))
        self.label_6 = QLabel(FormAbsensi)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 410, 158, 37))
        self.label_6.setFont(font1)

        self.retranslateUi(FormAbsensi)

        QMetaObject.connectSlotsByName(FormAbsensi)
    # setupUi

    def retranslateUi(self, FormAbsensi):
        FormAbsensi.setWindowTitle(QCoreApplication.translate("FormAbsensi", u"Form", None))
        self.label.setText(QCoreApplication.translate("FormAbsensi", u"ABSENSI KARYAWAN", None))
        self.rHadir.setText(QCoreApplication.translate("FormAbsensi", u"Hadir", None))
        self.rIzin.setText(QCoreApplication.translate("FormAbsensi", u"Izin", None))
        self.rSakit.setText(QCoreApplication.translate("FormAbsensi", u"Sakit", None))
        self.label_2.setText(QCoreApplication.translate("FormAbsensi", u"Kode Absen", None))
        self.label_3.setText(QCoreApplication.translate("FormAbsensi", u"Nik", None))
        self.label_4.setText(QCoreApplication.translate("FormAbsensi", u"Nama", None))
        self.label_5.setText(QCoreApplication.translate("FormAbsensi", u"Tanggal Rekap", None))
        ___qtablewidgetitem = self.tableAbsen.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormAbsensi", u"kd_absen", None));
        ___qtablewidgetitem1 = self.tableAbsen.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormAbsensi", u"nik", None));
        ___qtablewidgetitem2 = self.tableAbsen.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormAbsensi", u"nama_karyawan", None));
        ___qtablewidgetitem3 = self.tableAbsen.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormAbsensi", u"tgl_rekap", None));
        ___qtablewidgetitem4 = self.tableAbsen.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormAbsensi", u"status_kehadiran", None));
        self.btnDone.setText(QCoreApplication.translate("FormAbsensi", u"Simpan", None))
        self.btnEdit.setText(QCoreApplication.translate("FormAbsensi", u"Edit", None))
        self.btnBersih.setText(QCoreApplication.translate("FormAbsensi", u"BERSIH", None))
        self.btnHapus.setText(QCoreApplication.translate("FormAbsensi", u"Hapus", None))
        self.label_6.setText(QCoreApplication.translate("FormAbsensi", u"Cari Absen", None))
    # retranslateUi

