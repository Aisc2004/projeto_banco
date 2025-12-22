from banco import Banco
import conta
import pessoa

#-------------------------------------- testes----------------------------------------
#inicializando o banco com agencias, contas e clientes
banco = Banco()

cliente1 = pessoa.Cliente('luiza', '05/06/2004')
conta_pou_cl1 = conta.ContaPoupanca(111, 123, 20)
cliente1.conta = conta_pou_cl1

cliente2 = pessoa.Cliente('Flavio', '05/06/1950')
conta_cor_cl2 = conta.ContaCorrente(222, 890, 12, 90)
cliente2.conta = conta_cor_cl2

cliente3 = pessoa.Cliente('Ana', '05/06/2001')
conta_pou_cl3 = conta.ContaPoupanca(333, 235, 345)
cliente3.conta = conta_pou_cl3

banco.clientes.append(cliente1)
banco.contas.append(conta_pou_cl1)
banco.agencias.append(111)

banco.clientes.append(cliente2)
banco.contas.append(conta_cor_cl2)
banco.agencias.append(222)

banco.clientes.append(cliente3)
banco.contas.append(conta_pou_cl3)
banco.agencias.append(333)

print(banco)

#TESTE DE SUCESSO  
print()
if banco.autenticar(cliente1, conta_pou_cl1):
    print(f'saldo disponivel de {cliente1.nome}: {conta_pou_cl1.saldo}')

#TESTE DE VINCULO (CLIENTE CERTO, CONTA ERRADA)
print()
banco.autenticar(cliente1, conta_cor_cl2)

#TESTE DE CLIENTE QUE NÃO ESTÁ NO BANCO
print()
cliente_anonimo = pessoa.Cliente('Anonimo', '05/06/2004')
banco.autenticar(cliente_anonimo, conta_pou_cl3)

#TESTE DE AGÊNCIA INCORRETA
print()
errada_agencia = conta.ContaPoupanca(999, 123, 20)
cliente1.conta = errada_agencia
banco.autenticar(cliente1, errada_agencia)

#-------------------------------TESTE DE OPERAÇÕES BANCÁRIAS-------------------------------

#TESTE COM A CONTA CORRENTE
print()
if banco.autenticar(cliente2, conta_cor_cl2):
    print(f'saldo disponivel de {cliente2.nome}: {conta_cor_cl2.saldo}')

    conta_cor_cl2.sacar(30)
    conta_cor_cl2.depositar(10)
    conta_cor_cl2.sacar(90)
    print()
    print(f'VALOR ATUALIZADO: {cliente2.conta.saldo}\n')

#TESTE DE SUCESSO COM A CONTA POUPANCA
if banco.autenticar(cliente3, conta_pou_cl3):
    print(f'saldo disponivel de {cliente3.nome}: {conta_pou_cl3.saldo}')

    conta_pou_cl3.sacar(345)
    conta_pou_cl3.sacar(1)

#------------------------------------ TESTES DE ERROS --------------------------------------

print('\nTIPAGEM')
try:
    cliente_novo = pessoa.Cliente('05/06/1980', 'carlos')
except ValueError as e:
    print(f'TESTE COM SUCESSO: {e}') 

print('\nERRO DE VALOR')
try:
    cliente_novo = pessoa.Cliente('carlos', '05/06/2009')
except ValueError as e:
    print(f'TESTE COM SUCESSO: {e}')

print('\nTIPAGEM')
try:
    cliente_novo = pessoa.Cliente('carlos', '05/06/2004')
    conta_pou_novo = conta.ContaPoupanca('sis', 233, 0)
    cliente_novo.conta = conta_pou_novo
    banco.contas.append(conta_pou_novo)
except TypeError as e:
    print(f'TESTE COM SUCESSO: {e}')

print('\nTIPAGEM')
try:
    cliente_novo = pessoa.Cliente('carlos', '05/06/2004')
    conta_cor_novo = conta.ContaCorrente(111, 'sis', 0, 100)
    cliente_novo.conta =conta_cor_novo
    banco.contas.append(conta_cor_novo)
except TypeError as e:
    print(f'TESTE COM SUCESSO: MENSAGEM: {e}')

print('\nTIPAGEM')
try:
    conta_cor_cl2.depositar('sss')
except TypeError as e:
    print(f'TESTE COM SUCESSO: MENSAGEM: {e}')

print('\nERRO DE VALOR')
try:
    conta_cor_cl2.depositar(-2)
except ValueError as e:
    print(f'TESTE COM SUCESSO: MENSAGEM: {e}')

print('\nTIPAGEM')
try:
    conta_pou_cl1.sacar('sss')

except TypeError as e:
    print(f'TESTE COM SUCESSO: MENSAGEM: {e}')

print('\nERRO DE VALOR')
try:
    conta_pou_cl1.sacar(-3)

except ValueError as e:
    print(f'TESTE COM SUCESSO: MENSAGEM: {e}')

print('\nTIPAGEM')
try:
    conta_cor_cl2.sacar('sss')
except TypeError as e:
    print(f'TESTE COM SUCESSO: MENSAGEM: {e}')

print('\nERRO DE VALOR')  
try:
    conta_cor_cl2.sacar(-2)
except ValueError as e:
    print(f'TESTE COM SUCESSO: MENSAGEM: {e}')



   
