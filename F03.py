import fungsi


def login(data):
    # Input usename, password, serta data usernamnya
    username = input("Masukan username: ")
    password = input("Masukan password: ")
    datauser = fungsi.caridatalist(data, 1, username)

    # Mencek apakah usernamenya ada atau tidak
    if not datauser:
        print("Username tidak ditemukan!")
        return False

    # Mencek password
    else:
        if datauser[3] == password:
            print("Halo " + username + "! Selamat datang di 'BNMO'! ")
            return [[True], datauser]
        else:
            print("Password tidak ditimeukan")
            return [[False], datauser]
