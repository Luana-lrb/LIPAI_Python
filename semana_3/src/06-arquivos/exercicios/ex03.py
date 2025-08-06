""" Exercício 2 """

def linha_para_dict(linha, dict):
    dicionario = {}
    dados = linha.split(',')
    for i in range(len(dict)):
        if i< len(dados):
            dicionario[dict[i]] = dados[i].strip()
        else:
            dicionario[dict[i]] = ''
    return dicionario

tupla = linha_para_dict('SP000001,Maria da Silva,maria@email.com', ['prontuario', 'nome', 'email'])
print(tupla)