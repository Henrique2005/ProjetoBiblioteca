# Henrique Mateus Teodoro
from Usuario import Usuario
import Interfaces


class Administrador(Usuario):

    def __init__(self, nome, cpf, senha):
        super().__init__(nome, cpf, senha)

    def cadastrarLivro(self, biblioteca, livro):
        listaLivros = biblioteca.getListaLivros()
        listaLivros.append(livro)
        biblioteca.setListaLivros(listaLivros)
        Interfaces.mensagem("Cadastrado de livro", "Livro cadastrado com sucesso!")

    def editarLivro(self, biblioteca, codigo, nome, situacao, penalidade):
        listaLivros = biblioteca.getListaLivros()
        for i in range(len(listaLivros)):
            if listaLivros[i].getCodigo() == codigo:
                listaLivros[i].setNome(nome)
                listaLivros[i].setSituacao(situacao)
                listaLivros[i].setPenalidade(penalidade)
                Interfaces.mensagem("Atualização de livro", "Livro atualizado com sucesso!")
                break

    def excluirLivro(self, biblioteca, codigo):
        listaLivros = biblioteca.getListaLivros()
        for i in range(len(listaLivros)):
            if listaLivros[i].getCodigo() == codigo:
                if listaLivros[i].isEmprestado():
                    Interfaces.erro("Exclusão de livro", "Não foi possível excluir o livro, pois ele está emprestado!")
                    return False
                else:
                    del listaLivros[i]
                    Interfaces.mensagem("Exclusão de livro", "Livro excluído com sucesso!")
                    return True
