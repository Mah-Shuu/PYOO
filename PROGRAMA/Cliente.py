class Cliente:
    def __init__(self,nome,idade,fone,email):
        self._nome = nome
        self.idade = idade
        self.fone = fone
        self.email = email

    def comprar(self):
        print(f"{self._nome} realiza compras")

    def getNome(self): #MÉTODO GET PARA ACESSAR
        return self._nome
    
class ClientePremium(Cliente):
    def __init__(self, nome, idade, fone, email, areavip=True,desconto=20):
        super().__init__(nome, idade, fone, email)
        self.areavip = areavip
        self.desconto = desconto

    def comprar(self): #POLIFORMISMO REESCREVER O MÉTODO HERDADO
        print(f"{self._nome} compra muito com {self.desconto}% de desconto")

cliPremium = ClientePremium("Mateus",32,9999,"mateus@gmail.com")

cliPremium.comprar()