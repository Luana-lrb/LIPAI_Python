""" Exercício 1 """

def carregar_dados_alunos(arquivo):
    alunos = []
    with open(arquivo, 'r') as arq:
        for linha in arq :
            linha = linha.strip()
            if not linha : continue
            dados = linha.split(',')
            if len(dados) == 3:
                aluno = {
                    'prontuario' : dados[0].strip(),
                    'nome' : dados[1].strip(),
                    'email' : dados[2].strip()
                }
                alunos.append(aluno)
    return tuple(alunos)

tupla = carregar_dados_alunos(r'C:\UFU\IC\semana_3\src\06-arquivos\exercicios\arq.txt')
print(tupla)     