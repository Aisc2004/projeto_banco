from abc import ABC, abstractmethod

class Conta(ABC):
    """
    Classe Abstrada que define a estrutura base para os tipos de conta (poupança/corrente)
    Não pode ser instanciada diretamente
    Gerência os depósitos, saldo, agência, conta e o método abstrado sacar
    """
    def __init__(self, agencia: int, num_conta: int, saldo = 0):
        """
        Inicialização dos objetos da classe

        :agencia -> número da agência (inteiro)
        :num_conta -> número da conta (inteiro)
        :saldo -> valor da conta (int ou float), por padrão 0  
        """
        self.historico = []
        self.agencia = agencia
        self.num_conta = num_conta
        self._saldo = saldo 

    @property
    def agencia(self):
        """Retorna o número da agência."""
        return self._agencia
        
    @agencia.setter
    def agencia(self, num_agencia : int):
        """
        Realiza a validação de tipo da agência
        
        Raises:
            TypeError: se o número da agência não for um inteiro
        """
        if not isinstance(num_agencia, int):
            raise TypeError('o número da agência deve ser um inteiro')
        self._agencia = num_agencia

    @property
    def num_conta(self):
        """Retorna o número da agência."""
        return self._num_conta
        
    @num_conta.setter
    def num_conta(self, num: int):
        """
        Realiza a validação de tipo da num_conta
        
        Raises: 
            TypeError: se o número da conta não for um inteiro
        """
        if not isinstance(num, int):
            raise TypeError('o número da conta deve ser um inteiro')
        self._num_conta = num

    @property
    def saldo(self):
        """
        Retorna o valor do saldo
        """
        return self._saldo

    def depositar(self, valor: float | int):
        """
        Realiza a validação de tipo e valor 
        
        Raises:
            TypeError: se o valor do depósito não for um inteiro
            ValueError: se o valor informado for negativo
        """
        
        if not isinstance(valor, (int, float)):
            raise TypeError('O valor digitado não é um número')
        if valor <= 0:
            raise ValueError('O valor informado não está correto')
        
        self.historico.append([f'DEPÓSITO, {valor}'])
        self._saldo += valor
        
        self.detalhes(f'(DEPÓSITO {valor})')

    @abstractmethod
    def sacar(self, valor: float | int):
        """
        Método Abstrato para realizar saques, deve ser implementado nas subclasses (ContaPoupanca, ContaCorrente)
        """
        pass

    def detalhes(self, msg=''):
        """
        Imprime o saldo atual acompanhado de uma mensagem personalizada.
        """
        print(f'O seu saldo é {self.saldo:.2f} {msg}')

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(Agencia: {self.agencia!r} | Conta: {self.num_conta!r} | Saldo: {self._saldo!r})'

class ContaPoupanca(Conta):
    """
    Implementação de Conta Poupança que herda de Conta
    O saque só é permitido se o saldo final não for negativo.
    """
    def sacar(self, valor : int | float):
        """
        Implementação do Método Abstrato sacar de Conta
        Realiza a validação de tipo e valor
        Também verifica se o valor do saque não ultrapassa o saldo do cliente

        Raises:
            TypeError: se o valor do saque não for um inteiro
            ValueError: se o valor do saque informado for negativo
        """

        if not isinstance(valor, (int, float)):
            raise TypeError('o valor digitado não é um número')
        
        if valor < 0:
            raise ValueError('o valor não pode ser negativo')

        if valor > self.saldo:
            self.detalhes('SAQUE NEGADO: valor a ser retirado não é permitido') 
            return
        
        self.historico.append([f'SAQUE: {valor}'])
        self._saldo -= valor
        self.detalhes(f'SACADO: {valor}')
        return self._saldo
    
class ContaCorrente(Conta): 
    """
    Implementação de Conta Corrente que herda de Conta com Limite Extra.
    Permite que o saldo fique negativo até o limite definido.
    """
    def __init__(self, agencia : int, num_conta : int, saldo, limite=0):
        """
        Inicializa a ContaCorrente com limite extra
        
        :limite -> valor extra (além do saldo)
        """
        super().__init__(agencia, num_conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        """
        Implementação do Método Abstrato sacar de Conta
        Realiza a validação de tipo e valor
        Permite o cliente sacar se o valor está dentro do limite
        
        Raises:
            TypeError: se o valor do saque não for um inteiro
            ValueError: se o valor do saque informado for negativo
        """
        
        if not isinstance(valor, (int, float)):
            raise TypeError('o valor não é um número') 
        if valor < 0:
            raise ValueError('o valor não pode ser negativo')
        
        saque = self._saldo - valor
        limite_maximo = -self.limite
 
        if saque >= limite_maximo:
            self._saldo -= valor
            limite_restante = self.limite + self._saldo
            self.detalhes(f'SACADO: {valor}')
            print(f'Limite atual: {limite_restante}')
            return self._saldo
            
        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')

    
    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}(Agencia: {self.agencia!r} | Conta: {self.num_conta!r} | Saldo: {self._saldo!r} | Limite {self.limite!r})'
    