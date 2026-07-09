estoque = {}

def entrar():
    item = str(input("Item do produto: "))
    quantidade = int(input("Quantidade do Produto: "))

    estoque[item] = quantidade
    print(estoque)

entrar()
