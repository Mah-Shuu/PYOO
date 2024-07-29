class Carrinho:
    def __init__(self):
        self.produtos = []

    def inserirProduto(self,produto):
        self.produtos.append(produto)

    def listarProdutos(self):
        for prod in self.produtos:
            print(f"Nome: {prod.nome} Preço: R$ {prod.preco:.2f}")

    def mostrarTotal(self):
        soma = 0
        for prod in self.produtos:
            soma+=prod.preco
        print(f"Soma: R$ {soma:.2f}")