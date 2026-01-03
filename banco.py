import conta
import pessoa

class Banco:
    """
    Essa classe gerencia as contas, agências e clientes realizando validação e a operação bancária
    """
    def __init__(self, agencias: list[int] | None =None, 
                 clientes: list[pessoa.Cliente] | None=None, 
                 contas: list[conta.Conta] | None = None):
        """
        Inicializa o Banco com listas
        
        :agencias -> lista de números de agências permitidas
        :clientes -> lista de objetos Clientes cadastrados
        :contas -> lista de objetos Conta cadastrados
        """
        
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []

    def _checagem_agencia(self, conta):
        """Verifica se a agência da conta está cadastrada no banco."""
        if conta.agencia in self.agencias:
            return True
        return False

    def _checagem_cliente(self, cliente):
        """Verifica se o cliente está cadastrado no banco."""
        if cliente in self.clientes:
            return True
        return False

    def _checagem_conta(self, conta): 
        """Verifica se a conta está cadastrada no banco."""
        if conta in self.contas:
            return True
        return False

    def _chegagem_conta_cliente(self, cliente, conta):
        """Verifica se a conta informada pertence ao cliente informado."""
        if conta is cliente.abrir_conta_poupanca or cliente.abrir_conta_corrente:
            return True
        return False
    
    def autenticar(self, cliente : pessoa.Cliente, conta: conta.Conta, senha_digitada : int):
        """
        Realiza as validações:
        
        1. se agência é válida
        2. se cliente é válido
        3. se conta é válida
        4. se a conta é do cliente

        :conta -> o objeto da conta que tenta a operação
        :cliente -> o objeto do cliente que tenta a operação
        """
        if not self._checagem_agencia(conta):
            print('agencia informada não existe')
            return False

        if not self._checagem_cliente(cliente):
            print('o cliente informado não existe')
            return False


        if not self._checagem_conta(conta):
            print('a conta informada não existe')
            return False
        
        if not self._chegagem_conta_cliente(cliente, conta):
            print('o cliente não está vinculado a essa conta')
            return False

        if not cliente.verificar_senha(senha_digitada):
            print('senha incorreta')
            return False
        
        print('autenticação concluída')
        return True

        
    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name} (AGENCIA: {self.agencias!r}, CONTAS: {self.contas!r}, CLIENTES: {self.clientes!r})' 

    def __str__(self):
        return f'AGÊNCIA: {self.agencias} | CONTAS: {self.contas} | CLINTES: {self.clientes}'
