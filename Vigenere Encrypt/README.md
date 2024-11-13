# Vigenère Cipher - Enkripsi dan Deskripsi

Program ini mengimplementasikan algoritma **Vigenère Cipher** untuk melakukan enkripsi dan dekripsi teks. Program ini memungkinkan pengguna untuk mengenkripsi atau mendekripsi pesan menggunakan kata kunci yang disediakan.

## Fitur

- **Enkripsi**: Menggunakan Vigenère Cipher untuk mengubah pesan yang dimasukkan dengan menggunakan kata kunci.
- **Deskripsi**: Mengembalikan pesan terenkripsi ke bentuk aslinya menggunakan kata kunci yang sama.
- **Input interaktif**: Pengguna dapat memilih untuk mengenkripsi atau mendekripsi pesan melalui input yang diberikan.
- **Penanganan spasi dan karakter non-alfabet**: Program ini mempertahankan spasi dan karakter non-alfabet dalam pesan tanpa mengubahnya.

## Struktur Program

### 1. Fungsi `vigenere(pesan, kunci, arahan=1)`
Fungsi ini melakukan enkripsi atau dekripsi pada pesan yang diberikan dengan menggunakan algoritma **Vigenère Cipher**.

- **Parameter**:
  - `pesan`: Pesan yang akan dienkripsi atau didekripsi.
  - `kunci`: Kata kunci yang digunakan untuk enkripsi atau dekripsi.
  - `arahan`: Nilai yang menentukan arah proses (1 untuk enkripsi, -1 untuk dekripsi).
  
- **Pengembalian**: Mengembalikan pesan yang telah dienkripsi atau didekripsi.

### 2. Fungsi `proses()`
Fungsi ini menangani proses interaktif untuk menerima input pengguna dan menampilkan hasil enkripsi atau dekripsi.

- Fungsi ini meminta pengguna untuk memilih antara enkripsi (`ENC`) atau dekripsi (`DEC`).
- Kemudian, pengguna diminta untuk memasukkan pesan dan kata kunci.
- Setelah itu, hasil enkripsi atau dekripsi ditampilkan.

### 3. Pengulangan Proses
Program ini juga mendukung pengulangan. Setelah satu operasi selesai, pengguna dapat memilih untuk melanjutkan dengan memasukkan pesan baru atau keluar dari program.

## Cara Instalasi dan Penggunaan

1. **Instalasi**: 
   Tidak ada dependensi eksternal yang diperlukan untuk menjalankan program ini. Kamu hanya perlu memiliki Python terinstal di komputer kamu.

2. **Menjalankan Program**:
   Salin kode ini ke dalam file Python (misalnya `vigenere_cipher.py`), lalu jalankan file tersebut.

   ```bash
   python vigenere_cipher.py
3. **Input**:
   - Ketika diminta, pilih ENC untuk enkripsi atau DEC untuk dekripsi.
   - Masukkan pesan yang ingin diproses.
   - Masukkan kata kunci yang akan digunakan dalam proses enkripsi atau dekripsi.
4. **Contoh Penggunaan**:

   ```bash
       ==========<[ENCRYPT dan DECRYPT]>==================
    Pilih yang mau kamu lakukan (ENC/DEC): ENC
    Masukkan kata yang ini di Encrypt : Hello
    Masukkan kata yang ingin dijadikan kunci encrypt : key
    
    ----------- hasil Enkripsi -----------
    Kalimat awal : hello
    Kalimat hasil Encrypt : riijv
    Dengan kata kunci : key
    ---------------------------------------
    Apakah ingin mengulang lagi ? (Y/T): Y
  - Untuk Dekripsi, pilih DEC dan masukkan pesan yang terenkripsi serta kata kunci yang digunakan saat enkripsi.
5. 
