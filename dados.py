import sqlite3
# conectar ao banco de dados ou criar um novo banco de dados

con= sqlite3.connect('dados.db')

# Criar uma tabela de livros
con.execute('CREATE TABLE livros(\
                id INTEGER PRIMARY KEY,\
                titulo TEXT,\
                autor TEXT,\
                editora  tEXT,\
                ano_publicacao INTEGER,\
                isbn TEXT)')

# Criando tabela de usuarios
con.execute('CREATE TABLE usuarios(\
                id INTEGER PRIMARY KEY,\
                nome TEXT,\
                sobrenome TEXT,\
                endereco  tEXT,\
                email TEXT,\
                contato TEXT)')

# Criando tabela de emprestimo
con.execute('CREATE TABLE emprestimos(\
                id INTEGER PRIMARY KEY,\
                id_livro INTEGER,\
                id_usuario INTEGER,\
                data_emprestimo TEXT,\
                data_devolucao TEXT,\
                FOREING KEY(id_livros) REFERENCES livros(id),\
                FOREING KEY(id_usuarios) REFERENCES usuarios(id))')