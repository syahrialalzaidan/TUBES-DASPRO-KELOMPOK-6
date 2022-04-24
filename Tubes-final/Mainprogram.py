# Program BNMO

# KAMUS
# type gameData : < id : string;
# 				nama : string;
# 				kategori : string;
# 				tahun_rilis : string;
# 				harga : string;
# 				stok : string >
# type userData : < id : string;
# 				username : string;
# 				nama : string;
# 				password : string;
# 				role : string;
# 				saldo : string >
# type historyData : < game_id : string;
# 				   nama : string;
# 				   harga : integer;
# 				   user_id : string;
# 				   tahun_beli : string >
# type kepemilikanData : < game_id : string;
# 					  user_id : string >
# folder : boolean
# user : array of userData
# game : array of gameData
# history : array of historyData
# kepemilikan : array of kepemilikanData
# perintah : string


# ALGORITMA
from F15 import load
import fungsi

# Menjalankan fungsi load
folder = load()
if folder:
    pass
else:
    exit()

# Mengimport fungsi-fungsi
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
history = fungsi.csv_to_array("riwayat.csv")
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
# ID user
IDuser = datauser[1][0]


# Program Utamanya
while True:     
    perintah = input(">>> ")

    # F02 - register
    if perintah == "register":
        if role == "Admin":
            user = F02.register(user)
            continue
        else:
            print("Maaf, hanya Admin yang dapat menjalankan program ini! ")

    # F04 - tambah_game
    elif perintah == "tambah_game":
        if role == "Admin":
            game = F04.tambahGame(game)
            continue
        else:
            print("Maaf, hanya Admin yang dapat menjalankan program ini! ")

    # F05 - ubah_game
    elif perintah == "ubah_game":
        if role == "Admin":
            game = F05.ubahGame(game)
            continue
        else:
            print("Maaf, hanya Admin yang dapat menjalankan program ini! ")
     
    # F06 - ubah_stok
    elif perintah == "ubah_stok":
        if role == "Admin":
            game = F06.ubah_stok("game.csv")
        else:
            print("Maaf, hanya Admin yang dapat menjalankan program ini! ")       
    
    # F07 - list_game_toko
    elif perintah == "list_game_toko":
        F07.list_game_toko(game)
            
    # F08 - buy_game
    elif perintah == "buy_game":
        if role == "User":
            user, kepemilikan = F08.buy_game(username, game, user, kepemilikan)
        else:
            print("Maaf, hanya user yang dapat menjalankan program ini!")
    
    # F09 - list_game
    elif perintah == "list_game":
        if role == "User":
            F09.list_game(username, role, user, kepemilikan, game)
        else:
            print("Maaf, hanya user yang dapat menjalankan program ini!")
    
    # F10 - search_my_game
    elif perintah == "search_my_game":
        if role == "User":
            F10.search_my_game(IDuser, game, kepemilikan)
        else:
            print("Maaf, hanya user yang dapat menjalankan program ini!")
        
    
    # F11 - search_game_at_store
    elif perintah == "search_game_at_store":
        F11.search_game_at_store(game)
    
    # F12 - topup
    elif perintah == "topup":
        if role == "Admin":
            user = F12.topup(user)
        else:
            print("Maaf, hanya Admin yang dapat menjalankan program ini! ")

    # F13 - riwayat 
    elif perintah == "riwayat":
        if role == "User":
            F13.riwayat(username, user, history)
        else:
            print("Maaf, hanya user yang dapat menjalankan program ini!")
    
    # F14 - help
    elif perintah == "help":
        F14.helpSetelahLogin(role)
    
    # F16 - save
    elif perintah == "save":
        F16.save(game, kepemilikan, history, user)
    
    # F17 - exit
    elif perintah == "exit":
        F17.exit(game, kepemilikan, history, user)  
    
    # B02 - kerangajaib
    elif perintah == "kerangajaib":
        B02.kerangajaib()
    
    # B03 - tictactoe
    elif perintah == "tictactoe":
        B03.tictactoe()
        
    # Perintah tidak valid
    else:
        print("Perintah tidak valid. Ketik 'help' untuk melihat opsi perintah yang bisa digunakan.")  
