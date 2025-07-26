""" Aula 1 - Operadores """

# Aritméticos
print('1+1', 1 + 1 , type(1+1) )
print('1.2 + 1.3', 1.2 +1.3, type(1.2 +1.3))
print(3-1)
print(3*3, type(3*3))
print(3/3, type(3/3))
print(3%3, type(3%3))
print(3//3)
print(3**3)

# Atribuiçao
x = 20
# Comparação
print('3 == 3',3 == 3, type(3==3))
print('3 != 3',3 != 3, type(3!=3))
print('3 > 3',3 > 3, type(3>3))
print('3 >= 3',3 >= 3, type(3>=3))
print('3 < 3',3 < 3, type(3<3))
print('3 <= 3',3 <= 3, type(3<=3))

#Operadores lógicos
print('True and True', True and True, type(True and True))
print('True and False', True and False, type(True and False))
print('False and True',False and True, type(False and True))
print('False and False', False and False, type(False and False))

print('True or True', True or True, type(True or True))
print('True or False', True or False, type(True or False))
print('False or True',False or True, type(False or True))
print('False or False', False or False, type(False or False))

condicao = False

print('not condicao', not condicao, type(not condicao))

# Operadores especiais 

# is - verifica se as variáveis apontam para o mesmo objeto na memória 
# == - compara se os valores são iguais, mas podem ser variáveis diferentes

a = 2
b = 2

print(a is b)
print(a == b)

# in
# str, list, tuple, set, dic(chave)

frase = 'Você é legal'
print('legal' in frase, type('legal' in frase))

pessoa = {
    'nome' : 'Maria',
    'idade': 22 
}
print( 'nome' in pessoa)