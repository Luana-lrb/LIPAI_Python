""" Aula 01 - Debug"""
breakpoint()
n1 = 3
n2 = 4
n3 = 5

def soma3 (n1, n2, n3):
    soma = n1 + n2 + n3
    print(soma)
    return soma

soma = soma3(n1,n2,n3)
print(soma)