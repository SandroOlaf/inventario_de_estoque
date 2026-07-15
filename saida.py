from entrada import estoque

def saida_de_material():
    nome_do_material = input("Digite o nome do material: ")

    if nome_do_material in estoque: #Teste 2 (Saldo):
        quantidade = int(input(f"Digite a quantidade do {nome_do_material} a retirar: "))

        if quantidade > estoque[nome_do_material]:
            print("Operação cancelada! Saldo insuficiente.")
        else:
            estoque[nome_do_material] -= quantidade
            print(f"Sucesso! Segue Saldo atual: {estoque}")

    else:
        print("Produto não encontrado!")
    print(f"Estoque Atual: {estoque}\n")

saida_de_material()