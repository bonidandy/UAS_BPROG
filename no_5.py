import mysql.connector
import os

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database="bahasa_pemrograman"
)


def insert_data(db):
  Nama = input("Masukan nama: ")
  asal = input("Masukan alamat: ")
  Kelamin = input("Masukan jenis kelamin : ")
  Jurusan = input("Masukan jurusan: ")
  Nim = input("Masukan Nim: ")
  val = (Nama, asal, Kelamin, Jurusan,Nim)
  cursor = db.cursor()
  sql = "INSERT INTO mahasiswa (Nama, asal, Kelamin, Jurusan, Nim) VALUES (%s, %s, %s, %s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM mahasiswa"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)

def search_data(db):
  cursor = db.cursor()
  keyword = input("cari dengan nama : ")
  sql = "SELECT * FROM mahasiswa WHERE Nama LIKE %s OR asal LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("Tidak ada data")
  else:
    for data in results:
      print(data)


def show_menu(db):
  print("=== APLIKASI DATABASE PYTHON ===")
  print("1. Insert Data")
  print("2. Tampilkan Data")
  print("3. Cari Data")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(db)