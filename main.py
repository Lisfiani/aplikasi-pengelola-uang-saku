import json
from datetime import datetime

saldo = 0
transaksi = []
FILE_DATA = "data.json"

def simpan_data():
    with open(FILE_DATA, "w") as file:
        json.dump({"saldo": saldo, "transaksi": transaksi}, file, indent=2)

def muat_data():
    global saldo, transaksi
    try:
        with open(FILE_DATA, "r") as file:
            data = json.load(file)
            saldo = data.get("saldo", 0)
            transaksi = data.get("transaksi", [])
    except FileNotFoundError:
        saldo = 0
        transaksi = []

def tambah_pemasukan():
    global saldo
    keterangan = input("Masukkan keterangan pemasukan: ")
    jumlah = int(input("Masukkan jumlah pemasukan: "))
    saldo += jumlah
    transaksi.append({
        "tipe": "Pemasukan",
        "keterangan": keterangan,
        "jumlah": jumlah,
        "tanggal": datetime.now().strftime("%d/%m/%Y %H:%M")
    })
    print(f"Pemasukan sebesar Rp{jumlah} berhasil ditambahkan!")
    simpan_data()

def tambah_pengeluaran():
    global saldo
    keterangan = input("Masukkan keterangan pengeluaran: ")
    jumlah = int(input("Masukkan jumlah pengeluaran: "))
    if saldo >= jumlah:
        saldo -= jumlah
        transaksi.append({
            "tipe": "Pengeluaran",
            "keterangan": keterangan,
            "jumlah": jumlah,
            "tanggal": datetime.now().strftime("%d/%m/%Y %H:%M")
        })
        print(f"Pengeluaran sebesar Rp{jumlah} berhasil dicatat!")
        simpan_data()
    else:
        print(f"Peringatan! Saldo tidak cukup. Saldo Anda hanya Rp{saldo}")

def lihat_saldo():
    print("=" * 35)
    print(f"Saldo Anda saat ini: Rp{saldo}")
    print("=" * 35)

def lihat_laporan():
    print("\n" + "=" * 50)
    print("LAPORAN PEMASUKAN DAN PENGELUARAN")
    print("=" * 50)
    
    if not transaksi:
        print("Belum ada transaksi")
        print("=" * 50)
        return
    
    total_pemasukan = 0
    total_pengeluaran = 0
    
    print(f"{'No':<3} {'Tipe':<12} {'Keterangan':<20} {'Jumlah':<12} {'Tanggal':<17}")
    print("-" * 50)
    
    for i, t in enumerate(transaksi, 1):
        tipe = t["tipe"]
        keterangan = t["keterangan"][:19]
        jumlah = t["jumlah"]
        tanggal = t["tanggal"]
        
        print(f"{i:<3} {tipe:<12} {keterangan:<20} Rp{jumlah:<10} {tanggal:<17}")
        
        if tipe == "Pemasukan":
            total_pemasukan += jumlah
        else:
            total_pengeluaran += jumlah
    
    print("-" * 50)
    print(f"Total Pemasukan    : Rp{total_pemasukan}")
    print(f"Total Pengeluaran  : Rp{total_pengeluaran}")
    print(f"Saldo Akhir        : Rp{saldo}")
    print("=" * 50 + "\n")

def menu():
    print("\n=== Aplikasi Pengelola Uang Saku ===")
    print("1. Tambah pemasukan")
    print("2. Tambah pengeluaran")
    print("3. Lihat saldo")
    print("4. Lihat laporan")
    print("5. Keluar")

muat_data()

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_pemasukan()
    elif pilihan == "2":
        tambah_pengeluaran()
    elif pilihan == "3":
        lihat_saldo()
    elif pilihan == "4":
        lihat_laporan()
    elif pilihan == "5":
        simpan_data()
        print("Data berhasil disimpan. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid")