from fungsi import samecount

def search_game_at_store (game) :
    #KAMUS LOKAL
    #nomor : integer
    #found, lengkap, sebagian : boolean
    #spek_game,kosong : array of string
    
    #ALGORITMA
    try :
        #Deklarasi variabel yang diperlukan
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
        
        #Menentukan status input lengkap atau sebagian atau tidak keduanya
        lengkap = True
        sebagian = False
        for x in spek_game :
            if x == '' :
                lengkap = False
            else :
                sebagian = True
        
        #kondisi ketika input lengkap
        if lengkap :
            for a in game :
                b = ['' for x in range(5)]
                for x in range(5) :
                    b[x] = a[x]
                
                if b == spek_game :
                    found = True
                    print(f'{nomor}. {samecount(a[0])}  | {samecount(a[1])} | {samecount(a[4])} | {samecount(a[2])} | {samecount(a[3])} | {samecount(str(a[5][:-1]))}')
                    nomor += 1
            if not found :
                print('Tidak ada game pada toko yang memenuhi kriteria')
    except :
        pass

    else :
        #Ketika input kosong
        if spek_game == kosong :
            for a in game :
                #ngatur ulang list biar sesuai yang diminta abangnya
                if a[0] != 'id' : 
                    print(f'{nomor}. {(a[0])}  | {(a[1])} | {(a[4])} | {(a[2])} | {(a[3])} | {(str(a[5][:-1]))}')  #kalo ini dipakein samecount jadi error
                    nomor += 1

        #ketika input diisi sebagian            
        elif sebagian and not lengkap : 
            for a in game :
                b = ['' for x in range(5)]

                for i in range(5) :
                    b[i] = a[i]
                sama = True 

                for y in range(5) :
                    if spek_game[y] == '' :
                        continue
                    else :
                        nemu_b = False 
                        for x in b :
                            if x == spek_game[y] :
                                nemu_b = True
                        if nemu_b :
                            continue
                        else :
                            sama = False
                if sama :
                    found = True
                    print(f'{nomor}. {(a[0])}  | {(a[1])} | {(a[4])} | {(a[2])} | {(a[3])} | {(str(a[5][:-1]))}')
                    nomor += 1
            if not found :
                print('Tidak ada game pada toko yang memenuhi kriteria')


#search_game_at_store()
