from fungsi import csv_to_array,split, samecount

user = csv_to_array("user.csv")
# Isi array game -> [[id, nama, katergori, tahun rilis, harga, stok], [id, nama, katergori, tahun rilis, harga, stok]]
game = csv_to_array("game.csv")
# Isi array riwayat -> [[game id, nama, harga, user id, tahun beli], [game id, nama, harga, user id, tahun beli]]
history = csv_to_array("riwayat.csv")
#variabelnya gak bisa dinamain "riwayat" karena bakal rancu sama nama fungsinya

# Isi array kepemilikan -> [[game id, user id], [game id, user id]]
kepemilikan = csv_to_array("kepemilikan.csv")

def riwayat(username) :
    user_id = ''
    found = False
    nomor = 1

    #cari user_id
    for x in user :
        if x[1] == username :
            user_id = x[0]
        else :
            pass
    
    #ngefilter history berdasarkan user_id
    for i in history :
        if i[3] == user_id :
            print(f'{nomor}. {(i[0])}  | {(i[1])} | {(i[2])} | {(i[4])} | ')
            nomor += 1
        else :
            pass    
riwayat()
