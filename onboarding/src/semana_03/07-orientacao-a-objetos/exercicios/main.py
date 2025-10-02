from ex01 import Aluno
from ex02_e_04 import Projeto
from ex03 import Participacao

print("Iniciando testes...")

aluno = Aluno('SP0101,João da Silva,joao@email.com')
print(aluno)

projeto = Projeto('102,Desenvolvimento de Software,João da Silva')
print(projeto)

participacao = Participacao('101, 01/08/2025, 31/12/2025', aluno, projeto)
print(participacao)