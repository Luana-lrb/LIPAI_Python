""" Exercício 1 """
class Aluno:
    def __init__(self, dados):
        aluno = dados.split(',')
        if len(aluno) != 3:
            raise ValueError("String deve ter 3 informações")
        
        self.prontuario = aluno[0].strip()
        self.nome = aluno[1].strip()
        self.email = aluno[2].strip()
        pass
    
    @property
    def prontuario(self):
        return self._prontuario
    
    @prontuario.setter
    def prontuario(self, value):
        if not value or value.strip() == "":
            raise ValueError("Prontuário não pode ser vazio")
        self._prontuario = value
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        if not value or value.strip() == "":
            raise ValueError("Nome não pode ser vazio")
        self._nome = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if not value or value.strip() == "":
            raise ValueError("Email não pode ser vazio")
        self._email = value
    
    def __eq__(self, value):
        if isinstance(value, Aluno):
            return self.prontuario == value.prontuario  
        return False    
    def __str__(self):
        return f"Aluno('{self.prontuario}', '{self.nome}', '{self.email}')"
    
    
aluno = Aluno('SP0101,João da Silva,joao@email.com')
print(f"SUCESSO: {aluno}")