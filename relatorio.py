from entrada import estoque

def exibir_relatorio():

    if not estoque:
        print("Estoque encontra-se vazio!")

    for chave, valor in estoque:
        print(f"Saldo de Estoque atualizado: Items:{chave} / Quantidade:{valor} /n")

