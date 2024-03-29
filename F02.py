import fungsi
import B01
def cekusername(username):
    # Menginput sebuah string lalu mengeluarkan False jika string tidak kosong dan True jika string kosong
    # Kamus lokal
    # i : char
    for i in username:
        if ord(i) == 45 or ord(i) == 95 or 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
            return True
        else:
            return False


def register(data):
    # Fungsi merigister user baru dimasukan ke data
    # I.S. : data tidak kosong
 	# F.S. : procedur menginput data data untuk dimasukan dalam userbaru yang kemudian jika sudah divalidasi akan dimasukan dalam data
    # Kamus
    # nama : string
    # username : string
    # password : string
    # id : integer
    # userbaru : array [0..5] of string
    # Input nama
    nama = input("Masukan nama: ")

    # Input dan cek usernamenya sesuai kententuan atau tidak
    while True:
        username = input("Masukan username: ")
        if cekusername(username):
            break
        else:
            print("Masukan username salah ulangi!")

    # Input password
    password = input("Masukan password: ")
    password = B01.CaesarChiper("something", 7, password, "encoded")
    
    # Membuat ID baru
    id = int(data[-1][0]) + 1
    userbaru = [[str(id), username, nama, password, "User", "0"]]
    data = data + userbaru

    # Mencek apakah usernamenya sudah ada atau tidak
    if fungsi.caridatalist(data, 1, username) == []:
        print("Username " + username + " berhasil ditambahkan!")
        return data
    else:
        print("Username " + username + " sudah ada. Silahkan gunakan username lain!")
        return data
