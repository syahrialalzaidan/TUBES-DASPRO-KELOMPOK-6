from fungsi import csv_to_array,split, samecount

user = csv_to_array("user.csv")
# Isi array game -> [[id, nama, katergori, tahun rilis, harga, stok], [id, nama, katergori, tahun rilis, harga, stok]]
history = csv_to_array("riwayat.csv")
#variabelnya gak bisa dinamain "riwayat" karena bakal rancu sama nama fungsinya

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
            found = True
            print(f'{nomor}. {(i[0])}  | {(i[1])} | {(i[2])} | {(i[4])} | ')
            nomor += 1
        else :
            pass    
    if not found :
        print('Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.')   
