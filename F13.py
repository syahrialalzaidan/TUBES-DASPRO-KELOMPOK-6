from fungsi import split
from F08 import history #history = list berupa daftar pembelian dari F08


def riwayat() :
  data = open('game.csv', 'r') 
  nomor = 1
  for x in data.readlines() :
    a = split(x) 
    if a[0] in history :
      print(f'{nomor}. {a[0]} | {a[1]} | {a[4]} | {a[3]} |')
      nomor += 1

riwayat()