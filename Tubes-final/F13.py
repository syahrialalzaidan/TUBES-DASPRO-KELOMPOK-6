def riwayat(username, user, history) :
    #KAMUS LOKAL 
    #user_id : string
    #found : boolean
    #nomor : integer

    #ALGORITMA

    #Deklarasi variabel
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
