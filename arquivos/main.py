from Biblioteca import Biblioteca
from Administrador import Administrador
from Livro import Livro
from Cliente import Cliente
import Interfaces

# instancia a biblioteca
b1 = Biblioteca([], [], [])

# cria o administrador
adm = Administrador("administrador", "11111111111", "12345")
b1.adicionarAdministrador(adm)

# cria um cliente que seja utilizado para teste
c1 = Cliente("Henrique", "22222222222", "12345", 0.0, [])
b1.adicionarCliente(c1)

# criamos um livro e o emprestamos para o cliente c1 com o método
# emprestarParaTeste da biblioteca. É a única vez que esse método é utilizado e serve somente para o teste das multas
livro = Livro("Chiquinha", "Disponível", 1.0)
adm.cadastrarLivro(b1, livro)
livroo = b1.getListaLivros()
b1.emprestarParaTeste(c1, livroo[0])

# Inicia a aplicação
Interfaces.tela_de_login(b1)
