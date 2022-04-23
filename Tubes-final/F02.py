import fungsi
import B01
def cekusername(username):
    for i in username:
        if ord(i) == 45 or ord(i) == 95 or 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
            continue
        else:
            return False
    return True


def register(data):
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
 
    # Mencek apakah usernamenya sudah ada atau tidak
    if not(fungsi.caridatalist(data, 1, username)):
        data = data + userbaru
        return data
    else:
        print("Username " + username + " sudah ada. Silahkan gunakan username lain!")
