def cekkosong(nama):
    for i in nama:
        if i != " " and i != "":
            return False
        else:
            continue
    return True



def tambahGame(data):
    # Menginput serta mencek data game yang dimasukan
    while True:
        nama = input("Masukan nama game: ")
        kategori = input("Masukan kategori: ")
        tahunrilis = input("Masukan tahun rilis: ")
        harga = input("Masukan harga: ")
        stok = input("Masukan stok awal: ")
        if cekkosong(nama) or cekkosong(kategori) or cekkosong(tahunrilis) or cekkosong(harga) or cekkosong(stok):
            break
        else:
            print("Mohon masukan semua informasi mengenai game agar dapat disimpan di BNMO")
    print("Selamat! Berhasil menambahkan game " + nama)

    # Membuat ID baru untuk gamenya
    id = data[-1][0]
    angka = ""
    for i in range(4, 7):
        angka += id[i]
    idAngka = int(angka) + 1
    id = "GAME" + str(idAngka)

    # Menambahkan game ke list game
    data = data + [id, nama, kategori, tahunrilis, harga, stok]
    return data