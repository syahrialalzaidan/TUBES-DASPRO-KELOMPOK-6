# Program utamanya

from F15 import load
import fungsi

# Menjalankan fungsi load
folder = load()
if folder:
    pass
else:
    exit()

# Ini kalau ada solusi buat cara biar diawalnya engga banyak banget import gitu kasih tau yak
# Sama buat program buat khusus admin doang, aku belum buat fungsi biar bisa cepet

import F02
import F03
import F04
import F05
import F06
import F07
import F08
import F09
import F10
import F11
import F12
import F13
import F14
import F16
import F17
import B02
import B03
# Isi elemen arraynya string semua (kalau misalnya perlu isinya type lain kasih tau aja)
# Tapi itu baru yang user dan game aja

# Isi array user -> [[id, username, nama, password, role, saldo], [id, username, nama, password, role, saldo]]
user = fungsi.csv_to_array("user.csv")
# Isi array game -> [[id, nama, katergori, tahun rilis, harga, stok], [id, nama, katergori, tahun rilis, harga, stok]]
game = fungsi.csv_to_array("game.csv")
# Isi array riwayat -> [[game id, nama, harga, user id, tahun beli], [game id, nama, harga, user id, tahun beli]]
riwayat = fungsi.csv_to_array("riwayat.csv")
# Isi array kepemilikan -> [[game id, user id], [game id, user id]]
kepemilikan = fungsi.csv_to_array("kepemilikan.csv")

# Fungsi login F03

login = False
while login == False:
    perintah = input(">>> ")
    if perintah == "login":
        datauser = F03.login(user)
        login = datauser[0][0]
    elif perintah == "help":
        F14.helpSebelumLogin()
    else:
        print("Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain “login”")

# Isi datauser -> [[True], [id, username, nama, password, role, saldo]]
# Role usernya
role = datauser[1][4]
# Username
username = datauser[1][1]


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
     
    # F06 - ubah_stok
    elif perintah == "ubah_stok":
        if role == "admin":
            game = F06.ubah_stok(game)
        else:
            print("Maaf, hanya Admin yang dapat menjalankan program ini! ")       
    
    # F07 - list_game_toko
    elif perintah == "list_game_toko":
        F07.list_game_toko(game)
            
    # F08 - buy_game
    elif perintah == "buy_game":
        if role == "user":
            user, kepemilikan = F08.buy_game(username, game, user, kepemilikan)
        else:
            print("Maaf, hanya user yang dapat menjalankan program ini!")
    
    # F09 - list_game
    elif perintah == "list_game":
        if role == "user":
            F09.list_game(username, role, user, kepemilikan, game)
    
    # F10 - search_my_game
    elif perintah == "search_my_game":
        if role == "user":
            F10.search_my_game(username)
        else:
            print("Maaf, hanya user yang dapat menjalankan program ini!")
    
    # F11 - search_game_at_store
    elif perintah == "search_game_at_store":
        F11.search_game_at_store()
    
    # F12 - topup
    elif perintah == "topup":
        if role == "admin":
            user = F12.topup()
        else:
            print("Maaf, hanya Admin yang dapat menjalankan program ini! ")

    # F13 - riwayat 
    elif perintah == "riwayat":
        if role == "user":
            F13.riwayat()
    
    # F14 - help
    elif perintah == "help":
        F14.helpSetelahLogin(role)
    
    # F16 - save
    elif perintah == "save":
        F16.save(game, kepemilikan, riwayat, user)
    
    # F17 - exit
    elif perintah == "exit":
        F17.exit(game, kepemilikan, riwayat, user)  
    
    # B02 - kerangajaib
    elif perintah == "kerangajaib":
        B02.kerangajaib()
    
    # B03 - tictactoe
    elif perintah == "tictactoe":
        B03.tictactoe()
        
    # Perintah tidak valid
    else:
        print("Perintah tidak valid. Ketik 'help' untuk melihat opsi perintah yang bisa digunakan.")  


