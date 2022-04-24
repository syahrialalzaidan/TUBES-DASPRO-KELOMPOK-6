# Fungsi save
# Fungsi yang melakukan penyimpanan data ke file dalam suatu folder 

# KAMUS
# nama_folder : string
# fileGame = SEQFILE of gameData
# fileKepemilikan = SEQFILE of kepemilikanData
# fileRiwayat = SEQFILE of historyData
# fileUser = SEQFILE of userData

# ALGORITMA
def save(dataGame, dataKepemilikan, dataRiwayat, dataUser):
  from fungsi import length
  import os
  from os import path  

  # Cek folder
  def cekFolder(nama_folder):
    # Fungsi yang mengecek apakah folder ada atau tidak. Jika tidak ada, maka fungsi ini akan membuat folder sesuai dengan nama folder yang dimasukkan pengguna
    # KAMUS LOKAL
    # ALGORITMA
    if not(path.isdir(nama_folder)):
      os.mkdir(nama_folder)

  # Cek file 
  def cekFile(nama_folder):
    # Fungsi yang mengecek keberadaan file. Jika tidak ada file, maka fungsi ini akan mengembalikan nilai false. Jika ada file, fungsi akan mengembalikan nilai true
    # KAMUS LOKAL
    # files : array of string
    # ALGORITMA
    for (root, dirs, files) in os.walk(nama_folder, topdown=True):
      if files == ['game.csv', 'kepemilikan.csv', 'riwayat.csv', 'user.csv']:
        return True
      else: 
        return False

  def saveFile(arrData, fileData):
    # Fungsi yang melakukan save pada file masing-masing
    # KAMUS LOKAL
    # i : integer (untuk array indeks)
    # ALGORITMA
    for i in range(length(arrData)):
      for data in arrData[i]:
        if data == arrData[i][0]:
          fileData.write(str(data))
        else:
          fileData.write(";{}".format(str(data)))
      if arrData[i] != arrData[-1]:
        fileData.write('\n')

  # Menerima masukan pengguna berupa nama folder dan melakukan validasi folder
  os.chdir("..")
  nama_folder = input("Masukkan nama folder penyimpanan: ")
  cekFolder(nama_folder)

  # Folder sudah pasti ada

  if cekFile(nama_folder): # file sudah ada di folder dan harus dihapus 
    os.remove("{}/game.csv".format(nama_folder))
    os.remove("{}/kepemilikan.csv".format(nama_folder))
    os.remove("{}/riwayat.csv".format(nama_folder))
    os.remove("{}/user.csv".format(nama_folder))

  # Buat file dan save data 
  fileGame = open("{}/game.csv".format(nama_folder), 'w')
  fileKepemilikan = open("{}/kepemilikan.csv".format(nama_folder), 'w')
  fileRiwayat = open("{}/riwayat.csv".format(nama_folder), 'w')
  fileUser = open("{}/user.csv".format(nama_folder), 'w')

  # Melakukan save data pada file
  saveFile(dataGame, fileGame)
  saveFile(dataKepemilikan, fileKepemilikan)
  saveFile(dataRiwayat, fileRiwayat)
  saveFile(dataUser, fileUser)
  
  # Menutup file
  fileGame.close()
  fileKepemilikan.close()
  fileRiwayat.close()
  fileUser.close()  

  os.chdir("./{}".format(nama_folder))
  
  # Menampilkan pesan feedback
  print("saving...")
  print("Data telah disimpan pada folder {}".format(nama_folder))
