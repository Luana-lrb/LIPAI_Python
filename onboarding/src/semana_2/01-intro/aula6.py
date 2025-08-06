""" Aula 6 -  conversão de tipo """

# Implícita 
leitura = 5.53
peso = 3
total = leitura * peso

print(total, type(total))

# Explícita (type casting)
soma = 13.4 + float('3.5')
print(soma, type(soma))

idade = '32'
print(idade, type(idade))

altura = 1.70
nome = 'Maria'

mensagem = nome + ' tem a altura ' + str(altura)
mensagem2 = f'{nome} tem a altura {altura}'
print(mensagem)
print(mensagem2)
