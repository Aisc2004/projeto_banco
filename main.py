from banco import Banco
import conta
import pessoa 
import random

#aqui vai ter uma interface, por enquanto tô fazendo teste aqui
banco = Banco()

def menu():
    
    while True:

        print('[1] Criar Conta')
        print('[2] Sacar')
        print('[3] Depositar')
        print('[4] Conferir o Histórico')
        print('[5] Volta para o menu')
        print('[6] Sair')

        resposta = input('Informe sua resposta')

        if resposta == '1':
            nome_cliente = input('Informe seu nome:')
            data_nasc = input('Informe sua data de nascimento(DD/MM/AAAA):')
            senha_cliente = input('Digite senha de 4 dígitos:')
            cpf_cliente = input('Informe o CPF: ')

            novo_cliente = pessoa.Cliente(nome_cliente, data_nasc, senha_cliente, cpf_cliente)

            print('[1] CONTA CORRENTE')
            print('[2] CONTA POUPANÇA')
            tipo_conta = input('Informe o tipo de conta:')

            agencia_cliente = random.randrange(1, 300)
            conta_cliente = random.randrange(1, 300)

            if tipo_conta == '1':
                conta_cliente = novo_cliente.abrir_conta_poupanca(agencia_cliente, conta_cliente, saldo=0)
                print('conta criada com sucesso')
            elif tipo_conta == '2':
                conta_cliente = novo_cliente.abrir_conta_corrente(agencia_cliente, conta_cliente, saldo=0, limite=0)
                print('conta criada com sucesso')
            else:
                print('Opção não existe')

       
        banco.clientes.append(novo_cliente)
        banco.contas.append(conta_cliente)
        banco.agencias.append(agencia_cliente)     
        print(banco)


        if resposta == '2':
            verificacao_cpf = input('Inforem o cpf')
            busca_cliente = None

            for cliente in banco.clientes:
                if cliente._cpf == verificacao_cpf:
                    busca_cliente = cliente




menu()

# banco = Banco()
# p1 = pessoa.Cliente('Ana', '20/10/2004', 1234)
# criando_conta = p1.abrir_conta_poupanca(111, 222, 100)
# criando_conta_cor = p1.abrir_conta_corrente(111, 223, 10, 9)

# p1.conta = criando_conta_cor
# p1.conta = criando_conta

# banco.clientes.append(p1)
# banco.contas.append(criando_conta)
# banco.agencias.append(111)
# banco.contas.append(criando_conta_cor)

# print(banco)

# senha = input('informe a senha: ')

# if banco.autenticar(p1, criando_conta, senha):
#     print(f'saldo disponivel de {p1.nome}: {criando_conta.saldo}')
#     criando_conta.depositar(50)
#     criando_conta.depositar(100)
#     criando_conta.sacar(10)
#     criando_conta.sacar(20)
#     for historic in criando_conta.historico:
#         print(historic)


