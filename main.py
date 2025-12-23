from banco import Banco
import conta
import pessoa 

#aqui vai ter uma interface, por enquanto tô fazendo teste aqui

banco = Banco()
p1 = pessoa.Cliente('Ana', '20/10/2004', 1234)
conta_pou_cl1 = conta.ContaPoupanca(111, 123, 20)
p1.conta = conta_pou_cl1

banco.clientes.append(p1)
banco.contas.append(conta_pou_cl1)
banco.agencias.append(111)

print(banco)

senha = input('informe a senha: ')
if banco.autenticar(p1, conta_pou_cl1, senha):
    print(f'saldo disponivel de {p1.nome}: {conta_pou_cl1.saldo}')
