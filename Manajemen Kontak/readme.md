**Dokumentasi Program Manajemen Kontak**

Deskripsi :
Program ini memungkinkan pengguna untuk menambah, melihat, dan menghapus kontak yang disimpan dalam file kontak.json. Setiap kontak memiliki tiga atribut: Nama, Nomor, dan Email.

Fungsi Utama :
Program ini memiliki beberapa fitur utama:

Menambah kontak baru.
Melihat daftar kontak.
Menghapus kontak berdasarkan nama.
Keluar dari program.
Data kontak disimpan dalam file JSON yang dikelola oleh program. Jika file JSON tidak ada, program akan membuat file baru. Semua perubahan yang dilakukan pada kontak akan langsung disimpan ke dalam file tersebut.

Fungsi-fungsi yang Tersedia
1. tambah_kontak(nama, nomor, email)
Fungsi ini digunakan untuk menambahkan kontak baru ke dalam file kontak.json. Jika file kontak.json belum ada, program akan membuat file baru.

Input:

nama: Nama kontak yang akan ditambahkan (tipe data: str).
nomor: Nomor telepon kontak yang akan ditambahkan (tipe data: str).
email: Alamat email kontak yang akan ditambahkan (tipe data: str).
Proses:

Membaca data dari file kontak.json jika ada, dan menambahkan kontak baru ke dalam list data.
Jika file kontak.json tidak ada, maka akan membuat list kosong.
Setelah kontak baru ditambahkan, data disimpan kembali ke file kontak.json.
Output:

Menampilkan pesan konfirmasi bahwa kontak berhasil ditambahkan.
Contoh Penggunaan:

python
Salin kode
tambah_kontak("John Doe", "081234567890", "johndoe@example.com")
