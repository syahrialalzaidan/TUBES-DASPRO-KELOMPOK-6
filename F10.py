from fungsi import split

def output_f10(a, tahun, nomor) :
    print(str(nomor) + '.', end=' ') #ketemu
    nomor += 1

    for spek in a :
        if spek != tahun and spek != a[5] : 
            print(spek, end=' | ')
        elif spek == tahun :
            print(spek)
        else :
            pass
    
    

def search_my_game() : #data diambil dari file game.csv yang udah di sort berdasarkan id
    try :
        id = input('Masukkan ID Game: ')
        tahun = input('Masukkan Tahun Rilis Game: ')
        data = open('game.csv','r')
        nomor = 1
        found = False
        if id != '' and tahun != '' : 
            print('Daftar game pada inventory yang memenuhi kriteria: ')
            for x in data.readlines() :
                a = split(x)
                #ngatur ulang list biar sesuai yang diminta abangnya
                kategori = a[2]
                year = a[3]
                harga = a[4]
                a[2] = harga 
                a[3] = kategori
                a[4] = year

                if a[0] == id and a[4] == tahun :
                    found = True
                    output_f10(a,tahun, nomor)
                else :
                    continue
            if not found :
                print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
        

    except :
        pass
    else :
        if id == '' and tahun != '' :
            nomor = 1
            found = False
            print('Daftar game pada inventory yang memenuhi kriteria: ')
            for x in data.readlines() :
                a = split(x)
                #ngatur ulang list biar sesuai yang diminta abangnya
                kategori = a[2]
                year = a[3]
                harga = a[4]
                a[2] = harga 
                a[3] = kategori
                a[4] = year

                if a[4] == tahun :
                    found = True
                    output_f10(a,tahun, nomor)    
                    nomor += 1
                else :
                    continue
            if not found :
    
                print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
        
        elif tahun == '' and id != '': 
            nomor = 1
            found = False
            print('Daftar game pada inventory yang memenuhi kriteria: ')
            for x in data.readlines() :
                a = split(x)
                #ngatur ulang list biar sesuai yang diminta
                kategori = a[2]
                year = a[3]
                harga = a[4]
                a[2] = harga 
                a[3] = kategori
                a[4] = year

                if a[0] == id :
                    found = True
                    output_f10(a,tahun, nomor)
                    nomor += 1
        
                else :
                    continue
            if not found :
                print('Tidak ada game pada inventory-mu yang memenuhi kriteria')

        elif tahun == '' and id == '' :
            nomor = 1
            print('Daftar game pada inventory yang memenuhi kriteria: ')
            for x in data.readlines() :
                a = split(x)
                #ngatur ulang list biar sesuai yang diminta abangnya
                if a[0] != 'id' : 
                    kategori = a[2]
                    year = a[3]
                    harga = a[4]
                    a[2] = harga 
                    a[3] = kategori
                    a[4] = year

                    output_f10(a ,year, nomor) 
                    nomor += 1   
        else :
            pass

search_my_game()