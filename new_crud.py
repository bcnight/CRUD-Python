menu_item = 0

listnama = []

while menu_item != 9:
    print("---------------------------------")
    print("1. Mencetak List")
    print("2. Menambahkan nama ke dalam list ")
    print("3. Menghapus nama dari list ")
    print("4. Mengubah data dari list ")
    print("9. Keluar ")
    menu_item = int(input("Pilih Menu: "))
    if menu_item == 1:
        sekarang = 0
        if len(listnama) > 0:
            while sekarang < len(listnama):
                print(sekarang,".", listnama[sekarang])
                sekarang = sekarang + 1

        else:
            print("List Kosong")

    elif menu_item == 2:
        name = input("Masukkan nama: ")
        listnama.append(name)

    elif menu_item == 3:
        hapus_nama = input("Nama yang ingin di hapus: ")
        if hapus_nama in listnama:
            # namelist.remove(del_name) dapat digunakan
            item_number = listnama.remove(hapus_nama)
            # kode di atas hanya menghapus nama pertama yang ada
            # kode di bawah ini manghapus semua nama
            # while del_name in namelist:
            # item_number = namelist.index(del_name)
            # del namelist [item_number]
        else:
            print(hapus_nama, "tidak ditemukan")

    elif menu_item == 4:
        nama_lama = input("Nama apa yang ingin diubah: ")
        if nama_lama in listnama:
            item_number = listnama.index(nama_lama)
            nama_baru = input("Nama baru: ")
            listnama[item_number] = nama_baru
        else:
            print(nama_lama, "tidak ditemukan")

print("Bye Bye")
