""" Aula 5 -  Tipos de Dados """

# Numéricos 
# Int e Float
idade = 20
peso = 70.5
print(idade, type(idade))
print(peso, type(peso))

# String
nome = 'João'
sobrenome = 'dos Santos'
nome_completo = nome + ' ' + sobrenome
print(nome_completo)

produto = 'Coca-cola'

# O cliente nome_completo comprou o produto

print(f'O cliente {nome} {sobrenome} comprou o produto {produto}')

print(nome[0], nome[-1])
print(nome.lower())
print(nome.upper())

print(1, 2, 3, 4, sep='X')

# Boolean 
resultado = 10 < 3
print(resultado, type(resultado))

#Listas
frutas = ['banana', 'uva', 'morango']
print(frutas[0])
print(frutas[1])
print(frutas[2])

frutas[0] = 'banana naninca'
frutas.append('abacaxi')
print(frutas)
print(len(frutas))

for fruta in frutas:
    print(frutas.upper())

# Tupla
codigos = ('SP01', 'SP02')
print(codigos[0])

# codigos[0] = SP05 #TypeError
print(len(codigos))

# Conjuntos
resultado_sorteio = {10, 4, 3, 2, 9}
print(resultado_sorteio)

resultado_sorteio.add(20)
print(resultado_sorteio)

# Dicionário

funcionario = {
    "código" : 123,
    "nome" : "Maria Silva"
}

print(funcionario)
print(funcionario["código"])
print(funcionario["nome"])

print(funcionario.keys())
print(funcionario.values())

funcionario['código'] = 900