# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QAbstractItemView, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from crudDB import my_cruddb

class Gaji(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        ui_file_name = "gaji_form.ui"
        ui_file = QFile(ui_file_name)

        if not ui_file.open(QFile.ReadOnly):
            print(f"Error: Tidak bisa membuka file {ui_file_name}")
            sys.exit(-1)

        loader = QUiLoader()
        self.formGaji = loader.load(ui_file, None)
        ui_file.close()
        self.formGaji.setWindowTitle("Form Data Gaji")
        self.crud = my_cruddb()
        self.formGaji.btnTambah.clicked.connect(self.doSimpanGaji)
        self.formGaji.btnEdit.clicked.connect(self.doUbahGaji)
        self.formGaji.btnHapus.clicked.connect(self.doHapusGaji)
        self.formGaji.btnBersih.clicked.connect(self.doBersihForm)
        self.formGaji.tableGaji.cellClicked.connect(self.onTableCellClicked)
        self.formGaji.editcari.textChanged.connect(self.doCariGaji)
        self.tampilData()

    def tampilData(self):
        table = self.formGaji.tableGaji
        data = self.crud.dataGaji()
        table.setRowCount(0)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        headers = ["KD Gaji", "NIK", "Tunjangan", "Total Lembur", "Total Gaji"]
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)

        if not data:
            return

        for r in data:
            i = table.rowCount()
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(str(r.get("kd_gaji"))))
            table.setItem(i, 1, QTableWidgetItem(str(r.get("nik"))))
            table.setItem(i, 2, QTableWidgetItem(str(r.get("tunjangan"))))
            table.setItem(i, 3, QTableWidgetItem(str(r.get("total_lembur"))))
            table.setItem(i, 4, QTableWidgetItem(str(r.get("total_gaji"))))
        table.resizeColumnsToContents()

    def onTableCellClicked(self, row, column):
        table = self.formGaji.tableGaji
        kd_gaji = table.item(row, 0).text()
        nik = table.item(row, 1).text()
        tunjangan = table.item(row, 2).text()
        total_lembur = table.item(row, 3).text()
        total_gaji = table.item(row, 4).text()
        self.formGaji.kd_gaji.setText(kd_gaji)
        self.formGaji.nik.setText(nik)
        self.formGaji.tunjangan.setText(tunjangan)
        self.formGaji.total_lembur.setText(total_lembur)
        self.formGaji.total_gaji.setText(total_gaji)
        self.formGaji.kd_gaji.setReadOnly(True)

    def doSimpanGaji(self):
        if not self.formGaji.nik.text().strip():
            QMessageBox.information(None,"Informasi","NIK belum di isi")
            self.formGaji.nik.setFocus()
        elif not self.formGaji.tunjangan.text().strip():
            QMessageBox.information(None,"Informasi","Tunjangan belum di isi")
            self.formGaji.tunjangan.setFocus()
        elif not self.formGaji.total_lembur.text().strip():
            QMessageBox.information(None,"Informasi","Total Lembur belum di isi")
            self.formGaji.total_lembur.setFocus()
        elif not self.formGaji.total_gaji.text().strip():
            QMessageBox.information(None,"Informasi","Total Gaji belum di isi")
            self.formGaji.total_gaji.setFocus()
        else:

            pesan = QMessageBox.question(None, "Konfirmasi Simpan", "Apakah Anda Yakin Menyimpan Data Gaji Ini?",
                                         QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                nik = self.formGaji.nik.text()
                tunjangan = self.formGaji.tunjangan.text()
                total_lembur = self.formGaji.total_lembur.text()
                total_gaji = self.formGaji.total_gaji.text()
                self.crud.simpanGaji(nik, tunjangan, total_lembur, total_gaji)
                QMessageBox.information(None,"Informasi","Data Gaji Berhasil di Simpan")
                self.tampilData() # Sesuai referensi
                self.doBersihForm()
            else:
                pass

    def doUbahGaji(self):
        kd_gaji = self.formGaji.kd_gaji.text()
        nik = self.formGaji.nik.text()
        tunjangan = self.formGaji.tunjangan.text()
        total_lembur = self.formGaji.total_lembur.text()
        total_gaji = self.formGaji.total_gaji.text()
        self.crud.ubahGaji(kd_gaji, nik, tunjangan, total_lembur, total_gaji)
        self.tampilData()
        self.doBersihForm()

    def doHapusGaji(self):
        kd_gaji = self.formGaji.kd_gaji.text()
        if not kd_gaji.strip():
            QMessageBox.information(None,"Informasi","Kode Gaji harus diisi (Pilih dari tabel)")
            return
        self.crud.hapusGaji(kd_gaji)
        self.tampilData()
        self.doBersihForm()

    def doCariGaji(self):
        kata = self.formGaji.editcari.text()
        data = self.crud.CariGaji(kata)
        table = self.formGaji.tableGaji
        table.setRowCount(0)

        for r in data:
            i = table.rowCount()
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(str(r["kd_gaji"])))
            table.setItem(i, 1, QTableWidgetItem(r["nik"]))
            table.setItem(i, 2, QTableWidgetItem(str(r["tunjangan"])))
            table.setItem(i, 3, QTableWidgetItem(str(r["total_lembur"])))
            table.setItem(i, 4, QTableWidgetItem(str(r["total_gaji"])))

    def doBersihForm(self):
        self.formGaji.kd_gaji.clear()
        self.formGaji.nik.clear()
        self.formGaji.tunjangan.clear()
        self.formGaji.total_lembur.clear()
        self.formGaji.total_gaji.clear()
        self.formGaji.kd_gaji.setReadOnly(False)
        self.formGaji.editcari.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Gaji()
    window.formGaji.show()
    sys.exit(app.exec())
