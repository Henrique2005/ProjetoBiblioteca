# Henrique Mateus Teodoro
import Interfaces
from Emprestimo import Emprestimo
from datetime import date, timedelta


class Biblioteca:

    def __init__(self, listaClientes, listaAdministradores, listaLivros):
        self.__listaClientes = listaClientes
        self.__listaAdministradores = listaAdministradores
        self.__listaLivros = listaLivros

    def getListaClientes(self):
        return self.__listaClientes

    def getListaAdministradores(self):
        return self.__listaAdministradores

    def getListaLivros(self):
        return self.__listaLivros

    def setListaClientes(self, listaClientes):
        self.__listaClientes = listaClientes

    def setListaAdministradores(self, listaAdministradores):
        self.__listaAdministradores = listaAdministradores

    def setListaLivros(self, __listaLivros):
        self.__listaLivros = __listaLivros

    def emprestar(self, cliente, livro):
        if cliente.isNegativado():
            Interfaces.alerta("Empréstimo", "Tentativa de empréstimo negada, seus créditos estão negativos!")
        elif livro.isEmprestado():
            Interfaces.alerta("Empréstimo", "Tentativa de empréstimo negada, este livro já está alocado por outro cliente!")
        elif len(cliente.getListaEmprestimos()) >= 3:
            Interfaces.alerta("Empréstimo", "Tentativa de empréstimo negada, você atingiu o número máximo de locações (3)!")
        else:
            dataAtual = date.today()
            seteDias = timedelta(7)
            dataDevolucao = dataAtual + seteDias

            emprestimo = Emprestimo(cliente, livro, dataAtual, dataDevolucao)

            cliente.alocarLivro(emprestimo)

            livro.setSituacao("Alocado")

            Interfaces.mensagem("Empréstimo", "Empréstimo realizado com sucesso!")

    def devolver(self, cliente, emprestimo):
        listaEmprestimos = cliente.getListaEmprestimos()
        for i in range(len(listaEmprestimos)):
            if listaEmprestimos[i].getLivro() == emprestimo.getLivro():
                livro = listaEmprestimos[i].getLivro()
                livro.setSituacao("Disponível")
                dataAtual = date.today()
                dataDevolucao = emprestimo.getDataDevolucao()
                if dataDevolucao < dataAtual:
                    self._punir(cliente, emprestimo.getLivro(), dataAtual, dataDevolucao)
                del listaEmprestimos[i]
                Interfaces.mensagem("Devolução", "Livro devolvido com sucesso!")
                break

    def renovar(self, emprestimo, cliente):
        diferenca = emprestimo.getDataDevolucao() - emprestimo.getDataEmprestimo()

        if diferenca.days >= 21:
            Interfaces.alerta("Renovação", "Você já realizou o número máximo de renovações possíveis!")
            return False
        else:
            dataAtual = date.today()
            dataDevolucao = emprestimo.getDataDevolucao()
            if dataDevolucao < dataAtual:
                Interfaces.alerta("Renovação", "Renovação negada, esse livro já está com devolução atrasada!")
            else:
                if cliente.isNegativado():
                    Interfaces.alerta("Renovação", "Renovação negada, seus créditos estão negativos!")
                else:
                    seteDias = timedelta(7)
                    novaDataDevolucao = emprestimo.getDataDevolucao() + seteDias
                    emprestimo.setDataDevolucao(novaDataDevolucao)
                    return True

    def _punir(self, cliente, livro, dataAtual, dataDevolucao):
        quantidade_dias = abs((dataAtual - dataDevolucao).days)
        print(quantidade_dias, livro.getPenalidade())
        valorMulta = livro.getPenalidade() * quantidade_dias
        cliente.setCreditos(cliente.getCreditos() - valorMulta)
        Interfaces.alerta("Multa", f"Você foi multado(a) no valor de R${valorMulta} por conta do atraso na devolução do livro!")

    def adicionarCliente(self, cliente):
        self.__listaClientes.append(cliente)

    def editarCliente(self, cliente, nome, cpf, senha):
        cliente.setNome(nome)
        cliente.setCpf(cpf)
        cliente.setSenha(senha)
        Interfaces.mensagem("Atualização", "Cliente atualizado com sucesso!")

    def removerCliente(self, cliente):
        if cliente.isNegativado():
            Interfaces.erro("Exclusão de cliente", "Erro na exclusão do cliente, seus créditos não podem estar negativos!")
            return False
        elif len(cliente.getListaEmprestimos()) != 0:
            Interfaces.erro("Exclusão de cliente", "Erro na exclusão do cliente, você possui empréstimos ativos!")
            return False
        else:
            for i in range(len(self.__listaClientes)):
                if self.__listaClientes[i].getCpf() == cliente.getCpf():
                    del self.__listaClientes[i]
                    Interfaces.mensagem("Exclusão de cliente", "Cliente excluído com sucesso!")
                    return True

    def adicionarAdministrador(self, adm):
        self.__listaAdministradores.append(adm)

    def emprestarParaTeste(self, cliente, livro): # método utilizado somente para testar a funcionalidade das multas
        if cliente.isNegativado():
            Interfaces.alerta("Empréstimo", "Tentativa de empréstimo negada, seus créditos estão negativos!")
        elif livro.isEmprestado():
            Interfaces.alerta("Empréstimo", "Tentativa de empréstimo negada, este livro já está alocado por outro cliente!")
        elif len(cliente.getListaEmprestimos()) >= 3:
            Interfaces.alerta("Empréstimo", "Tentativa de empréstimo negada, você atingiu o número máximo de locações (3)!")
        else:
            dataAtual = date(2023, 5, 15)
            seteDias = timedelta(7)
            dataDevolucao = dataAtual + seteDias

            emprestimo = Emprestimo(cliente, livro, dataAtual, dataDevolucao)

            cliente.alocarLivro(emprestimo)

            livro.setSituacao("Alocado")

            Interfaces.mensagem("Empréstimo", "Empréstimo realizado com sucesso!")
