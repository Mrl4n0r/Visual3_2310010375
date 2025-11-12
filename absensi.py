# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QAbstractItemView, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate
from crudDB import my_cruddb

class Absensi(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        ui_file_name = "absensi_form.ui"
        ui_file = QFile(ui_file_name)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formAbsensi = loader.load(ui_file, None)
        ui_file.close()
        self.formAbsensi.setWindowTitle("Form Data Absensi")
        self.crud = my_cruddb()
        self.formAbsensi.btnDone.clicked.connect(self.doSimpanAbsensi)
        self.formAbsensi.btnEdit.clicked.connect(self.doUbahAbsensi)
        self.formAbsensi.btnHapus.clicked.connect(self.doHapusAbsensi)
        self.formAbsensi.btnBersih.clicked.connect(self.doBersihForm)
        self.formAbsensi.tableAbsen.cellClicked.connect(self.onTableCellClicked)
        self.formAbsensi.editcari.textChanged.connect(self.doCariAbsensi)
        self.tampilData()
        self.formAbsensi.tglrekap.setDate(QDate.currentDate())
        self.formAbsensi.rHadir.setChecked(True)

    def tampilData(self):
        baris = self.crud.dataAbsensi()
        table = self.formAbsensi.tableAbsen
        table.setRowCount(0)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)
        headers = ["KD Absen", "NIK", "Nama Karyawan", "Tgl Rekap", "Status"]
        table.setColumnCount(len(headers))
        table.setHorizontalHeaderLabels(headers)

        if not baris:
            return

        for r in baris:
            i = table.rowCount()
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(str(r["kd_absen"])))
            table.setItem(i, 1, QTableWidgetItem(r["nik"]))
            table.setItem(i, 2, QTableWidgetItem(r["nama_karyawan"]))
            table.setItem(i, 3, QTableWidgetItem(str(r["tgl_rekap"])))
            table.setItem(i, 4, QTableWidgetItem(r["status_kehadiran"]))
        table.resizeColumnsToContents()

    def onTableCellClicked(self, row, column):
        table = self.formAbsensi.tableAbsen
        kd_absen = table.item(row, 0).text()
        nik = table.item(row, 1).text()
        nama_kry = table.item(row, 2).text()
        tgl_rekap = table.item(row, 3).text()
        status = table.item(row, 4).text()
        self.formAbsensi.kdAbsen.setText(kd_absen)
        self.formAbsensi.nik.setText(nik)
        self.formAbsensi.namaKry.setText(nama_kry)
        qdate = QDate.fromString(tgl_rekap, "yyyy-MM-dd")
        self.formAbsensi.tglrekap.setDate(qdate)

        if status == "Hadir":
            self.formAbsensi.rHadir.setChecked(True)
        elif status == "Izin":
            self.formAbsensi.rIzin.setChecked(True)
        elif status == "Sakit":
            self.formAbsensi.rSakit.setChecked(True)
        self.formAbsensi.kdAbsen.setReadOnly(True)

    def _getStatusFromRadio(self):
        if self.formAbsensi.rHadir.isChecked():
            return "Hadir"
        if self.formAbsensi.rIzin.isChecked():
            return "Izin"
        if self.formAbsensi.rSakit.isChecked():
            return "Sakit"
        return "Hadir"

    def doSimpanAbsensi(self):
        if not self.formAbsensi.nik.text().strip():
            QMessageBox.information(None,"Informasi","NIK belum di isi")
            self.formAbsensi.nik.setFocus()
        elif not self.formAbsensi.namaKry.text().strip():
            QMessageBox.information(None,"Informasi","Nama Karyawan belum di isi")
            self.formAbsensi.namaKry.setFocus()
        else:
            pesan = QMessageBox.question(None, "Konfirmasi Simpan",
                                         "Apakah Anda Yakin Menyimpan Data Ini?",
                                         QMessageBox.Yes | QMessageBox.No)
            if pesan == QMessageBox.Yes:
                nik = self.formAbsensi.nik.text()
                nama_kry = self.formAbsensi.namaKry.text()
                tanggal = self.formAbsensi.tglrekap.date().toString("yyyy-MM-dd")
                status = self._getStatusFromRadio()
                self.crud.simpanAbsensi(nik, nama_kry, tanggal, status)
                self.tampilData()
                QMessageBox.information(None,"Informasi","Data Absensi Berhasil di Simpan")
                self.doBersihForm()
            else:
                pass

    def doUbahAbsensi(self):
        kd_absen = self.formAbsensi.kdAbsen.text()
        nik = self.formAbsensi.nik.text()
        nama_kry = self.formAbsensi.namaKry.text()
        tanggal = self.formAbsensi.tglrekap.date().toString("yyyy-MM-dd")
        status = self._getStatusFromRadio()
        self.crud.ubahAbsensi(kd_absen, nik, nama_kry, tanggal, status)
        self.tampilData()
        QMessageBox.information(None,"Informasi","Data Absensi Berhasil di Ubah")
        self.doBersihForm()

    def doHapusAbsensi(self):
        kd_absen = self.formAbsensi.kdAbsen.text()
        self.crud.hapusAbsensi(kd_absen)
        self.tampilData()
        QMessageBox.information(None,"Informasi","Data Absensi Berhasil di Hapus")
        self.doBersihForm()

    def doCariAbsensi(self):
        keyword = self.formAbsensi.editcari.text()
        baris = self.crud.CariAbsensi(keyword)
        table = self.formAbsensi.tableAbsen
        table.setRowCount(0)

        for r in baris:
            i = table.rowCount()
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(str(r["kd_absen"])))
            table.setItem(i, 1, QTableWidgetItem(r["nik"]))
            table.setItem(i, 2, QTableWidgetItem(r["nama_karyawan"]))
            table.setItem(i, 3, QTableWidgetItem(str(r["tgl_rekap"])))
            table.setItem(i, 4, QTableWidgetItem(r["status_kehadiran"]))

    def doBersihForm(self):
        self.formAbsensi.kdAbsen.clear()
        self.formAbsensi.nik.clear()
        self.formAbsensi.namaKry.clear()
        self.formAbsensi.tglrekap.setDate(QDate.currentDate())
        self.formAbsensi.rHadir.setChecked(True)
        self.formAbsensi.kdAbsen.setReadOnly(False)
        self.formAbsensi.editcari.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Absensi()
    window.formAbsensi.show()
    sys.exit(app.exec())
