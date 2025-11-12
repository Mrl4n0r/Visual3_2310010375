# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QAbstractItemView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QDate
from crudDB import my_cruddb

class Karyawan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file = QFile("karyawan_form.ui")
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.formKaryawan = loader.load(ui_file, None)
        ui_file.close()
        self.formKaryawan.setWindowTitle("Form Data Karyawan")
        self.crud = my_cruddb()
        self.formKaryawan.btnSimpan.clicked.connect(self.simpan)
        self.formKaryawan.btnUbah.clicked.connect(self.ubah)
        self.formKaryawan.btnHapus.clicked.connect(self.hapus)
        self.formKaryawan.btnBersih.clicked.connect(self.bersih)
        self.formKaryawan.tableKaryawan.cellClicked.connect(self.pilihBaris)
        self.formKaryawan.comboJk.addItems(["Laki-laki", "Perempuan"])
        self.formKaryawan.cAgama.addItems(["Islam", "Kristen", "Katolik", "Hindu", "Buddha", "Khonghucu"])
        self.formKaryawan.dateEdit.setDate(QDate.currentDate())
        self.formKaryawan.editcari.textChanged.connect(self.doCariKaryawan)
        self.loadData()

    def loadData(self):
        baris = self.crud.getAllKaryawan()
        table = self.formKaryawan.tableKaryawan
        table.setRowCount(0)
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        header = ["NIK", "Nama", "JK", "Tgl Lahir", "Alamat", "Agama", "No HP", "Pendidikan", "Kd. Jabatan"]
        table.setColumnCount(len(header))
        table.setHorizontalHeaderLabels(header)

        for r in baris:
            i = table.rowCount()
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(r["nik"]))
            table.setItem(i, 1, QTableWidgetItem(r["nama_karyawan"]))
            table.setItem(i, 2, QTableWidgetItem(r["jk"]))
            table.setItem(i, 3, QTableWidgetItem(str(r["tgl_lahir"])))
            table.setItem(i, 4, QTableWidgetItem(r["alamat_karyawan"]))
            table.setItem(i, 5, QTableWidgetItem(r["agama"]))
            table.setItem(i, 6, QTableWidgetItem(r["no_hp"]))
            table.setItem(i, 7, QTableWidgetItem(r["pendidikan"]))
            table.setItem(i, 8, QTableWidgetItem(r["kd_jabatan"]))
        table.resizeColumnsToContents()

    def doCariKaryawan(self):
        cari = self.formKaryawan.editcari.text().strip()
        baris = self.crud.CariKaryawan(cari)
        table = self.formKaryawan.tableKaryawan
        table.setRowCount(0)

        for r in baris:
            i = table.rowCount()
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(r["nik"]))
            table.setItem(i, 1, QTableWidgetItem(r["nama_karyawan"]))
            table.setItem(i, 2, QTableWidgetItem(r["jk"]))
            table.setItem(i, 3, QTableWidgetItem(str(r["tgl_lahir"])))
            table.setItem(i, 4, QTableWidgetItem(r["alamat_karyawan"]))
            table.setItem(i, 5, QTableWidgetItem(r["agama"]))
            table.setItem(i, 6, QTableWidgetItem(r["no_hp"]))
            table.setItem(i, 7, QTableWidgetItem(r["pendidikan"]))
            table.setItem(i, 8, QTableWidgetItem(r["kd_jabatan"]))

    def simpan(self):
        if not self.formKaryawan.lineNik.text().strip():
            QMessageBox.information(None,"Informasi","NIK Karyawan belum di isi")
            self.formKaryawan.lineNik.setFocus()
        elif not self.formKaryawan.lineNama.text().strip():
            QMessageBox.information(None,"Informasi","Nama Karyawan belum di isi")
            self.formKaryawan.lineNama.setFocus()
        elif not self.formKaryawan.lineAlamat.text().strip():
            QMessageBox.information(None,"Informasi","Alamat belum di isi")
            self.formKaryawan.lineAlamat.setFocus()
        elif not self.formKaryawan.lineNotlp.text().strip():
            QMessageBox.information(None,"Informasi","No. Telpon belum di isi")
            self.formKaryawan.lineNotlp.setFocus()
        elif not self.formKaryawan.linePendidikan.text().strip():
            QMessageBox.information(None,"Informasi","Pendidikan belum di isi")
            self.formKaryawan.linePendidikan.setFocus()
        elif not self.formKaryawan.lineKjabatan.text().strip():
            QMessageBox.information(None,"Informasi","Kode Jabatan belum di isi")
            self.formKaryawan.lineKjabatan.setFocus()
        else:
            pesan = QMessageBox.question(None, "Konfirmasi Simpan",
                                         "Apakah Anda Yakin Menyimpan Data Ini?",
                                         QMessageBox.Yes | QMessageBox.No)

            if pesan == QMessageBox.Yes:
                nik = self.formKaryawan.lineNik.text()
                nama = self.formKaryawan.lineNama.text()
                jk = self.formKaryawan.comboJk.currentText()
                tgl = self.formKaryawan.dateEdit.date().toString("yyyy-MM-dd")
                alamat = self.formKaryawan.lineAlamat.text()
                agama = self.formKaryawan.cAgama.currentText()
                notlp = self.formKaryawan.lineNotlp.text()
                pendidikan = self.formKaryawan.linePendidikan.text()
                kjabatan = self.formKaryawan.lineKjabatan.text()
                self.crud.simpanKaryawan(nik, nama, jk, tgl, alamat, agama, notlp, pendidikan, kjabatan)
                self.loadData()
                QMessageBox.information(None,"Informasi","Data Berhasil di Simpan")
                self.bersih()
            else:
                pass

    def ubah(self):
        nik = self.formKaryawan.lineNik.text()
        nama = self.formKaryawan.lineNama.text()
        jk = self.formKaryawan.comboJk.currentText()
        tgl = self.formKaryawan.dateEdit.date().toString("yyyy-MM-dd")
        alamat = self.formKaryawan.lineAlamat.text()
        agama = self.formKaryawan.cAgama.currentText()
        notlp = self.formKaryawan.lineNotlp.text()
        pendidikan = self.formKaryawan.linePendidikan.text()
        kjabatan = self.formKaryawan.lineKjabatan.text()
        self.crud.ubahKaryawan(nik, nama, jk, tgl, alamat, agama, notlp, pendidikan, kjabatan)
        self.loadData()
        QMessageBox.information(None,"Informasi","Data Berhasil di Ubah")
        self.bersih()

    def hapus(self):
        nik = self.formKaryawan.lineNik.text()
        self.crud.hapusKaryawan(nik)
        self.loadData()
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")
        self.bersih()

    def pilihBaris(self, row, col):
        t = self.formKaryawan.tableKaryawan
        self.formKaryawan.lineNik.setText(t.item(row, 0).text())
        self.formKaryawan.lineNama.setText(t.item(row, 1).text())
        self.formKaryawan.comboJk.setCurrentText(t.item(row, 2).text())
        qdate = QDate.fromString(t.item(row, 3).text(), "yyyy-MM-dd")
        self.formKaryawan.dateEdit.setDate(qdate)
        self.formKaryawan.lineAlamat.setText(t.item(row, 4).text())
        self.formKaryawan.cAgama.setCurrentText(t.item(row, 5).text())
        self.formKaryawan.lineNotlp.setText(t.item(row, 6).text())
        self.formKaryawan.linePendidikan.setText(t.item(row, 7).text())
        self.formKaryawan.lineKjabatan.setText(t.item(row, 8).text())
        self.formKaryawan.lineNik.setReadOnly(True)

    def bersih(self, kecuali_nik=False):
        if not kecuali_nik:
            self.formKaryawan.lineNik.clear()
        self.formKaryawan.lineNik.setReadOnly(False)
        self.formKaryawan.lineNama.clear()
        self.formKaryawan.comboJk.setCurrentIndex(0)
        self.formKaryawan.dateEdit.setDate(QDate.currentDate())
        self.formKaryawan.lineAlamat.clear()
        self.formKaryawan.cAgama.setCurrentIndex(0)
        self.formKaryawan.lineNotlp.clear()
        self.formKaryawan.linePendidikan.clear()
        self.formKaryawan.lineKjabatan.clear()
        self.formKaryawan.editcari.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Karyawan()
    w.formKaryawan.show()
    sys.exit(app.exec())
