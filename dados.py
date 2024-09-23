import sqlite3

conn= sqlite3.connect("banco_de_dados.db")

cursor = conn.cursor()
#Avalista#########################################################################################################
cursor.execute("""
CREATE TABLE IF NOT EXISTS senha(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            CPF TEXT NOT NULL,  
            SENHA TEXT NOT NULL
                )
""")

#Aluno#######################################################################################################
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            CPF NUMERIC NOT NULL,  
            Aluno TEXT NOT NULL,
            ENDERECO TEXT NOT NULL,
            DDD NUMERIC NOT NULL,
            CONTATO NUMERIC NOT NULL,
            ANO_LETIVO TEXT NOT NULL,
            DATA_DE_NASCIMENTO NUMERIC NOT NULL,
            RESPONSAVEL TEXT NOT NULL
               )
""")
#Notas#########################################################################################################
cursor.execute("""
CREATE TABLE IF NOT EXISTS notas(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
            ALUNO TEXT NOT NULL,
            ANO_LETIVO TEXT NOT NULL,
            lINGUA_PORTUGUESA NUMERIC NOT NULL,
            lINGUA_INGLESA  NUMERIC NOT NULL, 
            lINGUA_ESPANHOLA  NUMERIC NOT NULL,
            MATEMATICA NUMERIC NOT NULL,
            QUIMICA NUMERIC NOT NULL,
            FISICA NUMERIC NOT NULL,
            HISTORIA NUMERIC NOT NULL,
            GEOGRAFIA NUMERIC NOT NULL,
            CIENCIAS NUMERIC NOT NULL,
            EDUCACAO_FISICA NUMERIC NOT NULL,
            ARTES NUMERIC NOT NULL
           )
""")

    