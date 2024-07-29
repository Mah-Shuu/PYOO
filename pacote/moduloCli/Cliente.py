class Cliente:
    def __init__(self,nome,idade):
        self.__nome = nome
        self.idade = idade

    def getNome(self):
        print(f"CLIENTE: {self.__nome}")
        
    def getEstoque(self):
        print(f"IDADE: {self.idade}")

    def setNome(self,novoNome):
        self.__nome = novoNome

    def setIdade(self,novaIdade):
        self.idade = novaIdade