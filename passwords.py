import sqlite3

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS services (
        service TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
''')

def menu():
    print("*****************************")
    print("* i : inserir nova senha * ")
    print("* l : listar serviços salvos * ")
    print("* r : recuperar uma senha * ")
    print("* s : sair * ")
    print("*****************************")

def getPassword(service):
    cursor.execute("""
        SELECT username, password FROM users
        WHERE service  = ?
    """, (service,))

    if cursor.rowcount == 0:
        print("Serviço não cadastrado (Utilize 'l' para verificar os serviços).")
    else:
        for user in cursor.fetchall():
            print(user)

def insertPassword(service, username, password):
    cursor.execute("""
        INSERT INTO users (service, username, password)
        VALUES (?,?,?)
    """,(service,username,password))
    conn.commit()

def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)
    
while True:
    
    menu()
    op = input("O que deseja fazer?")
    if op not in ['i', 'l', 'r', 's']:
        print("Opção inválida!")
        continue

    if op == 's':
        break
    
    if op == 'i':
        service = input('Qual o nome do serviço?')
        username = input('Qual o nome de usuário?')
        password = input('Qual a senha?')
        insertPassword(service, username, password)
    
    if op == 'l':
        show_services()

    if op == 'r':
        service = input('Qual o serviço para qual quer a senha?')
        getPassword(service)

conn.close()
