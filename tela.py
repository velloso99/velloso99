from tkinter. ttk import *
from tkinter import *
from tkinter import ttk
from turtle import home
from PIL import Image, ImageTk
from tkinter import messagebox
#Importando as funções da view
from view import * 


#cores
co0 = "#2e2b2b" #Preta
co1 = "#feffff" #branca
co2 = "#fa882"  #verdepip
co3 = "#38576b" #valor
co4 = "#403d3d" #letra
co5 = "#e06636" #- profit
co6 = "#E9A178"
co7 = "3fbfb9"  #verde
co8 = "#263238" # + verde
co9 = "#e9edf5" # + verde
co10 = "#6e8faf"
co11 = "#f2f4f2"



# Criando Janela 
janela = Tk()
janela.title("")
janela.geometry('770x330')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

Style= Style(janela)
Style.theme_use("clam")

# Frames 
frameCima = Frame(janela, width= 770, height=50, bg=co6, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsquerda = Frame(janela, width= 150, height=265, bg=co4, relief="solid")
frameEsquerda.grid(row=1, column=0, sticky=NSEW)

frameDireita = Frame(janela, width= 600, height=265, bg=co1, relief="raised")
frameDireita.grid(row=1, column=1, sticky=NSEW)

# Logo
# Abrindo a imagem
app_img = Image.open('icons/logo.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW, bg=co6, fg=co1)
app_logo.place(x=5, y=0)

app_ = Label(frameCima, text="Sistema de Gerenciamento de Livros", compound=LEFT, padx=5, anchor=NW, font=('verdana 15 bold'), bg=co6, fg=co1)
app_.place(x=50, y=7)

app_linha = Label(frameCima, width=770, height=1, padx=5, anchor=NW, font=('verdana 1'), bg=co3, fg=co1)
app_linha.place(x=0, y=47)

#novo usuario
def novo_usuario():

    global img_salvar

    def add():

        first_name = e_p_nome.get()
        last_name = e_p_sobrenome.get()
        address = e_p_endereco.get()
        email= e_p_email.get()
        phone= e_p_contato.get()

        lista = [first_name, last_name, address, email, phone]

        # Verificando caso algum campo esteja vazio ou não
        for i in lista:
            if i =='':
                messagebox.showerror('Error', 'Preencha todos os campos')
                return
        #inserindo os dados no banco de dados
        insert_user(first_name, last_name, address, email, phone)

        messagebox.showinfo('Sucesso', 'Usuario inserido com sucesso')

        #limpando os ocampos de entrada
        e_p_nome.delete(0,END)
        e_p_sobrenome.delete(0,END)
        e_p_endereco.delete(0,END)
        e_p_email.delete(0,END)
        e_p_contato.delete(0,END)



    app_= Label(frameDireita, text=("Inserir novo usuario"), width=50, compound=LEFT, padx=5, pady=10, font=('verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    app_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    l_p_nome=Label(frameDireita, text="Nome*",anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_p_nome.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_p_nome=Entry(frameDireita, width=25, justify='left', relief='solid')
    e_p_nome.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    l_p_sobrenome=Label(frameDireita, text="Sobrenome*",anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_p_sobrenome.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_p_sobrenome=Entry(frameDireita, width=25, justify='left', relief='solid')
    e_p_sobrenome.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    l_p_endereco=Label(frameDireita, text="Endereço*",anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_p_endereco.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_p_endereco=Entry(frameDireita, width=25, justify='left', relief='solid')
    e_p_endereco.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    l_p_email=Label(frameDireita, text="E-mail*",anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_p_email.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_p_email=Entry(frameDireita, width=25, justify='left', relief='solid')
    e_p_email.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    l_p_contato=Label(frameDireita, text="Contato*",anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_p_contato.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    e_p_contato=Entry(frameDireita, width=25, justify='left', relief='solid')
    e_p_contato.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)

    #Botão salvar
    img_salvar = Image.open('icons/save.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text=' Salvar', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, padx=5, pady=6, sticky=NSEW)
    
#ver Usuarios
def ver_usuarios():

    app_= Label(frameDireita, text=("Ver Usuarios"), width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    dados= get_users()
    
    #creating a treeview with duol scrolbars
    list_header = ['id', 'Nome', 'Sobrenome', 'Endereço', 'E-mail', 'Contato']
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show="headings")
    #Vertical scrollbar
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
    #horizontal scrollbar
    hsb = ttk.Scrollbar(frameDireita, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0,row=2,sticky='NSEW')
    vsb.grid(column=1,row=2,sticky='NS')
    hsb.grid(column=0,row=3,sticky='EW')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,80,80,120,120,76,100]
    n=0

    for col in list_header:
      tree.heading(col, text=col, anchor='nw')
      tree.column(col, width=h[n], anchor=hd[n])

      n+=1

    for item in dados:
        tree.insert('','end', values=item)


#Novo Livro
def novo_livro():
    global img_salvar

    def add():
        title = e_titlo.get()
        author = e_autor.get()
        publisher= e_editora.get()
        year= e_ano.get()
        isbn= e_isbn.get()

        lista= [title,author,publisher,year,isbn]

       # Verificando caso algum campo esteja vazio ou não
        for i in lista:
            if i =='':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
        #inserindo os dados no banco de dados
        insert_book(title,author,publisher,year,isbn)

        messagebox.showinfo('Sucesso', 'Livfro inserido com sucesso')

        #limpando os ocampos de entrada
        e_titlo.delete(0,END)
        e_autor.delete(0,END)
        e_editora.delete(0,END)
        e_ano.delete(0,END)
        e_isbn.delete(0,END)

    app_= Label(frameDireita, text=("Inserir um novo livro"), width=50, compound=LEFT, padx=5, pady=10, font=('verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    app_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    l_titlo=Label(frameDireita, text="Titulo do livro*",anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_titlo.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_titlo=Entry(frameDireita, width=25, justify='left', relief='solid')
    e_titlo.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    l_autor=Label(frameDireita, text="Autor do livro*",anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_autor.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_autor=Entry(frameDireita, width=25, justify='left', relief='solid')
    e_autor.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    l_editora=Label(frameDireita, text="Editora do livro*",anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_editora.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_editora=Entry(frameDireita, width=25, justify='left', relief='solid')
    e_editora.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    l_ano=Label(frameDireita, text="Ano de publicação do livro*",anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_ano.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_ano=Entry(frameDireita, width=25, justify='left', relief='solid')
    e_ano.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    l_isbn=Label(frameDireita, text="ISBN do livro*",anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_isbn.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    e_isbn=Entry(frameDireita, width=25, justify='left', relief='solid')
    e_isbn.grid(row=6, column=1, padx=5, pady=5, sticky=NSEW)

    #Botão salvar
    img_salvar = Image.open('icons/save.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text=' Salvar', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, padx=5, pady=6, sticky=NSEW)


#função ver livro
def ver_livros():

    app_= Label(frameDireita, text=("Todos os livros no banco de dados"), width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    dados= exibir_livros()
    
    #creating a treeview with duol scrolbars
    list_header = ['id', 'titulo', 'Autor', 'Editora', 'Ano', 'ISBN']
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show="headings")
    #Vertical scrollbar
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
    #horizontal scrollbar
    hsb = ttk.Scrollbar(frameDireita, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0,row=2,sticky='NSEW')
    vsb.grid(column=1,row=2,sticky='NS')
    hsb.grid(column=0,row=3,sticky='EW')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","nw"]
    h=[20,160,110,100,50,50,100]
    n=0

    for col in list_header:
      tree.heading(col, text=col, anchor='nw')
      tree.column(col, width=h[n], anchor=hd[n])

      n+=1

    for item in dados:
        tree.insert('','end', values=item)

#Realizar emprestimo 
def realizar_emprestimo():

    global img_salvar

    def add():

        user_id = e_id_usuarios.get()
        book_id = e_id_livros.get()

        lista=[user_id, book_id]


        #verificando caso algum esteja vazio ou não
        for i in lista:
            if i=='':
                messagebox.showerror('Erro', 'Preencha Todos os campos')
                return
        # Inserindo os dados no banco de daos
        insert_loan(user_id, book_id, hoje, None) # type: ignore

        messagebox.showinfo('Sucesso', 'Livro inserido com sucesso')

        #Limpando os campos de entradas
        e_id_usuarios.delete(0,END)
        e_id_livros.delete(0,END)

    app_= Label(frameDireita, text=("Inserir novo usuario"), width=50, compound=LEFT, padx=5, pady=10, font=('verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    app_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)
    

    l_id_usuarios=Label(frameDireita, text="Digite o ID do usuario*",anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_id_usuarios.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_usuarios=Entry(frameDireita, width=25, justify='left', relief='solid')
    e_id_usuarios.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    l_id_livros=Label(frameDireita, text="Digite o ID do livro*",anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_id_livros.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_livros=Entry(frameDireita, width=25, justify='left', relief='solid')
    e_id_livros.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

     #Botão salvar
    img_salvar = Image.open('icons/save.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text=' Salvar', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, padx=5, pady=6, sticky=NSEW)





#Devolução de um emprestimo
def devolucao_emprestimo():

    global img_salvar

    def add():

        loan_id = e_id_emprestimo.get()
        return_date_id =  e_data_retorno.get()

        lista= [loan_id, return_date_id]


        #verificando caso algum esteja vazio ou não
        for i in lista:
            if i=='':
                messagebox.showerror('Erro', 'Preencha Todos os campos')
                return
        # Inserindo os dados no banco de daos
        update_loan_return_date(loan_id, return_date_id)

        messagebox.showinfo('Sucesso', 'Livro retornado com sucesso')

        #Limpando os campos de entradas
        e_id_emprestimo.delete(0,END)
        e_data_retorno.delete(0,END)

    app_= Label(frameDireita, text=("Atualizar Devolução de um Emprestimo"), width=50, compound=LEFT, padx=5, pady=10, font=('verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    app_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    app_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)
    

    l_id_emprestimo=Label(frameDireita, text="ID Emprestimo*",anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_id_emprestimo.grid(row=2, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_emprestimo=Entry(frameDireita, width=25, justify='left', relief='solid')
    e_id_emprestimo.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    l_data_retorno=Label(frameDireita, text="Nova de Devolução(Formato: AAAA-MM-DD*",anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_data_retorno.grid(row=3, column=0, paemprestimody=5, sticky=NSEW)
    e_data_retorno=Entry(frameDireita, width=25, justify='left', relief='solid')
    e_data_retorno.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

     #Botão salvar
    img_salvar = Image.open('icons/save.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text=' Salvar', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, padx=5, pady=6, sticky=NSEW)




#Função para controlar menu
def control(i):

    #novo Usuario
    if i =='novo_usuario':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        #chamando a função novo usuario
        novo_usuario()
     #ver Usuarios
    if i =='ver_usuarios':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        #chamando a função novo usuario
        ver_usuarios()

        #Novo Livro
    if i =='novo_livro':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        #chamando a função novo usuario
        novo_livro()

        #ver Livro
    if i =='ver_livro':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        #chamando a função ver usuario
        ver_livros()

    #Retorno do Emprestimo
    if i =='retono':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        #chamando a função Emprestimo
        devolucao_emprestimo()
   
# Menu

#Novo Usuario
img_usuario = Image.open('icons/add.png')
img_usuario = img_usuario.resize((18,18))
img_usuario = ImageTk.PhotoImage(img_usuario)
b_usuario = Button(frameEsquerda, command=lambda:control('novo_usuario'), image=img_usuario, compound=LEFT, anchor=NW, text=' Novo usuario', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)
# Novo Livro
img_novo_livro = Image.open('icons/add.png')
img_novo_livro = img_novo_livro.resize((18,18))
img_novo_livro = ImageTk.PhotoImage(img_novo_livro)
b_Novo_livro = Button(frameEsquerda,command=lambda:control('novo_livro'), image=img_novo_livro, compound=LEFT, anchor=NW, text=' Novo Livro', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_Novo_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)
# Ver Livros
img_ver_livro = Image.open('icons/logo.png')
img_ver_livro = img_ver_livro.resize((18,18))
img_ver_livro = ImageTk.PhotoImage(img_ver_livro)
b_ver_livro = Button(frameEsquerda,command=lambda:control('ver_livro'), image=img_ver_livro, compound=LEFT, anchor=NW, text=' Exibir todos os Livros', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_livro.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)
#ver Usuarios
img_ver_usuario = Image.open('icons/user.png')
img_ver_usuario = img_ver_usuario.resize((18,18))
img_ver_usuario = ImageTk.PhotoImage(img_ver_usuario)
b_ver_usuario = Button(frameEsquerda,command=lambda:control('ver_usuarios'), image=img_ver_usuario, compound=LEFT, anchor=NW, text=' Exibir todos os usuarios', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_usuario.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)
#Realizar um emprestimo
img_imprestimo = Image.open('icons/add.png')
img_imprestimo = img_imprestimo.resize((18,18))
img_imprestimo = ImageTk.PhotoImage(img_imprestimo)
b_ver_imprestimo = Button(frameEsquerda,command=lambda:control('realizar_emprestimo'), image=img_imprestimo, compound=LEFT, anchor=NW, text=' Realizar um emprestimo', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_imprestimo.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)
# Devolução de  um emprestimo
img_devolucao = Image.open('icons/update.png')
img_devolucao = img_devolucao.resize((18,18))
img_devolucao = ImageTk.PhotoImage(img_devolucao)
b_ver_devolucao = Button(frameEsquerda,command=lambda:control('devolução_emprestimio'), image=img_devolucao, compound=LEFT, anchor=NW, text=' Devolução de um emprestimo', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_devolucao.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)
# Livros emprestados no momento
img_livros_emprestados = Image.open('icons/livros.png')
img_livros_emprestados = img_livros_emprestados.resize((18,18))
img_livros_emprestados = ImageTk.PhotoImage(img_livros_emprestados)
b_ver_livros_emprestados = Button(frameEsquerda,command=lambda:control('ver_livros_emrprestados'), image=img_livros_emprestados, compound=LEFT, anchor=NW, text=' Livros Emprestados no momento', bg=co4, fg=co1, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_livros_emprestados.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)


janela.mainloop()