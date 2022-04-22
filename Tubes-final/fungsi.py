def inputdata(file, data):
# Kalau ada yang punya ide buat input data di line baru boleh ubah aja
# File: tempat filenya (string cth:"user.csv"), data : isi data yang mau dimasukin (string udah dipisah pake ';')
# data yang diinput berupa teks yang sudah dipisah dengan koma
    folder = open(file, "a")
    folder.write("\n" + data)
    folder.close()


def caridata(file,urutan,cek):
    # Ini kalau misalnya datanya engga ketemu bakal ngeluarin teks yang engga ketemu
    # File: tempat filenya (string cth:"user.csv")
    # Urutan : integer (nah kan nanti tuh si teks per line dari filenya di split terus teksnya berubah jadi matriks,
    #                   si urutan ini tuh nandain indeks data yang dicari di bagian mana, dimulai dari 0)
    # cek : string (fungsi ini tuh awalnya buat nyari data yang elemennya sama kek password sama username, jadi ada ini
    #               kalau misalnya banyak fungsi yang engga perlu pake variabel ini bilang aja)
    # Keluarannya list
    folder = open(file, "r")
    for a in folder.readlines():
        b = split(a)
        if b[urutan] == cek:
            return b
        else:
            continue
    return "tidak ketemu bang"


def split(a):   # Note kalau misalnya nginput datanya pake fungsi input data si '\n' kebawa di elemen list terakhir
    # a : string yang dipisah ';'
    # keluaran list
    total = 0
    for i in a:
        if i == ";":
            total += 1
        else:
            continue
    hasil = ["" for i in range(total+1)]
    teks = ""
    k = 0
    for j in a:
        if j == ";":
            hasil[k] = teks
            k += 1
            teks = ""
        else:
            teks += j
    hasil[k] = teks
    return hasil

# Kalo ga salah, length gitu gabisa jd make ini aja
def length(array):
   ## initializing the count to 0
   sum = 0
   for char in array:
      sum += 1
   return sum

# Baru kalo mau make tambahan buat append make + aja
# semisalnya A = [1,2,3,4], B = [5] langsung A + B

def count_csv_row(file) : 
    data = open(file, 'r')
    row = 0 
    for a in data.readlines():
        row += 1
    return row   #ini include header

def count_csv_column(file) :
    data = open(file, 'r')
    column = 0 
    b = split(data.readlines()[0])
    for x in b:
        column += 1
    return column

def caridatalist(data,urutan,cek):
# Kaya fungsi caridata tapi buat di matiksnya
    for i in range(length(data)):
        if data[i][urutan] == cek:
            return data[i]
        else:
            continue
    return []


def indeksdata(data, urutan, cek):
# Nyari indeksnya
    indeks = 0
    for i in range(length(data)):
        if data[i][urutan] == cek:
            return indeks
        else:
            indeks += 1
    return (-1)

def csv_to_array(x) :
    #bikin array dari  user.csv
    file = open(x, 'r')
    array_user = [['' for x in range(count_csv_column(x))] for i in range(count_csv_row(x))]
    i = 0 
    kolom = count_csv_column(x)

    #csv to array
    for x in file.readlines() :
        array_user[i] = split(x)
        i += 1
    
    #data cleansing buat yang ada "\n"
    for x in array_user :
        if x !=  array_user[-1] :
            x[kolom-1] = (x[kolom-1][:-1])
        else :
            continue

    return array_user

# Biar jumlah huruf nya diakalin sama
# Ini terpake untuk Fungsi09 biar output nya rapi
def samecount(kata):
    panjangkata = length(kata)
    A = ['' for i in range (panjangkata)]
    for i in range(panjangkata): 
        A[i] = kata[i]

    if panjangkata < 20: 
        sisa_kata = 20 - panjangkata 
        # Buat matriks baru yang berisi " " sebanyak panjang data
        kosong = [" " for j in range(sisa_kata)]
        for j in range(sisa_kata):
            kosong[j] = " "
        
        kata_baru = A + kosong 
        keluaran = ''
        for char in kata_baru: 
            keluaran += char
    return keluaran 

# Validasi Role
# data_user = csv_to_array('user.csv')
# datagame = csv_to_array('game.csv')
# data_kepemilikan = csv_to_array('kepemilikan.csv')

# def cekRole(username): 
#   for i in range(1,length(data_user)):
#     if (data_user[i][1]) == username:
#       return(data_user[i][4])

# def isAdmin(username):
#   if cekRole(username) == "Admin":
#     return True 
#   else:
#     return False


# def isUser(username):
#   if cekRole(username) == "User":
#     return True 
#   else:
#     return False

