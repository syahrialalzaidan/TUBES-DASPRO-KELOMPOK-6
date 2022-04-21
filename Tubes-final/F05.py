import fungsi
def cekkosong(nama):
    for i in nama:
        if i != " " and i != "":
            return False
        else:
            continue
    return True


def ubahGame(data):
    # Menginput ID game yang ingin diubah
    id = input("Masukan ID game: ")

    # Mencari data dari ID game tersebut
    datagame = fungsi.caridatalist(data, 0, id)

    # Mencek isi dari data tersebut
    if not datagame:
        print("ID game tidak ditemukan")
        return

    # Mengisi data baru untuk gamenya
    else:
        nama = input("Masukan nama game: ")
        kategori = input("Masukan kategori: ")
        tahunrilis = input("Masukan tahun rilis: ")
        harga = input("Masukan harga: ")
        stok = datagame[5]
    databaru = [id, nama, kategori, tahunrilis, harga, stok]

    # Mengubah data baru untuk gamenya
    for i in range(6):
        if cekkosong(databaru[i]):
            continue
        else:
            datagame[i] = databaru[i]

    # Memasukan data baru tersebut ke list game
    indeks = fungsi.indeksdata(data, 0, id)
    data[indeks] = datagame
    return data
