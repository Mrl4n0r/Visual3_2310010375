# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

from karyawan import Karyawan
from jabatan import Jabatan
from mitra import Mitra
from absensi import Absensi
from gaji import Gaji


class HalamanUtama(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        ui_file_name = "form.ui"
        file_form_utama = QFile(ui_file_name)

        if not file_form_utama.open(QFile.ReadOnly):
            print(f"Error: Tidak bisa membuka file {ui_file_name}")
            sys.exit(-1)

        loader = QUiLoader()
        self.formutama = loader.load(file_form_utama, self)
        file_form_utama.close()

        self.setCentralWidget(self.formutama)
        self.setMenuBar(self.formutama.menuBar())
        self.resize(self.formutama.size())
        self.setWindowTitle("Sistem Informasi Karyawan")
        self.formutama.actionKaryawan.triggered.connect(self.buka_form_karyawan)
        self.formutama.actionJabatan.triggered.connect(self.buka_form_jabatan)
        self.formutama.actionMitra.triggered.connect(self.buka_form_mitra)
        self.formutama.actionAbsensi.triggered.connect(self.buka_form_absensi)
        self.formutama.actionGaji.triggered.connect(self.buka_form_gaji)

    def buka_form_karyawan(self):
        self.form_karyawan_window = Karyawan()
        self.form_karyawan_window.formKaryawan.show()

    def buka_form_jabatan(self):
        self.form_jabatan_window = Jabatan()
        self.form_jabatan_window.formJabatan.show()

    def buka_form_mitra(self):
        self.form_admin_window = Mitra()
        self.form_admin_window.formMitra.show()

    def buka_form_absensi(self):
        self.form_absensi_window = Absensi()
        self.form_absensi_window.formAbsensi.show()

    def buka_form_gaji(self):
        self.form_gaji_window = Gaji()
        self.form_gaji_window.formGaji.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = HalamanUtama()
    widget.show()
    sys.exit(app.exec())
