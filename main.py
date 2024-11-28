from modulos import*
from func import func
from placeholder import EntPlaceHolder




janela=tix.Tk()

class application(func):
    
    def __init__(self):
        self.janela=janela
        self.tela()
        
        self.frame_tela()
        self.menu()
        
        
        janela.mainloop()
        
#################################################################################################
#--------------------------CONSTRUÇÃ0------------------------------------------------------------
########################################################################################################
#--------------------------------CEP-------------------------------------------
    def cepCorreiros(self):
        try:
            
            self.logradouro_entry.delete(0, END)
            self.bairro_entry.delete(0, END)
            self.cidade_entry.delete(0, END)
            
            zipcode = self.cep_entry.get()
            dadosCep = pycep_correios.get_address_from_cep(zipcode)
            self.logradouro_entry.insert(END, dadosCep['logradouro'])
            self.bairro_entry.insert(END, dadosCep['bairro'])
            self.cidade_entry.insert(END, dadosCep['cidade'])
            
        except:
            messagebox.showinfo('Titulo da janela', "Cep não encontrado")





#----------------------------------TELA-------------------------------------
    def tela(self):
        self.janela.title("Escola Estadual")
        self.janela.configure(background=co0)
        self.janela.geometry("900x700")
        self.janela.resizable(FALSE,FALSE)
        self.janela.maxsize(width=900, height=700)
        self.janela.minsize(width=500, height=400)
 
 #------------------------------------FRAME-----------------------------------------      
    def frame_tela(self):
        
        self.frame_cima = Frame(self.janela, bd=4, bg=co1, highlightbackground=co2, highlightthickness=3)
        self.frame_cima.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        
        self.frame_baixo= Frame(self.janela, bd=4, bg=co1, highlightbackground=co2, highlightthickness=3 )
        self.frame_baixo.place(relx=0.02, rely=0.50, relwidth=0.96, relheight=0.46)
######################################################################################################################
 
#---------------------------------CADASTRAR ALUNOS---------------------------------------------------------
    def cad_alunos(self):
        
        
        #Botões
        self.gravar= Button(self.frame_cima, text="Gravar",bd=2,bg=co1,fg=co11, font=('verdana',10,"bold"))
        self.gravar.place(relx=0.0, rely=0.0, relwidth=0.1, relheight=0.15)

        self.atualizar= Button(self.frame_cima, text="Atualizar",bd=2,bg=co1,fg=co11, font=('verdana',10,"bold"))
        self.atualizar.place(relx=0.10, rely=0.0, relwidth=0.1, relheight=0.15)

        self.limpar= Button(self.frame_cima,command=self.limpa_tela_alunos,text="Limpar",bd=2,bg=co1,fg=co11, font=('verdana',10,"bold"))
        self.limpar.place(relx=0.20, rely=0.0, relwidth=0.1, relheight=0.15)

        self.apagar= Button(self.frame_cima, text="Apagar",bd=2,bg=co1,fg=co11, font=('verdana',10,"bold"))
        self.apagar.place(relx=0.30, rely=0.0, relwidth=0.1, relheight=0.15)

        self.buscar= Button(self.frame_cima, text="Buscar",bd=2,bg=co1,fg=co11, font=('verdana',10,"bold"))
        self.buscar.place(relx=0.40, rely=0.0, relwidth=0.1, relheight=0.15)

        self.buscar_cep= Button(self.frame_cima,command=self.cepCorreiros,text="Buscar CEP",bd=2,bg=co1,fg=co11, font=('verdana',10,"bold"))
        self.buscar_cep.place(relx=0.50, rely=0.0, relwidth=0.1, relheight=0.15)

        self.imprimir= Button(self.frame_cima, text="Imprimir",bd=2,bg=co1,fg=co11, font=('verdana',10,"bold"))
        self.imprimir.place(relx=0.60, rely=0.0, relwidth=0.1, relheight=0.15)

        #area digitavel
        self.lb_matricula = Label(self.frame_cima,text="Matrícula", bg=co1, fg=co11)
        self.lb_matricula.place(relx=0.01,rely=0.2)
        self.matricula_entry=Entry(self.frame_cima)
        self.matricula_entry.place(relx=0.10,rely=0.2,relwidth=0.08)

        self.lb_cpf = Label(self.frame_cima,text="CPF:",bg=co1,fg=co11)
        self.lb_cpf.place(relx=0.01,rely=0.27)
        self.cpf_entry= EntPlaceHolder(self.frame_cima,"Digite o CPF")
        self.cpf_entry.place(relx=0.10, rely=0.27,relwidth=0.2)

        self.lb_nome = Label(self.frame_cima,text="Nome:",bg=co1,fg=co11)
        self.lb_nome.place(relx=0.01,rely=0.34)
        self.nome_entry= EntPlaceHolder(self.frame_cima,"Digite o nome completo")
        self.nome_entry.place(relx=0.10, rely=0.34,relwidth=0.5)

        self.lb_nome_mae = Label(self.frame_cima,text="Mãe:",bg=co1,fg=co11)
        self.lb_nome_mae.place(relx=0.01,rely=0.41)
        self.nome_mae_entry= EntPlaceHolder(self.frame_cima,"Digite o nome completo")
        self.nome_mae_entry.place(relx=0.10, rely=0.41,relwidth=0.5)

        self.lb_nome_pai = Label(self.frame_cima,text="Pai:",bg=co1,fg=co11)
        self.lb_nome_pai.place(relx=0.01,rely=0.48)
        self.nome_pai_entry= EntPlaceHolder(self.frame_cima,"Digite o nome completo")
        self.nome_pai_entry.place(relx=0.10, rely=0.48,relwidth=0.5)

        self.lb_contato = Label(self.frame_cima,text="Contato:",bg=co1,fg=co11)
        self.lb_contato.place(relx=0.01,rely=0.55)
        self.contato_entry= EntPlaceHolder(self.frame_cima,"Digite o contato com DDD")
        self.contato_entry.place(relx=0.10, rely=0.55,relwidth=0.2)

        self.lb_nascimento = Label(self.frame_cima,text="Nascimento:",bg=co1,fg=co11)
        self.lb_nascimento.place(relx=0.01,rely=0.62)
        self.nascimento_entry= EntPlaceHolder(self.frame_cima,"Digite a data de nascimento")
        self.nascimento_entry.place(relx=0.10, rely=0.62,relwidth=0.2)
        
        self.lb_ano_letivo = Label(self.frame_cima,text="Série:",bg=co1,fg=co11)
        self.lb_ano_letivo.place(relx=0.01,rely=0.69)
        self.ano_letivo_entry= EntPlaceHolder(self.frame_cima,"Digite o ano letivo")
        self.ano_letivo_entry.place(relx=0.10, rely=0.69,relwidth=0.2)

        self.lb_cep = Label(self.frame_cima,text="CEP:", bg=co1, fg=co11)
        self.lb_cep.place(relx=0.35,rely=0.69)
        self.cep_entry=EntPlaceHolder(self.frame_cima, "Digite o CEP")
        self.cep_entry.place(relx=0.40,rely=0.69,relwidth=0.1)

        self.lb_logradouro = Label(self.frame_cima,text="Logradouro:",bg=co1,fg=co11)
        self.lb_logradouro.place(relx=0.01,rely=0.76)
        self.logradouro_entry= EntPlaceHolder(self.frame_cima,"Digite o endereço completo")
        self.logradouro_entry.place(relx=0.10, rely=0.76,relwidth=0.5)

        self.lb_numero = Label(self.frame_cima,text="N°:",bg=co1,fg=co11)
        self.lb_numero.place(relx=0.62,rely=0.76)
        self.numero_entry= EntPlaceHolder(self.frame_cima," Numero")
        self.numero_entry.place(relx=0.65, rely=0.76,relwidth=0.1)

        self.lb_bairro = Label(self.frame_cima,text="Bairro:",bg=co1,fg=co11)
        self.lb_bairro.place(relx=0.01,rely=0.83)
        self.bairro_entry= EntPlaceHolder(self.frame_cima,"Digite o bairro")
        self.bairro_entry.place(relx=0.10, rely=0.83,relwidth=0.5)

        self.lb_cidade = Label(self.frame_cima,text="Cidade:",bg=co1,fg=co11)
        self.lb_cidade.place(relx=0.01,rely=0.90)
        self.cidade_entry= EntPlaceHolder(self.frame_cima,"Digite o nome completo")
        self.cidade_entry.place(relx=0.10, rely=0.90,relwidth=0.5)
        
        self.listalunos= ttk.Treeview(self.frame_baixo, height=3, columns=("col1", "col2","col3","col4","col5","col6","col7","col8","col9","col10","col11","col12","col13"))
        self.listalunos.heading("#0", text="")
        self.listalunos.heading("#1", text="Matricula")
        self.listalunos.heading("#2", text="CPF")
        self.listalunos.heading("#3", text="Nome")
        self.listalunos.heading("#4", text="Mãe")
        self.listalunos.heading("#5", text="Pai")
        self.listalunos.heading("#6", text="Contato")
        self.listalunos.heading("#7", text="Nascimento")
        self.listalunos.heading("#8", text="Ano Letivo")
        self.listalunos.heading("#9", text="CEP")
        self.listalunos.heading("#10", text="Logradouro")
        self.listalunos.heading("#11", text="Numero")
        self.listalunos.heading("#12", text="Bairro")
        self.listalunos.heading("#13", text="Cidade")
        
        self.listalunos.column("#0", width=1)
        self.listalunos.column("#1", width=50)
        self.listalunos.column("#2", width=200)
        self.listalunos.column("#3", width=125)
        self.listalunos.column("#4", width=125)
        self.listalunos.column("#5", width=125)
        self.listalunos.column("#6", width=125)
        self.listalunos.column("#7", width=125)
        self.listalunos.column("#8", width=125)
        self.listalunos.column("#9", width=125)
        self.listalunos.column("#10", width=125)
        self.listalunos.column("#11", width=125)
        self.listalunos.column("#12", width=125)
        self.listalunos.column("#13", width=125)
        
        self.listalunos.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)
       
        self.scroolista = Scrollbar(self.frame_baixo, orient='vertical')
        self.listalunos.configure(vscroll=self.scroolista.set)
        self.scroolista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.listalunos.bind("<Double-1")
        
        
        
        

#------------------------------CADASTRAR PROFESSOR------------------------------------       
    def cad_professor(self):
        
        
        #Botões
        self.gravar= Button(self.frame_cima, text="Gravar",bd=2,bg=co1,fg=co11, font=('verdana',10,"bold"))
        self.gravar.place(relx=0.0, rely=0.0, relwidth=0.1, relheight=0.15)

        self.atualizar= Button(self.frame_cima, text="Atualizar",bd=2,bg=co1,fg=co11, font=('verdana',10,"bold"))
        self.atualizar.place(relx=0.10, rely=0.0, relwidth=0.1, relheight=0.15)

        self.limpar= Button(self.frame_cima,command=self.limpa_tela_professor,text="Limpar",bd=2,bg=co1,fg=co11, font=('verdana',10,"bold"))
        self.limpar.place(relx=0.20, rely=0.0, relwidth=0.1, relheight=0.15)

        self.apagar= Button(self.frame_cima, text="Apagar",bd=2,bg=co1,fg=co11, font=('verdana',10,"bold"))
        self.apagar.place(relx=0.30, rely=0.0, relwidth=0.1, relheight=0.15)

        self.buscar= Button(self.frame_cima, text="Buscar",bd=2,bg=co1,fg=co11, font=('verdana',10,"bold"))
        self.buscar.place(relx=0.40, rely=0.0, relwidth=0.1, relheight=0.15)

        self.buscar_cep= Button(self.frame_cima,command=self.cepCorreiros,text="Buscar CEP",bd=2,bg=co1,fg=co11, font=('verdana',10,"bold"))
        self.buscar_cep.place(relx=0.50, rely=0.0, relwidth=0.1, relheight=0.15)

        self.imprimir= Button(self.frame_cima, text="Imprimir",bd=2,bg=co1,fg=co11, font=('verdana',10,"bold"))
        self.imprimir.place(relx=0.60, rely=0.0, relwidth=0.1, relheight=0.15)

        #area digitavel
        self.lb_matricula = Label(self.frame_cima,text="Matrícula", bg=co1, fg=co11)
        self.lb_matricula.place(relx=0.01,rely=0.2)
        self.matricula_entry=Entry(self.frame_cima)
        self.matricula_entry.place(relx=0.10,rely=0.2,relwidth=0.08)

        self.lb_cpf = Label(self.frame_cima,text="CPF:",bg=co1,fg=co11)
        self.lb_cpf.place(relx=0.01,rely=0.27)
        self.cpf_entry= EntPlaceHolder(self.frame_cima,"Digite o CPF")
        self.cpf_entry.place(relx=0.10, rely=0.27,relwidth=0.2)

        self.lb_nome = Label(self.frame_cima,text="Nome:",bg=co1,fg=co11)
        self.lb_nome.place(relx=0.01,rely=0.34)
        self.nome_entry= EntPlaceHolder(self.frame_cima,"Digite o nome completo")
        self.nome_entry.place(relx=0.10, rely=0.34,relwidth=0.5)

        self.lb_nome_mae = Label(self.frame_cima,text="Mãe:",bg=co1,fg=co11)
        self.lb_nome_mae.place(relx=0.01,rely=0.41)
        self.nome_mae_entry= EntPlaceHolder(self.frame_cima,"Digite o nome completo")
        self.nome_mae_entry.place(relx=0.10, rely=0.41,relwidth=0.5)

        self.lb_nome_pai = Label(self.frame_cima,text="Pai:",bg=co1,fg=co11)
        self.lb_nome_pai.place(relx=0.01,rely=0.48)
        self.nome_pai_entry= EntPlaceHolder(self.frame_cima,"Digite o nome completo")
        self.nome_pai_entry.place(relx=0.10, rely=0.48,relwidth=0.5)

        self.lb_contato = Label(self.frame_cima,text="Contato:",bg=co1,fg=co11)
        self.lb_contato.place(relx=0.01,rely=0.55)
        self.contato_entry= EntPlaceHolder(self.frame_cima,"Digite o contato com DDD")
        self.contato_entry.place(relx=0.10, rely=0.55,relwidth=0.2)

        self.lb_nascimento = Label(self.frame_cima,text="Nascimento:",bg=co1,fg=co11)
        self.lb_nascimento.place(relx=0.01,rely=0.62)
        self.nascimento_entry= EntPlaceHolder(self.frame_cima,"Digite a data de nascimento")
        self.nascimento_entry.place(relx=0.10, rely=0.62,relwidth=0.2)
        
        self.lb_materia = Label(self.frame_cima,text="Matéria:",bg=co1,fg=co11)
        self.lb_materia.place(relx=0.01,rely=0.69)
        self.materia_entry= EntPlaceHolder(self.frame_cima,"Digite o ano letivo")
        self.materia_entry.place(relx=0.10, rely=0.69,relwidth=0.2)

        self.lb_cep = Label(self.frame_cima,text="CEP:", bg=co1, fg=co11)
        self.lb_cep.place(relx=0.35,rely=0.69)
        self.cep_entry=EntPlaceHolder(self.frame_cima, "Digite o CEP")
        self.cep_entry.place(relx=0.40,rely=0.69,relwidth=0.1)

        self.lb_logradouro = Label(self.frame_cima,text="Logradouro:",bg=co1,fg=co11)
        self.lb_logradouro.place(relx=0.01,rely=0.76)
        self.logradouro_entry= EntPlaceHolder(self.frame_cima,"Digite o endereço completo")
        self.logradouro_entry.place(relx=0.10, rely=0.76,relwidth=0.5)

        self.lb_numero = Label(self.frame_cima,text="N°:",bg=co1,fg=co11)
        self.lb_numero.place(relx=0.62,rely=0.76)
        self.numero_entry= EntPlaceHolder(self.frame_cima," Numero")
        self.numero_entry.place(relx=0.65, rely=0.76,relwidth=0.1)

        self.lb_bairro = Label(self.frame_cima,text="Bairro:",bg=co1,fg=co11)
        self.lb_bairro.place(relx=0.01,rely=0.83)
        self.bairro_entry= EntPlaceHolder(self.frame_cima,"Digite o bairro")
        self.bairro_entry.place(relx=0.10, rely=0.83,relwidth=0.5)

        self.lb_cidade = Label(self.frame_cima,text="Cidade:",bg=co1,fg=co11)
        self.lb_cidade.place(relx=0.01,rely=0.90)
        self.cidade_entry= EntPlaceHolder(self.frame_cima,"Digite o nome completo")
        self.cidade_entry.place(relx=0.10, rely=0.90,relwidth=0.5)









#-------------------------------------MENU------------------------------------------------------------------
    def menu(self):
        
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu1 = Menu(menubar)
        
        def quit(): self.janela.destroy()
        
        menubar.add_cascade(label= "Alunos", menu= filemenu)
        menubar.add_cascade(label= "Professor", menu=filemenu1)
        
        filemenu.add_cascade(label= "Cadastrar", command= self.cad_alunos)
        filemenu.add_cascade(label="Sair", command=quit)

        filemenu1.add_cascade(label= "Cadastrar", command=self.cad_professor)




application()
        