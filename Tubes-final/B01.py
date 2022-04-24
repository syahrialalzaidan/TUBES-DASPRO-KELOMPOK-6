def index(data, cek):
    # Fungsi untuk mencari indeks dari sebuah data pada suatu array
    # Kamus lokal
    # index : integer
    # i : integer
    index = 0
    for i in data:
        if i == cek:
            return index
        else:
            index += 1
    return -1


def CaesarChiper(kunci, shift, teks, tipe):
    # Fungsi mengubah suatu teks menjadi teks lain yang acak menrut kata kunci serta shiftnya, 
    # algoritma chiper ini mengikuti algoritma Keyed Caesar Chiper
    
    # Kamus lokal
    # alphabet : array of integer
    # keymaker : array of integer
    # indeks : integer
    # text : string
    # huruf : char
    # m : integer
    # hasil : string
    
    # indekshuruf : integer
    # Variabel yang akan digunakan
    alphabet = [i for i in range(26)]
    keymaker = [-1 for i in range(26)]
    indeks = 0
    kunci = kunci.lower()
    # Mengisi keymaker dengan kata kunci diawal, jika sudah ada huruf yang sama maka huruf tersebut dihapus
    while True:
        if kunci != "":
            # Menginput hurufnya ke keymaker dalam bentuk ascii
            huruf = kunci[0]
            keymaker[indeks] = ord(huruf)
            alphabet[ord(huruf) - 97] = -1
            text = ""

            # Menghapus huruf yang sama pada 'kunci'
            for k in kunci:
                if k != huruf:
                    text += k
                else:
                    continue
            kunci = text
            indeks += 1

        # Saat semua kata sudah dipakai
        else:
            break

    # Mengisi sisa dari keymaker dengan urutan alphabet
    for m in alphabet:
        if m == -1:
            continue
        else:
            keymaker[indeks] = m + 97
            indeks += 1

    hasil = ""
    # Jika ingin teks di encoded
    if tipe == "encoded":
        for m in teks:
            # Untuk huruf yang bukan alphabet
            if (ord(m) > 122 or ord(m) < 97) and (ord(m) < 65 or ord(m) > 90):
                hasil += m
            # Untuk yang alphabet
            else:
                # Mengubah nilai ascii huruf menjadi indeks agar bisa dicari hurufnya menjadi apa di keymaker
                if 97 <= ord(m) <= 122:
                    indekshuruf = ((ord(m) + shift) - 97) % 26
                else:
                    indekshuruf = ((ord(m) + shift) - 65) % 26

                # Mengambil ascii dari indeks keymaker
                huruf = chr(keymaker[indekshuruf])

                # Untuk huruf besar dilakukan kapital
                if 65 <= ord(m) <= 90:
                    huruf = huruf.upper()

                hasil += huruf

    # Untuk di decoded
    elif tipe == "decoded":
        for m in teks:
            # Diluar alphabet
            if (ord(m) > 122 or ord(m) < 97) and (ord(m) < 65 or ord(m) > 90):
                hasil += m
            else:
                # Mencari indeks dari huruf ascii pada keymaker
                if 97 <= ord(m) <= 122:
                    indekshuruf = (index(keymaker, ord(m))) - shift
                else:
                    indekshuruf = (index(keymaker, ord(m) + 32)) - shift

                # Mengubah angka indeks menjadi huruf
                if indekshuruf < 0:
                    huruf = chr(indekshuruf + 123)
                    if 65 <= ord(m) <= 90:
                        huruf = huruf.upper()
                else:
                    huruf = chr(indekshuruf + 97)
                    if 65 <= ord(m) <= 90:
                        huruf = huruf.upper()

                hasil += huruf
    return hasil
