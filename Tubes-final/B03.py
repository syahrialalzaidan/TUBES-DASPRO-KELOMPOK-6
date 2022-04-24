def tictactoe():
    # I.S. : -
	# F.S. : procedur untuk melakukan permainan tictactoe dan setiap giliran akan mencetak kondisi papan
    # Kamus lokal
    # papan : array of array of string
    # simbol : char
    # i,j,k,m : integer
    # x : integer
    # y : integer

    papan = [["#", "#", "#"], ["#", "#", "#"], ["#", "#", "#"]]

    # Informasi awal
    print("Legenda:")
    print("# Kosong \nX Pemain 1 \nO Pemain 2")
    print("X dan Y bernilai [1,3]\n")
    print("Status papan: \n###\n###\n###")


    # Pengulangan
    for k in range(10):
        # Pergantian giliran
        if k == 9:
            print("Seri. Tidak ada pemenang")
            return
        elif k % 2 == 0:
            simbol = 'X'
        else:
            simbol = 'O'

        # Menginput isi papan
        while True:
            print("Giliran pemain " + simbol)
            x = int(input("X: "))
            y = int(input("Y: "))
            # Kalau input tidak valid
            if x < 1 or x > 3 or y < 1 or y > 3:
                print("Kotak tidak valid")
                continue
            # Kalau papannya udah keisi
            elif papan[y - 1][x - 1] != "#":
                print("Kotak sudah terisi")
                continue
            # Kalau aman
            else:
                papan[y - 1][x-1] = simbol
                break

        # Mencetak papan
        for i in range(3):
            teks = ""
            for j in range(3):
                teks += papan[i][j]
            print(teks)

        # Cek vertikal dan horizontal
        for m in range(3):
            if (papan[m][0] == simbol and papan[m][1] == simbol and papan[m][2] == simbol) or \
                    (papan[0][m] == simbol and papan[1][m] == simbol and papan[2][m] == simbol):
                print("Pemenangnya " + simbol)
                return
            else:
                continue
            # Cek diagonal ke kanan bawah dan kiri bawah
        if (papan[0][0] == simbol and papan[1][1] == simbol and papan[2][2] == simbol) or \
                (papan[0][2] == simbol and papan[1][1] == simbol and papan[2][0] == simbol):
            print("Pemenangnya " + simbol)
            return
        else:
            continue
