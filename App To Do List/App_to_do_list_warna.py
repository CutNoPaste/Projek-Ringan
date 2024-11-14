import json, os, datetime, re
import random
import time
from colorama import Fore, Back, init

# Inisialisasi untuk Windows
init(autoreset=True)

# Fungsi untuk membaca file JSON
def baca_json():
    try:
        with open('tdlnow.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Fungsi untuk menyimpan file JSON
def simpan_json(daft_tugas):
    with open('tdlnow.json', 'w') as file:
        json.dump(daft_tugas, file, indent=4)

# Fungsi untuk membersihkan layar
def bersihkanlayar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Fungsi untuk menampilkan daftar tugas
def lih_daf_tug():
    tug_num = 0
    daft_tug = baca_json()
    if daft_tug == []:
        print(Fore.YELLOW + "-------------------")
        print(Fore.RED + "Tidak ada Kegiatan (Silahkan tambah kegiatan) !")
        print(Fore.YELLOW + "-------------------")
    else:
        for x in daft_tug:
            tug_num += 1
            print(Fore.CYAN + "------------------------------------------")
            print(Fore.GREEN + f"Tugas No. {tug_num}")
            for key, value in x.items():
                if value == False:
                    value = "❌"
                elif value == True:
                    value = "✔️"
                if key == "is_done":
                    key = "Apakah sudah"
                print(Fore.MAGENTA + f"{key} : {value}")
            if "-" in x['deadline']:
                deadline_str = datetime.datetime.strptime(x['deadline'], "%d-%m-%Y").date()
            else:
                deadline_str = datetime.datetime.strptime(x['deadline'], "%d/%m/%Y").date()
            date_now = datetime.date.today()
            delta = deadline_str - date_now
            if x['is_done'] == True:
                print(Fore.GREEN + "Pekerjaan kamu sudah selesai ! YEAY !")
            elif delta.days < 0:
                print(Fore.RED + f"Pekerjaan kamu terlambat sekitar '{delta.days}' Hari")
            elif delta.days > 0:
                print(Fore.YELLOW + f"Deadline kamu tersisa '{delta.days}' hari")
            else:
                print(Fore.CYAN + "Deadline kamu hari ini ! segera tuntaskan !")
            print()

# Fungsi untuk menambahkan tugas baru
def tambah_tugas(kegiatan, tanggal, is_done = False):
    try:
        daft_tug = baca_json()
    except FileNotFoundError:
        daft_tug = []

    kontak_baru = {
        "kegiatan": kegiatan,
        "deadline": tanggal,
        "is_done": is_done
    }

    daft_tug.append(kontak_baru)
    simpan_json(daft_tug)
    print(Fore.GREEN + f"Tugas {kegiatan} Tanggal {tanggal} sudah ditambahkan !")

# Fungsi untuk mengedit status tugas
def edit_tugas(tugas_ke):
    daft_tug = baca_json()
    hal = int(tugas_ke) - 1
    if 0 <= hal < len(daft_tug):
        if daft_tug[hal]["is_done"] == False:
            daft_tug[hal]["is_done"] = True
            print(Fore.GREEN + f"Berhasil merubah status Sudah dari Tugas ke '{hal + 1}' dengan judul tugas '{daft_tug[hal]['kegiatan']}' ")
        else:
            print(Fore.YELLOW + "Sudah berstatus DIKERJAKAN !")
    else:
        print(Fore.RED + f"Tidak ada tugas ke '{hal + 1}'")
    simpan_json(daft_tug)

# Fungsi untuk menghapus tugas
def hapus_tugas(tug_ke):
    daft_tug = baca_json()
    hal = int(tug_ke) - 1
    if 0 <= hal < len(daft_tug):
        print(Fore.RED + f"Tugas ke {hal + 1} dengan nama {daft_tug[hal]['kegiatan']} sudah di Hapus !")
        daft_tug.pop(hal)
    else:
        print(Fore.RED + f"Tidak ada pilihan tugas ke {hal + 1}")
    simpan_json(daft_tug)

# Fungsi untuk mengekspor tugas ke file "tugas.txt"
def export_txt():
    daft_tug = baca_json()

    if not daft_tug:
        print(Fore.YELLOW + "Tidak ada tugas untuk diekspor!")
        return

    with open('tugas.txt', 'w', encoding='utf-8') as file:
        for idx, tugas in enumerate(daft_tug, start=1):
            file.write(f"Tugas No. {idx}\n")
            for key, value in tugas.items():
                if value == False:
                    value = "❌"
                elif value == True:
                    value = "✔️"
                if key == "is_done":
                    key = "Apakah sudah"
                file.write(f"{key}: {value}\n")

            if "-" in tugas['deadline']:
                deadline_str = datetime.datetime.strptime(tugas['deadline'], "%d-%m-%Y").date()
            else:
                deadline_str = datetime.datetime.strptime(tugas['deadline'], "%d/%m/%Y").date()
            date_now = datetime.date.today()
            delta = deadline_str - date_now
            if tugas['is_done'] == True:
                file.write("Pekerjaan kamu sudah selesai ! YEAY !\n")
            elif delta.days < 0:
                file.write(f"Pekerjaan kamu terlambat sekitar '{delta.days}' Hari\n")
            elif delta.days > 0:
                file.write(f"Deadline kamu tersisa '{delta.days}' hari\n")
            else:
                file.write("Deadline kamu hari ini ! segera tuntaskan !\n")

            file.write("\n" + "-" * 40 + "\n")

    print(Fore.GREEN + "Daftar tugas telah diekspor ke 'tugas.txt'.")

# Fungsi untuk validasi input tanggal
def validasi_tanggal(input_tanggal):
    pattern = r"^\d{2}-(0[1-9]|1[0-2])-\d{4}$"
    pattern2 = r"^\d{2}\/(0[1-9]|1[0-2])\/\d{4}$"

    while True:
        input_tanggal = input(input_tanggal)
        if not re.match(pattern, input_tanggal) and not re.match(pattern2, input_tanggal):
            print(Fore.RED + "Format tanggal tidak valid. Pastikan formatnya adalah DD-MM-YYYY. atau DD/MM/YYYY")
        else:
            return input_tanggal

# Daftar warna untuk animasi
warna_warna = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA]

# Fungsi untuk animasi warna-warni pada judul aplikasi
def animasi_warna_warni(teks, durasi=0.5, ulangi=10):
    for _ in range(ulangi):
        warna = random.choice(warna_warna)
        print(warna + teks, end='\r')  # Tampilkan teks dengan warna acak
        time.sleep(durasi)  # Delay untuk efek animasi

# Menampilkan animasi warna-warni untuk judul aplikasi
animasi_warna_warni("🎉 Aplikasi To-Do List 📝", durasi=0.3, ulangi=10)

# Main loop aplikasi
while True:
    print(Fore.CYAN + "------------- APLIKASI TO DO LIST -------------")
    print(Fore.YELLOW + "Pilih apa yang mau kamu lakukan :\n"
          f"1. Lihat daftar tugas {Fore.GREEN}📋\n"
          f"2. Tambah tugas {Fore.CYAN}➕\n"
          f"3. Tandai tugas selesai {Fore.GREEN}✔️\n"
          f"4. Hapus tugas {Fore.RED}❌\n"
          f"5. Export ke 'file.txt' {Fore.YELLOW}💾\n"
          f"6. Keluar {Fore.MAGENTA}🚪")
    pilihan1 = input(Fore.MAGENTA + "Pilih angka '1-5' : ")
    if pilihan1 in ["1", "2", "3", "4", "5", "6"]:
        if pilihan1 == "1":
            bersihkanlayar()
            print(Fore.YELLOW + "------------- DAFTAR TUGAS -------------")
            lih_daf_tug()
            input(Fore.CYAN + "Tekan apa saja untuk keluar ")
            bersihkanlayar()
        elif pilihan1 == "2":
            bersihkanlayar()
            print(Fore.GREEN + "------------- TAMBAH TUGAS -------------")
            kegiatan = input(Fore.CYAN + "Masukkan nama kegiatan : ")
            tanggal = validasi_tanggal(Fore.YELLOW + "Masukkan tanggal deadline : ")
            tambah_tugas(kegiatan, tanggal)
            input(Fore.CYAN + "Tekan apa saja untuk keluar")
            bersihkanlayar()
        elif pilihan1 == "3":
            bersihkanlayar()
            print(Fore.GREEN + "------------- TANDAI TUGAS -------------")
            num_tugas = input(Fore.YELLOW + "Masukkan Tugas no berapa yang akan ditandakan selesai? : ")
            edit_tugas(num_tugas)
            input(Fore.CYAN + "Tekan apa saja untuk keluar")
            bersihkanlayar()
        elif pilihan1 == "4":
            bersihkanlayar()
            print(Fore.RED + "------------- HAPUS TUGAS -------------")
            try:
                jaw_hap = int(input(Fore.YELLOW + "Masukkan No Tugas yang ingin kamu hapus : "))
                hapus_tugas(jaw_hap)
            except ValueError:
                print(Fore.RED + f"Isian '{jaw_hap}' Tidak Valid !")
            input(Fore.CYAN + "Tekan apa saja untuk keluar")
            bersihkanlayar()
        elif pilihan1 == "5":
            export_txt()
        elif pilihan1 == "6":
            print(Fore.GREEN + "Terima kasih sudah menggunakan Aplikasi ini")
            print(Fore.CYAN + "Aplikasi ini dibuat oleh : Abil Nur Fadillah (Aka. CNP)")
            input(Fore.LIGHTGREEN_EX + "Tekan apa saja untuk keluar !")
            break
        else:
            print(Fore.RED + f"Tidak ada pilihan '{pilihan1}'")
