from tkinter import *
from tkinter import Tk as Tk
from tkinter import ttk
from tkinter import messagebox
from view import * 
from sqlite3 import *

#########################################################################################################################################

janela= Tk=Tk()
janela.geometry("900x500")
janela.title("Projeto Piloto Vida Financeira das Crianças")
janela.resizable(FALSE,FALSE)
#####################################CORES################################################################################################
co0= "#A9A9A9"  #DarkGray Cinza escuro
co1= "#F0F8FF"  #AliceBlue
co2= "#008000"  #Green Verde
co3= "#000000"  #Black
co4= "#D3D3D3"  #LightGrey
#######################################################################################################################################
frame_Cima = Frame(janela, width= 900, height=100, bg=co0, relief="flat")
frame_Cima.grid(row=0, column=0,  sticky=NSEW)

frame_Centro = Frame(janela, width= 900, height=50, bg=co0, relief="solid")
frame_Centro.grid(row=1, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width= 900, height=400, bg=co0, relief="solid")
frame_baixo.grid(row=2, column=0, sticky=NSEW)
#---------------------------------------------------

#-----------------------------------------------------
def Cad_usuario():
        for widget in frame_Cima.winfo_children():
            widget.destroy()
        for widget in frame_Centro.winfo_children():
            widget.destroy()
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        cadastar_novo_usuario()
#-----------------------------------------------------
def abrir_pag_principal():
        for widget in frame_Cima.winfo_children():
            widget.destroy()
        for widget in frame_Centro.winfo_children():
            widget.destroy()
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        pag_principal()
#--------------------------------------------------------------

#-----------------------------------------------------------------
def voltar_pagina():
        for widget in frame_Cima.winfo_children():
            widget.destroy()
        for widget in frame_Centro.winfo_children():
            widget.destroy()
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        pag_principal()
#----------------------------------------------------------------------------------------------------------------
def abrir_aluno():
        for widget in frame_Cima.winfo_children():
            widget.destroy()
        for widget in frame_Centro.winfo_children():
            widget.destroy()
        for widget in frame_baixo.winfo_children():
            widget.destroy()    
        novo_aluno()
#--------------------------------------------------------------------------------------------------
def cadastrar_aluno():
        
        for widget in frame_Centro.winfo_children():
            widget.destroy()
        for widget in frame_baixo.winfo_children():
            widget.destroy()    
        cadastar_aluno()
#-----------------------------------------------------------------------------------------------
def voltar_aluno():
        for widget in frame_Cima.winfo_children():
            widget.destroy()
        for widget in frame_Centro.winfo_children():
            widget.destroy()
        for widget in frame_baixo.winfo_children():
            widget.destroy()   
        abrir_aluno()     
#-----------------------------------------------------------------------------------------------
def voltar_conta():
        for widget in frame_Cima.winfo_children():
            widget.destroy()
        for widget in frame_Centro.winfo_children():
            widget.destroy()
        for widget in frame_baixo.winfo_children():
            widget.destroy()   
        abrir_conta() 
#----------------------------------------------------------------------------
def nova_conta():
        for widget in frame_Cima.winfo_children():
            widget.destroy()
        for widget in frame_Centro.winfo_children():
            widget.destroy()
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        abrir_conta()
#-------------------------------------------------------------------------
def abrir_notas():
        for widget in frame_Cima.winfo_children():
            widget.destroy()
        for widget in frame_Centro.winfo_children():
            widget.destroy()
        for widget in frame_baixo.winfo_children():
            widget.destroy()
        incluir_notas()



#lIsta combobox##########################################################################

listanoletivo=["1° Série", "2° Série", "3° Série", "4° Série", "5° Série", "6° Série", "7° Série", "8° Série", "9° Série", "1° Ano", "2° Ano", "3° Ano"]
lb_ano_letivo= Label( text="Ano Letivo")

listalunos=[]
lb_alunos= Label( text="Alunos")

#travar numero de telefone##################################################################

def validar_entrada(entrada):
    return entrada.isdigit() and len(entrada)<=9
validacao_cmd= (frame_baixo.register(validar_entrada), '%P')



#COMANDO SENHA###############################################################################
def verificar_login():

    cpf= e_user.get()
    senha = e_senha.get()

    conn = sqlite3.connect('banco_de_dados.db')
    cursor = conn.cursor()
    cursor.execute("SELECT*FROM senha WHERE cpf=? AND senha=?", (cpf,senha))
    resultado= cursor.fetchall()
    if resultado:
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        abrir_pag_principal()
    else:
        messagebox.showerror("Erro", "CPF ou senha incorretos!")
    cursor.close()
#ATUALIZAR DADOS###########################################################################


#Login##############################################################################################################################
app_titulo= Label(frame_Cima, text="Login", compound=CENTER, padx=5, anchor=NW, font=('Verdana 20 bold'), bg=co0, fg=co3)
app_titulo.place(x=400, y=7)

app_linha= Label(frame_Cima, width=900, height=30, padx=5, anchor=NW, font=('Verdana 1'), bg=co2, fg=co1)
app_linha.place(x=0, y=70)
#-----------------------------------------------------------------------------------------------------------------------
l_user= Label(frame_baixo, text="CPF*", anchor=NW, font=('Ariel, 20'), bg=co0, fg=co3)
l_user.place(x=410, y=1)
e_user=Entry(frame_baixo, width=25, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
e_user.place(x=310, y=50)

l_senha= Label(frame_baixo, text="Senha*", anchor=NW, font=('Ariel, 20'), bg=co0, fg=co3)
l_senha.place(x=410, y=100)
e_senha=Entry(frame_baixo, width=25, justify=LEFT, font=("",15),show="*", highlightthickness=1, relief="solid")
e_senha.place(x=310, y=150)

b_enter = Button(frame_baixo, compound=LEFT, width=10, command= verificar_login,text="Entrar", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE) 
b_enter.grid(row=1, column=1, padx=400, pady=250, sticky=NSEW)

b_cadastrar = Button(frame_Centro, compound=LEFT, width=20,command=Cad_usuario, text="Cadastrar novo usuario", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_cadastrar.grid(row=1, column=1, padx=5, pady=5, sticky=NSEW)
#---------------------------------------------------------------------------------------------------------------------------------------------------
def cadastar_novo_usuario():

    def add_1():

        cpf=e_cpf.get()
        senha=e_senha.get()
        
        

        lista=[cpf,senha]

        for i in lista:
             if i =="":
                messagebox.showerror('Error', "Preencha todos os campos!")
                return
        insert_senha(cpf,senha)

        messagebox.showinfo('Sucesso', 'Senha inserido com sucesso')

        e_cpf.delete(0,END)
        e_senha.delete(0,END)
        
    app_titulo= Label(frame_Cima, text="Cadastrar Novo Usuario", compound=CENTER, padx=5, anchor=NW, font=('Verdana 20 bold'), bg=co0, fg=co3)
    app_titulo.place(x=100, y=7)

    app_linha= Label(frame_Cima, width=900, height=30, padx=5, anchor=NW, font=('Verdana 1'), bg=co2, fg=co1)
    app_linha.place(x=0, y=70)

    app_titulo= Label(frame_baixo, text="A senha é individual e tem que ter 8 digitos", compound=CENTER, padx=5, anchor=NW, font=('Arabic 20 bold'), bg=co0, fg=co3)
    app_titulo.place(x=100, y=250)
#-----------------------------------------------------------------------------------------------------------------------------------------------
    b_salvar = Button(frame_Centro, compound=LEFT, width=10, command=add_1, text="Salvar", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE) # type: ignore
    b_salvar.grid(row=1, column=1, padx=5, pady=5, sticky=NSEW)

    b_atualizar = Button(frame_Centro, compound=LEFT, width=10, text="Atualizar", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_atualizar.grid(row=1, column=2, padx=5, pady=5, sticky=NSEW)

    b_fechar = Button(frame_Centro,command=janela.destroy, compound=LEFT, width=10, text="fechar", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_fechar.grid(row=1, column=3, padx=5, pady=5, sticky=NSEW)
#---------------------------------------------------------------------------------------------------------------------------------------------

    l_cpf= Label(frame_baixo, text="CPF*", anchor=NW, font=('Ariel, 10'), bg=co0, fg=co3)
    l_cpf.place(x=10, y=1)
    e_cpf=Entry(frame_baixo, width=25, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_cpf.place(x=130, y=1)

    l_senha= Label(frame_baixo, text="Senha*", anchor=NW, font=('Ariel, 10') ,bg=co0, fg=co3)
    l_senha.place(x=10, y=40)
    e_senha=Entry(frame_baixo, width=25, justify=LEFT, font=("",15),show="*", highlightthickness=1, relief="solid")
    e_senha.place(x=130, y=40)


#######################################################################################################################################
def pag_principal():

    app_titulo= Label(frame_Cima, text="Projeto Piloto Vida Financeira das Crianças", compound=CENTER, padx=5, anchor=NW, font=('Verdana 20 bold'), bg=co0, fg=co3)
    app_titulo.place(x=100, y=7)

    app_linha= Label(frame_Cima, width=900, height=30, padx=5, anchor=NW, font=('Verdana 1'), bg=co2, fg=co1)
    app_linha.place(x=0, y=70)
#BOTÕES TELA PRINCIAPAL####################################################################################################
    app_titulo= Label(frame_baixo, text="Escola Aderbal da Silva", compound=CENTER, padx=5, anchor=NW, font=('Arabic 20 bold'), bg=co0, fg=co3)
    app_titulo.place(x=300, y=100)

    b_aluno = Button(frame_Centro, compound=LEFT, width=10, command= abrir_aluno, text="Alunos", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE) # type: ignore
    b_aluno.grid(row=1, column=1, padx=5, pady=5, sticky=NSEW)

    b_notas = Button(frame_Centro, compound=LEFT, width=10, command=abrir_notas,text="Notas", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_notas.grid(row=1, column=2, padx=5, pady=5, sticky=NSEW)

    b_conta = Button(frame_Centro, compound=LEFT, width=10, command=abrir_conta,text="Conta Virtual", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_conta.grid(row=1, column=3, padx=5, pady=5, sticky=NSEW)

    b_fechar = Button(frame_Centro,command=janela.destroy, compound=LEFT, width=10, text="fechar", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_fechar.grid(row=1, column=4, padx=5, pady=5, sticky=NSEW)

#NOVO ALUNO#########################################################################################################################################
def novo_aluno():
    
    app_titulo= Label(frame_Cima, text="Cadastrar Alunos", compound=CENTER, padx=5, anchor=NW, font=('Verdana 20 bold'), bg=co0, fg=co3)
    app_titulo.place(x=300, y=7)

    app_linha= Label(frame_Cima, width=900, height=50, padx=5, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    app_linha.place(x=0, y=70)
#-----------------------------------------------------------------------------------------------------------------------
    b_cadastrar = Button(frame_Centro, compound=LEFT, width=10, command= cadastrar_aluno, text="Cadastrar", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE) # type: ignore
    b_cadastrar.grid(row=1, column=1, padx=5, pady=5, sticky=NSEW)

    b_Atualizar = Button(frame_Centro, compound=LEFT, width=10,  text="Atualizar", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_Atualizar.grid(row=1, column=2, padx=5, pady=5, sticky=NSEW)

    #b_notas = Button(frame_Centro, compound=LEFT, width=10, text="", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    #b_notas.grid(row=1, column=3, padx=5, pady=5, sticky=NSEW)

    b_conta = Button(frame_Centro, compound=LEFT, width=10, command=abrir_conta, text="Conta Virtual", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_conta.grid(row=1, column=3, padx=5, pady=5, sticky=NSEW)

    b_fechar = Button(frame_Centro, compound=LEFT, width=10,command=voltar_pagina, text="fechar", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_fechar.grid(row=1, column=4, padx=5, pady=5, sticky=NSEW)

#---------------------------------------------------------------------------------------------------------------------------------------
def cadastar_aluno():

    def add_2():

        cpf=e_cpf.get()
        aluno=e_aluno.get()
        endereco=e_endereco.get()
        ddd=e_ddd.get()
        contato=e_contato.get()
        al=aletivo.get()
        dn=e_data_nasci.get()
        respo=e_responsavel.get()

        lista=[cpf,aluno,endereco,ddd,contato,al,dn,respo]

        for i in lista:
             if i =="":
                messagebox.showerror('Error', "Preencha todos os campos!")
                return
        insert_alunos(cpf,aluno,endereco,ddd,contato,al,dn,respo)

        messagebox.showinfo('Sucesso', 'Aluno inserido com sucesso')

        e_cpf.delete(0,END)
        e_aluno.delete(0,END)
        e_endereco.delete(0,END)
        e_ddd.delete(0,END)
        e_contato.delete(0,END)
        e_data_nasci.delete(0,END)
        e_responsavel.delete(0,END)


        

#----------------------------------------------------------------------------------------------------------------------------------------------------   
    b_salvar = Button(frame_Centro, compound=LEFT, width=10, command=add_2, text="Salvar", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=1, column=0, padx=5, pady=5, sticky=NSEW)   
     
    b_Atualizar = Button(frame_Centro, compound=LEFT, width=10, text="Atualizar", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_Atualizar.grid(row=1, column=1, padx=5, pady=5, sticky=NSEW)

    b_fechar = Button(frame_Centro, compound=LEFT, width=10,command=voltar_aluno, text="fechar", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_fechar.grid(row=1, column=2, padx=5, pady=5, sticky=NSEW)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
    
    l_cpf= Label(frame_baixo, text="CPF*", anchor=NW, font=('Ariel, 10'), bg=co0, fg=co3)
    l_cpf.place(x=10, y=1)
    e_cpf=Entry(frame_baixo, width=25, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_cpf.place(x=130, y=1)

    l_aluno= Label(frame_baixo, text="Aluno*", anchor=NW, font=('Ariel, 10'), bg=co0, fg=co3)
    l_aluno.place(x=10, y=40)
    e_aluno=Entry(frame_baixo, width=45, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_aluno.place(x=130, y=40)

    l_endereco= Label(frame_baixo, text="Endereço*", anchor=NW, font=('Ariel, 10'), bg=co0, fg=co3)
    l_endereco.place(x=10, y=80)
    e_endereco=Entry(frame_baixo, width=65, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_endereco.place(x=130, y=80)

    l_contato= Label(frame_baixo, text="Contato*", anchor=NW, font=('Ariel, 10'), bg=co0, fg=co3)
    l_contato.place(x=10, y=120)
    e_ddd=Entry(frame_baixo, width=5, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_ddd.place(x=120, y=120)
    e_contato=Entry(frame_baixo, width=15,validate="key", validatecommand=validacao_cmd, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_contato.place(x=150, y=120)
    

    aletivo=ttk.Combobox(frame_baixo, values=listanoletivo)
    aletivo.set("Ano Letivo")
    aletivo.place(x=130, y=160)

    l_data_nasci= Label(frame_baixo, text="Data de Nasc.*", anchor=NW, font=('Ariel, 10'), bg=co0, fg=co3)
    l_data_nasci.place(x=10, y=200)
    e_data_nasci=Entry(frame_baixo, width=15, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_data_nasci.place(x=130, y=200)

    l_responsavel= Label(frame_baixo, text="Responsavel Legal*", anchor=NW, font=('Ariel, 10'), bg=co0, fg=co3)
    l_responsavel.place(x=10, y=240)
    e_responsavel=Entry(frame_baixo, width=45, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_responsavel.place(x=130, y=240)


#ABRIR CONTA#############################################################################################################
def abrir_conta():

    app_titulo= Label(frame_Cima, text="Conta Corrente", compound=CENTER, padx=5, anchor=NW, font=('Verdana 20 bold'), bg=co0, fg=co3)
    app_titulo.place(x=250, y=7)

    app_linha= Label(frame_Cima, width=900, height=50, padx=5, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    app_linha.place(x=0, y=70)

    
#---------------------------------------------------------------------------------------------------------------------
    b_cadastrar = Button(frame_Centro, compound=LEFT, width=10, command=cadastar_aluno, text="Abrir Conta", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE) # type: ignore
    b_cadastrar.grid(row=1, column=1, padx=5, pady=5, sticky=NSEW)

    b_Atualizar = Button(frame_Centro, compound=LEFT, width=10, text="Atualizar", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_Atualizar.grid(row=1, column=2, padx=5, pady=5, sticky=NSEW)

    b_extrato = Button(frame_Centro, compound=LEFT, width=10, text="Extrato", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_extrato.grid(row=1, column=3, padx=5, pady=5, sticky=NSEW)

    b_depositar = Button(frame_Centro, compound=LEFT, width=10,  text="Depositar", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_depositar.grid(row=1, column=4, padx=5, pady=5, sticky=NSEW)

    b_ret = Button(frame_Centro, compound=LEFT, width=10, text="Retirada", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_ret.grid(row=1, column=5, padx=5, pady=5, sticky=NSEW)

    b_fechar = Button(frame_Centro, compound=LEFT, width=10,command=voltar_conta, text="fechar", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_fechar.grid(row=1, column=6, padx=5, pady=5, sticky=NSEW)



#NOTAS#########################################################################################################################################
def incluir_notas():

    def add_4():


        aluno=e_aluno.get()
        cb=aletivo.get()
        lp=e_lp.get()
        li=e_ingles.get()
        le=e_esp.get()
        me=e_mat.get()
        fi=e_fisic.get()
        al=e_quim.get()
        hi=e_História.get()
        go=e_geo.get()
        cie=e_cien.get()
        edf=e_ed_fisc.get()
        ar=e_artes.get()


        lista2=[aluno,cb,lp,li,le,me,fi,al,hi,go,cie,edf,ar]

        for i in lista2:
             if i =="":
                messagebox.showerror('Error', "Preencha todos os campos!")
                return
        insert_notas(aluno,cb,lp,li,le,me,fi,al,hi,go,cie,edf,ar)

        messagebox.showinfo('Sucesso', 'Notas inserido com sucesso')

        e_aluno.delete(0,END)
        e_lp.delete(0,END)
        e_ingles.delete(0,END)
        e_esp.delete(0,END)
        e_mat.delete(0,END)
        e_fisic.delete(0,END)
        e_quim.delete(0,END)
        e_História.delete(0,END)
        e_geo.delete(0,END)
        e_cien.delete(0,END)
        e_ed_fisc.delete(0,END)
        e_artes.delete(0,END)
        

#------------------------------------------------------------------------------------------------------------------------------------------
    app_titulo= Label(frame_Cima, text="Incluir Notas das Avaliações", compound=CENTER, padx=5, anchor=NW, font=('Verdana 20 bold'), bg=co0, fg=co3)
    app_titulo.place(x=250, y=7)

    app_linha= Label(frame_Cima, width=900, height=50, padx=5, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    app_linha.place(x=0, y=70)

    


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    b_cadastrar = Button(frame_Centro, compound=LEFT, width=10, command=add_4, text="Salvar", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE) # type: ignore
    b_cadastrar.grid(row=1, column=1, padx=5, pady=5, sticky=NSEW)

    b_Atualizar = Button(frame_Centro, compound=LEFT, width=10, text="Atualizar", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_Atualizar.grid(row=1, column=2, padx=5, pady=5, sticky=NSEW)

    b_enviar = Button(frame_Centro, compound=LEFT, width=10, text="Enviar", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_enviar.grid(row=1, column=3, padx=5, pady=5, sticky=NSEW)

    b_bol = Button(frame_Centro, compound=LEFT, width=10, text="Boletim", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_bol.grid(row=1, column=4, padx=5, pady=5, sticky=NSEW)

    b_fechar = Button(frame_Centro, compound=LEFT, width=10,command=voltar_pagina, text="fechar", bg=co4, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_fechar.grid(row=1, column=5, padx=5, pady=5, sticky=NSEW)
 #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    aletivo=ttk.Combobox(frame_baixo, values=listanoletivo)
    aletivo.set("Ano Letivo")
    aletivo.place(x=500, y=15)



    l_aluno= Label(frame_baixo, text="Aluno*", anchor=NW, font=('Ariel, 10'), bg=co0, fg=co3)
    l_aluno.place(x=10, y=1)
    e_aluno=Entry(frame_baixo, width=25, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_aluno.place(x=120, y=1)

    l_lp= Label(frame_baixo, text="Lingua Portuguesa", anchor=NW, font=('Ariel, 15'), bg=co0, fg=co3)
    l_lp.place(x=10, y=100)
    e_lp=Entry(frame_baixo, width=10, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_lp.place(x=200, y=100)

    l_ingles= Label(frame_baixo, text="Lingua Inglesa", anchor=NW, font=('Ariel, 15'), bg=co0, fg=co3)
    l_ingles.place(x=10, y=130)
    e_ingles=Entry(frame_baixo, width=10, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_ingles.place(x=200, y=130)

    l_esp= Label(frame_baixo, text="Lingua Espanhola", anchor=NW, font=('Ariel, 15'), bg=co0, fg=co3)
    l_esp.place(x=10, y=160)
    e_esp=Entry(frame_baixo, width=10, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_esp.place(x=200, y=160)

    l_mat= Label(frame_baixo, text="Matemática", anchor=NW, font=('Ariel, 15'), bg=co0, fg=co3)
    l_mat.place(x=10, y=190)
    e_mat=Entry(frame_baixo, width=10, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_mat.place(x=200, y=190)

    l_fisic= Label(frame_baixo, text="Fisica", anchor=NW, font=('Ariel, 15'), bg=co0, fg=co3)
    l_fisic.place(x=10, y=220)
    e_fisic=Entry(frame_baixo, width=10, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_fisic.place(x=200, y=220)

    l_quim= Label(frame_baixo, text="Quimica", anchor=NW, font=('Ariel, 15'), bg=co0, fg=co3)
    l_quim.place(x=10, y=250)
    e_quim=Entry(frame_baixo, width=10, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_quim.place(x=200, y=250)

    l_História= Label(frame_baixo, text="História", anchor=NW, font=('Ariel, 15'), bg=co0, fg=co3)
    l_História.place(x=400, y=100)
    e_História=Entry(frame_baixo, width=10, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_História.place(x=500, y=100)

    l_geo= Label(frame_baixo, text="Geografia", anchor=NW, font=('Ariel, 15'), bg=co0, fg=co3)
    l_geo.place(x=400, y=130)
    e_geo=Entry(frame_baixo, width=10, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_geo.place(x=500, y=130)

    l_cien= Label(frame_baixo, text="Ciências", anchor=NW, font=('Ariel, 15'), bg=co0, fg=co3)
    l_cien.place(x=400, y=160)
    e_cien=Entry(frame_baixo, width=10, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_cien.place(x=500, y=160)

    l_ed_fisc= Label(frame_baixo, text="Ed. Física", anchor=NW, font=('Ariel, 15'), bg=co0, fg=co3)
    l_ed_fisc.place(x=400, y=190)
    e_ed_fisc=Entry(frame_baixo, width=10, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_ed_fisc.place(x=500, y=190)

    l_artes= Label(frame_baixo, text="Artes", anchor=NW, font=('Ariel, 15'), bg=co0, fg=co3)
    l_artes.place(x=400, y=220)
    e_artes=Entry(frame_baixo, width=10, justify=LEFT, font=("",15), highlightthickness=1, relief="solid")
    e_artes.place(x=500, y=220)
    
    
#CONTA VIRTUAL##############################################################################################################

     
    



    
     




    
   







janela.mainloop()