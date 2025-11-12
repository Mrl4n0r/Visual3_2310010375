# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'karyawan_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_FormKaryawan(object):
    def setupUi(self, FormKaryawan):
        if not FormKaryawan.objectName():
            FormKaryawan.setObjectName(u"FormKaryawan")
        FormKaryawan.resize(586, 830)
        self.verticalLayoutWidget = QWidget(FormKaryawan)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(250, 40, 281, 431))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lineNik = QLineEdit(self.verticalLayoutWidget)
        self.lineNik.setObjectName(u"lineNik")

        self.verticalLayout.addWidget(self.lineNik)

        self.lineNama = QLineEdit(self.verticalLayoutWidget)
        self.lineNama.setObjectName(u"lineNama")

        self.verticalLayout.addWidget(self.lineNama)

        self.comboJk = QComboBox(self.verticalLayoutWidget)
        self.comboJk.setObjectName(u"comboJk")

        self.verticalLayout.addWidget(self.comboJk)

        self.dateEdit = QDateEdit(self.verticalLayoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.verticalLayout.addWidget(self.dateEdit)

        self.lineAlamat = QLineEdit(self.verticalLayoutWidget)
        self.lineAlamat.setObjectName(u"lineAlamat")

        self.verticalLayout.addWidget(self.lineAlamat)

        self.cAgama = QComboBox(self.verticalLayoutWidget)
        self.cAgama.setObjectName(u"cAgama")

        self.verticalLayout.addWidget(self.cAgama)

        self.lineNotlp = QLineEdit(self.verticalLayoutWidget)
        self.lineNotlp.setObjectName(u"lineNotlp")

        self.verticalLayout.addWidget(self.lineNotlp)

        self.linePendidikan = QLineEdit(self.verticalLayoutWidget)
        self.linePendidikan.setObjectName(u"linePendidikan")

        self.verticalLayout.addWidget(self.linePendidikan)

        self.lineKjabatan = QLineEdit(self.verticalLayoutWidget)
        self.lineKjabatan.setObjectName(u"lineKjabatan")

        self.verticalLayout.addWidget(self.lineKjabatan)

        self.verticalLayoutWidget_2 = QWidget(FormKaryawan)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(50, 40, 160, 421))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(10)
        font.setBold(False)
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
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

        self.label_7 = QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_2.addWidget(self.label_7)

        self.label_8 = QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_2.addWidget(self.label_8)

        self.label_9 = QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_2.addWidget(self.label_9)

        self.horizontalLayoutWidget = QWidget(FormKaryawan)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 460, 522, 87))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnSimpan = QPushButton(self.horizontalLayoutWidget)
        self.btnSimpan.setObjectName(u"btnSimpan")

        self.horizontalLayout.addWidget(self.btnSimpan)

        self.btnUbah = QPushButton(self.horizontalLayoutWidget)
        self.btnUbah.setObjectName(u"btnUbah")

        self.horizontalLayout.addWidget(self.btnUbah)

        self.btnBersih = QPushButton(self.horizontalLayoutWidget)
        self.btnBersih.setObjectName(u"btnBersih")

        self.horizontalLayout.addWidget(self.btnBersih)

        self.btnHapus = QPushButton(self.horizontalLayoutWidget)
        self.btnHapus.setObjectName(u"btnHapus")

        self.horizontalLayout.addWidget(self.btnHapus)

        self.label_10 = QLabel(FormKaryawan)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(140, 10, 321, 38))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_10.setFont(font1)
        self.tableKaryawan = QTableWidget(FormKaryawan)
        if (self.tableKaryawan.columnCount() < 9):
            self.tableKaryawan.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableKaryawan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableKaryawan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableKaryawan.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableKaryawan.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableKaryawan.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableKaryawan.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableKaryawan.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableKaryawan.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableKaryawan.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableKaryawan.setObjectName(u"tableKaryawan")
        self.tableKaryawan.setGeometry(QRect(30, 600, 521, 192))
        self.label_11 = QLabel(FormKaryawan)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(50, 550, 158, 40))
        self.label_11.setFont(font)
        self.editcari = QLineEdit(FormKaryawan)
        self.editcari.setObjectName(u"editcari")
        self.editcari.setGeometry(QRect(250, 550, 279, 28))

        self.retranslateUi(FormKaryawan)

        QMetaObject.connectSlotsByName(FormKaryawan)
    # setupUi

    def retranslateUi(self, FormKaryawan):
        FormKaryawan.setWindowTitle(QCoreApplication.translate("FormKaryawan", u"Form", None))
        self.label.setText(QCoreApplication.translate("FormKaryawan", u"Nik", None))
        self.label_2.setText(QCoreApplication.translate("FormKaryawan", u"Nama Karyawan", None))
        self.label_3.setText(QCoreApplication.translate("FormKaryawan", u"Jenis Kelamin", None))
        self.label_4.setText(QCoreApplication.translate("FormKaryawan", u"Tanggal Lahir", None))
        self.label_5.setText(QCoreApplication.translate("FormKaryawan", u"Alamat", None))
        self.label_6.setText(QCoreApplication.translate("FormKaryawan", u"Agama", None))
        self.label_7.setText(QCoreApplication.translate("FormKaryawan", u"No Telpon", None))
        self.label_8.setText(QCoreApplication.translate("FormKaryawan", u"Pendidikan", None))
        self.label_9.setText(QCoreApplication.translate("FormKaryawan", u"Kode Jabatan", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormKaryawan", u"SIMPAN", None))
        self.btnUbah.setText(QCoreApplication.translate("FormKaryawan", u"EDIT", None))
        self.btnBersih.setText(QCoreApplication.translate("FormKaryawan", u"BERSIH", None))
        self.btnHapus.setText(QCoreApplication.translate("FormKaryawan", u"HAPUS", None))
        self.label_10.setText(QCoreApplication.translate("FormKaryawan", u"KARYAWAN PERUSAHAAN", None))
        ___qtablewidgetitem = self.tableKaryawan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormKaryawan", u"nik", None));
        ___qtablewidgetitem1 = self.tableKaryawan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormKaryawan", u"nama_karyawan", None));
        ___qtablewidgetitem2 = self.tableKaryawan.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormKaryawan", u"jk", None));
        ___qtablewidgetitem3 = self.tableKaryawan.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormKaryawan", u"tgl_lahir", None));
        ___qtablewidgetitem4 = self.tableKaryawan.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormKaryawan", u"alamat_karyawan", None));
        ___qtablewidgetitem5 = self.tableKaryawan.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FormKaryawan", u"agama", None));
        ___qtablewidgetitem6 = self.tableKaryawan.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("FormKaryawan", u"no_hp", None));
        ___qtablewidgetitem7 = self.tableKaryawan.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("FormKaryawan", u"pendidikan", None));
        ___qtablewidgetitem8 = self.tableKaryawan.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("FormKaryawan", u"kd_jabatan", None));
        self.label_11.setText(QCoreApplication.translate("FormKaryawan", u"Cari Karyawan", None))
    # retranslateUi

