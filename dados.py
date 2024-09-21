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
            CPF TEXT NOT NULL,  
            Aluno TEXT NOT NULL,
            ENDERECO TEXT NOT NULL,
            DDD TEXT NOT NULL,
            CONTATO TEXT NOT NULL,
            ANO_LETIVO TEXT NOT NULL,
            DATA_DE_NASCIMENTO TEXT NOT NULL,
            RESPONSAVEL TEXT NOT NULL
               )
""")
#Notas#########################################################################################################
cursor.execute("""
CREATE TABLE IF NOT EXISTS notas(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
            ALUNO TEXT NOT NULL,
            ANO_LETIVO TEXT NOT NULL,
            lINGUA_PORTUGUESA TEXT NOT NULL,
            lINGUA_INGLESA  TEXT NOT NULL, 
            lINGUA_ESPANHOLA  TEXT NOT NULL,
            MATEMATICA TEXT NOT NULL,
            QUIMICA TEXT NOT NULL,
            FISICA TEXT NOT NULL,
            HISTORIA TEXT NOT NULL,
            GEOGRAFIA TEXT NOT NULL,
            CIENCIAS TEXT NOT NULL,
            EDUCACAO_FISICA TEXT NOT NULL,
            ARTES TEXT NOT NULL
           )
""")

    