from fungsi import count_csv_row,split

def topup() : 
    #kalo mau ngambil data array buat csvnya, pake fungsi topup() karena return berupa array
    #misal x = topup(), maka x itu array "array_user" yang udah di update saldonya

    #bikin array dari  user.csv
    array_user  = csv_to_array('user.csv')
    
    #data cleansing buat yang ada "\n"
    for x in array_user :
        if '\n' in x[5] :
            x[5] = int(x[5][:-1])
        else :
            x[5] = int(x[5])
    
    username = input('Masukan username: ')
    ammount = int(input('Masukkan saldo: '))
    found = False
    print()
    user = []
    valid = True
    for x in array_user :
        if x[4] == 'user' :
            if username == x[1] :
                found = True 
                user = x
                if ammount < 0 : 
                    if (x[5] + ammount) < 0 :
                        valid = False
                    else :
                        x[5] += ammount
                else :
                    x[5] += ammount
        else :
            pass


    if found and valid :
        print('Top up berhasil. Saldo', user[2], 'bertambah menjadi', user[5] ) #BUAT NGASIH OUTPUT KE PENGGUNA
        return array_user
    elif valid and not found :
        print(f'Username "{username}" tidak ditemukan')
        return array_user
    else :
        print('Masukan tidak valid')
        return array_user

# topup() bakal ngejalanin program sesuai prosedur tapi arraynya gak di save ke mana-mana
# array_user = topup() bakal ngejalanin program sesuai prosedur dan nyimpen value arraynya ke variabel "array_user" meskipun masukan tidak valid
