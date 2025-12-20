import conta

class Pessoa():
    """
    Classe base para representar uma pessoa no sistema, ela realiza a validação de nome e idade
    """
    def __init__(self, nome: str, idade: int):
        """
        Inicializa os objetos da classe

        :nome -> nome da pessoa será formato com .title() 
        :idade -> idade da pessoa 
        """
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        """retorna o nome formatado da pessoa"""
        return self._nome.title()
    
    @nome.setter
    
    def nome(self, nome : str):
        """define o nome da pessoa"""
        self._nome = nome

    @property
    def idade(self):
        """retorna o valor da idade"""
        return self._idade
    
    @idade.setter
    def idade(self, idade : int):
        """
        Realiza a validação da idade de tipo e valor
        
        Raises:
            TypeError: se a idade não for um número inteiro
            ValueError: se a idade for menor que 18 anos
        """

        if not isinstance(idade, int):
            raise TypeError('idade é inteiro')
        if idade < 18:
            raise ValueError('idade deve ser maior que 18')    
        self._idade = idade

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(Nome: {self.nome!r} | Idade: {self.idade!r})'

class Cliente(Pessoa):
    """
    Classe que representa uma pessoa do banco e herda de Pessoa
    Além de nome e idade, o cliente também possui um vínculo com uma conta
    """
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self.conta : conta.Conta | None = None
