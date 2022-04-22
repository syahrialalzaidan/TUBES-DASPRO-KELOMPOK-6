import fungsi
import B01


def login(data):
    # Input usename, password, serta data usernamnya
    username = input("Masukan username: ")
    password = input("Masukan password: ")
    datauser = fungsi.caridatalist(data, 1, username)

    # Mencek apakah usernamenya ada atau tidak
    if not datauser:
        print("Username tidak ditemukan!")
        return [[False],[]]

    # Mencek password
    else:
        if B01.CaesarChiper("something", 7, datauser[3], "decoded") == password:
            print("Halo " + username + "! Selamat datang di 'BNMO'! ")
            return [[True], datauser]
        else:
            print("Password Salah!")
            return [[False], datauser]
