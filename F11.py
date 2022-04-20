from fungsi import split

def format_f11(x) : #ngeformat list biar sesuai output di f11
    a = split(x)
    kategori = a[2]
    year = a[3]
    harga = a[4]
    a[2] = harga 
    a[3] = kategori
    a[4] = year
    return a

def output_f11(a, n, nomor) :
    print(str(nomor) + '.', end=' ') #ketemu
    
    if n == 1: 
        for spek in a :
            if spek != a[5] : 
                print(spek, end=' | ')
                nomor +=1 
            else :
                print(spek, end='')
                nomor += 1
    else :
        for spek in a :
            if spek != a[5] : 
                print(spek, end=' | ')
            else :
                print(spek)

def search_game_at_store () :
    try :
        data = open('game.csv', 'r')
        nomor = 1
        found = False 
        spek_game = ['' for x in range(5)]
        kosong =  ['' for x in range(5)]
        spek_game[0] = input('Masukkan ID Game: ')
        spek_game[1] = input('Masukkan Nama Game: ')
        spek_game[2] = input('Masukkan Harga Game: ')
        spek_game[3] = input('Masukkan Kategori Game: ')
        spek_game[4] = input('Masukkan Tahun Rilis Game: ')
        print('Daftar game pada toko yang memenuhi kriteria: ')
        if '' not in spek_game :
            for x in data.readlines() :
                a = format_f11(x)
                b = ['' for x in range(5)]
                for x in range(5) :
                    b[x] = a[x]
                
                if b == spek_game :
                    found = True
                    output_f11(a, 2,nomor)
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
                    a = format_f11(x)
                    output_f11(a, 1, nomor)
                    nomor += 1
        elif '' in spek_game : 
            for x in data.readlines() :
                a = format_f11(x)
                b = ['' for x in range(5)]

                for i in range(5) :
                    b[i] = a[i]
                sama = True 

                for y in range(5) :
                    if spek_game[y] == '' :
                        continue
                    else :
                        if spek_game[y] == b[y] :
                            continue
                        else :
                            sama = False
                if sama :
                    found = True
                    output_f11(a, 1, nomor)
            if not found :
                print('Tidak ada game pada toko yang memenuhi kriteria')
search_game_at_store()