# Henrique Mateus Teodoro

class Emprestimo:

    def __init__(self, cliente, livro, dataEmprestimo, dataDevolucao):
        self.__cliente = cliente
        self.__livro = livro
        self.__dataEmprestimo = dataEmprestimo
        self.__dataDevolucao = dataDevolucao

    def getCliente(self):
        return self.__cliente

    def getLivro(self):
        return self.__livro

    def getDataEmprestimo(self):
        return self.__dataEmprestimo

    def getDataDevolucao(self):
        return self.__dataDevolucao

    def setCliente(self, cliente):
        self.__cliente = cliente

    def setLivro(self, livro):
        self.__livro = livro

    def setDataEmprestimo(self, dataEmprestimo):
        self.__dataEmprestimo = dataEmprestimo

    def setDataDevolucao(self, dataDevolucao):
        self.__dataDevolucao = dataDevolucao
