# Fungsi load
# Fungsi yang akan mengecek folder yang diberikan untuk memulai program. Dijalankan automatis ketika program dijalankan

# KAMUS
# folder : boolean

# ALGORITMA
def load():
  # Mengimport argparse yang akan digunakan untuk membaca masukan pengguna melalui terminal
  import argparse 
  parser = argparse.ArgumentParser()
  # Menerima input berupa nama folder
  parser.add_argument("nama_folder", nargs="?", help="Masukkan nama folder", type=str)
  args = parser.parse_args()

  # Mengimport os yag akan digunakan untuk validasi folder
  import os.path
  from os import path 

  folder = False
  # Validasi folder
  if args.nama_folder is None: # jika pengguna tidak memasukkan nama folder
    print("Tidak ada nama folder yang diberikan!")
    print("Usage: python program_binomo.py <nama_folder>")
    return folder
  else: # jika pengguna memasukkan nama folder, akan dicek apakah folder ada atau tidak
    if path.isdir(args.nama_folder): # jika folder ada 
      print("Loading...")
      print('Selamat datang di antarmuka "Binomo"')
      os.chdir("./{}".format(args.nama_folder)) # Pindah folder
      folder = True
      return folder
    else: # jika nama folder yang diberikan pengguna tidak ada
      print("Folder {} tidak ditemukan.".format(args.nama_folder))
      return folder
