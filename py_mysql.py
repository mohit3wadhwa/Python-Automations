import mysql.connector
import tkinter as tk

mydb = mysql.connector.connect(
  #host="localhost",
  host="127.0.0.1",
  port="8080",
  user="root",
  passwd="admin",
  db="simidb"
)
print(mydb)

mycursor = mydb.cursor()

sql = "INSERT INTO simidb.item_tb (Item_ID, Item_name, Item_cat, Item_expiry) VALUES (%s, %s, %s, %s)"
val = ("45", "shoes", "abc", "2020-10-31")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
