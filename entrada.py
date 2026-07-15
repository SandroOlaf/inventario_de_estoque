estoque = {}

def entrar():
    item = str(input("Nome do produto: ")).strip().lower()
    quantidade = int(input("Quantidade do Produto: "))

    # A única validação necessária: O produto já foi cadastrado antes?
    if item in estoque:
        # Se já existe, apenas somamos a nova quantidade ao saldo atual
        estoque[item] += quantidade
        print(f"-> Estoque atualizado! {item} agora tem {estoque[item]} unidades.")
    else:
        # Se NÃO existe (é um produto novo), criamos a chave e definimos o valor inicial
        estoque[item] = quantidade
        print(f"-> Novo produto cadastrado! {item} adicionado com {quantidade} unidades.")

    print(f"Estado atual do estoque: {estoque}\n")

# Simulando duas rodadas para teste
