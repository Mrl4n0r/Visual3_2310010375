# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class Jabatan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        ui_file = QFile("jabatan_form.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formJabatan = loader.load(ui_file, None)
        ui_file.close()
        self.formJabatan.setWindowTitle("Form Data Jabatan")
        self.crud = my_cruddb()
        self.formJabatan.btnTambah.clicked.connect(self.doSimpan)
        self.formJabatan.btnEdit.clicked.connect(self.doUbah)
        self.formJabatan.btnHapus.clicked.connect(self.doHapus)
        self.formJabatan.btnBersih.clicked.connect(self.bersih)
        self.formJabatan.tableJabatan.cellClicked.connect(self.pilihBaris)
        self.formJabatan.editcari.textChanged.connect(self.doCari)
        self.tampilData()

    def tampilData(self):
        table = self.formJabatan.tableJabatan
        data = self.crud.dataJabatan()
        table.setRowCount(0)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        headers = ["KD Jabatan", "Nama Jabatan", "Tunjangan", "Gaji Pokok", "Deskripsi"]
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)

        if not data:
            return

        for r in data:
            i = table.rowCount()
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(str(r["kd_jabatan"])))
            table.setItem(i, 1, QTableWidgetItem(str(r["nama_jabatan"])))
            table.setItem(i, 2, QTableWidgetItem(str(r["tunjangan"])))
            table.setItem(i, 3, QTableWidgetItem(str(r["gaji_pokok"])))
            table.setItem(i, 4, QTableWidgetItem(str(r["deskripsi"] or "")))

        table.resizeColumnsToContents()

    def doSimpan(self):
        if not self.formJabatan.kd_jabatan.text().strip():
            QMessageBox.information(None,"Informasi","Kode Jabatan belum di isi")
            self.formJabatan.kd_jabatan.setFocus()
        elif not self.formJabatan.nama_jabatan.text().strip():
            QMessageBox.information(None,"Informasi","Nama Jabatan belum di isi")
            self.formJabatan.nama_jabatan.setFocus()
        elif not self.formJabatan.tunjangan.text().strip():
            QMessageBox.information(None,"Informasi","Tunjangan belum di isi")
            self.formJabatan.tunjangan.setFocus()
        elif not self.formJabatan.gaji_pokok.text().strip():
            QMessageBox.information(None,"Informasi","Gaji Pokok belum di isi")
            self.formJabatan.gaji_pokok.setFocus()
        else:

            pesan = QMessageBox.question(None, "Konfirmasi", "Apakah Anda Yakin Menyimpan Data Ini?",
                                         QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                kd = self.formJabatan.kd_jabatan.text()
                nama = self.formJabatan.nama_jabatan.text()
                tunjangan = self.formJabatan.tunjangan.text()
                gaji = self.formJabatan.gaji_pokok.text()
                desk = self.formJabatan.deskripsi.text()
                self.crud.simpanJabatan(kd, nama, tunjangan, gaji, desk)
                self.tampilData()
                QMessageBox.information(None,"Informasi","Data Berhasil di Simpan")
                self.bersih()
            else:
                pass

    def doUbah(self):
        kd = self.formJabatan.kd_jabatan.text()
        nama = self.formJabatan.nama_jabatan.text()
        tunjangan = self.formJabatan.tunjangan.text()
        gaji = self.formJabatan.gaji_pokok.text()
        desk = self.formJabatan.deskripsi.text()
        self.crud.ubahJabatan(kd, nama, tunjangan, gaji, desk)
        self.tampilData()
        QMessageBox.information(None,"Informasi","Data Berhasil di Ubah")
        self.bersih()

    def doHapus(self):
        kd = self.formJabatan.kd_jabatan.text()
        self.crud.hapusJabatan(kd)
        self.tampilData()
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")
        self.bersih()

    def doCari(self):
        kata = self.formJabatan.editcari.text()
        data = self.crud.CariJabatan(kata)
        table = self.formJabatan.tableJabatan
        table.setRowCount(0)

        for r in data:
            i = table.rowCount()
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(r["kd_jabatan"]))
            table.setItem(i, 1, QTableWidgetItem(r["nama_jabatan"]))
            table.setItem(i, 2, QTableWidgetItem(str(r["tunjangan"])))
            table.setItem(i, 3, QTableWidgetItem(str(r["gaji_pokok"])))
            table.setItem(i, 4, QTableWidgetItem(r["deskripsi"] or ""))

    def pilihBaris(self, row, col):
        t = self.formJabatan.tableJabatan
        self.formJabatan.kd_jabatan.setText(t.item(row, 0).text())
        self.formJabatan.nama_jabatan.setText(t.item(row, 1).text())
        self.formJabatan.tunjangan.setText(t.item(row, 2).text())
        self.formJabatan.gaji_pokok.setText(t.item(row, 3).text())
        self.formJabatan.deskripsi.setText(t.item(row, 4).text())

        self.formJabatan.kd_jabatan.setReadOnly(True)

    def bersih(self):
        self.formJabatan.kd_jabatan.clear()
        self.formJabatan.nama_jabatan.clear()
        self.formJabatan.tunjangan.clear()
        self.formJabatan.gaji_pokok.clear()
        self.formJabatan.deskripsi.clear()
        self.formJabatan.editcari.clear()
        self.formJabatan.kd_jabatan.setReadOnly(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Jabatan()
    w.formJabatan.show()
    sys.exit(app.exec())
