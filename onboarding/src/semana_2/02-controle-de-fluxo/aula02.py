""" Aula 2 - instrução if """

# if condicao:

from traceback import print_tb


desconto = 30.0

if descont >= 20.0:
    print('Desconto especial')   
else:
    print('Sem desconto especial')
    
nome = 'Lo'
print(len(nome), type(len(nome)))

if len(nome) < 3:
    print('Nome deve ter pelo menos 3 caracteres')
else: 
    print('Nome válido')
    
NOME_VALIDO = len(nome >= 3 )

if not NOME_VALIDO:
    print('Nome deve ter pelo menos 3 caracteres')
else: 
    print('Nome válido')
    
nome = 'Ki'
idade =  17
erros = []

NOME_INVALIDO = len(nome < 3 )

if NOME_INVALIDO:
    erros.append('Nome deve ter eplo menos 3 caracteres')
IDADE_INVALIDA = idade < 18

if IDADE_INVALIDA:
    erros.append('Idade deve ser maior que 18')
    
if erros :
    print(erros)
else: 
    print('Dados válido')