def search_my_game(username,game,kepemilikan) :
    #KAMUS LOKAL
    #nomor  : integer
    #my_game : array of string
    #id : string
    #tahun : string
    #found,punya : Boolean


    #ALGORITMA
    nomor = 1
    #nyari game yang dimiliki 
    my_game = []
    found = False
    for x in kepemilikan :
        if username == x[1] :
            my_game += [x[0]]

    #memakai try karena berpotensi menerima input kosong
    try :
        id = input('Masukan ID Game: ')
        tahun = input('Masukkan Tahun Rilis Game: ')
        if id != '' and tahun != '' :
            #menentukan apakah punya atau tidak melalui looping
            punya = False
            for x in my_game :
                if x == id :
                    punya = True
            if punya :
                for x in game :
                    if x[0] == id and x[3] == tahun :
                        found = True
                        #mengeluarkan output sesuai yang diminta
                        print(f'{nomor}. {(x[0])}   | {(x[1])} | {(x[4])}    | {(x[2])} | {(x[3])}')
                        nomor += 1

            if not found :
                print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
    except :
        pass
    else :
        if id == '' and tahun != '' :
            #memfilter tiap game yang ada di toko
            for x in game :
                #menentukan kepemilikan game
                punya = False
                for y in my_game :
                    if x[0] == y :
                        punya = True
                if punya :
                    if x[3] == tahun :
                        found = True
                        print(f'{nomor}. {(x[0])}   | {(x[1])} | {(x[4])}    | {(x[2])} | {(x[3])}')
                        nomor += 1
            if not found :
                print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
            
        elif id != '' and tahun == '' :
            #menentukan kepemilikan game
            punya = False
            for x in my_game :
                if x == id :
                    punya = True
            if punya  :
                for x in game :
                    if x[0] == id :
                        found = True
                        print(f'{nomor}. {(x[0])}   | {(x[1])} | {(x[4])}    | {(x[2])} | {(x[3])}')
                        nomor += 1
            if not found :
                print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
                    
        
        elif id == '' and tahun == '' :
            for x in game :
                punya = False
                for y in my_game :
                    if x[0] == y :
                        punya = True
                if punya : #if x[0] in my_game :
                    print(f'{nomor}. {(x[0])}   | {(x[1])} | {(x[4])}    | {(x[2])} | {(x[3])}')
                    nomor += 1
        else :
            pass
# search_my_game()
