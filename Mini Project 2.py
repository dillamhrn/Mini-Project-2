
from prettytable import PrettyTable
import sys

#tabel login
def tabel_login():
    pilihan_login = PrettyTable()
    pilihan_login.field_names = ["No.", "Login Sebagai"]
    pilihan_login.add_row(["1.", "Kasir"])
    pilihan_login.add_row(["2.", "Customer"])
    print(pilihan_login)

#tabel fitur kasir
def tabel_fitur_kasir():
    kasir = PrettyTable()
    kasir.field_names = ["No.", "Fitur"]
    kasir.add_row(["1.", "Lihat Menu"])
    kasir.add_row(["2.", "Tambah Menu"])
    kasir.add_row(["3.", "Hapus Menu"])
    kasir.add_row(["4.", "Perbarui Menu"])
    kasir.add_row(["5.", "Keluar/Login Kembali"])
    kasir.add_row(["5.", "Login ulang"])
    kasir.add_row(["6.", "Keluar"])
    print(kasir)

#tabel menu
tabel_menu = PrettyTable()
tabel_menu.field_names = ["No.", "Menu", "Harga"]
list_menu = [
    ["1", "Chicken Double Roll (CDR)", "27000"],
    ["2", "CDR Mozzarella", "32000"],  
    ["3", "Tuna Spicy Roll", "27000"],
    ["4", "Chicken Rock N Roll", "27000"],
    ["5", "Salmon Mentai Roll", "42000"],
    ["6", "California Roll", "32000"],
    ["7", "Kani Mentai", "27000"],
    ["8", "Yakituna Nigiri", "27000"],
    ["9", "Tamago Nigiri", "22000"],
    ["10", "Inari Kanibiko", "42000"]
]
for item in list_menu:
    tabel_menu.add_row(item)

#login✅
def login():
    print("\n--------------------------------------")
    print("Selamat Datang di Kimorawr Tsutsi 🍣🍥")
    print("--------------------------------------")
    tabel_login()
    while True:
        pilih_mode = input("Pilih mode login (isi sesuai angkanya): ")
        if pilih_mode == "1":
            kasir()
        elif pilih_mode == "2":
            customer()
        else:
            print("\n----------------------------------------")
            print("Pilihan tidak sesuai, silakan coba lagi.")
            print("----------------------------------------")
            continue

#customer✅
def customer():
    print("\nHalo✨ mau pesan apa?")
    lihat_menu()

    while True: 
        no = input("\nPilih menu (isi sesuai angkanya): ")
        
        found = False
        for row in tabel_menu._rows:
            if row[0] == no:
                found = True 
                jumlah_pesanan = input("Jumlah porsi: ")
                try:
                    jumlah_pesanan = int(jumlah_pesanan)
                    harga = int(row[2])
                    total_harga = jumlah_pesanan*harga

                    print(f"\nPesanan anda: {row[1]} sebanyak {jumlah_pesanan} porsi, \nTotal: {total_harga}")
                    print("\nPesanan akan segera diproses.")
                    selesai()

                except ValueError:
                    print("\n---------------------------------------------------")
                    print("Jumlah porsi harus berupa angka, silakan coba lagi.")
                    print("---------------------------------------------------")
                    continue

        if not found:
            print("\n----------------------------------------")
            print("Menu tidak ditemukan, silakan coba lagi.")
            print("----------------------------------------")
            continue

#kasir✅
def kasir():
    print("\n---------------")
    print("Halo, kasir! 👩‍💻")
    print("---------------")
    tabel_fitur_kasir()
    while True:
        pilihan_fitur = input("\nPilih fitur (isi sesuai angkanya): ")
        if pilihan_fitur == "1":
            lihat_menu()
        elif pilihan_fitur == "2":
            fitur_tambah_menu()
        elif pilihan_fitur == "3":
            fitur_hapus_menu()
        elif pilihan_fitur == "4":
            fitur_perbarui_menu()
        elif pilihan_fitur == "5":
            login()
        elif pilihan_fitur == "6":
            selesai()
        else:
            print("\n----------------------------------------")
            print("Pilihan tidak sesuai, silakan coba lagi.")
            print("----------------------------------------")
            continue

#fitur lihat menu✅
def lihat_menu():
    print("\n---------------------")
    print("🍣🍥 List menu 🍣🍥")
    print("---------------------")
    print(tabel_menu)

#fitur tambah menu✅
def tambah_menu(no, menu, harga):
    tabel_menu.add_row([no, menu, harga])

def fitur_tambah_menu():
    lihat_menu()
    print("\n-----------------------------")
    print("👇➕ Silakan tambah list menu ➕👇")
    print("-----------------------------")
    while True:
        no = input("\nNomor menu baru: ")
        menu = input("Nama menu baru: ")
        harga = input("Harga menu baru: ")

        try:
            harga = int(harga)
            tambah_menu(no, menu, harga)
            print("---------------------------------------------------------------------------")
            print(f"Menu baru nomor {no} --> {menu} dengan harga {harga} berhasil ditambahkan.")
            print("---------------------------------------------------------------------------")
        except ValueError:
            print("\n------------------------------------------")
            print("Harga harus berupa angka, silakan coba lagi.")
            print("------------------------------------------")
            continue

        tambah_lagi = input("Mau tambah menu lagi? (y/t): ")
        if tambah_lagi == "y":
            continue
        elif tambah_lagi == "t":
            kasir()

#fitur hapus menu✅
def fitur_hapus_menu():
    lihat_menu()
    print("\n------------------------------------")
    print("👇➖ Silakan hapus list menu ➖👇")
    print("------------------------------------")
    while True:
        no = input("\nPilih nomor menu yang ingin dihapus: ")
        
        found = False
        for row in tabel_menu._rows:
            if row[0] == no:
                tabel_menu.del_row(tabel_menu._rows.index(row))
                found = True
                print("\n--------------------------------------")
                print(f"Menu dengan nomor {no} sudah dihapus.")
                print("--------------------------------------")
                break
        
        if not found:
            print("\n--------------------------------------------")
            print("Nomor menu tidak ditemukan, silakan coba lagi.")
            print("--------------------------------------------")
            continue

        hapus_lagi = input("\nMau menghapus menu lagi? (y/t): ")
        if hapus_lagi == "y":
            continue
        elif hapus_lagi == "t":
            kasir()

#fitur perbarui menu✅
def fitur_perbarui_menu():
    lihat_menu()
    while True:
        no = input("\nPilih nomor menu yang ingin diubah: ")
        found = False
        for row in tabel_menu._rows:
            if row[0] == no:
                found = True
        if not found:
            print("\n----------------------------------------")
            print("Pilihan tidak sesuai, silakan coba lagi.")
            print("----------------------------------------")
            continue 

        for row in tabel_menu._rows:
            if row[0] == no:
                pilihan_ubah = input("\nMau ubah menu atau harga? (menu/harga): ")
                if pilihan_ubah != "menu" and pilihan_ubah != "harga":
                    print("\n----------------------------------------")
                    print("Pilihan tidak sesuai, silakan coba lagi.")
                    print("----------------------------------------")
                    continue
                
                perubahan = input(f"Masukkan {pilihan_ubah} yang baru: ")

                if pilihan_ubah == "menu":
                    row[1] = perubahan
                elif pilihan_ubah == "harga":
                    try:
                        row[2] = int(perubahan)
                    except ValueError:
                        print("\n--------------------------------------------")
                        print("Harga harus berupa angka, silakan coba lagi.")
                        print("--------------------------------------------")
                        continue
                else:
                    print("\n----------------------------------------")
                    print("Pilihan tidak sesuai, silakan coba lagi.")
                    print("----------------------------------------")
                    continue 

                print("\n--------------------------------------------")
                print(f"Menu pada nomor {no} berhasil diperbarui.")
                print("--------------------------------------------")
                kasir()

#selesai✅
def selesai():
    print("----------------------------------")
    print("Terima kasih atas waktunya! 🍣🍥")
    print("----------------------------------")
    sys.exit()

#mulai program✅
login()
