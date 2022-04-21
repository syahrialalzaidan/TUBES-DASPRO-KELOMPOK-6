from fungsi import csv_to_array, split, count_csv_column,count_csv_row, samecount
username = input('Masukkan Username: ') #kalo belom diinput dan kalo udah ada berarti harus ganti variabel di fungsinya

def search_my_game() :
    inventory = csv_to_array('kepemilikan.csv')
    data_game = csv_to_array('game.csv')
    nomor = 1
    #nyari game yang dimiliki 
    my_game = []
    found = False
    for x in inventory :
        if username == x[1] :
            my_game += [x[0]]

    try :
        id = input('Masukan ID Game: ')
        tahun = input('Masukkan Tahun Rilis Game: ')
        if id != '' and tahun != '' :
            if id in my_game :
                for x in data_game :
                    if x[0] == id and x[3] == tahun :
                        found = True
                        print(f'{nomor}. {(x[0])}   | {(x[1])} | {(x[4])}    | {(x[2])} | {(x[3])}')
                        nomor += 1

            if not found :
                print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
    except :
        pass
    else :
        if id == '' and tahun != '' :
            for x in data_game :
                if x[3] == tahun :
                    found = True
                    print(f'{nomor}. {(x[0])}   | {(x[1])} | {(x[4])}    | {(x[2])} | {(x[3])}')
                    nomor += 1
            if not found :
                print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
            
        elif id != '' and tahun == '' :
            if id in my_game :
                for x in data_game :
                    if x[0] == id :
                        found = True
                        print(f'{nomor}. {(x[0])}   | {(x[1])} | {(x[4])}    | {(x[2])} | {(x[3])}')
                        nomor += 1
            if not found :
                print('Tidak ada game pada inventory-mu yang memenuhi kriteria')
                    
        
        elif id == '' and tahun == '' :
            for x in data_game :
                if x[0] in my_game :
                    print(f'{nomor}. {(x[0])}   | {(x[1])} | {(x[4])}    | {(x[2])} | {(x[3])}')
                    nomor += 1
        else :
            pass
# search_my_game()
