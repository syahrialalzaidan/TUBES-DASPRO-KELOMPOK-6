import time
# Nama program
# Kamus


# Algoritma
def kerangajaib():
    # Mengenrate angka yang random (diambil dari waktunya)
    waktu = time.time_ns() // 1000
    angka_random = (11 * waktu + 20) % 10

    # Pertanyaan dan jawaban
    input("Apa pertanyaan mu? ")
    jawaban = ["Boleh jadi", "Bisa jadi", "Mungkin", "Sepertinya", "Siapa tau", "Bisa saja", "Mungkin iya", "Mungkin tidak",
               "Entahlah", "Tidak tau"]
    print(jawaban[angka_random])
