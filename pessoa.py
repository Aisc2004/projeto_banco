import conta
 
from datetime import datetime
from dateutil.relativedelta import relativedelta

class Pessoa():
    """
    Classe base para representar uma pessoa no sistema, ela realiza a validação de nome e data_nascimento
    """
    def __init__(self, nome: str, data_nascimento: str, senha: int, cpf: int):
        """
        Inicializa os objetos da classe

        :nome -> nome da pessoa será formato com .title() 
        :data_nascimento -> data_nascimento da pessoa 
        """
        self.nome = nome
        self.data_nascimento = data_nascimento
        self._senha = senha
        self._cpf = cpf
        self.conta_poupanca = None
        self.conta_corrente = None

    @property
    def nome(self):
        """retorna o nome formatado da pessoa"""
        return self._nome.title()
    
    @nome.setter
    def nome(self, nome : str):
        """define o nome da pessoa"""
        if not isinstance(nome, str):
            raise TypeError('Tipo errado')
        self._nome = nome

    @property
    def data_nascimento(self):
        """retorna o valor da data_nascimento"""
        return self._data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, valor : str):
        """
        Realiza a validação da data_nascimento de tipo e valor
        
        Raises:
            TypeError: se a data_nascimento não for uma string
            ValueError: se a data_nascimento for menor que 18 anos
        """
        if not isinstance(valor, str):
            raise TypeError('data deve ser uma string')
        
        try:
            form_data = '%d/%m/%Y'
            data = datetime.strptime(valor, form_data)
            data_br = data.strftime(form_data)
        except:
            raise ValueError("Formato de data inválido. Use DD/MM/AAAA")
            
        hoje = datetime.today()
        idade = relativedelta(hoje, data)
            
        if idade.years < 18:
            raise ValueError('data_nascimento deve ser maior que 18') 
              
        self._data_nascimento = data_br

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, digitos):
        if len(digitos) < 11 or len(digitos) > 11:
            print('quantidade de dígitos')
        self._cpf = digitos

    def verificar_senha(self, senha_digitada: str):
        if len(senha_digitada) < 4 or len(senha_digitada) > 4:
            print('senha deve conter 4 dígitos')

        if not senha_digitada.isnumeric():
            raise TypeError('senha deve ser um número')
        
        senha_int = int(senha_digitada)

        return self._senha == senha_int

    def abrir_conta_poupanca(self, agencia, numero, saldo):
        if self.conta_poupanca is None:
            nova_poupanca = conta.ContaPoupanca(agencia, numero, saldo)
            self.conta_poupanca = nova_poupanca
            print('conta_poupança criada com sucesso')
            return nova_poupanca
        else:
            print('já possui uma conta poupança')

    def abrir_conta_corrente(self, agencia, numero, saldo, limite):
        if self.conta_corrente is None:
            nova_corrente = conta.ContaCorrente(agencia, numero, saldo, limite)
            self.conta_corrente = nova_corrente
            print('conta_corrente criada com sucesso')
            return nova_corrente
        else:
            print('já possui uma conta corrente')

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(Nome: {self.nome!r} | data_nascimento: {self.data_nascimento!r})'

class Cliente(Pessoa):
    """
    Classe que representa uma pessoa do banco e herda de Pessoa
    Além de nome e data_nascimento, o cliente também possui um vínculo com uma conta
    """
    def __init__(self, nome: str, data_nascimento: str, senha: int, cpf: int):
        super().__init__(nome, data_nascimento, senha, cpf)
        self.conta : conta.Conta | None = None




