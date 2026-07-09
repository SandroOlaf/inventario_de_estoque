from entrada import entrar

#Estrutura de FUNCIONAMENTO do sistema
while True:
    inicializar = int(input("Digite a sua opção: "))

    print("---- BEM-VINDO AO SISTEMA DE INVENTÁRIO ----")
    print("1-REGISTRAR ENTRADA")
    print("2-REGISTRAR SÁIDA")
    print("3-EXIBIR SALDO ATUAL")
    print("4-ENCERRAR SISTEMA")
    print()

    if inicializar == 1:
        entrar()
    elif inicializar == 2:
        ...
    elif inicializar == 3:
        ...
    elif inicializar == 4:
        ...
    else:
        break