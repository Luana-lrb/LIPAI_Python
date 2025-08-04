""" Exercício 2 """
entrada = input('Digite as notas separadas por espaço: ')
notas = []
for item in entrada.split():
    try:
        n = float(item)
        notas.append(n)
    except ValueError:
        print('Digite um número válido')
    
soma = 0
for nota in notas:
    soma = soma + nota
    
media = soma / len(notas) 

print(f'O resultado da média é: {media}')
    