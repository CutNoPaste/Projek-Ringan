# Dokumentasi Program Manajemen Kontak

## Deskripsi
Program ini memungkinkan pengguna untuk menambah, melihat, dan menghapus kontak yang disimpan dalam file `kontak.json`. Setiap kontak memiliki tiga atribut: **Nama**, **Nomor**, dan **Email**.

## Fungsi Utama
Program ini memiliki beberapa fitur utama:
1. **Menambah kontak baru**.
2. **Melihat daftar kontak**.
3. **Menghapus kontak berdasarkan nama**.
4. **Keluar dari program**.

Data kontak disimpan dalam file JSON yang dikelola oleh program. Jika file JSON tidak ada, program akan membuat file baru. Semua perubahan yang dilakukan pada kontak akan langsung disimpan ke dalam file tersebut.

---

## Fungsi-fungsi yang Tersedia

### 1. `tambah_kontak(nama, nomor, email)`
Fungsi ini digunakan untuk menambahkan kontak baru ke dalam file `kontak.json`. Jika file `kontak.json` belum ada, program akan membuat file baru.

#### Input:
- `nama`: Nama kontak yang akan ditambahkan (tipe data: `str`).
- `nomor`: Nomor telepon kontak yang akan ditambahkan (tipe data: `str`).
- `email`: Alamat email kontak yang akan ditambahkan (tipe data: `str`).

#### Proses:
- Membaca data dari file `kontak.json` jika ada, dan menambahkan kontak baru ke dalam list data.
- Jika file `kontak.json` tidak ada, maka akan membuat list kosong.
- Setelah kontak baru ditambahkan, data disimpan kembali ke file `kontak.json`.

#### Output:
- Menampilkan pesan konfirmasi bahwa kontak berhasil ditambahkan.

#### Contoh Penggunaan:
```python
tambah_kontak("Abil 1", "08123123123", "abil@example.com")
```

### 2. `hapus_kontak(nama)`
Fungsi ini digunakan untuk menghapus kontak berdasarkan nama dari file kontak.json.

Input:
```nama: Nama kontak yang ingin dihapus (tipe data: str).```
#### Proses:
Membaca file kontak.json dan mencari kontak dengan nama yang sesuai.
Jika kontak ditemukan, maka kontak tersebut akan dihapus dari list.
Menyimpan kembali perubahan ke dalam file kontak.json.
#### Output:
Menampilkan pesan konfirmasi jika kontak berhasil dihapus.
Menampilkan pesan kesalahan jika kontak dengan nama yang diberikan tidak ditemukan.
Contoh Penggunaan:
hapus_kontak("Abil 1")

Struktur Data JSON
Data kontak disimpan dalam file JSON dengan format berikut:
```
[
    {
        "Nama": "Abil 1",
        "Nomor": "08123123123",
        "Email": "abil1@example.com"
    },
    {
        "Nama": "Abil 2,
        "Nomor": "08321321321",
        "Email": "abil2@example.com"
    }
]
```
Setiap objek dalam list berisi informasi tentang satu kontak, dengan Nama, Nomor, dan Email sebagai atribut.
Penanganan Error
Program ini dilengkapi dengan penanganan error untuk memastikan bahwa program tidak crash jika terjadi masalah dengan file JSON:

File Tidak Ditemukan: Jika file kontak.json tidak ada, program akan membuat file baru dan melanjutkan eksekusi.
Kesalahan Pembacaan atau Penulisan JSON: Jika terjadi kesalahan saat membaca atau menulis file JSON (misalnya jika file rusak), program akan menampilkan pesan kesalahan yang sesuai.
Contoh Penggunaan
Berikut adalah contoh penggunaan program ini secara keseluruhan:
```
--------- MANAJEMEN KONTAK ---------
Masukkan pilihan : 
1. lihat kontak
2. Tambah kontak 
3. Hapus Kontak
4. Keluar
Masukkan pilihan : 2
Masukkan nama : Abil
Masukkan nomor : 08123123123
Masukkan email : abil@example.com
Kontak Abil 2 berhasil ditambahkan!

--------- MANAJEMEN KONTAK ---------
Masukkan pilihan : 
1. lihat kontak
2. Tambah kontak 
3. Hapus Kontak
4. Keluar
Masukkan pilihan : 1
--------------------------
Kontak No. 1
Nama : Abil 1
Nomor : 08321321321
Email : abil@example.com

--------------------------
Kontak No. 2
Nama : Abil 2
Nomor : 08123123123
Email : abil2@example.com
```
Kesimpulan
Program ini adalah aplikasi manajemen kontak sederhana yang menyimpan data dalam format JSON. Program ini memungkinkan pengguna untuk menambah, melihat, dan menghapus kontak. Dilengkapi dengan validasi input dan penanganan error untuk meningkatkan pengalaman pengguna.


---
