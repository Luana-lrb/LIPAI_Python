""" Aula 4 - Variáveis, Constantes e Literais """

# Variáveis - container para guardar dados
# Inferencia de tipo
numero = 10
print(numero)
print(type(numero))

# Alterar o valor da variável
numero = 20
print(numero)

# Multiplas atribuições
nome, idade, endereco = 'Maria', 20, 'Ruas das ...'
print(nome, idade, endereco)

# Atribuir o mesmo valor para várias variávis
nome1 = nome2 = nome3 = 'João'
print(nome1, nome2, nome3)

# snake_case - Variáveis
id_funcionario = 209
print(id_funcionario)

# Upper case + snake_case = constantes
MAIORIDADE = 18
print(MAIORIDADE)

# Literais - valores fixos
idade = 27
print(idade)
print(27)

# Numéricos
print(10, type(10))
print(10, type(-10))
print(10.5, type(10.5))

# String
print('Maria', type('Maria'))
print("Maria", type("Maria"))
print("Jon's Family")
print('O filme estava "excelente"')

# Booleano
print(True, type(True))
print(False, type(False))

# None
print(None, type(None))

# Coleções
# Lista(list) - mutável
numeros = [1, 2, 3]
print(numeros, type(numeros))

# Tupla (tuple) -  imutável
emails = ('joao@email.com', 'maria@email.com')
print(emails, type(emails))

# Conjunto (set) -  sem elemntos duplicados
nomes = {'maria', 'joao', 'pedro', 'maria'}
print(nomes, type(nomes))

# Dicionário (dictionary)
aluno = {
    'nome' : 'Maria',
    'idade' : 20
}
print(aluno, type(aluno))