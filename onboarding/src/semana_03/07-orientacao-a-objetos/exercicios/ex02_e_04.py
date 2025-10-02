""" Exercício 2 """
from ex03 import Participacao

class Projeto:
    def __init__(self, dados):
        projeto = dados.split(',')
        if len(projeto) != 3:
            raise ValueError("String deve ter 3 informações")
        if not projeto[0].strip().isdigit():
            raise ValueError("Código deve ser um número")
        self.codigo = int(projeto[0].strip())
        self.titulo = projeto[1].strip()
        self.responsavel = projeto[2].strip()
        self.participacoes = []
        pass
    
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, value):
        if not value or value is None:
            raise ValueError("Código não pode ser vazio")
        self._codigo = value
        
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, value):
        if not value or value.strip() == "":
            raise ValueError("Título não pode ser vazio")
        self._titulo = value
    
    @property
    def responsavel(self):
        return self._responsavel
    
    @responsavel.setter
    def responsavel(self, value):
        if not value or value.strip() == "":
            raise ValueError("Responsável não pode ser vazio")
        self._responsavel = value
    
    def __eq__(self, value):
        if isinstance(value, Projeto):
            return self.codigo == value.codigo
        return False    
    
    def __str__(self):
        return f"Projeto('{self.codigo}', '{self.titulo}', '{self.responsavel}')"
    
    def add_participacao(self, participacao):
        if not isinstance(participacao, Participacao):
            raise ValueError("Deve ser um objeto Participacao")
        self.participacoes.append(participacao)
    

