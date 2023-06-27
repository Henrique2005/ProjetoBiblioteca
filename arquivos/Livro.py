# Henrique Mateus Teodoro

class Livro:
    __contador__ = 0

    def __init__(self, nome, situacao, penalidade):
        Livro.__contador__ += 1
        self.__codigo = Livro.__contador__
        self.__nome = nome
        self.__situacao = situacao
        self.__penalidade = penalidade

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def getSituacao(self):
        return self.__situacao

    def getPenalidade(self):
        return self.__penalidade

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def setNome(self, nome):
        self.__nome = nome

    def setSituacao(self, situacao):
        self.__situacao = situacao

    def setPenalidade(self, penalidade):
        self.__penalidade = penalidade

    def isEmprestado(self):
        if self.__situacao == "Alocado":
            return True
        else:
            return False
