import sqlite3
# conectar ao banco de dados 
def connect():
    conn= sqlite3.connect('dados.db')
    return conn

# Função pata inserir um novo livro
def insert_book(titulo, autor, editora, ano_publicacao, isbn):
    conn = connect()
    conn.execute ("INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn) values (?, ?, ?, ?, ?)", (titulo, autor, editora, ano_publicacao, isbn))
    conn.commit()
    conn.close()

# Função para inserir usuarios 
def insert_user(nome, sobrenome, endereco, email, contato):
    conn = connect()
    conn.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email, contato) values(?, ?, ?, ?, ?)", (nome, sobrenome, endereco, email, contato))
    conn.commit()
    conn.close()

# Função para exibir usuarios
def get_users():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    users= c.fetchall()
    conn.close()
    return users

#Função para inserir os livros
def exibir_livros():
    conn = connect()
    livros = conn.execute("SELECT * FROM livros").fetchall()
    conn.close()
    return(livros)

#função para realizr emprestimos
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao)\
                  values(?, ?, ?, ?)",(id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()
#funação para exibir todos os livros emprestados no momento
def get_books_on_loan():
 conn=connect()
 result = conn.execute("SELECT livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.id, emprestimos.data_emprestimo, emprestimos.data_devolucao\
                        FROM livros\
                        INNER JOIN emprestimos ON livros.id = emprestimos.id_livro\
                        INNER JOIN usuarios  ON usuarios.id = emprestimos.id_usuario\
                        WHERE emprestimos.data_devolucao IS NULL ").fetchall()
 conn.close()
 return result
#Função para atualizar a data de devolução de emprestimos
def update_loan_return_date(id_emprestimo, data_devolucao):
    conn= connect
    conn.execute("UPDATE emprestimos SET data_devolucao =? WHERE id= ?", (id_emprestimo, data_devolucao))
    conn.commit()
    conn.close()


       
# Exexmplo de das funções 
#insert_book("Dom Quixote", "Miguel", "Editora 1", 1605, "12345")
#insert_user("João", "SIlva", "Angola, Cabina", "joao@gmail.com", "+244 123")
#insert_loan(1, 1, "2022-08-13", None)
livros_emprestados= get_books_on_loan()

print(livros_emprestados)

#update_loan_return_date(2,"2022-09-21")
#exibir_livros()