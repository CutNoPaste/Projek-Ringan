# Fungsi enkripsi dan deskripsi
def vigenere(pesan, kunci, arahan=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    pesan_akhir = ''
    kunci = kunci.lower()
    for karakter in pesan.lower():

        # menambahkan spasi jika ada
        if not karakter.isalpha():
            pesan_akhir += karakter
        else:
            # Mencari key yang benar untuk encrypt atau decrypt
            kunci_karakter = kunci[key_index % len(kunci)]
            key_index += 1

            # memberikan hasil pada encrypt atau decrypt
            offset = alphabet.index(kunci_karakter)
            index = alphabet.find(karakter)
            new_index = (index + offset * arahan) % len(alphabet)
            pesan_akhir += alphabet[new_index]

    return pesan_akhir

# Fungsi buat inputan
def proses():
    if pilihan.upper() == 'DEC':
        kalimat = input('Masukkan kata yang ini di Decrypt : ')
        kunci_kalimat = input('Masukkan kata yang ingin dijadikan kunci Encrypt : ')
        dekpripsi = vigenere(kalimat, kunci_kalimat, -1)
        print('\n----------- hasil deskripsi -----------')
        print(f'Kalimat awal : {kalimat}')
        print(f'Kalimat hasil decrypt : {dekpripsi}')
        print(f'Dengan kata kunci : {kunci_kalimat}')
        print('---------------------------------------')
    elif pilihan.upper() == 'ENC':
        kalimat = input('Masukkan kata yang ini di Encrypt : ')
        kunci_kalimat = input('Masukkan kata yang ingin dijadikan kunci encrypt : ')
        enkripsi = vigenere(kalimat, kunci_kalimat)
        print('\n----------- hasil Enkripsi -----------')
        print(f'Kalimat awal : {kalimat}')
        print(f'Kalimat hasil Encrypt : {enkripsi}')
        print(f'Dengan kata kunci : {kunci_kalimat}')
        print('---------------------------------------')

# Pengulangan di Intro
while True:
    print("\n============<[ENCRYPT dan DECRYPT]>==================")
    while True:
        pilihan = input("Pilih yang mau kamu lakukan (ENC/DEC): ")
        if pilihan.upper() == "ENC" or pilihan.upper() == "DEC":
            proses()
            break
        else:
            print("isi dengan benar !")
    ulang = input("Apakah ingin mengulang lagi ? (Y/T): ")
    if ulang.upper().strip() == "Y":
        pass
    else:
        print("Terima kasih...")
        break
