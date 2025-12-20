# Sistema Bancário Python (POO)

Este projeto simula a lógica de um sistema bancário, focando em segurança e integridade de dados através dos pilares da **Programação Orientada a Objetos**.

## Funcionalidades:

- **Autenticação Rigorosa:** O banco valida agência, cliente, conta e o vínculo entre eles;
- **Tipos de Conta:** 
        **Conta Corrente:** Possui limite extra e permite saldo negativo até esse limite
        **Conta Poupança:** Bloqueia saques que deixariam o saldo negativo.
- **Segurança de Dados:** Uso de `@property` e `@setter` com levantamento de exceções (`TypeError` e `ValueError`);
- **Validação de Maioridade:** Bloqueio automático de cadastro para menores de 18 anos.

## Tecnologias e Conceitos Utilizados

- **Python 3.13**
- **Abstração:** Uso de classes abstratas (`ABC`) para modelos de conta;
- **Polimorfismo:** Métodos de saque é implementado de forma diferente em cada tipo de conta;
- **Encapsulamento:** Proteção de atributos sensíveis como `_saldo`.

## Estrutura do Projeto

* `pessoa.py`: Contém as classes `Pessoa` (base) e a `Cliente` que herda de Pessoa;
* `conta.py`: Contém a classe abstrata `Conta` e as implementações `ContaCorrente` e `ContaPoupanca` que herdam de Conta;
* `banco.py`: Classe principal que gerencia os dados e a lógica de autenticação;
* `main.py`: Script de execução que contém os cenários de teste.
