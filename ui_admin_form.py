# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_form.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_FormAdmin(object):
    def setupUi(self, FormAdmin):
        if not FormAdmin.objectName():
            FormAdmin.setObjectName(u"FormAdmin")
        FormAdmin.resize(530, 409)
        self.horizontalLayoutWidget = QWidget(FormAdmin)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(90, 260, 383, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tambah = QPushButton(self.horizontalLayoutWidget)
        self.tambah.setObjectName(u"tambah")

        self.horizontalLayout.addWidget(self.tambah)

        self.edit = QPushButton(self.horizontalLayoutWidget)
        self.edit.setObjectName(u"edit")

        self.horizontalLayout.addWidget(self.edit)

        self.hapus = QPushButton(self.horizontalLayoutWidget)
        self.hapus.setObjectName(u"hapus")

        self.horizontalLayout.addWidget(self.hapus)

        self.pencari = QPushButton(self.horizontalLayoutWidget)
        self.pencari.setObjectName(u"pencari")

        self.horizontalLayout.addWidget(self.pencari)

        self.verticalLayoutWidget = QWidget(FormAdmin)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(190, 150, 171, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.admin = QLineEdit(self.verticalLayoutWidget)
        self.admin.setObjectName(u"admin")

        self.verticalLayout.addWidget(self.admin)

        self.password = QLineEdit(self.verticalLayoutWidget)
        self.password.setObjectName(u"password")

        self.verticalLayout.addWidget(self.password)

        self.label = QLabel(FormAdmin)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 70, 191, 20))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(FormAdmin)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 160, 63, 20))
        font1 = QFont()
        font1.setFamilies([u"Tahoma"])
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(FormAdmin)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 200, 81, 20))
        self.label_3.setFont(font1)

        self.retranslateUi(FormAdmin)

        QMetaObject.connectSlotsByName(FormAdmin)
    # setupUi

    def retranslateUi(self, FormAdmin):
        FormAdmin.setWindowTitle(QCoreApplication.translate("FormAdmin", u"Form", None))
        self.tambah.setText(QCoreApplication.translate("FormAdmin", u"Tambah", None))
        self.edit.setText(QCoreApplication.translate("FormAdmin", u"Edit", None))
        self.hapus.setText(QCoreApplication.translate("FormAdmin", u"Hapus", None))
        self.pencari.setText(QCoreApplication.translate("FormAdmin", u"Pencari", None))
        self.label.setText(QCoreApplication.translate("FormAdmin", u"HALAMAN ADMIN", None))
        self.label_2.setText(QCoreApplication.translate("FormAdmin", u"User", None))
        self.label_3.setText(QCoreApplication.translate("FormAdmin", u"Password", None))
    # retranslateUi

