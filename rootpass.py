import sqlite3

conn = sqlite3.connect('rootpassword.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS root (
        password TEXT NOT NULL
    );
''')

rootPassword = input('Informe uma senha root: ')
cursor.execute("""
    INSERT INTO root (password)
    VALUES (?)
""", (rootPassword,))
conn.commit()