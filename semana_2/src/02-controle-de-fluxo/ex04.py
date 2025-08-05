""" Exercício 4 """

identificador = input('Informe o identificador: ')
erros = []

numero = identificador[2:6]

if not identificador.startswith("BR"):
    erros.append('O identificar não inicia com a sequencias "BR"')
    
if not (numero.isdigit() and 1 <= int(numero) <= 9999):
    erros.append('O identificador não apresenta números inteiros entre 0001 e 9999')
    
if not identificador.endswith("X"):
    erros.append('O identificar não finaliza com o caracter X')
    
if len(erros) == 0:
    print("Identificador válido")
else:
    print("Identificador inválido")
    print ("Erros:")
    for erro in erros:
        print(erro)
