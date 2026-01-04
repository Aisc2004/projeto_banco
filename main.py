from banco import Banco
import conta
import pessoa 
import random

banco = Banco()

def menu():
    '''
    Essa função gera o menu que gerencia o fluxo das atividades do banco que são: Criar Conta, Sacar, Depositar, Conferir o Histórico e Sair
    '''
    while True:

        print('[1] Criar Conta')
        print('[2] Sacar')
        print('[3] Depositar')
        print('[4] Conferir o Histórico')
        print('[5] Sair')

        resposta = input('Informe sua resposta: ')

        if resposta == '1':
            try:
                nome_cliente = input('Informe seu nome: ')
                data_nasc = input('Informe sua data de nascimento(DD/MM/AAAA): ')
                senha_cliente = input('Digite senha de 4 dígitos: ')
                cpf_cliente = input('Informe o CPF: ')
            
                novo_cliente = pessoa.Cliente(nome_cliente, data_nasc, senha_cliente, cpf_cliente)

                print('[1] CONTA POUPANÇA')
                print('[2] CONTA CORRENTE')
                tipo_conta = input('Informe o tipo de conta: ')

                if tipo_conta != '1' and tipo_conta != '2':
                    print('ERRO: tipo de conta informado não existe')
                    continue

                agencia_cliente = random.randrange(1, 300)
                conta_range = random.randrange(1, 300)

                if tipo_conta == '1':
                    conta_cliente = novo_cliente.abrir_conta_poupanca(agencia_cliente, conta_range, saldo=0)
                elif tipo_conta == '2':
                    conta_cliente = novo_cliente.abrir_conta_corrente(agencia_cliente, conta_range, saldo=0, limite=50)
                else:
                    print('Opção não existe')

                print(novo_cliente, conta_cliente)
                banco.clientes.append(novo_cliente)
                banco.contas.append(conta_cliente)
                banco.agencias.append(agencia_cliente)    
                
            except ValueError as e:
                print(e)
            except TypeError as e:
                print(e) 

        elif resposta > '1' and resposta < '5':
            try:
                verificacao_cpf = input('Informe o cpf: ')
                verificacao_conta = input('Informe a conta: ')

                if not verificacao_conta:
                    print('Número da conta não foi informado')
                    continue
                
                busca_cliente = None
                busca_conta = None    

                for cliente in banco.clientes:
                    if cliente._cpf == verificacao_cpf:
                        busca_cliente = cliente

                for conta in banco.contas:
                    if conta.num_conta == int(verificacao_conta):
                        busca_conta = conta

                if busca_cliente != None and busca_conta != None:
                    print(f'{busca_cliente, busca_conta}')
                    senha_inserida = input('Informe a senha: ')

                    if banco.autenticar(busca_cliente, busca_conta, senha_inserida):
                        if resposta == '2':
                            sacar = float(input('Informe quanto deseja sacar: '))
                            busca_conta.sacar(sacar)

                        elif resposta == '3':
                            depositar = float(input('Informe quanto deseja depositar: '))
                            busca_conta.depositar(depositar)

                        else:
                            for historico in busca_conta.historico:
                                print(historico)
                else:
                    print('ERRO: Suas informações não foram encontradas no Banco')

            except ValueError as e:
                print(e)
            except TypeError as e:
                print(e)                
        else:
            return
              
menu()


