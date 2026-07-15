from entrada import entrar
from saida import saida_de_material
from relatorio import exibir_relatorio

#Estrutura de FUNCIONAMENTO do sistema
while True: 
    print("---- BEM-VINDO AO SISTEMA DE INVENTÁRIO ----")
    print("1-REGISTRAR ENTRADA")
    print("2-REGISTRAR SÁIDA")
    print("3-EXIBIR SALDO ATUAL")
    print("4-ENCERRAR SISTEMA")
    print()

    inicializar = int(input("Digite a sua opção: "))

    if inicializar == 1:
        entrar()
    elif inicializar == 2:
        saida_de_material()
    elif inicializar == 3:
        exibir_relatorio()
        break
    else:
        print("Opção inválida!")