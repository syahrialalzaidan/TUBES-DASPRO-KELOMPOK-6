from fungsi import length, count_csv_row

history = ['' for x in range(count_csv_row('game.csv'))]
# username_terbaru = input()
def idUser (username, datauser):
  for i in range(length(datauser)):
    if datauser[i][1] == username:
      return(datauser[i][0])

def indexUser(username, datauser):
    for i in range(length(datauser)):
      if datauser[i][1] == username:
        return i

def buy_game(username, datagame, datauser, datakepemilikan):
  IDgame = input("Masukkan ID Game: ")
  # Validasi ID
  valid = False
  for i in range(length(datagame)):
    if datagame[i][0] == IDgame:
      valid = True
      # Validasi sudah ada di kepemilikan atau bukan 
      # Berarti membutuhkan ID dari si user 
      IDuser = idUser(username, datauser)
      indeksUser = indexUser(username, datauser)
      # Validasi di Kepemilikan 
      # Buat array menampung semua game dimiliki user

      game_own = False
      for i in range(1,length(datakepemilikan)):
        if datakepemilikan[i][1] == IDuser and datakepemilikan[i][0] == IDgame:
          game_own = True 
      
      # Validasi bahwa Saldo Cukup
      # Mengambil saldo dari user 
      saldoUser = datauser[indeksUser][5]
      saldoUser = int(saldoUser) # Jadikan integer

      # Cek Harga Game
      for i in range(length(datagame)):
        if datagame[i][0] == IDgame: 
          hargaGame = datagame[i][4]
          hargaGame = int(hargaGame)
          stock = datagame[i][5]
          stock = int(stock) # Jadikan integer
          nama = datagame[i][1]

      # Mencari semua kemungkinan
      if valid == True and game_own == False and saldoUser>hargaGame and stock > 0:
        print(f"Game {nama} berhasil dibeli")
        #masukin ke list history
        i = 0 
        while True :
          if history[i] == '' :
            history[i] = IDgame
            break
          else :
            i += 1
        
        # Masukkan data ke array
        datakepemilikan = datakepemilikan + [[IDgame, IDuser]]
        # Mengurangi saldo user
        datauser[int(IDuser)][5] = int(datauser[int(IDuser)][5]) - hargaGame
        
      elif game_own == True:
        print("Anda sudah memiliki Game tersebut")
      elif saldoUser - hargaGame < 0 :
        print("Saldo anda tidak cukup untuk membeli Game tersebut")
      elif stock < 0:
        print("Stock Game tersebut sedang habis!")
      else: # Banyak kondisi tak terpenuhi
        print("Tidak ada kemungkinan membeli game")
  if valid == False:
    print("Tidak ada Game yang sesuai")
  
  return datauser, datakepemilikan
