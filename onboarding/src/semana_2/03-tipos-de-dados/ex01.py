""" Exercício 1 """

dados = []

for i in range(3):
    dado = input('Informe o número: ')
    while True:
        try:
            numero = float(dado)
            dados.append(numero)
            break
        except ValueError: 
            print('Digite um número válido.')

minimo = maximo = dados[0]
for dado in dados:
    if dado > maximo: maximo = dado
    if dado < minimo: minimo = dado 

print(f"\nNúmeros digitados: {dados}")
print(f"Menor elemento: {minimo}")
print(f"Maior elemento: {maximo}")
    
# Ou simplismente:
menor = min(dados)
maior = max(dados)
    
print(f"\nNúmeros digitados: {dados}")
print(f"Menor elemento: {menor}")
print(f"Maior elemento: {maior}")