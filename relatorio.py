from entrada import estoque

def exibir_relatorio():

    if not estoque:
        print("Estoque vazio no momento.")

    for item in estoque:
        quantidade = estoque[item]
        print(f"Saldo de Estoque atualizado: Items:{item}\ Quantidade: {quantidade} \n")

