# Aplikasi To-Do List 📝

Aplikasi To-Do List ini memungkinkan kamu untuk mengelola daftar tugas yang perlu diselesaikan. Kamu dapat menambah, melihat, menandai tugas sebagai selesai, menghapus tugas, serta mengekspor daftar tugas ke dalam file teks.

## Fitur

- **Lihat Daftar Tugas**: Menampilkan semua tugas yang sudah ditambahkan beserta detailnya.
- **Tambah Tugas**: Menambah tugas baru dengan nama kegiatan dan tanggal deadline.
- **Tandai Tugas Selesai**: Tandai tugas yang sudah selesai.
- **Hapus Tugas**: Menghapus tugas yang sudah tidak diperlukan.
- **Export ke File Teks**: Menyimpan daftar tugas yang ada ke dalam file `tugas.txt`.
- **Antarmuka Warna**: Setiap tugas ditampilkan dengan warna berbeda untuk menambah kenyamanan pengguna.

## Prasyarat

Pastikan kamu sudah menginstall Python dan pustaka `colorama`:

1. **Python 3.x**
2. **colorama**: Pustaka untuk memberi warna pada terminal.

Untuk menginstall pustaka `colorama`, jalankan perintah berikut:

```bash
pip install colorama
```
## Cara Menjalankan

1. Jalankan aplikasi dengan menggunakan Python:
   ```bash
   python todolist.py
   ```
2. Pilih opsi yang tersedia:
```
  1: Lihat daftar tugas
  2: Tambah tugas
  3: Tandai tugas selesai
  4: Hapus tugas
  5: Export ke tugas.txt
  6: Keluar
```
3. Aplikasi akan menampilkan animasi warna-warni pada judul aplikasi dan memberikan pilihan menu dengan emotikon dan warna yang menarik.

## Contoh Tampilan

### Menu Utama : 

```
------------- APLIKASI TO DO LIST -------------
Pilih apa yang mau kamu lakukan :
1. Lihat daftar tugas 📋
2. Tambah tugas ➕
3. Tandai tugas selesai ✔️
4. Hapus tugas ❌
5. Export ke 'file.txt' 💾
6. Keluar 🚪
```

## Menambahkan Tugas :

```
Masukkan nama kegiatan : Mengerjakan project
Masukkan tanggal deadline : 23-10-2024
Tugas Mengerjakan project Tanggal 23-10-2024 sudah ditambahkan !
```

## Daftar Tugas :

```
Tugas No. 1
Kegiatan : Mengerjakan project
Deadline : 23-10-2024
Apakah sudah : ❌
Pekerjaan kamu tersisa '3' hari
```
