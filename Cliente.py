# Henrique Mateus Teodoro
from Usuario import Usuario


class Cliente(Usuario):

    def __init__(self, nome, cpf, senha, creditos, listaEmprestimos):
        super().__init__(nome, cpf, senha)
        self.__creditos = creditos
        self.__listaEmprestimos = listaEmprestimos

    def getCreditos(self):
        return self.__creditos

    def getListaEmprestimos(self):
        return self.__listaEmprestimos

    def setCreditos(self, creditos):
        self.__creditos = creditos

    def setListaEmprestimos(self, listaEmprestimos):
        self.__listaEmprestimos = listaEmprestimos

    def isNegativado(self):
        if self.__creditos < 0:
            return True
        else:
            return False

    def pagar(self, valor):
        self.__creditos += valor

    def alocarLivro(self, emprestimo):
        self.__listaEmprestimos.append(emprestimo)

    def imprimeRelatorio(self):
        super().imprimeRelatorio()
        print("Créditos: ", self.__creditos)
        print("Empréstimos deste cliente: ")
        for emprestimo in self.__listaEmprestimos:
            livro = emprestimo.getLivro()
            print("Nome do livro: ", livro.getNome())
            print("Data do empréstimo: ", emprestimo.getDataEmprestimo())
            print("Data de devolução: ", emprestimo.getDataDevolucao())
            print("=-"*15)
