class Participacao:
    def __init__(self, dados, _aluno, _projeto):
        participacao = dados.split(',')
        if len(participacao) != 3:
            raise ValueError("String deve ter 3 informações")
        if not participacao[0].strip().isdigit():
            raise ValueError("Código deve ser um número")
        self.codigo = int(participacao[0].strip())
        self.data_inicio = participacao[1].strip()
        self.data_fim = participacao[2].strip()
        
        self.aluno = _aluno
        if not _projeto:
            raise ValueError("Projeto não pode ser vazio")
        self.projeto = _projeto
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
    def data_inicio(self):
        return self._data_inicio
    @data_inicio.setter
    def data_inicio(self, value):
        if not value or value.strip() == "":
            raise ValueError("Data de início não pode ser vazia")
        self._data_inicio = value
    
    @property
    def data_fim(self):
        return self._data_fim
    @data_fim.setter
    def data_fim(self, value):
        if not value or value.strip() == "":
            raise ValueError("Data de fim não pode ser vazia")
        self._data_fim = value
        
    @property
    def aluno(self):
        return self._aluno
    
    @aluno.setter
    def aluno(self, value):
        if not value:
            raise ValueError("Aluno não pode ser vazio")
        self._aluno = value
        
    @property
    def projeto(self):
        return self._projeto
    @projeto.setter
    def projeto(self, value):
        if not value:
            raise ValueError("Projeto não pode ser vazio")
        self._projeto = value
    
    
    def __str__(self):
        return (f"Participação(codigo={self.codigo}, aluno={self.aluno}, projeto={self.projeto}, "
                f"data_inicio={self.data_inicio}, data_fim={self.data_fim})")

