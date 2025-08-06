""" Exercício 2 """

def carregar_dados_projetos(arquivo):
    projetos = []
    with open(arquivo, 'r') as arq:
        for linha in arq :
            linha = linha.strip()
            if not linha : continue
            dados = linha.split(',')
            if len(dados) == 3:
                projeto = {
                    'codigo' : int (dados[0].strip()),
                    'titulo' : dados[1].strip(),
                    'responsavel' : dados[2].strip()
                }
                projetos.append(projeto)
    return tuple(projetos)

tupla = carregar_dados_projetos(r'C:\UFU\IC\semana_3\src\06-arquivos\exercicios\project.txt')
print(tupla)     