from fungsi import length, csv_to_array


def ubah_stok(gamecsv):
  datagame = csv_to_array(gamecsv)
  # Mengambil
  ID = input("Masukkan ID Game: ")
  Jumlah = int(input("Masukkan jumlah: "))

  # Validasi ID 
  idBenar = False
  for i in range(length(datagame)):
    if datagame[i][0] == ID:
      idBenar = True
      indeksID = i 

  if idBenar: 
    if Jumlah > 0:
      print(f"Stock game {datagame[indeksID][1]} berhasil ditambahkan. Stock sekarang: {int(datagame[indeksID][5])+Jumlah}")
      datagame[indeksID][5] = int(datagame[indeksID][5]) + Jumlah
    else:
      if int(datagame[indeksID][5]) + Jumlah >= 0:
        print(f"Stock game {datagame[indeksID][1]} berhasil dikurangi. Stock sekarang: {int(datagame[indeksID][5]) + Jumlah}")
        datagame[indeksID][5] = int(datagame[indeksID][5]) + Jumlah
      else:
        print(f"Stock game {datagame[indeksID][1]} gagal dikurangi karena stock kurang. Stock sekarang: {str(datagame[indeksID][5])} (< {-1*(Jumlah)})")
  else: 
    print("Tidak ada game dengan ID tersebut") 
    
  return datagame 
