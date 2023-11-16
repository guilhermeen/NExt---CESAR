from datetime import datetime, timedelta
import sqlite3
from random import randint
import csv

connection = sqlite3.connect('./System.sqlite3')

cursor = connection.cursor()

def createTables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS latenciaCliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            latencia INTEGER NOT NULL,
            unidade TEXT NOT NULL,
            data DATE NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS falhas (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            quantidade_falha INTEGER NOT NULL,
            tipo_falha TEXT NOT NULL,
            data DATE NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ataques (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            tipo_ataque TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            data DATE NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS latenciaAPI (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            latencia INTEGER NOT NULL,
            unidade TEXT NOT NULL,
            data DATE NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS novosUsuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            quantidade INTEGER NOT NULL,
            data DATE NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS acessos (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            quantidade INTEGER NOT NULL,
            data DATE NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            quantidade INTEGER NOT NULL,
            data DATE NOT NULL
        )
    ''')


def insertUsersTable():

    lista_cidades = ['São José dos Campos', 'Recife', 'João Pessoa', 'Curitiba']

    with open('./ibge-mas-10000.csv', 'r') as file:
        read = csv.reader(file)

        count = 0
        for row in read:
            if count <= 1500:
                rand = randint(0, 3)
                cidade = lista_cidades[rand]
                cursor.execute(f'INSERT INTO users (nome, cidade) VALUES ("{row[0]}", "{cidade}")')
                count += 1

    with open('./ibge-fem-10000.csv', 'r') as file:
        read = csv.reader(file)

        count = 0
        for row in read:
            if count <= 1500:
                rand = randint(0, 3)
                cidade = lista_cidades[rand]
                cursor.execute(f'INSERT INTO users (nome, cidade) VALUES ("{row[0]}", "{cidade}")')
                count += 1

    connection.commit()


def insertAtaquesTable():
    lista_ataques = ['DDoS', 'DoS', 'Spoofing', 'Exploits']
    
    date = datetime(2021, 1, 1)
    for r in range(1, 365+1):
        rand_lista = randint(0, 3)
        rand_qntd = randint(0, 5)
        date_f = date.strftime("%Y-%m-%d")

        if rand_qntd != 0:
            cursor.execute(f'''
                INSERT INTO ataques (tipo_ataque, quantidade, data) VALUES ("{lista_ataques[rand_lista]}", "{rand_qntd}", "{date_f}")
            ''')
        elif rand_qntd == 0:
            cursor.execute(f'''
                INSERT INTO ataques (tipo_ataque, quantidade, data) VALUES ("Nenhum ataque", "{rand_qntd}", "{date_f}")
            ''')

        connection.commit()

        date += timedelta(days=1)


def insertLatenciaClienteTable():
    date = datetime(2021, 1, 1)
    date_final_Ano = datetime(2021, 10, 1)
    for r in range(1, 365+1):
        if date < date_final_Ano:
            rand_latencia = randint(25, 45)
            date_f = date.strftime("%Y-%m-%d")
            cursor.execute(f'''
                INSERT INTO latenciaCliente (latencia, unidade, data) VALUES ("{rand_latencia}", "ms", "{date_f}")
            ''')
        else:
            rand_latencia = randint(100, 175)
            date_f = date.strftime("%Y-%m-%d")
            cursor.execute(f'''
                INSERT INTO latenciaCliente (latencia, unidade, data) VALUES ("{rand_latencia}", "ms", "{date_f}")
            ''')
        
        connection.commit()
        
        date += timedelta(days=1)


def insertFalhasTable():
    date = datetime(2021, 1, 1)
    date_black = datetime(2021, 11, 26)
    lista_tipo_falhas = ['Servidor indisponível', 'API pagamento indisponível', 'Sem estoque']
    for r in range(1, 365+1):
        if date < date_black:
            rand_falhas = randint(0, 5)
            rand_tipo_falha = randint(0, len(lista_tipo_falhas)-1)
            date_f = date.strftime("%Y-%m-%d")
            cursor.execute(f'''
                INSERT INTO falhas (quantidade_falha, tipo_falha, data) VALUES ("{rand_falhas}", "{lista_tipo_falhas[rand_tipo_falha]}", "{date_f}")
            ''')
        elif date == date_black:
            rand_falhas = randint(20, 45)
            date_f = date.strftime("%Y-%m-%d")
            cursor.execute(f'''
                INSERT INTO falhas (quantidade_falha, tipo_falha, data) VALUES ("{rand_falhas}", "{lista_tipo_falhas[rand_tipo_falha]}", "{date_f}")
            ''')
        else:
            rand_falhas = randint(0, 10)
            date_f = date.strftime("%Y-%m-%d")
            cursor.execute(f'''
                INSERT INTO falhas (quantidade_falha, tipo_falha, data) VALUES ("{rand_falhas}", "{lista_tipo_falhas[rand_tipo_falha]}", "{date_f}")
            ''')

        connection.commit()

        date += timedelta(days=1)


def insertLatenciaAPITable():
    date = datetime(2021, 1, 1)
    date_final_Ano = datetime(2021, 11, 1)
    for r in range(1, 365+1):
        if date < date_final_Ano:
            rand_latencia = randint(5, 13)
            date_f = date.strftime("%Y-%m-%d")
            cursor.execute(f'''
                INSERT INTO latenciaAPI (latencia, unidade, data) VALUES ("{rand_latencia}", "ms", "{date_f}")
            ''')
        else:
            rand_latencia = randint(45, 70)
            date_f = date.strftime("%Y-%m-%d")
            cursor.execute(f'''
                INSERT INTO latenciaAPI (latencia, unidade, data) VALUES ("{rand_latencia}", "ms", "{date_f}")
            ''')

        connection.commit()

        date += timedelta(days=1)


def insertNovosUsuariosTable():
    date = datetime(2021, 1, 1)
    date_final_Ano = datetime(2021, 10, 16)
    date_lastWeek_black = datetime(2021, 11, 24)
    for r in range(1, 365+1):
        if date < date_final_Ano:
            rand_novosUsuarios = randint(50, 100)
            date_f = date.strftime("%Y-%m-%d")
            cursor.execute(f'''
                INSERT INTO novosUsuarios (quantidade, data) VALUES ("{rand_novosUsuarios}", "{date_f}")
            ''')
        elif date > date_final_Ano and date < date_lastWeek_black:
            rand_novosUsuarios = randint(200, 400)
            date_f = date.strftime("%Y-%m-%d")
            cursor.execute(f'''
                INSERT INTO novosUsuarios (quantidade, data) VALUES ("{rand_novosUsuarios}", "{date_f}")
            ''')
        else:
            rand_novosUsuarios = randint(100, 200)
            date_f = date.strftime("%Y-%m-%d")
            cursor.execute(f'''
                INSERT INTO novosUsuarios (quantidade, data) VALUES ("{rand_novosUsuarios}", "{date_f}")
            ''')

        connection.commit()

        date += timedelta(days=1)


def insertAcessosTable():
    date = datetime(2021, 1, 1)
    date_final_Ano = datetime(2021, 10, 16)
    for r in range(1, 365+1):
        if date < date_final_Ano:
            rand_acessos = randint(1400, 1600)
            date_f = date.strftime("%Y-%m-%d")
            cursor.execute(f'''
                INSERT INTO acessos (quantidade, data) VALUES ("{rand_acessos}", "{date_f}")
            ''')
        else:
            rand_acessos = randint(2000, 2500)
            date_f = date.strftime("%Y-%m-%d")
            cursor.execute(f'''
                INSERT INTO acessos (quantidade, data) VALUES ("{rand_acessos}", "{date_f}")
            ''')

        connection.commit()

        date += timedelta(days=1)


def insertVendasTable():
    date = datetime(2021, 1, 1)
    date_final_Ano = datetime(2021, 10, 16)
    for r in range(1, 365+1):
        if date < date_final_Ano:
            rand_vendas = randint(350, 550)
            date_f = date.strftime("%Y-%m-%d")
            cursor.execute(f'''
                INSERT INTO vendas (quantidade, data) VALUES ("{rand_vendas}", "{date_f}")
            ''')
        else:
            rand_vendas = randint(600, 800)
            date_f = date.strftime("%Y-%m-%d")
            cursor.execute(f'''
                INSERT INTO vendas (quantidade, data) VALUES ("{rand_vendas}", "{date_f}")
            ''')

        connection.commit()

        date += timedelta(days=1)


createTables()
insertUsersTable()
insertAtaquesTable()
insertLatenciaClienteTable()
insertFalhasTable()
insertLatenciaAPITable()
insertNovosUsuariosTable()
insertAcessosTable()
insertVendasTable()