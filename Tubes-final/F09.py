from fungsi import length,samecount

def list_game(username, role, data_user, data_kepemilikan, datagame): 
  # Mencari ID Terlebih Dahulu 
  for i in range(length(data_user)):
    if role == "User":
       if username == data_user[i][1]:
        user_now = data_user[i][0]
  list_game = []
  for i in range(1,length(data_kepemilikan)):
    if data_kepemilikan[i][1] == user_now:
      list_game += [data_kepemilikan[i][0]]
  # Untuk melakukan print 
  if length(list_game) <= 0:
    return ("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
  else:
    count = 0
    for i in range(length(list_game)): 
      for j in range(length(datagame)):
        if list_game[i] == datagame[j][0]:
          count += 1
          print(f"{count}. {samecount(datagame[j][0])}   | {samecount(datagame[j][1])}   | {samecount(datagame[j][2])}   | {samecount(datagame[j][3])}   | {samecount(datagame[j][4])}")
  return ("Di atas ditampilkan game yang anda miliki.")

# if isUser(username) == True:
#   print(list_game())
# else : 
#   print("Anda Tidak Memiliki Akses untuk Melihat Game yang Dimiliki")
