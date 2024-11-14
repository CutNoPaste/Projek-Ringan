import json, os, datetime, re

def baca_json():
    try:
        with open('tdlnow.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def simpan_json(daft_tugas):
    with open('tdlnow.json', 'w') as file:
        json.dump(daft_tugas, file, indent=4)

def bersihkanlayar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def lih_daf_tug():
    tug_num = 0
    daft_tug = baca_json()
    if daft_tug == []:
        print("-------------------")
        print("Tidak ada Kegiatan (Silahkan tambah kegiatan) !")
        print("-------------------")
    else:
        for x in daft_tug:
            tug_num += 1
            print("------------------------------------------")
            print(f"Tugas No. {tug_num}")
            for key, value in x.items():
                if value == False :
                    value = "❌"
                elif value == True :
                    value = "✔️"
                if key == "is_done" :
                    key = "Apakah sudah"
                print(f"{key} : {value}")
            if "-" in x['deadline']:
                deadline_str = datetime.datetime.strptime(x['deadline'], "%d-%m-%Y").date()
            else:
                deadline_str = datetime.datetime.strptime(x['deadline'], "%d/%m/%Y").date()
            date_now = datetime.date.today()
            delta = deadline_str - date_now
            if x['is_done'] == True:
                print("Pekerjaan kamu sudah selesai ! YEAY !")
            elif delta.days < 0:
                print(f"Pekerjaan kamu terlambat sekitar '{delta.days}' Hari")
            elif delta.days > 0:
                print("------------------------------------------")
                print(f"Deadline kamu tersisa '{delta.days}' hari")
            else:
                print("------------------------------------------")
                print("Deadline kamu hari ini ! segera tuntaskan !")
            print()

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

    print(f"Tugas {kegiatan} Tanggal {tanggal} sudah ditambahkan !")
def edit_tugas(tugas_ke):
    daft_tug = baca_json()
    hal = tugas_ke
    hal = int(hal)
    hal -= 1
    if 0 <= hal < len(daft_tug):
        if daft_tug[hal]["is_done"] == False:
            daft_tug[hal]["is_done"] = True
            print(f"Berhasil merubah status Sudah dari Tugas ke '{hal + 1}' dengan judul tugas '{daft_tug[hal]["kegiatan"]}' ")
        else:
            print("Sudah berstatus DIKERJAKAN !")
    else:
        print(f"Tidak ada tugas ke '{hal}'")
    simpan_json(daft_tug)
def hapus_tugas(tug_ke):
    daft_tug = baca_json()
    hal = tug_ke
    hal = int(hal)
    hal -= 1

    if 0 <= hal < len(daft_tug):
        print(f"Tugas ke {hal + 1} dengan nama {daft_tug[hal]["kegiatan"]} sudah di Hapus !")
        daft_tug.pop(hal)
    else:
        print(f"Tidak ada pilihan tugas ke {hal + 1}")

    simpan_json(daft_tug)

def export_txt():
    pass


def validasi_tanggal(input_tanggal):
    pattern = r"^\d{2}-(0[1-9]|1[0-2])-\d{4}$"
    pattern2 = r"^\d{2}\/(0[1-9]|1[0-2])\/\d{4}$"

    while True:
        input_tanggal = input(input_tanggal)
        if not re.match(pattern, input_tanggal) and not re.match(pattern2, input_tanggal) :
            print("Format tanggal tidak valid. Pastikan formatnya adalah DD-MM-YYYY. atau DD/MM/YYYY")
            input_tanggal = "Masukkan tanggal yang benar (format DD-MM-YYYY atau DD/MM/YYYY) : "
        else:
            return input_tanggal


def export_txt():
    """Mengekspor daftar tugas ke dalam file teks"""
    daft_tug = baca_json()

    if not daft_tug:
        print("Tidak ada tugas untuk diekspor!")
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

    print("Daftar tugas telah diekspor ke 'tugas.txt'.")


bersihkanlayar()
while True:
    print("------------- APLIKASI TO DO LIST -------------")
    print("Pilih apa yang mau kamu lakukan :\n"
          "1. Lihat daftar tugas\n"
          "2. Tambah tugas\n"
          "3. Tandai tugas selesai\n"
          "4. Hapus tugas\n"
          "5. Export ke 'file.txt'\n"
          "6. Keluar")
    pilihan1 = input("Pilih angka '1-5' : ")
    if pilihan1 in ["1","2","3","4","5","6"]:
        if pilihan1 == "1":
            bersihkanlayar()
            print("------------- DAFTAR TUGAS -------------")
            lih_daf_tug()
            input("Tekan apa saja untuk keluar ")
            bersihkanlayar()
        elif pilihan1 == "2":
            bersihkanlayar()
            print("------------- TAMBAH TUGAS -------------")
            kegiatan = input("Masukkan nama kegiatan : ")
            tanggal = validasi_tanggal("Masukkan tanggal deadline : ")
            tambah_tugas(kegiatan,tanggal)
            input("Tekan apa saja untuk keluar")
            bersihkanlayar()
        elif pilihan1 == "3":
            bersihkanlayar()
            print("------------- TANDAI TUGAS -------------")
            num_tugas = input("Masukkan Tugas no berapa yang akan ditandakan selesai? : ")
            edit_tugas(num_tugas)
            input("Tekan apa saja untuk keluar")
            bersihkanlayar()
        elif pilihan1 == "4":
            bersihkanlayar()
            print("------------- HAPUS TUGAS -------------")
            try:
                jaw_hap = int(input("Masukkan No Tugas yang ingin kamu hapus : "))
                hapus_tugas(jaw_hap)
            except ValueError:
                print(f"Isian '{jaw_hap}' Tidak Valid !")
            input("Tekan apa saja untuk keluar")
            bersihkanlayar()
        elif pilihan1 == "5":
            export_txt()
        elif pilihan1 == "6":
            print("Terima kasih sudah menggunakan Aplikasi ini")
            print("Aplikasi ini dibuat oleh : Abil Nur Fadillah (Aka. CNP)")
            break
        else:
            print(f"Tidak ada pilihan '{pilihan1}'")
