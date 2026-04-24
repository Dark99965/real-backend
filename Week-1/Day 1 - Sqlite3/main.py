import sqlite3

conn = sqlite3.connect("app.db")
cursor = conn.cursor()

username = input("What is Your name: \n")

email = input("What is your email: \n")
