""" I/O Input and Output """

# saída padrão - sys stdout

from encodings import utf_8


print('hello word', 'Maria', 1, True, sep='@', end='!!!!!\n' )

arquivo = open('arq.txt', 'w', encoding='utf_8')
print('Jon','Mary','Gab', sep=';', file=arquivo)

# Entrada
nome = input('Digite seu nome: ')
idade = int(input('Digite a sua idade: '))

if idade >= 18:
    print(f'{nome} você é maior de idade')
    
# File

arquivo_notas = open('notas.txt', 'r', encoding='utf_8')
conteudo = arquivo_notas.read()
print(conteudo, type(conteudo))
notas = conteudo.split(sep=';')

media = (float(notas[0]) + float(notas[1]) + float(notas[2]))/len(notas)

print(media)