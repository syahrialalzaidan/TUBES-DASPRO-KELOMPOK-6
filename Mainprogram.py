# Program utamanya
# Ini kalau ada solusi buat cara biar diawalnya engga banyak banget import gitu kasih tau yak
# Sama buat program buat khusus admin doang, aku belum buat fungsi biar bisa cepet

import fungsi
import F02
import F03
import F04
import F05
# Isi elemen arraynya string semua (kalau misalnya perlu isinya type lain kasih tau aja)
# Tapi itu baru yang user dan game aja

# Isi array user -> [[id, username, nama, password, role, saldo], [id, username, nama, password, role, saldo]]
user = []
# Isi array game -> [[id, nama, katergori, tahun rilis, harga, stok], [id, nama, katergori, tahun rilis, harga, stok]]
game = []
# Isi array riwayat -> [[game id, nama, harga, user id, tahun beli], [game id, nama, harga, user id, tahun beli]]
riwayat = []
# Isi array kepemilikan -> [[game id, user id], [game id, user id]]
kepemilikan = []


# Fungsi LOAD


# Fungsi login F03

login = False
while login == False:
    perintah = input(">>> ")
    if perintah == "login":
        datauser = F03.login(user)
        login = datauser[0][0]
    else:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”")

# Isi datauser -> [[True], [id, username, nama, password, role, saldo]]
# Role usernya
role = fungsi.cekRole(datauser[1][1], user)


# Program Utamanya
while True:     # Ini buat di 'break' pake fungsi exit, ubah aja cara nge loopnya kalau perlu
    perintah = input(">>> ")

    # F02
    if perintah == "register":
        if role == "Admin":
            user = F02.register(user)
            continue
        else:
            print("Maaf, hanya Admin yang dapat menjalankan program ini! ")

    # F04
    elif perintah == "tambah_game":
        if role == "Admin":
            game = F04.tambahGame(game)
            continue
        else:
            print("Maaf, hanya Admin yang dapat menjalankan program ini! ")

    # F05
    elif perintah == "ubah_game":
        if role == "Admin":
            game = F05.ubahGame(game)
            continue
        else:
            print("Maaf, hanya Admin yang dapat menjalankan program ini! ")






