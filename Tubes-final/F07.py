import fungsi
def outputF07(array):
    # Buat nyetak array-nya
    for i in array:
        teks = ""
        for j in range(6):
            if j == 5:
                teks += i[5]
            else:
                teks += i[j] + " | "
        print(teks)
    return


def bagianTeks(teks, urutAwal, urutAkhir):
    # Buat ngambil bagian dari sebuah teks
    hasil = ""
    for i in range(urutAwal, (urutAkhir + 1)):
        hasil += teks[i]
    return hasil


def list_game_toko(data):
    # Mengcopy isi dari game
    datacopy = []
    for isi in data:
        datacopy += [isi]
        
    # Menginput skema sortingnya
    skema = input("Skema sorting: ").lower()

    # Kalau kosong, langsung print semua (harusnya list 'data' udah terurut ID nya)
    if skema == "":
        outputF07(datacopy)
        return

    else:
        # Buat skema sorting tahun (yang dilihat indeks tahunnya)
        if bagianTeks(skema, 0, (fungsi.length(skema) - 2)).lower() == "tahun":
            indeks = 3

        # Buat skema sorting harga (yang dilihat indeks harganya)
        elif bagianTeks(skema, 0, (fungsi.length(skema) - 2)).lower() == "harga":
            indeks = 4

        # Kalau skema sorting salah
        else:
            print("Skema sorting tidak valid! ")
            return

        # Skema sorting (liat dari edunex :v)
        n = fungsi.length(datacopy)
        for i in range(1, n-1):
            # Buat sorting yang naik (cari indeks yang nilai min dimana)
            if skema[-1] == "+":
                kecilbesar = i
                for j in range(i+1, n):
                    if int(datacopy[j][indeks]) < int(datacopy[kecilbesar][indeks]):
                        kecilbesar = j
                    else:
                        continue

            # Buat sorting yang turun (cari indeks yang nilai maks dimana)
            elif skema[-1] == "-":
                kecilbesar = i
                for k in range(i+1, n):
                    if int(datacopy[k][indeks]) > int(datacopy[kecilbesar][indeks]):
                        kecilbesar = k
                    else:
                        continue

            # Kalau skema sorting salah
            else:
                print("Skema sorting tidak valid !")
                return

            # Tukeran data
            temp = datacopy[kecilbesar]
            datacopy[kecilbesar] = datacopy[i]
            datacopy[i] = temp

        # output data
        outputF07(datacopy)

    return
