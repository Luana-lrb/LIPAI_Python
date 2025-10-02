""" Exercício 4 """


def soma(*args):
    soma = 0
    for numero in args:
        soma = soma + numero
    return soma

resultado = soma(1,2,3,4,5)

print(resultado)