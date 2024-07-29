from Produto import Produto
from moduloCli.Cliente import Cliente
from funcoes import *

cli = Cliente("Joao Francisco",56)

cli.getNome()

cli.__nome = "Thiago Almeida"

cli.setNome("João Roberto")

cli.getNome()