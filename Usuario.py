# Henrique Mateus Teodoro
from datetime import datetime


class Usuario:

    def __init__(self, nome, cpf, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = senha

    def getNome(self):
        return self.__nome

    def getCpf(self):
        return self.__cpf

    def getSenha(self):
        return self.__senha

    def setNome(self, nome):
        self.__nome = nome

    def setCpf(self, cpf):
        self.__cpf = cpf

    def setSenha(self, senha):
        self.__senha = senha

    def imprimeRelatorio(self):
        print("-"*50)
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
        print("Data e hora atual: ", data_e_hora_em_texto)
        print("Nome: ", self.__nome)
        print("CPF: ", self.__cpf)
