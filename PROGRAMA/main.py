from Produto import Produto
from Carrinho import Carrinho

car = Carrinho()

p1 = Produto("IPhone 15",9999,99)
p2 = Produto("NoteBook Asus",4999,99)
p3 = Produto("Camiseta do time ruim",499,3)
p4 = Produto("Camiseta do time bom",15,1000)

car.inserirProduto(p1)
car.inserirProduto(p2)
car.inserirProduto(p3)
car.inserirProduto(p4)

car.listarProdutos()

car.mostrarTotal()