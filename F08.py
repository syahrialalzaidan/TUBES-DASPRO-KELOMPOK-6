from HelperFunction import data_user,length, datagame,isUser,data_kepemilikan
from fungsi import count_csv_row

history = ['' for x in range(count_csv_row('game.csv'))]
username_terbaru = input()
def idUser (username):
  for i in range(length(data_user)):
    if data_user[i][1] == username:
      return(data_user[i][0])

def indexUser(username):
    for i in range(length(data_user)):
      if data_user[i][1] == username:
        return i

def buy_game():
  if isUser(username_terbaru):
    IDgame = input()
    # Validasi ID
    valid = False
    for i in range(length(datagame)):
      if datagame[i][0] == IDgame:
        valid = True
        # Validasi sudah ada di kepemilikan atau bukan 
        # Berarti membutuhkan ID dari si user 
        IDuser = idUser(username_terbaru)
        indeksUser = indexUser(username_terbaru)
        # Validasi di Kepemilikan 
        # Buat array menampung semua game dimiliki user

        game_own = False
        for i in range(1,length(data_kepemilikan)):
          if data_kepemilikan[i][1] == IDuser and data_kepemilikan[i][0] == IDgame:
            game_own = True 
        
        # Validasi bahwa Saldo Cukup
        # Mengambil saldo dari user 
        saldoUser = data_user[indeksUser][5]
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
  else:
    print("Anda tidak bisa membuka menu ini!")
  return "-------------------------------------"
print(buy_game())
