import fungsi
def cekkosong(nama):
    # Menginput sebuah string lalu mengeluarkan False jika string tidak kosong dan True jika string kosong 
    # i : char
    for i in nama:
        if i != " " and i != "":
            return False
        else:
            continue
    return True


def ubahGame(data):
    # Fungsi mengubah data dari id game yang dipilihnya
    # I.S. : data tidak kosong
	# F.S. : Procedur menginput data data yang diperlukan untuk menambah sebuah game dan divalidasi agar datanya tidak ada yang kosong, 
    #        kemudian prosedur mengeluarkan data yang baru  

    
    # Kamus lokal
    # id : string
    # datagame : array [0..5] of string
    # nama : string
    # kategori : string
    # tahunrilis : string
    # harga : string
    # stok : string
    # databaru : array [0..5] of string
    # i : integer
    # indeks : integer
    
    # Menginput ID game yang ingin diubah
    id = input("Masukan ID game: ")

    # Mencari data dari ID game tersebut
    datagame = fungsi.caridatalist(data, 0, id)

    # Mencek isi dari data tersebut
    if not datagame:
        print("ID game tidak ditemukan")
        return data

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
    print("Data game berhasil diubah!")
    return data
