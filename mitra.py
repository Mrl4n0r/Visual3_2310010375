# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QMessageBox, QAbstractItemView, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class Mitra(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        ui_file_name = "mitra_form.ui"
        ui_file = QFile(ui_file_name)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formMitra = loader.load(ui_file, None)
        ui_file.close()
        self.formMitra.setWindowTitle("Form Data Mitra")
        self.crud = my_cruddb()
        self.formMitra.btnTambah.clicked.connect(self.doSimpan)
        self.formMitra.btnEdit.clicked.connect(self.doUbah)
        self.formMitra.btnHapus.clicked.connect(self.doHapus)
        self.formMitra.btnBersih.clicked.connect(self.bersih)
        self.formMitra.tableMitra.cellClicked.connect(self.pilihBaris)
        self.formMitra.editcari.textChanged.connect(self.doCari)
        self.tampilData()

    def tampilData(self):
        table = self.formMitra.tableMitra
        data = self.crud.dataMitra()
        table.setRowCount(0)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)

        headers = ["Kode Mitra", "Nama Mitra", "Alamat", "Telepon", "Email"]
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)

        if not data:
            return

        for r in data:
            i = table.rowCount()
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(r.get("kd_mitra")))
            table.setItem(i, 1, QTableWidgetItem(r.get("nama_mitra")))
            table.setItem(i, 2, QTableWidgetItem(r.get("alamat_mitra") or ""))
            table.setItem(i, 3, QTableWidgetItem(r.get("telepon_mitra") or ""))
            table.setItem(i, 4, QTableWidgetItem(r.get("email_mitra") or ""))
        table.resizeColumnsToContents()

    def pilihBaris(self, row, col):
        table = self.formMitra.tableMitra
        kd_mitra = table.item(row, 0).text()
        nama_mitra = table.item(row, 1).text()
        alamat_mitra = table.item(row, 2).text()
        telepon_mitra = table.item(row, 3).text()
        email_mitra = table.item(row, 4).text()

        self.formMitra.kd_mitra.setText(kd_mitra)
        self.formMitra.nama_mitra.setText(nama_mitra)
        self.formMitra.alamat_mitra.setText(alamat_mitra)
        self.formMitra.telepon_mitra.setText(telepon_mitra)
        self.formMitra.email_mitra.setText(email_mitra)
        self.formMitra.kd_mitra.setReadOnly(True)

    def doSimpan(self):
        if not self.formMitra.kd_mitra.text().strip():
            QMessageBox.information(None,"Informasi","Kode Mitra belum di isi")
            self.formMitra.kd_mitra.setFocus()
        elif not self.formMitra.nama_mitra.text().strip():
            QMessageBox.information(None,"Informasi","Nama Mitra belum di isi")
            self.formMitra.nama_mitra.setFocus()
        elif not self.formMitra.alamat_mitra.text().strip():
            QMessageBox.information(None,"Informasi","Alamat Mitra belum di isi")
            self.formMitra.alamat_mitra.setFocus()
        elif not self.formMitra.telepon_mitra.text().strip():
            QMessageBox.information(None,"Informasi","Telepon Mitra belum di isi")
            self.formMitra.telepon_mitra.setFocus()
        elif not self.formMitra.email_mitra.text().strip():
            QMessageBox.information(None,"Informasi","Email Mitra belum di isi")
            self.formMitra.email_mitra.setFocus()
        else:
            pesan = QMessageBox.question(None, "Konfirmasi Simpan", "Simpan Mitra baru ini?",
                                         QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                kd_mitra = self.formMitra.kd_mitra.text()
                nama_mitra = self.formMitra.nama_mitra.text()
                alamat_mitra = self.formMitra.alamat_mitra.text()
                telepon_mitra = self.formMitra.telepon_mitra.text()
                email_mitra = self.formMitra.email_mitra.text()
                self.crud.simpanMitra(kd_mitra, nama_mitra, alamat_mitra, telepon_mitra, email_mitra)
                QMessageBox.information(None,"Informasi","Data Mitra Berhasil di Simpan")
                self.tampilData()
                self.bersih()
            else:
                pass

    def doUbah(self):
        kd_mitra = self.formMitra.kd_mitra.text()
        nama_mitra = self.formMitra.nama_mitra.text()
        alamat_mitra = self.formMitra.alamat_mitra.text()
        telepon_mitra = self.formMitra.telepon_mitra.text()
        email_mitra = self.formMitra.email_mitra.text()
        self.crud.ubahMitra(kd_mitra, nama_mitra, alamat_mitra, telepon_mitra, email_mitra)
        self.tampilData()
        QMessageBox.information(None,"Informasi","Data Mitra Berhasil di Ubah")
        self.bersih()

    def doHapus(self):
        kd_mitra = self.formMitra.kd_mitra.text()
        self.crud.hapusMitra(kd_mitra)
        self.tampilData()
        QMessageBox.information(None,"Informasi","Data Mitra Berhasil di Hapus")
        self.bersih()

    def doCari(self):
        kata = self.formMitra.editcari.text()
        data = self.crud.CariMitra(kata)
        table = self.formMitra.tableMitra
        table.setRowCount(0)

        for r in data:
            i = table.rowCount()
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(r.get("kd_mitra")))
            table.setItem(i, 1, QTableWidgetItem(r.get("nama_mitra")))
            table.setItem(i, 2, QTableWidgetItem(r.get("alamat_mitra") or ""))
            table.setItem(i, 3, QTableWidgetItem(r.get("telepon_mitra") or ""))
            table.setItem(i, 4, QTableWidgetItem(r.get("email_mitra") or ""))

    def bersih(self):
        self.formMitra.kd_mitra.clear()
        self.formMitra.kd_mitra.setReadOnly(False)
        self.formMitra.nama_mitra.clear()
        self.formMitra.alamat_mitra.clear()
        self.formMitra.telepon_mitra.clear()
        self.formMitra.email_mitra.clear()
        self.formMitra.editcari.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mitra()
    window.formMitra.show()
    sys.exit(app.exec())
