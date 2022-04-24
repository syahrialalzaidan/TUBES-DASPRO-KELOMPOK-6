def topup(user) : 
    #KAMUS LOKAL :
    #array_user : array of array of string
    #username : string
    #ammount : integer
    #found, valid,negatif : boolean

    #ALGORITMA

    #kalo mau ngambil data array buat csvnya, pake fungsi topup() karena return berupa array
    #misal x = topup(), maka x itu array "array_user" yang udah di update saldonya
    array_user  = user
    
    #mengubah data saldo menjadi integer
    for x in array_user :
        if x[0] == 'id':
            pass
        else:
            x[5] = int(x[5])
    
    #menerima input username dan saldo yang ingin ditambahkan     
    username = input('Masukan username: ')
    ammount = int(input('Masukkan saldo: '))
    found = False
    print()
    valid = True
    negatif = False 

    #Validasi apakah input valid
    for x in array_user :
        if x[0] == 'id':
            pass
        else:
            if username == x[1] :
                found = True 
                user = x
                if ammount < 0 : 
                    negatif = True
                    if (x[5] + ammount) < 0 :
                        valid = False
                    else :
                        x[5] += ammount
                else :
                    x[5] += ammount
    
    array_user[0][5] = array_user[0][5][:-1]


    #Mengeluarkan output berdasarkan hasil validasi
    if found and valid and not negatif:
        print('Top up berhasil. Saldo', user[2], 'bertambah menjadi', user[5] ) #BUAT NGASIH OUTPUT KE PENGGUNA
        return array_user
    elif found and valid and negatif :
        print('Top up berhasil. Saldo', user[2], 'berkurang menjadi', user[5] ) 
        return array_user
    elif valid and not found :
        print(f'Username "{username}" tidak ditemukan')
        return array_user
    else :
        print('Masukan tidak valid')
        return array_user
