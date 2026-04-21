import sqlite3

conn = sqlite3.connect("app.db")
curser = conn.cursor()

username = input("What's your name: \n")