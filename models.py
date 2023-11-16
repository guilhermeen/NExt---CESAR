from django.db import models
import sqlite3

# Create your models here.

class System():
    def __init__(self):
        self.connection = sqlite3.connect('./System.sqlite3')
        self.cursor = self.connection.cursor()

    def getLatenciaCliente(self):
        list = []
        latenciaCliente = self.cursor.execute('SELECT latencia, data FROM latenciaCliente')
        for latencia, data in latenciaCliente:
            dict_ = {}
            dict_.update({'latencia': latencia, 'data': data})
            list.append(dict_)

        return list
    
    def getFalhas(self):
        list = []
        falhas = self.cursor.execute('SELECT tipo_falha, quantidade_falha, data FROM falhas')
        for tipo_falha, quantidade_falha, data in falhas:
            dict_ = {}
            dict_.update({'tipo_falha': tipo_falha, 'quantidade_falha': quantidade_falha, 'data': data})
            list.append(dict_)

        return list

    def getAtaques(self):
        list = []
        ataques = self.cursor.execute('SELECT tipo_ataque, quantidade, data FROM ataques')
        for tipo_ataque, quantidade, data in ataques:
            dict_ = {}
            dict_.update({'tipo_ataque': tipo_ataque, 'quantidade': quantidade, 'data': data})
            list.append(dict_)

        return list

    def getLatenciaAPI(self):
        list = []
        latenciaAPI = self.cursor.execute('SELECT latencia, data FROM latenciaAPI')
        for latencia, data in latenciaAPI:
            dict_ = {}
            dict_.update({'latencia': latencia,'data': data})
            list.append(dict_)

        return list

    def getUsers(self):
        list = []
        users = self.cursor.execute('SELECT nome, cidade FROM users')
        for nome, cidade in users:
            dict_ = {}
            dict_.update({'nome': nome,'cidade': cidade})
            list.append(dict_)

        return list

    def getNovosUsuarios(self):
        list = []
        novos_usuarios = self.cursor.execute('SELECT quantidade, data FROM novosUsuarios')
        for quantidade, data in novos_usuarios:
            dict_ = {}
            dict_.update({'quantidade_Novos_usuarios': quantidade, 'data': data})
            list.append(dict_)

        return list


    def getAcessos(self):
        list = []
        acessos = self.cursor.execute('SELECT quantidade, data FROM acessos')
        for quantidade, data in acessos:
            dict_ = {}
            dict_.update({'quantidade_Acessos': quantidade, 'data': data})
            list.append(dict_)

        return list


    def getVendas(self):
        list = []
        vendas = self.cursor.execute('SELECT quantidade, data FROM vendas')
        for quantidade, data in vendas:
            dict_ = {}
            dict_.update({'quantidade_Vendas': quantidade, 'data': data})
            list.append(dict_)

        return list