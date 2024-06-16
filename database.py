# não está funcionando

import mysql.connector

conexao = mysql.connector.connect(
    host='192.168.0.104',
    user='root',
    passwd='',
    database='ongdb'
)

db = conexao.cursor()
# db.execute('CREATE DATABASE ONGDB')

# *tabela usuário
# db.execute('CREATE TABLE usuario(cod_usuario INT(8) PRIMARY KEY AUTO_INCREMENT,'
#             'login VARCHAR(50) NOT NULL UNIQUE,'
#             'senha VARCHAR(50) NOT NULL,'
#             'tipo_acesso VARCHAR(20) NOT NULL)')

# *tabela voluntário
# db.execute('CREATE TABLE voluntario(cpf VARCHAR(14) PRIMARY KEY,'
#             'nome VARCHAR(50) NOT NULL,'
#             'data_nascimento DATE NOT NULL,'
#             'experiencia VARCHAR(1000))')

# *tabela doação
# db.execute('CREATE TABLE doacao(cod_doacao INT PRIMARY KEY AUTO_INCREMENT,'
#             'data_doacao DATETIME NOT NULL,'
#             'nome_doador VARCHAR(50) NOT NULL,'
#             'valor DECIMAL(10,2) NOT NULL)')

# conexao.commit()

