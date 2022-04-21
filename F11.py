from fungsi import split,samecount

def search_game_at_store () :
    try :
        data = open('game.csv', 'r')
        nomor = 1
        found = False 
        spek_game = ['' for x in range(5)]
        kosong =  ['' for x in range(5)]
        spek_game[0] = input('Masukkan ID Game: ')
        spek_game[1] = input('Masukkan Nama Game: ')
        spek_game[4] = input('Masukkan Harga Game: ')
        spek_game[2] = input('Masukkan Kategori Game: ')
        spek_game[3] = input('Masukkan Tahun Rilis Game: ')
        print('Daftar game pada toko yang memenuhi kriteria: ')
        if '' not in spek_game :
            for x in data.readlines() :
                a = split(x)
                b = ['' for x in range(5)]
                for x in range(5) :
                    b[x] = a[x]
                
                if b == spek_game :
                    found = True
                    print(f'{nomor}. {samecount(a[0])}  | {samecount(a[1])} | {samecount(a[2])} | {samecount(a[3])} | {samecount(a[4])} | {samecount(str(a[5][:-1]))}')
                    nomor += 1
            if not found :
                print('Tidak ada game pada toko yang memenuhi kriteria')
    except :
        pass

    else :
        if spek_game == kosong :
            for x in data.readlines() :
                a = split(x)
                #ngatur ulang list biar sesuai yang diminta abangnya
                if a[0] != 'id' : 
                    print(f'{nomor}. {(a[0])}  | {(a[1])} | {(a[4])} | {(a[2])} | {(a[3])} | {(str(a[5][:-1]))}')  #kalo ini dipakein samecount jadi error
                    nomor += 1
        elif '' in spek_game : 
            for x in data.readlines() :
                a = split(x)
                b = ['' for x in range(5)]

                for i in range(5) :
                    b[i] = a[i]
                sama = True 

                for y in range(5) :
                    if spek_game[y] == '' :
                        continue
                    else :
                        if spek_game[y] in b :
                            continue
                        else :
                            sama = False
                if sama :
                    found = True
                    print(f'{nomor}. {(a[0])}  | {(a[1])} | {(a[2])} | {(a[3])} | {(a[4])} | {(str(a[5][:-1]))}')
                    nomor += 1
            if not found :
                print('Tidak ada game pada toko yang memenuhi kriteria')


search_game_at_store()
