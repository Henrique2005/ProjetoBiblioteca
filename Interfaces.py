from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from Cliente import Cliente
from Livro import Livro


def isnumber(value):
    try:
        float(value)
    except ValueError:
        return False
    return True


def mensagemConfirmacao(titulo, texto):
    msg = messagebox.askquestion(titulo, texto)
    return msg


def mensagem(titulo, texto):
    messagebox.showinfo(titulo, texto)


def alerta(titulo, texto):
    messagebox.showwarning(titulo, texto)


def erro(titulo, texto):
    messagebox.showerror(titulo, texto)


def tela_de_login(biblioteca, janela=None):
    if janela != None:
        janela.destroy()
    master = Tk()
    master.title("Login da Biblioteca")
    largura = 400
    altura = 200
    dimensoes = f"{largura}x{altura}"

    # Configurar as dimensões da janela
    master.geometry(dimensoes)

    fontePadrao = ("Arial", "10")
    primeiroContainer = Frame(master)
    primeiroContainer["pady"] = 10
    primeiroContainer.pack()

    segundoContainer = Frame(master)
    segundoContainer["padx"] = 20
    segundoContainer.pack()

    terceiroContainer = Frame(master)
    terceiroContainer["padx"] = 20
    terceiroContainer["pady"] = 10
    terceiroContainer.pack()

    quartoContainer = Frame(master)
    quartoContainer["pady"] = 20
    quartoContainer.pack()

    titulo = Label(primeiroContainer, text="Dados do usuário")
    titulo["font"] = ("Verdana", "10", "bold")
    titulo.pack()

    cpfLabel = Label(segundoContainer, text="CPF:  ", font=fontePadrao)
    cpfLabel.pack(side=LEFT)

    cpf = Entry(segundoContainer)
    cpf["width"] = 30
    cpf["font"] = fontePadrao
    cpf.pack(side=LEFT)

    senhaLabel = Label(terceiroContainer, text="Senha:", font=fontePadrao)
    senhaLabel.pack(side=LEFT)

    senha = Entry(terceiroContainer)
    senha["width"] = 30
    senha["font"] = fontePadrao
    senha["show"] = "*"
    senha.pack(side=LEFT)

    autenticar = Button(quartoContainer)
    autenticar["text"] = "Login"
    autenticar["font"] = ("Calibri", "9")
    autenticar["width"] = 12
    autenticar["command"] = lambda: verificaLogin(cpf.get(), senha.get(), master, biblioteca)
    autenticar.pack(side=LEFT)

    cadastrar = Button(quartoContainer)
    cadastrar["text"] = "Cadastre-se"
    cadastrar["font"] = ("Calibri", "9")
    cadastrar["width"] = 12
    cadastrar["command"] = lambda: tela_de_cadastro_cliente(biblioteca, master)
    cadastrar.pack(side=RIGHT)

    mensagem = Label(quartoContainer, text="", font=fontePadrao)
    mensagem.pack()
    master.mainloop()


# Método verificar senha
def verificaLogin(cpf, senha, janela, biblioteca):
    listaDeClientes = biblioteca.getListaClientes()
    listaDeAdministradores = biblioteca.getListaAdministradores()
    for i in listaDeAdministradores:
        if i.getCpf() == cpf and i.getSenha() == senha:
            print(f"--> administrador logou <--")
            i.imprimeRelatorio()
            tela_principal_adm(i, biblioteca, janela)
            return True
    for i in listaDeClientes:
        if i.getCpf() == cpf:
            print(f" --> cliente logado <-- ")
            i.imprimeRelatorio()
            tela_principal_cliente(i, biblioteca, janela)
            return True

    erro("Login", "CPF ou senha inválidos!")
    return False


def tela_de_cadastro_cliente(biblioteca, janela):
    janela.destroy()

    janelaCadastro = Tk()
    janelaCadastro.title("Cadastro de Cliente")
    largura = 500
    altura = 300
    dimensoes = f"{largura}x{altura}"

    # Configurar as dimensões da janela
    janelaCadastro.geometry(dimensoes)

    fontePadrao = ("Arial", "10")
    tituloContainer = Frame(janelaCadastro)
    tituloContainer["pady"] = 10
    tituloContainer.pack()

    cpfContainer = Frame(janelaCadastro)
    cpfContainer["padx"] = 20
    cpfContainer["pady"] = 10
    cpfContainer.pack()

    nomeContainer = Frame(janelaCadastro)
    nomeContainer["padx"] = 20
    nomeContainer["pady"] = 10
    nomeContainer.pack()

    senhaContainer = Frame(janelaCadastro)
    senhaContainer["padx"] = 20
    senhaContainer["pady"] = 10
    senhaContainer.pack()

    botoesContainer = Frame(janelaCadastro)
    botoesContainer["pady"] = 20
    botoesContainer.pack()

    titulo = Label(tituloContainer, text="Dados do cliente")
    titulo["font"] = ("Verdana", "10", "bold")
    titulo.pack()

    cpfLabel = Label(cpfContainer,text="CPF:  ", font=fontePadrao)
    cpfLabel.pack(side=LEFT)

    cpf = Entry(cpfContainer)
    cpf["width"] = 30
    cpf["font"] = fontePadrao
    cpf.pack(side=LEFT)

    nomeLabel = Label(nomeContainer, text="Nome:", font=fontePadrao)
    nomeLabel.pack(side=LEFT)

    nome = Entry(nomeContainer)
    nome["width"] = 30
    nome["font"] = fontePadrao
    nome.pack(side=LEFT)

    senhaLabel = Label(senhaContainer, text="Senha:", font=fontePadrao)
    senhaLabel.pack(side=LEFT)

    senha = Entry(senhaContainer)
    senha["width"] = 30
    senha["font"] = fontePadrao
    senha["show"] = "*"
    senha.pack(side=LEFT)

    cadastrar = Button(botoesContainer)
    cadastrar["text"] = "Cadastrar"
    cadastrar["font"] = ("Calibri", "9")
    cadastrar["width"] = 15
    cadastrar["command"] = lambda: cadastrarCliente(cpf.get().strip(), nome.get().strip(), senha.get().strip(), biblioteca, janelaCadastro)
    cadastrar.pack(side=LEFT)

    voltar = Button(botoesContainer)
    voltar["text"] = "Voltar"
    voltar["font"] = ("Calibri", "9")
    voltar["width"] = 15
    voltar["command"] = lambda: tela_de_login(biblioteca, janelaCadastro)
    voltar.pack(side=RIGHT)

    janelaCadastro.mainloop()


#Método para cadastrar clientes
def cadastrarCliente(cpf, nome, senha, biblioteca, janela):
    if cpf == "" or nome == "" or senha == "":  # verifica se os campos estão vazios
        erro("Erro no cadastro", "Digite todos os campos!")
        return False
    else:
        if len(cpf) != 11:
            erro("Erro no cadastro", "O CPF precisa ter 11 caracteres!")
            return False
        else:
            listaDeClientes = biblioteca.getListaClientes()
            listaDeAdministradores = biblioteca.getListaAdministradores()
            contador = 0
            for i in listaDeClientes:
                if i.getCpf() == cpf:
                    contador += 1
            for i in listaDeAdministradores:
                if i.getCpf() == cpf:
                    contador += 1
            if contador != 0:
                erro("Erro no cadastro", "Não foi possível realizar o cadastro. O CPF digitado já está cadastrado!")
                return False
            else:
                cliente = Cliente(nome, cpf, senha, 0, [])
                biblioteca.adicionarCliente(cliente)
                mensagem("Cadastro de cliente", "Cadastro realizado com sucesso!")
                janela.destroy()
                tela_de_login(biblioteca)
                return True


def tela_principal_adm(adm, biblioteca, janela):
    janela.destroy()

    tela_adm = Tk()
    tela_adm.title("Biblioteca - Administrador")
    largura = 530
    altura = 400
    dimensoes = f"{largura}x{altura}"

    # Configurar as dimensões da janela
    tela_adm.geometry(dimensoes)

    tituloContainer = Frame(tela_adm)
    tituloContainer["pady"] = 10
    tituloContainer.pack()

    buscaContainer = Frame(tela_adm)
    buscaContainer["pady"] = 10
    buscaContainer.pack()

    tableContainer = Frame(tela_adm)
    tableContainer.pack(fill=BOTH, expand=True)

    botoesContainer = Frame(tela_adm)
    botoesContainer["pady"] = 20
    botoesContainer.pack()

    titulo = Label(tituloContainer, text="Livros da Biblioteca")
    titulo["font"] = ("Verdana", "10", "bold")
    titulo.pack(side=LEFT)

    buscaEntrada = Entry(buscaContainer)
    buscaEntrada["width"] = 60
    buscaEntrada.pack(side=LEFT)

    busca = Button(buscaContainer)
    busca["text"] = "Buscar pelo nome"
    busca["font"] = ("Calibri", "9")
    busca["width"] = 25
    busca["command"] = lambda: search(buscaEntrada.get(), biblioteca, table)
    busca.pack(side=RIGHT)

    sair = Button(tela_adm)
    sair["text"] = "Sair"
    sair["font"] = ("Calibri", "9")
    sair["width"] = 10
    sair["command"] = lambda: tela_de_login(biblioteca, tela_adm)

    sair.place(x=10, y=10)

    table = ttk.Treeview(tableContainer, columns=("Codigo", "Nome", "Situacao", "Penalidade"), show="headings")

    # Criar cabeçalho da tabela
    table.heading('#0', text='', anchor=W)
    table.heading('Codigo', text='Código', anchor=CENTER)
    table.heading('Nome', text='Nome', anchor=CENTER)
    table.heading('Situacao', text='Situação', anchor=CENTER)
    table.heading('Penalidade', text='Penalidade p/dia de atraso em R$', anchor=CENTER)

    # Formatar as colunas
    table.column('#0', width=0, stretch= NO)
    table.column('Codigo', anchor=CENTER, width=100)
    table.column('Nome', anchor=CENTER, width=100)
    table.column('Situacao', anchor=CENTER, width=100)
    table.column('Penalidade', anchor=CENTER, width=220)

    scrollbar = ttk.Scrollbar(table, orient="vertical", command=table.yview)
    table.configure(yscroll=scrollbar.set)

    for i in biblioteca.getListaLivros():
        row = [i.getCodigo(), i.getNome(), i.getSituacao(), i.getPenalidade()]
        table.insert("", "end", values=row)

    table.pack(fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    cadastrar = Button(botoesContainer)
    cadastrar["text"] = "Cadastrar"
    cadastrar["font"] = ("Calibri", "9")
    cadastrar["width"] = 15
    cadastrar["command"] = lambda: tela_cadastro_livro(adm, biblioteca, table)
    cadastrar.pack(side=LEFT)

    editar = Button(botoesContainer)
    editar["text"] = "Editar"
    editar["font"] = ("Calibri", "9")
    editar["width"] = 15
    editar["command"] = lambda: tela_edicao_livro(adm, biblioteca, table, table.focus())
    editar.pack(side=LEFT)

    excluir = Button(botoesContainer)
    excluir["text"] = "Excluir"
    excluir["font"] = ("Calibri", "9")
    excluir["width"] = 15
    excluir["command"] = lambda: excluirLivro(table.focus(), biblioteca, adm, table)
    excluir.pack(side=RIGHT)

    tela_adm.mainloop()


def search(entrada, biblioteca, table):
    # Limpar a tabela antes de realizar a pesquisa
    table.delete(*table.get_children())

    # Realizar a pesquisa na tabela
    for livro in biblioteca.getListaLivros():
        if entrada.lower() in livro.getNome().lower():  # Comparar os nomes ignorando o case
            row = [livro.getCodigo(), livro.getNome(), livro.getSituacao(), livro.getPenalidade()]
            table.insert("", "end", values=row)


def excluirLivro(itemSelecionado, biblioteca, adm, table):
    if itemSelecionado == "":
        return False
    valores = table.item(itemSelecionado)['values']
    confirmacao = mensagemConfirmacao("Confirmação", f'Tem certeza que deseja excluir o livro "{valores[1]}" (código: {valores[0]})?')
    if confirmacao == 'yes':
        operacao = adm.excluirLivro(biblioteca, valores[0])
        if operacao:
            table.delete(itemSelecionado)


def tela_cadastro_livro(adm, biblioteca, table):

    janelaCadastroLivro = Tk()
    janelaCadastroLivro.title("Cadastro de Livro")
    largura = 500
    altura = 300
    dimensoes = f"{largura}x{altura}"

    # Configurar as dimensões da janela
    janelaCadastroLivro.geometry(dimensoes)

    fontePadrao = ("Arial", "10")
    tituloContainer = Frame(janelaCadastroLivro)
    tituloContainer["pady"] = 10
    tituloContainer.pack()

    nomeContainer = Frame(janelaCadastroLivro)
    nomeContainer["padx"] = 20
    nomeContainer["pady"] = 10
    nomeContainer.pack()

    penalidadeContainer = Frame(janelaCadastroLivro)
    penalidadeContainer["padx"] = 20
    penalidadeContainer["pady"] = 10
    penalidadeContainer.pack()

    botoesContainer = Frame(janelaCadastroLivro)
    botoesContainer["pady"] = 20
    botoesContainer.pack()

    titulo = Label(tituloContainer, text="Dados do livro")
    titulo["font"] = ("Verdana", "10", "bold")
    titulo.pack()

    nomeLabel = Label(nomeContainer, text="Nome:", font=fontePadrao)
    nomeLabel.pack(side=LEFT)

    nome = Entry(nomeContainer)
    nome["width"] = 30
    nome["font"] = fontePadrao
    nome.pack(side=LEFT)

    penalidadeLabel = Label(penalidadeContainer, text="Penalidade p/ dia em R$:", font=fontePadrao)
    penalidadeLabel.pack(side=LEFT)

    penalidade = Entry(penalidadeContainer)
    penalidade["width"] = 15
    penalidade["font"] = fontePadrao
    penalidade.pack(side=LEFT)

    cadastrar = Button(botoesContainer)
    cadastrar["text"] = "Cadastrar"
    cadastrar["font"] = ("Calibri", "9")
    cadastrar["width"] = 15
    cadastrar["command"] = lambda: cadastrarLivro(nome.get().strip(), penalidade.get().strip(), biblioteca, adm, janelaCadastroLivro, table)
    cadastrar.pack(side=LEFT)

    voltar = Button(botoesContainer)
    voltar["text"] = "Voltar"
    voltar["font"] = ("Calibri", "9")
    voltar["width"] = 15
    voltar["command"] = lambda: janelaCadastroLivro.destroy()
    voltar.pack(side=RIGHT)

    janelaCadastroLivro.mainloop()


def cadastrarLivro(nome, penalidade, biblioteca, adm, janela, table):
    if nome == "" or penalidade == "":  # verifica se os campos estão vazios
        erro("Erro no cadastro", "Digite todos os campos!")
        return False
    else:
        if not isnumber(penalidade):
            erro("Erro no cadastro", "Digite apenas números na penalidade!")
            return False
        else:
            livro = Livro(nome, "Disponível", float(penalidade))
            adm.cadastrarLivro(biblioteca, livro)
            row = [livro.getCodigo(), livro.getNome(), livro.getSituacao(), livro.getPenalidade()]
            table.insert("", "end", values=row)
            janela.destroy()
            return True


def tela_edicao_livro(adm, biblioteca, table, selected_item=None):
    if selected_item == "":
        return False

    values = table.item(selected_item)['values']

    janelaEditarLivro = Tk()
    janelaEditarLivro.title("Edição de Livro")
    largura = 500
    altura = 300
    dimensoes = f"{largura}x{altura}"

    # Configurar as dimensões da janela
    janelaEditarLivro.geometry(dimensoes)

    fontePadrao = ("Arial", "10")
    tituloContainer = Frame(janelaEditarLivro)
    tituloContainer["pady"] = 10
    tituloContainer.pack()

    nomeContainer = Frame(janelaEditarLivro)
    nomeContainer["padx"] = 20
    nomeContainer["pady"] = 10
    nomeContainer.pack()

    penalidadeContainer = Frame(janelaEditarLivro)
    penalidadeContainer["padx"] = 20
    penalidadeContainer["pady"] = 10
    penalidadeContainer.pack()

    botoesContainer = Frame(janelaEditarLivro)
    botoesContainer["pady"] = 20
    botoesContainer.pack()

    titulo = Label(tituloContainer, text="Dados do livro")
    titulo["font"] = ("Verdana", "10", "bold")
    titulo.pack()

    nomeLabel = Label(nomeContainer, text="Nome:", font=fontePadrao)
    nomeLabel.pack(side=LEFT)

    nome = Entry(nomeContainer)
    nome["width"] = 30
    nome["font"] = fontePadrao
    nome.insert(END, values[1])
    nome.pack(side=LEFT)

    penalidadeLabel = Label(penalidadeContainer, text="Penalidade p/ dia em R$:", font=fontePadrao)
    penalidadeLabel.pack(side=LEFT)

    penalidade = Entry(penalidadeContainer)
    penalidade["width"] = 15
    penalidade["font"] = fontePadrao
    penalidade.insert(END, values[3])
    penalidade.pack(side=LEFT)

    salvar = Button(botoesContainer)
    salvar["text"] = "Salvar"
    salvar["font"] = ("Calibri", "9")
    salvar["width"] = 15
    salvar["command"] = lambda: salvarEdicaoLivro(table, selected_item, values[0], nome.get().strip(), values[2], penalidade.get().strip(), janelaEditarLivro, adm, biblioteca)
    salvar.pack(side=LEFT)

    voltar = Button(botoesContainer)
    voltar["text"] = "Voltar"
    voltar["font"] = ("Calibri", "9")
    voltar["width"] = 15
    voltar["command"] = lambda: janelaEditarLivro.destroy()
    voltar.pack(side=RIGHT)

    janelaEditarLivro.mainloop()


def salvarEdicaoLivro(table, selected_item, codigo, nome, situacao, penalidade, janela, adm, biblioteca):
    if nome == "" or penalidade == "":  # verifica se os campos estão vazios
        erro("Erro na edição", "Digite todos os campos!")
        return False
    else:
        if not isnumber(penalidade):
            erro("Erro na edição", "Digite apenas números na penalidade!")
            return False
        else:
            adm.editarLivro(biblioteca, codigo, nome, situacao, float(penalidade))
            table.item(selected_item, values=(codigo, nome, situacao, penalidade))
            janela.destroy()
            return True


def tela_principal_cliente(cliente, biblioteca, janela):
    janela.destroy()

    tela_cliente = Tk()
    tela_cliente.title("Biblioteca - Cliente")
    largura = 510
    altura = 350
    dimensoes = f"{largura}x{altura}"

    # Configurar as dimensões da janela
    tela_cliente.geometry(dimensoes)

    tituloContainer = Frame(tela_cliente)
    tituloContainer["pady"] = 10
    tituloContainer.pack()

    livrosContainer = Frame(tela_cliente)
    livrosContainer["pady"] = 20
    livrosContainer.pack()

    emprestimosContainer = Frame(tela_cliente)
    emprestimosContainer["pady"] = 20
    emprestimosContainer.pack()

    pagarContainer = Frame(tela_cliente)
    pagarContainer["pady"] = 20
    pagarContainer.pack()

    perfilContainer = Frame(tela_cliente)
    perfilContainer["pady"] = 20
    perfilContainer["padx"] = 20
    perfilContainer.pack(side=LEFT)

    fontePadrao = ("Arial", "11")
    creditos = Label(tela_cliente, text=f"Créditos: R$ {cliente.getCreditos():.2f}", font=fontePadrao)
    if cliente.isNegativado():
        creditos["foreground"] = "red"
    else:
        creditos["foreground"] = "green"
    creditos.place(x=350, y=10)

    titulo = Label(tituloContainer, text="Home - Cliente")
    titulo["font"] = ("Verdana", "10", "bold")
    titulo.pack(side=LEFT)

    sair = Button(tela_cliente)
    sair["text"] = "Sair"
    sair["font"] = ("Calibri", "9")
    sair["width"] = 10
    sair["command"] = lambda: tela_de_login(biblioteca, tela_cliente)

    sair.place(x=10, y=10)

    livros = Button(livrosContainer)
    livros["text"] = "Ver livros da biblioteca"
    livros["font"] = ("Calibri", "9")
    livros["width"] = 25
    livros["height"] = 2
    livros["command"] = lambda: tela_livros_biblioteca_cliente(cliente, biblioteca, tela_cliente)
    livros.pack(side=LEFT)

    emprestimos = Button(emprestimosContainer)
    emprestimos["text"] = "Meus empréstimos"
    emprestimos["font"] = ("Calibri", "9")
    emprestimos["width"] = 25
    emprestimos["height"] = 2
    emprestimos["command"] = lambda: tela_emprestimo_cliente(cliente, biblioteca, tela_cliente)
    emprestimos.pack(side=LEFT)

    pagar = Button(pagarContainer)
    pagar["text"] = "Depositar créditos"
    pagar["font"] = ("Calibri", "9")
    pagar["width"] = 25
    pagar["height"] = 2
    pagar["command"] = lambda: tela_pagamento(cliente, creditos)
    pagar.pack(side=RIGHT)

    labelPerfil = Label(perfilContainer, text="Cliente: ", font=fontePadrao)
    labelPerfil.pack(side=LEFT)

    perfil = Button(perfilContainer)
    perfil["text"] = cliente.getNome()
    perfil["font"] = ("Calibri", "9")
    perfil["width"] = 25
    perfil["height"] = 2
    perfil["command"] = lambda: tela_edicao_cliente(biblioteca, cliente, tela_cliente)
    perfil.pack(side=RIGHT)

    tela_cliente.mainloop()


def tela_edicao_cliente(biblioteca, cliente, janela):

    janela.destroy()

    janelaEdicaoCliente = Tk()
    janelaEdicaoCliente.title("Edição de Cliente")
    largura = 500
    altura = 300
    dimensoes = f"{largura}x{altura}"

    # Configurar as dimensões da janela
    janelaEdicaoCliente.geometry(dimensoes)

    fontePadrao = ("Arial", "10")
    tituloContainer = Frame(janelaEdicaoCliente)
    tituloContainer["pady"] = 10
    tituloContainer.pack()

    cpfContainer = Frame(janelaEdicaoCliente)
    cpfContainer["padx"] = 20
    cpfContainer["pady"] = 10
    cpfContainer.pack()

    nomeContainer = Frame(janelaEdicaoCliente)
    nomeContainer["padx"] = 20
    nomeContainer["pady"] = 10
    nomeContainer.pack()

    senhaContainer = Frame(janelaEdicaoCliente)
    senhaContainer["padx"] = 20
    senhaContainer["pady"] = 10
    senhaContainer.pack()

    botoesContainer = Frame(janelaEdicaoCliente)
    botoesContainer["pady"] = 20
    botoesContainer.pack()

    titulo = Label(tituloContainer, text="Dados do cliente")
    titulo["font"] = ("Verdana", "10", "bold")
    titulo.pack()

    cpfLabel = Label(cpfContainer, text="CPF:  ", font=fontePadrao)
    cpfLabel.pack(side=LEFT)

    cpf = Entry(cpfContainer)
    cpf["width"] = 30
    cpf["font"] = fontePadrao
    cpf.insert(END, cliente.getCpf())
    cpf.config(state="disabled")
    cpf.pack(side=LEFT)

    nomeLabel = Label(nomeContainer, text="Nome:", font=fontePadrao)
    nomeLabel.pack(side=LEFT)

    nome = Entry(nomeContainer)
    nome["width"] = 30
    nome["font"] = fontePadrao
    nome.insert(END, cliente.getNome())
    nome.pack(side=LEFT)

    senhaLabel = Label(senhaContainer, text="Senha:", font=fontePadrao)
    senhaLabel.pack(side=LEFT)

    senha = Entry(senhaContainer)
    senha["width"] = 30
    senha["font"] = fontePadrao
    senha["show"] = "*"
    senha.insert(END, cliente.getSenha())
    senha.pack(side=LEFT)

    salvar = Button(botoesContainer)
    salvar["text"] = "Salvar"
    salvar["font"] = ("Calibri", "9")
    salvar["width"] = 15
    salvar["command"] = lambda: salvarEdicaoCliente(cpf.get().strip(), nome.get().strip(), senha.get().strip(), biblioteca, cliente, janelaEdicaoCliente)
    salvar.pack(side=LEFT)

    excluir = Button(botoesContainer)
    excluir["text"] = "Excluir perfil"
    excluir["font"] = ("Calibri", "9")
    excluir["width"] = 15
    excluir["command"] = lambda: excluirCliente(biblioteca, cliente, janelaEdicaoCliente)
    excluir.pack(side=LEFT)

    voltar = Button(botoesContainer)
    voltar["text"] = "Voltar"
    voltar["font"] = ("Calibri", "9")
    voltar["width"] = 15
    voltar["command"] = lambda: tela_principal_cliente(cliente, biblioteca, janelaEdicaoCliente)
    voltar.pack(side=RIGHT)

    janelaEdicaoCliente.mainloop()


def excluirCliente(biblioteca, cliente, janela):
    confirmacao = mensagemConfirmacao("Confirmação",
                                      f'Tem certeza que deseja excluir seu perfil da biblioteca?')
    if confirmacao == 'yes':
        operacao = biblioteca.removerCliente(cliente)
        if operacao:
            tela_de_login(biblioteca, janela)


def salvarEdicaoCliente(cpf, nome, senha, biblioteca, cliente, janela):
    if nome == "" or senha == "":  # verifica se os campos estão vazios
        erro("Erro na edição", "Digite todos os campos!")
        return False
    else:
        if len(cpf) != 11:
            erro("Erro na edição", "O CPF precisa ter 11 caracteres!")
            return False
        else:
            biblioteca.editarCliente(cliente, nome, cpf, senha)
            tela_principal_cliente(cliente, biblioteca, janela)
            return True


def tela_pagamento(cliente, label):
    janelaPagamento = Tk()
    janelaPagamento.title("Pagamento")
    largura = 450
    altura = 200
    dimensoes = f"{largura}x{altura}"

    # Configurar as dimensões da janela
    janelaPagamento.geometry(dimensoes)

    fontePadrao = ("Arial", "10")
    tituloContainer = Frame(janelaPagamento)
    tituloContainer["pady"] = 10
    tituloContainer.pack()

    valorContainer = Frame(janelaPagamento)
    valorContainer["padx"] = 20
    valorContainer["pady"] = 10
    valorContainer.pack()

    botoesContainer = Frame(janelaPagamento)
    botoesContainer["pady"] = 20
    botoesContainer.pack()

    titulo = Label(tituloContainer, text="Depositar créditos")
    titulo["font"] = ("Verdana", "10", "bold")
    titulo.pack()

    valorLabel = Label(valorContainer, text="Valor a ser depositado em R$:", font=fontePadrao)
    valorLabel.pack(side=LEFT)

    valor = Entry(valorContainer)
    valor["width"] = 30
    valor["font"] = fontePadrao
    valor.pack(side=LEFT)

    depositar = Button(botoesContainer)
    depositar["text"] = "Depositar"
    depositar["font"] = ("Calibri", "9")
    depositar["width"] = 15
    depositar["command"] = lambda: depositarCredito(valor.get().strip(), cliente, label, janelaPagamento)
    depositar.pack(side=LEFT)

    voltar = Button(botoesContainer)
    voltar["text"] = "Voltar"
    voltar["font"] = ("Calibri", "9")
    voltar["width"] = 15
    voltar["command"] = lambda: janelaPagamento.destroy()
    voltar.pack(side=RIGHT)

    janelaPagamento.mainloop()


def depositarCredito(deposito, cliente, label, janela):
    if deposito == "":  # verifica se os campos estão vazios
        erro("Erro no depósito", "Digite todos os campos!")
        return False
    else:
        if not isnumber(deposito):
            erro("Erro no depósito", "Digite apenas números no depósito!")
            return False
        elif float(deposito) <= 0:
            erro("Erro no depósito", "Digite apenas números positivos no depósito!")
            return False
        else:
            confirmacao = mensagemConfirmacao("Confirmação",
                                              f'Tem certeza que deseja depositar R${deposito}?')
            if confirmacao == 'yes':
                label["text"] = f"Créditos: R${(cliente.getCreditos() + float(deposito)):.2f}"
                cliente.setCreditos(cliente.getCreditos() + float(deposito))
                janela.destroy()
                if cliente.isNegativado():
                    label["foreground"] = "red"
                else:
                    label["foreground"] = "green"
                return True


def tela_emprestimo_cliente(cliente, biblioteca, janela):
    janela.destroy()

    tela_lista_emprestimos = Tk()
    tela_lista_emprestimos.title("Meus empréstimos - " + cliente.getNome())
    largura = 850
    altura = 400
    dimensoes = f"{largura}x{altura}"

    # Configurar as dimensões da janela
    tela_lista_emprestimos.geometry(dimensoes)

    tituloContainer = Frame(tela_lista_emprestimos)
    tituloContainer["pady"] = 10
    tituloContainer.pack()

    tableContainer = Frame(tela_lista_emprestimos)
    tableContainer.pack(fill=BOTH, expand=True)

    botoesContainer = Frame(tela_lista_emprestimos)
    botoesContainer["pady"] = 20
    botoesContainer.pack()

    titulo = Label(tituloContainer, text="Meus empréstimos")
    titulo["font"] = ("Verdana", "10", "bold")
    titulo.pack(side=LEFT)

    table = ttk.Treeview(tableContainer, columns=("Codigo", "Nome", "Penalidade", "DataEmprestimo", "DataDevolucao"), show="headings")

    # Criar cabeçalho da tabela
    table.heading('#0', text='', anchor=W)
    table.heading('Codigo', text='Código do livro', anchor=CENTER)
    table.heading('Nome', text='Nome do livro', anchor=CENTER)
    table.heading('Penalidade', text='Penalidade p/dia de atraso em R$', anchor=CENTER)
    table.heading('DataEmprestimo', text='Data do empréstimo', anchor=CENTER)
    table.heading('DataDevolucao', text='Data de devolução', anchor=CENTER)

    # Formatar as colunas
    table.column('#0', width=0, stretch= NO)
    table.column('Codigo', anchor=CENTER, width=100)
    table.column('Nome', anchor=CENTER, width=150)
    table.column('Penalidade', anchor=CENTER, width=180)
    table.column('DataEmprestimo', anchor=CENTER, width=180)
    table.column('DataDevolucao', anchor=CENTER, width=180)

    scrollbar = ttk.Scrollbar(table, orient="vertical", command=table.yview)
    table.configure(yscroll=scrollbar.set)

    for i in cliente.getListaEmprestimos():
        dataEmprestimo = i.getDataEmprestimo().strftime('%d/%m/%Y')
        dataDevolucao = i.getDataDevolucao().strftime('%d/%m/%Y')
        row = [i.getLivro().getCodigo(), i.getLivro().getNome(), i.getLivro().getPenalidade(), dataEmprestimo, dataDevolucao]
        table.insert("", "end", values=row)

    table.pack(fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    renovar = Button(botoesContainer)
    renovar["text"] = "Renovar"
    renovar["font"] = ("Calibri", "9")
    renovar["width"] = 15
    renovar["command"] = lambda: renovarLivro(table.focus(), biblioteca, cliente, table)
    renovar.pack(side=LEFT)

    devolver = Button(botoesContainer)
    devolver["text"] = "Devolver"
    devolver["font"] = ("Calibri", "9")
    devolver["width"] = 15
    devolver["command"] = lambda: devolverLivro(table.focus(), biblioteca, cliente, table)
    devolver.pack(side=LEFT)

    voltar = Button(botoesContainer)
    voltar["text"] = "Voltar"
    voltar["font"] = ("Calibri", "9")
    voltar["width"] = 15
    voltar["command"] = lambda: tela_principal_cliente(cliente, biblioteca, tela_lista_emprestimos)
    voltar.pack(side=RIGHT)

    tela_lista_emprestimos.mainloop()


def devolverLivro(itemSelecionado, biblioteca, cliente, table):
    if itemSelecionado == "":
        return False
    valores = table.item(itemSelecionado)['values']
    confirmacao = mensagemConfirmacao("Confirmação",
                                      f'Tem certeza que deseja devolver o livro "{valores[1]}" (código: {valores[0]})?')
    if confirmacao == 'yes':
        for emprestimo in cliente.getListaEmprestimos():
            livro = emprestimo.getLivro()
            if livro.getCodigo() == valores[0]:
                biblioteca.devolver(cliente, emprestimo)
                table.delete(itemSelecionado)


def renovarLivro(itemSelecionado, biblioteca, cliente, table):
    if itemSelecionado == "":
        return False
    valores = table.item(itemSelecionado)['values']
    confirmacao = mensagemConfirmacao("Confirmação",
                                      f'Tem certeza que deseja renovar o livro "{valores[1]}" (código: {valores[0]})?')
    if confirmacao == 'yes':
        for emprestimo in cliente.getListaEmprestimos():
            livro = emprestimo.getLivro()
            if livro.getCodigo() == valores[0]:
                renov = biblioteca.renovar(emprestimo, cliente)
                if renov:
                    valores[4] = emprestimo.getDataDevolucao().strftime('%d/%m/%Y')
                    table.item(itemSelecionado, values=valores)
                    return True


def tela_livros_biblioteca_cliente(cliente, biblioteca, janela):
    janela.destroy()

    tela_livros = Tk()
    tela_livros.title("Biblioteca - Livros Disponíveis")
    largura = 530
    altura = 400
    dimensoes = f"{largura}x{altura}"

    # Configurar as dimensões da janela
    tela_livros.geometry(dimensoes)

    tituloContainer = Frame(tela_livros)
    tituloContainer["pady"] = 10
    tituloContainer.pack()

    buscaContainer = Frame(tela_livros)
    buscaContainer["pady"] = 10
    buscaContainer.pack()

    tableContainer = Frame(tela_livros)
    tableContainer.pack(fill=BOTH, expand=True)

    botoesContainer = Frame(tela_livros)
    botoesContainer["pady"] = 20
    botoesContainer.pack()

    titulo = Label(tituloContainer, text="Livros da Biblioteca")
    titulo["font"] = ("Verdana", "10", "bold")
    titulo.pack(side=LEFT)

    buscaEntrada = Entry(buscaContainer)
    buscaEntrada["width"] = 60
    buscaEntrada.pack(side=LEFT)

    busca = Button(buscaContainer)
    busca["text"] = "Buscar pelo nome"
    busca["font"] = ("Calibri", "9")
    busca["width"] = 25
    busca["command"] = lambda: search(buscaEntrada.get(), biblioteca, table)
    busca.pack(side=RIGHT)

    table = ttk.Treeview(tableContainer, columns=("Codigo", "Nome", "Situacao", "Penalidade"), show="headings")

    # Criar cabeçalho da tabela
    table.heading('#0', text='', anchor=W)
    table.heading('Codigo', text='Código', anchor=CENTER)
    table.heading('Nome', text='Nome', anchor=CENTER)
    table.heading('Situacao', text='Situação', anchor=CENTER)
    table.heading('Penalidade', text='Penalidade p/dia de atraso em R$', anchor=CENTER)

    # Formatar as colunas
    table.column('#0', width=0, stretch=NO)
    table.column('Codigo', anchor=CENTER, width=100)
    table.column('Nome', anchor=CENTER, width=100)
    table.column('Situacao', anchor=CENTER, width=100)
    table.column('Penalidade', anchor=CENTER, width=220)

    scrollbar = ttk.Scrollbar(table, orient="vertical", command=table.yview)
    table.configure(yscroll=scrollbar.set)

    for i in biblioteca.getListaLivros():
        row = [i.getCodigo(), i.getNome(), i.getSituacao(), i.getPenalidade()]
        table.insert("", "end", values=row)

    table.pack(fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)

    alocar = Button(botoesContainer)
    alocar["text"] = "Alocar"
    alocar["font"] = ("Calibri", "9")
    alocar["width"] = 15
    alocar["command"] = lambda: alocarLivro(cliente, biblioteca, table.focus(), table)
    alocar.pack(side=LEFT)

    sair = Button(botoesContainer)
    sair["text"] = "Voltar"
    sair["font"] = ("Calibri", "9")
    sair["width"] = 15
    sair["command"] = lambda: tela_principal_cliente(cliente, biblioteca, tela_livros)
    sair.pack(side=RIGHT)

    tela_livros.mainloop()


def alocarLivro(cliente, biblioteca, itemSelecionado, table):
    if itemSelecionado == "":
        return False

    valores = table.item(itemSelecionado)['values']
    confirmacao = mensagemConfirmacao("Confirmação",
                                      f'Tem certeza que deseja alocar o livro "{valores[1]}" (código: {valores[0]})?')
    if confirmacao == 'yes':
        for livro in biblioteca.getListaLivros():
            if livro.getCodigo() == valores[0]:
                biblioteca.emprestar(cliente, livro)
                valores[2] = livro.getSituacao()
                table.item(itemSelecionado, values=valores)
                break
