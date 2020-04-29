import csv
import sqlite3

conn = sqlite3.connect('services.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS services (
        id integer PRIMARY KEY,
        service TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
''')

index = 0
with open('services.csv','r') as acountsfile:
    reader = csv.reader(acountsfile)
    for element in reader:
        if(index == 0):
            pass
        else:
            cursor.execute("""
                INSERT INTO services (service, username, password)
                VALUES (?,?,?)
            """,(element[1],element[2],element[3]))
            conn.commit()
        index += 1
