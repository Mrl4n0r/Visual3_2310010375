# This Python file uses the following encoding: utf-8
import mysql.connector

class my_cruddb:
    def __init__(self):
        # Koneksi ke database
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='visual3_2310010375'
        )

    # ------------------------
    # KARYAWAN
    # ------------------------
    def simpanKaryawan(self, nik, nama, jk, tgl, alamat, agama, notlp, pendidikan, kjabatan):
        kursor = self.conn.cursor()
        sql = """
            INSERT INTO karyawan (nik, nama_karyawan, jk, tgl_lahir, alamat_karyawan, agama, no_hp, pendidikan, kd_jabatan)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        data = (nik, nama, jk, tgl, alamat, agama, notlp, pendidikan, kjabatan)
        kursor.execute(sql, data)
        self.conn.commit()
        kursor.close()

    def ubahKaryawan(self, nik, nama, jk, tgl, alamat, agama, notlp, pendidikan, kjabatan):
        kursor = self.conn.cursor()
        sql = """
            UPDATE karyawan SET
            nama_karyawan=%s, jk=%s, tgl_lahir=%s, alamat_karyawan=%s, agama=%s, no_hp=%s, pendidikan=%s, kd_jabatan=%s
            WHERE nik=%s
        """
        data = (nama, jk, tgl, alamat, agama, notlp, pendidikan, kjabatan, nik)
        kursor.execute(sql, data)
        self.conn.commit()
        kursor.close()

    def hapusKaryawan(self, nik):
        kursor = self.conn.cursor()
        kursor.execute("DELETE FROM karyawan WHERE nik=%s", (nik,))
        self.conn.commit()
        kursor.close()

    def cariKaryawan(self, nik):
        kursor = self.conn.cursor(dictionary=True)
        kursor.execute("SELECT * FROM karyawan WHERE nik=%s", (nik,))
        result = kursor.fetchone()
        kursor.close()
        return result

    def getAllKaryawan(self):
        kursor = self.conn.cursor(dictionary=True)
        kursor.execute("SELECT * FROM karyawan ORDER BY nik ASC")
        records = kursor.fetchall()
        kursor.close()
        return records

    def CariKaryawan(self, param):
        sql = """SELECT * FROM karyawan WHERE nik LIKE %s OR nama_karyawan LIKE %s OR jk LIKE %s OR alamat_karyawan LIKE %s OR agama LIKE %s OR no_hp LIKE %s
                 OR pendidikan LIKE %s
                 OR kd_jabatan LIKE %s"""
        kursor = self.conn.cursor(dictionary=True)
        val = (
            f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%",
            f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%"
        )
        kursor.execute(sql, val)
        record = kursor.fetchall()
        kursor.close()
        return record

    # ------------------------
    # JABATAN
    # ------------------------
    def simpanJabatan(self, kd_jabatan, nama_jabatan, tunjangan, gaji_pokok, deskripsi):
        kursor = self.conn.cursor()
        sql = """
            INSERT INTO jabatan (kd_jabatan, nama_jabatan, tunjangan, gaji_pokok, deskripsi)
            VALUES (%s,%s,%s,%s,%s)
        """
        data = (kd_jabatan, nama_jabatan, tunjangan, gaji_pokok, deskripsi)
        kursor.execute(sql, data)
        self.conn.commit()
        kursor.close()

    def ubahJabatan(self, kd_jabatan, nama_jabatan, tunjangan, gaji_pokok, deskripsi):
        kursor = self.conn.cursor()
        sql = """
            UPDATE jabatan SET
            nama_jabatan=%s, tunjangan=%s, gaji_pokok=%s, deskripsi=%s
            WHERE kd_jabatan=%s
        """
        data = (nama_jabatan, tunjangan, gaji_pokok, deskripsi, kd_jabatan)
        kursor.execute(sql, data)
        self.conn.commit()
        kursor.close()

    def hapusJabatan(self, kd_jabatan):
        kursor = self.conn.cursor()
        kursor.execute("DELETE FROM jabatan WHERE kd_jabatan=%s", (kd_jabatan,))
        self.conn.commit()
        kursor.close()

    def cariJabatan(self, kd_jabatan):
        kursor = self.conn.cursor(dictionary=True)
        kursor.execute("SELECT * FROM jabatan WHERE kd_jabatan=%s", (kd_jabatan,))
        result = kursor.fetchone()
        kursor.close()
        return result

    def dataJabatan(self):
        kursor = self.conn.cursor(dictionary=True)
        kursor.execute("SELECT * FROM jabatan ORDER BY kd_jabatan ASC")
        records = kursor.fetchall()
        kursor.close()
        return records

    def CariJabatan(self, param):
        sql = """SELECT * FROM jabatan WHERE kd_jabatan LIKE %s OR nama_jabatan LIKE %s OR tunjangan LIKE %s OR gaji_pokok LIKE %s OR deskripsi LIKE %s"""
        kursor = self.conn.cursor(dictionary=True)
        val = (f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%")
        kursor.execute(sql, val)
        hasil = kursor.fetchall()
        kursor.close()
        return hasil

    # ------------------------
    # MITRA (Diperbarui 5 Kolom & Sesuai Referensi)
    # ------------------------
    def simpanMitra(self, kd_mitra, nama_mitra, alamat_mitra, telepon_mitra, email_mitra):
        kursor = self.conn.cursor()
        sql = """INSERT INTO mitra (kd_mitra, nama_mitra, alamat_mitra, telepon_mitra, email_mitra)
                 VALUES (%s, %s, %s, %s, %s)"""
        val = (kd_mitra, nama_mitra, alamat_mitra, telepon_mitra, email_mitra)
        kursor.execute(sql, val)
        self.conn.commit()
        kursor.close()

    def ubahMitra(self, kd_mitra, nama_mitra, alamat_mitra, telepon_mitra, email_mitra):
        kursor = self.conn.cursor()
        sql = """UPDATE mitra SET    nama_mitra = %s,    alamat_mitra = %s,    telepon_mitra = %s,   email_mitra = %s
                 WHERE kd_mitra = %s"""
        val = (nama_mitra, alamat_mitra, telepon_mitra, email_mitra, kd_mitra)
        kursor.execute(sql, val)
        self.conn.commit()
        kursor.close()

    def hapusMitra(self, kd_mitra):
        kursor = self.conn.cursor()
        kursor.execute("DELETE FROM mitra WHERE kd_mitra=%s", (kd_mitra,))
        self.conn.commit()
        kursor.close()

    def cariMitra(self, kd_mitra):
        kursor = self.conn.cursor(dictionary=True)
        kursor.execute("SELECT * FROM mitra WHERE kd_mitra=%s", (kd_mitra,))
        result = kursor.fetchone()
        kursor.close()
        return result

    def dataMitra(self):
        kursor = self.conn.cursor(dictionary=True)
        kursor.execute("SELECT * FROM mitra ORDER BY kd_mitra ASC")
        records = kursor.fetchall()
        kursor.close()
        return records

    def CariMitra(self, param):
        kursor = self.conn.cursor(dictionary=True)
        sql = """SELECT * FROM mitra WHERE kd_mitra LIKE %s OR nama_mitra LIKE %s OR alamat_mitra LIKE %s OR telepon_mitra LIKE %s OR email_mitra LIKE %s"""
        val = (f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%")
        kursor.execute(sql, val)
        hasil = kursor.fetchall()
        kursor.close()
        return hasil

    # ------------------------
    # ABSENSI
    # ------------------------

    def simpanAbsensi(self, nik, nama, tanggal, status):
        kursor = self.conn.cursor()
        sql = """
            INSERT INTO absensi (nik, nama_karyawan, tgl_rekap, status_kehadiran)
            VALUES (%s,%s,%s,%s)
        """
        data = (nik, nama, tanggal, status)
        kursor.execute(sql, data)
        self.conn.commit()
        kursor.close()

    def ubahAbsensi(self, kd_absen, nik, nama, tanggal, status):
        kursor = self.conn.cursor()
        sql = """
            UPDATE absensi SET
            nik=%s, nama_karyawan=%s, tgl_rekap=%s, status_kehadiran=%s
            WHERE kd_absen=%s
        """
        data = (nik, nama, tanggal, status, kd_absen)
        kursor.execute(sql, data)
        self.conn.commit()
        kursor.close()

    def hapusAbsensi(self, kd_absen):
        kursor = self.conn.cursor()
        kursor.execute("DELETE FROM absensi WHERE kd_absen=%s", (kd_absen,))
        self.conn.commit()
        kursor.close()

    def cariAbsensi(self, kd_absen):
        kursor = self.conn.cursor(dictionary=True)
        kursor.execute("SELECT * FROM absensi WHERE kd_absen=%s", (kd_absen,))
        result = kursor.fetchone()
        kursor.close()
        return result

    def CariAbsensi(self, keyword):
        kursor = self.conn.cursor(dictionary=True)
        sql = """SELECT * FROM absensi WHERE kd_absen LIKE %s OR nik LIKE %s OR nama_karyawan LIKE %s"""
        val = (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%")
        kursor.execute(sql, val)
        hasil = kursor.fetchall()
        kursor.close()
        return hasil

    def dataAbsensi(self):
        kursor = self.conn.cursor(dictionary=True)
        kursor.execute("SELECT * FROM absensi ORDER BY kd_absen ASC")
        records = kursor.fetchall()
        kursor.close()
        return records

    # ------------------------
    # GAJI
    # ------------------------

    def simpanGaji(self, nik, tunjangan, total_lembur, total_gaji):
        kursor = self.conn.cursor()
        sql = """
            INSERT INTO gaji (nik, tunjangan, total_lembur, total_gaji)
            VALUES (%s, %s, %s, %s)
        """
        data = (nik, tunjangan, total_lembur, total_gaji)
        kursor.execute(sql, data)
        self.conn.commit()
        kursor.close()

    def ubahGaji(self, kd_gaji, nik, tunjangan, total_lembur, total_gaji):
        kursor = self.conn.cursor()
        sql = """
            UPDATE gaji SET
            nik=%s, tunjangan=%s, total_lembur=%s, total_gaji=%s
            WHERE kd_gaji=%s
        """
        data = (nik, tunjangan, total_lembur, total_gaji, kd_gaji)
        kursor.execute(sql, data)
        self.conn.commit()
        kursor.close()

    def hapusGaji(self, kd_gaji):
        kursor = self.conn.cursor()
        kursor.execute("DELETE FROM gaji WHERE kd_gaji=%s", (kd_gaji,))
        self.conn.commit()
        kursor.close()

    def cariGaji(self, kd_gaji):
        kursor = self.conn.cursor(dictionary=True)
        kursor.execute("SELECT * FROM gaji WHERE kd_gaji=%s", (kd_gaji,))
        result = kursor.fetchone()
        kursor.close()
        return result

    def dataGaji(self):
        kursor = self.conn.cursor(dictionary=True)
        kursor.execute("SELECT * FROM gaji ORDER BY kd_gaji ASC")
        records = kursor.fetchall()
        kursor.close()
        return records

    def CariGaji(self, param):
        sql = """SELECT * FROM gaji WHERE kd_gaji LIKE %s OR nik LIKE %s OR tunjangan LIKE %s OR total_lembur LIKE %s OR total_gaji LIKE %s"""
        kursor = self.conn.cursor(dictionary=True)
        val = (f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%", f"%{param}%")
        kursor.execute(sql, val)
        hasil = kursor.fetchall()
        kursor.close()
        return hasil
