# 🧩 Visual3_2310010375
### Muhammad Maulana (2310010375)

## 🗂️ Sistem Informasi Karyawan (CRUD App) — PySide6 + MySQL

Aplikasi desktop berbasis GUI untuk **manajemen data perusahaan**, mencakup modul:
- Karyawan  
- Jabatan  
- Gaji  
- Absensi  
- Mitra

Dibangun **sepenuhnya dengan Python** menggunakan **PySide6** untuk antarmuka dan **MySQL** sebagai database.

---

## 🚀 Fitur Utama

### 👨‍💼 1. Manajemen Karyawan
- CRUD (Create, Read, Update, Delete) lengkap.  
- Validasi input menggunakan `QMessageBox` agar data tidak kosong.  
- Menampilkan data dalam `QTableWidget`.  
- Klik baris tabel → otomatis isi form.  
- Pencarian real-time berdasarkan NIK, Nama, Alamat, dll.

---

### 🏢 2. Manajemen Jabatan
- CRUD penuh untuk data jabatan (Kode Jabatan, Nama, Tunjangan, Gaji Pokok, Deskripsi).  
- Validasi dan konfirmasi sebelum simpan.  
- Tabel interaktif dengan fitur klik-isi-form.  
- Pencarian real-time.

---

### 💰 3. Manajemen Gaji
- CRUD data gaji karyawan.  
- Penanganan `AUTO_INCREMENT` pada `kd_gaji`.  
- Tampilan tabel dan pencarian live search.

---

### 🕒 4. Manajemen Absensi
- Input absensi harian (Hadir, Izin, Sakit) menggunakan `QRadioButton`.  
- Penanganan `AUTO_INCREMENT` pada `kd_absen`.  
- Tampilan tabel dan pencarian langsung.

---

### 🤝 5. Manajemen Mitra 
- CRUD data mitra   
- Menangani 5 kolom data kustom.  
- Tabel dan pencarian live search.

---

## 🧠 Teknologi yang Digunakan
| Komponen | Keterangan |
|-----------|-------------|
| **Python 3.x** | Bahasa pemrograman utama |
| **PySide6 (Qt for Python)** | Framework GUI |
| **Qt Designer** | Desain antarmuka `.ui` |
| **QUiLoader** | Memuat file `.ui` secara dinamis |
| **MySQL / XAMPP** | Database relasional |
| **mysql-connector-python** | Driver untuk MySQL |

---

## ⚙️ Cara Menjalankan Proyek

### 1️⃣ Prasyarat
Pastikan Anda sudah memiliki:
- Python 3.x  
- MySQL Server / XAMPP  
- (Opsional) Git  

---

### 2️⃣ Instalasi

#### 🧭 Klone Repositori
```bash
git clone https://github.com/Mrl4n0r/Visual3_2310010375
cd Visual3_2310010375
