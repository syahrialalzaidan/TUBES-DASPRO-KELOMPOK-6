# Fungsi exit
# Fungsi yang akan menghentikan program setelah jawaban yang diterima benar. Jika jawaban = y, akan dilakukan save sebelum keluar, jika jawaban = n, tidak dilakukan save sebelum keluar.

# KAMUS
# jawaban : character

# ALGORITMA
# Validasi jawaban
import os
def exit(dataGame, dataKepemilikan, dataRiwayat, dataUser): 
  while True:
    jawaban = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if jawaban == 'y' or jawaban == 'Y' or jawaban == 'n' or jawaban == 'N':
      break
  from F16 import save
  # Pemrosesan jawaban
  if jawaban == 'y' or jawaban == 'Y':
    save(dataGame, dataKepemilikan, dataRiwayat, dataUser)
    os.chdir("..")
    quit()
  else: # jawaban == 'n' or jawaban == 'N'
    # langsung exit
    os.chdir("..")
    quit()
    
