""" Exercício 1 """
class Aluno:
    def __init__(self, dados):
        aluno = dados.split(',')
        if len(aluno) != 3:
            raise ValueError("String deve ter 3 informações")
        
        self.prontuario = aluno[0].strip()
        self.nome = aluno[0].strip()
        self.email = aluno[0].strip()
        pass
    