# Visual3_2310010375
# Muhammad Maulana (2310010375)

Sistem Informasi Karyawan (CRUD App) dengan PySide6

Ini adalah aplikasi desktop (GUI) untuk manajemen data perusahaan, yang mencakup pengelolaan karyawan, jabatan, gaji, absensi, dan mitra. Aplikasi ini dibangun murni dengan Python, menggunakan library PySide6 untuk antarmuka pengguna dan MySQL sebagai database.

Fitur Utama

Aplikasi ini terdiri dari satu menu utama yang mengelola 5 modul (form) terpisah:

Manajemen Karyawan:

Operasi CRUD (Create, Read, Update, Delete) penuh untuk data karyawan.

Form input dengan validasi (QMessageBox) untuk mencegah data kosong.

Menampilkan semua karyawan dalam QTableWidget (tabel data).

Interaksi tabel: Mengklik baris di tabel akan otomatis mengisi form di atasnya.

Pencarian real-time (editcari) yang memfilter tabel secara langsung berdasarkan NIK, Nama, Alamat, dll.

Manajemen Jabatan:

CRUD penuh untuk data jabatan (Kode Jabatan, Nama, Tunjangan, Gaji Pokok, Deskripsi).

Validasi data dan konfirmasi simpan.

Tampilan tabel (QTableWidget) dengan fitur klik-untuk-mengisi-form.

Pencarian real-time (editcari) untuk memfilter jabatan.

Manajemen Gaji:

CRUD untuk data gaji karyawan.

Penanganan Primary Key AUTO_INCREMENT (kd_gaji) saat menyimpan data baru.

Tampilan tabel (QTableWidget) dan pencarian live search.

Manajemen Absensi:

Menyimpan data absensi harian (Hadir, Izin, Sakit) menggunakan QRadioButton.

Penanganan Primary Key AUTO_INCREMENT (kd_absen).

Tampilan tabel (QTableWidget) dan pencarian live search.

Manajemen Mitra (Admin):

CRUD untuk data mitra (sebelumnya Admin).

Menangani 5 kolom data kustom (Kode Mitra, Nama, Alamat, dll.).

Tampilan tabel (QTableWidget) dan pencarian live search.

Teknologi yang Digunakan

Python 3

PySide6 (Qt for Python): Digunakan untuk semua komponen GUI.

QUiLoader: Memuat file .ui secara dinamis (tanpa perlu kompilasi .ui ke .py).

Qt Designer: Digunakan untuk mendesain semua file antarmuka (.ui).

MySQL: Database relasional untuk menyimpan semua data.

mysql-connector-python: Driver Python untuk berkomunikasi dengan MySQL.

Cara Menjalankan Proyek

Untuk menjalankan proyek ini di komputer Anda, ikuti langkah-langkah berikut:

1. Prasyarat

Pastikan Anda memiliki:

Python 3.x terinstal.

Server MySQL (seperti XAMPP atau MariaDB) berjalan.

Git (opsional, untuk kloning).

2. Instalasi

1. Klone Repositori

git clone https://github.com/Mrl4n0r/Visual3_2310010375
cd Visual3_2310010375


2. Siapkan Database

Buka phpMyAdmin (atau client MySQL Anda).

Buat database baru dengan nama persis visual3_2310010375.

Pilih database tersebut, lalu klik tab "Impor".

Impor file visual3_2310010375 (2).sql yang ada di repositori ini.

3. Buat Virtual Environment (Sangat Direkomendasikan)

# Windows
python -m venv venv
venv\Scripts\activate


4. Instal Dependensi Python

pip install PySide6 mysql-connector-python


5. Jalankan Aplikasi
File utama untuk menjalankan seluruh aplikasi adalah main.py.

python main.py


Struktur Proyek

/
├── crudDB.py               # File UTAMA: Kelas my_cruddb, berisi SEMUA fungsi SQL (Simpan, Ubah, Hapus, Cari, etc.)
├── main.py                 # File UTAMA: Menjalankan aplikasi dan menu utama (QMainWindow)
│
├── karyawan.py             # File Logika (Python) untuk Form Karyawan
├── karyawan_form.ui        # File Desain (XML) untuk Form Karyawan
│
├── jabatan.py              # File Logika (Python) untuk Form Jabatan
├── jabatan_form.ui         # File Desain (XML) untuk Form Jabatan
│
├── gaji.py                 # File Logika (Python) untuk Form Gaji
├── gaji_form.ui            # File Desain (XML) untuk Form Gaji
│
├── absensi.py              # File Logika (Python) untuk Form Absensi
├── absensi_form.ui         # File Desain (XML) untuk Form Absensi
│
├── mitra.py                # File Logika (Python) untuk Form Mitra (Admin)
├── mitra_form.ui           # File Desain (XML) untuk Form Mitra (Admin)
│
├── form.ui                 # File Desain (XML) untuk Menu Utama (main.py)
│
└── visual3_2310010375 (2).sql # File backup database MySQL
