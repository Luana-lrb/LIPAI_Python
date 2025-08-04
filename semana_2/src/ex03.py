""" Exercício 3 """

identificador = input('Informe o identificador: ')

if len(identificador) == 7:
    prefixo = identificador[:2]
    numero = identificador[2:6]
    sufixo = identificador[6]

    if prefixo == "BR" and numero.isdigit() and 1 <= int(numero) <= 9999 and sufixo == "X":
        print("Identificador válido")
    else:
        print("Identificador inválido")
else:
    print("Identificador inválido")