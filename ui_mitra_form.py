# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mitra_form.ui'
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

class Ui_FormMitra(object):
    def setupUi(self, FormMitra):
        if not FormMitra.objectName():
            FormMitra.setObjectName(u"FormMitra")
        FormMitra.resize(530, 563)
        self.verticalLayoutWidget = QWidget(FormMitra)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(280, 60, 171, 241))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.kd_mitra = QLineEdit(self.verticalLayoutWidget)
        self.kd_mitra.setObjectName(u"kd_mitra")

        self.verticalLayout.addWidget(self.kd_mitra)

        self.nama_mitra = QLineEdit(self.verticalLayoutWidget)
        self.nama_mitra.setObjectName(u"nama_mitra")

        self.verticalLayout.addWidget(self.nama_mitra)

        self.alamat_mitra = QLineEdit(self.verticalLayoutWidget)
        self.alamat_mitra.setObjectName(u"alamat_mitra")

        self.verticalLayout.addWidget(self.alamat_mitra)

        self.telepon_mitra = QLineEdit(self.verticalLayoutWidget)
        self.telepon_mitra.setObjectName(u"telepon_mitra")

        self.verticalLayout.addWidget(self.telepon_mitra)

        self.email_mitra = QLineEdit(self.verticalLayoutWidget)
        self.email_mitra.setObjectName(u"email_mitra")

        self.verticalLayout.addWidget(self.email_mitra)

        self.label = QLabel(FormMitra)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 20, 191, 20))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.horizontalLayoutWidget = QWidget(FormMitra)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(70, 300, 383, 80))
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

        self.verticalLayoutWidget_2 = QWidget(FormMitra)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(80, 60, 160, 231))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(10)
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_5)

        self.editcari = QLineEdit(FormMitra)
        self.editcari.setObjectName(u"editcari")
        self.editcari.setGeometry(QRect(280, 380, 169, 28))
        self.label_7 = QLabel(FormMitra)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 370, 158, 40))
        self.label_7.setFont(font1)
        self.tableMitra = QTableWidget(FormMitra)
        if (self.tableMitra.columnCount() < 5):
            self.tableMitra.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableMitra.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableMitra.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableMitra.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableMitra.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableMitra.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableMitra.setObjectName(u"tableMitra")
        self.tableMitra.setGeometry(QRect(70, 430, 381, 192))

        self.retranslateUi(FormMitra)

        QMetaObject.connectSlotsByName(FormMitra)
    # setupUi

    def retranslateUi(self, FormMitra):
        FormMitra.setWindowTitle(QCoreApplication.translate("FormMitra", u"Form", None))
        self.label.setText(QCoreApplication.translate("FormMitra", u"HALAMAN ADMIN", None))
        self.btnTambah.setText(QCoreApplication.translate("FormMitra", u"Tambah", None))
        self.btnEdit.setText(QCoreApplication.translate("FormMitra", u"Edit", None))
        self.btnBersih.setText(QCoreApplication.translate("FormMitra", u"BERSIH", None))
        self.btnHapus.setText(QCoreApplication.translate("FormMitra", u"Hapus", None))
        self.label_3.setText(QCoreApplication.translate("FormMitra", u"Kode Mitra :", None))
        self.label_2.setText(QCoreApplication.translate("FormMitra", u"Nama Mitra :", None))
        self.label_6.setText(QCoreApplication.translate("FormMitra", u"Alamat Mitra :", None))
        self.label_4.setText(QCoreApplication.translate("FormMitra", u"No telpon :", None))
        self.label_5.setText(QCoreApplication.translate("FormMitra", u"Email :", None))
        self.label_7.setText(QCoreApplication.translate("FormMitra", u"Pencarian :", None))
        ___qtablewidgetitem = self.tableMitra.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormMitra", u"kd_mitra", None));
        ___qtablewidgetitem1 = self.tableMitra.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormMitra", u"nama_mitra", None));
        ___qtablewidgetitem2 = self.tableMitra.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormMitra", u"alamat_mitra", None));
        ___qtablewidgetitem3 = self.tableMitra.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormMitra", u"telepon_mitra", None));
        ___qtablewidgetitem4 = self.tableMitra.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormMitra", u"email_mitra", None));
    # retranslateUi

