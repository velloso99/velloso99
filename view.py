import sqlite3

def connect():

    conn= sqlite3.connect("banco_de_dados.db")
    return conn
#SENHA ##################################################################################
def insert_senha(cpf,senha):
    conn = connect()
    conn.execute("INSERT INTO senha(cpf,senha) values(?,?)",(cpf,senha))
    conn.commit()
    conn.close()
#INSERIR ALUNO ##################################################################################
def insert_alunos(cpf,aluno,endereco,ddd,contato,ano_letivo,data_de_nascimento,responsavel):
    conn = connect()
    conn.execute("INSERT INTO alunos(cpf,aluno,endereco,ddd,contato,ano_letivo,data_de_nascimento,responsavel) values(?,?,?,?,?,?,?,?)",(cpf,aluno,endereco,ddd,contato,ano_letivo,data_de_nascimento,responsavel))
    conn.commit()
    conn.close()

#Notas####################################################################################################3
def insert_notas(aluno,ano_letivo,lingua_portuguesa,lingua_inglesa,lingua_espanhola,matematica,fisica,quimica,historia,geografia,ciencias,educacao_fisica,artes):
    conn = connect()
    conn.execute("INSERT INTO notas(aluno,ano_letivo,lingua_portuguesa,lingua_inglesa,lingua_espanhola,matematica,fisica,quimica,historia,geografia,ciencias,educacao_fisica,artes) values(?,?,?,?,?,?,?,?,?,?,?,?,?)",(aluno,ano_letivo,lingua_portuguesa,lingua_inglesa,lingua_espanhola,matematica,fisica,quimica,historia,geografia,ciencias,educacao_fisica,artes))
    conn.commit()
    conn.close()

#************************************************************************************************************************************************************************************************

#Inserir SENha--------------------------------------------------------------------------------------
def inserir_senha():
    conn = connect()
    cadastro = conn.execute("SELECT * FROM  senha").fetchall()
    conn.close()
    return(cadastro)
#Inserir Alunos--------------------------------------------------------------------------------------
def inserir_alunos():
    conn = connect()
    cadastro1 = conn.execute("SELECT * FROM  alunos").fetchall()
    conn.close()
    return(cadastro1)
#Inserir avalista--------------------------------------------------------------------------------------
def inserir_notas():
    conn = connect()
    cadastro2 = conn.execute("SELECT * FROM  notas").fetchall()
    conn.close()
    return(cadastro2)

