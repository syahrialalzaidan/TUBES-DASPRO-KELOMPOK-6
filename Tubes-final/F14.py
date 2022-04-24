# Fungsi help 
# fungsi yang menampilkan panduan penggunaan sistem. Tidak perlu melakukan login terlebih dahulu untuk menggunakan fungsi ini

# KAMUS
# role : string

# ALGORITMA
def helpSetelahLogin(role):
  if role == "Admin":
    print("========== HELP ==========")
    print("1. register - Untuk mendaftarkan user baru")
    print("2. login - Untuk melakukan login ke dalam sistem")
    print("3. tambah_game - Untuk menambahkan game ke dalam toko")
    print("4. ubah_game - Untuk mengubah informasi game pada toko")
    print("5. ubah_stok - Untuk mengubah stok game pada toko")
    print("6. list_game_toko - Untuk menampilkan daftar game pada toko")
    print("7. search_game_at_store - Untuk mencari game pada toko sesuai dengan parameter yang dimasukkan")
    print("8. topup - Untuk menambahkan saldo ke pada user")
    print("9. help - Untuk menampilkan panduan penggunaan sistem")
    print("10. kerangajaib - Untuk mendapatkan jawaban dari segala pertanyaan")
    print("11. tictactoe - Untuk bermain tictactoe")
  else: #role == "user"
    print("========== HELP ==========")
    print("1. login - Untuk melakukan login ke dalam sistem")
    print("2. list_game_toko - Untuk menampilkan daftar game pada toko")
    print("3. buy_game - Untuk membeli game")
    print("4. list_game - Untuk menampilkan daftar game yang dimiliki user")
    print("5. search_my_game - Untuk mencari game yang dimiliki user sesuai dengan parameter yang dimasukkan")
    print("6. search_game_at_store - Untuk mencari game pada toko sesuai dengan parameter yang dimasukkan")
    print("7. riwayat - Untuk menampilkan riwayat pembelian")
    print("8. help - Untuk menampilkan panduan penggunaan sistem")
    print("9. kerangajaib - Untuk mendapatkan jawaban dari segala pertanyaan")
    print("10. tictactoe - Untuk bermain tictactoe")
  
def helpSebelumLogin():  
  print("========== HELP ==========")
  print("1. login - Untuk melakukan login ke dalam sistem")
