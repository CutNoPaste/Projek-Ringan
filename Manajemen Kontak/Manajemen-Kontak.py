import json

def tambah_kontak(nama, nomor, email):
    try:
        with open('kontak.json', 'r') as file:
            kontak_list = json.load(file)
    except FileNotFoundError:
        kontak_list = []

    kontak_baru = {
        "Nama": nama,
        "Nomor": nomor,
        "Email": email
    }

    kontak_list.append(kontak_baru)

    with open('kontak.json', 'w') as file:
        json.dump(kontak_list, file, indent=4)

    print(f"Kontak {nama} berhasil ditambahkan!")

def hapus_kontak(nama):
    try:
        with open('kontak.json', 'r') as file:
            kontak_list = json.load(file)

        kontak_terhapus = None
        for kontak in kontak_list:
            if kontak["Nama"].lower() == nama.lower():
                kontak_terhapus = kontak
                kontak_list.remove(kontak)
                break

        if kontak_terhapus:
            # Menyimpan perubahan ke file JSON
            with open('kontak.json', 'w') as file:
                json.dump(kontak_list, file, indent=4)
            print(f"Kontak {kontak_terhapus['Nama']} berhasil dihapus!")
        else:
            print(f"Kontak dengan nama {nama} tidak ditemukan.")

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("File tidak ditemukan atau JSON Decode Error !")


while True:
    print("--------- MANAJEMEN KONTAK ---------")
    print("Masukkan pilihan : ")
    print("1. lihat kontak\n"
          "2. Tambah kontak \n"
          "3. Hapus Kontak\n"
          "4. Keluar")
    while True:
        try:
            pilihan = int(input("Masukkan pilihan : "))
            break
        except ValueError:
            print("Isi dengan benar !")

    if pilihan == 2:
        nama = input("Masukkan nama : ")
        while True:
            try:
                nomor = int(input("Masukkan nomor : "))
                nomor = str(nomor)
                if len(nomor) > 9:
                    nomor = "0"+nomor
                break
            except ValueError:
                print("Isi nomor dengan benar !")
        email = input("Masukkan email : ")
        tambah_kontak(nama,nomor,email)

    elif pilihan == 1:
        kontak_nomor = 0
        with open('kontak.json', 'r') as file:
            kontak_list = json.load(file)
        if kontak_list == []:
            print("-------------------")
            print("Tidak ada kontak !")
            print("-------------------")
        else:
            for x in kontak_list:
                kontak_nomor += 1
                print("--------------------------")
                print(f"Kontak No. {kontak_nomor}")
                for key,value in x.items():
                    print(f"{key} : {value}")
                print()
    elif pilihan ==3:
        nama = input("Masukkan nama : ")
        hapus_kontak(nama)
    elif pilihan == 4:
        print("Terima kasih sudah menggunakan aplikasi saya.")
        break
