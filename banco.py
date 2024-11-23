import conta
import cliente
import random


class Banco:
    def __init__(self, agencias:list[int] | None = None,
                 contas: conta.Conta | None = None, cliente: cliente.Cliente | None = None) -> None:
        self.agencias = agencias or []
        self.contas = contas or []
        self.cliente = cliente or []


    def checa_agencia(self, agencia):
        return agencia in self.agencias or False
    

    def checa_conta(self, conta):
        return conta in self.contas or False
    
    def novo_cliente_corrente(self, conta_cliente, saldo):
        """
        Cria um novo cliente com conta corrente

        num_conta devereceber um inteiro aleatorio de 7 digitos para ser o numero da conta

        agencia recebe um inteiro de 4 digito como numero da agencia
        
        cc é a instância da ContaCorrente usando as variaveis previamente definidas como argumento

        cliente_conta define na classe cliente qual é a conta dele

        em seguida tudo é adicionado nas variaveis de classe
        """
        num_conta = random.randint(1,9999999)
        agencia = random.randint(1, 9999)
        cc = conta.ContaCorrente(agencia, num_conta, saldo)
        cliente_conta = conta_cliente
        cliente_conta.conta = cc
        self.contas.append(cc)
        self.agencias.append(agencia)
        self.cliente.append(cliente_conta)
        

    def novo_cliente_poupanca(self, conta_cliente, saldo):
        """
        Cria um novo cliente com conta poupanca

        num_conta devereceber um inteiro aleatorio de 7 digitos para ser o numero da conta

        agencia recebe um inteiro de 4 digito como numero da agencia
        
        cc é a instância da ContaCorrente usando as variaveis previamente definidas como argumento

        cliente_conta define na classe cliente qual é a conta dele

        em seguida tudo é adicionado nas variaveis de classe
        """
        num_conta = random.randint(1,9999999)
        agencia = random.randint(1, 9999)
        cp = conta.ContaPoupanca(agencia, num_conta, saldo)
        cliente_conta = conta_cliente
        cliente_conta.conta = cp
        self.contas.append(cp)
        self.agencias.append(agencia)
        self.cliente.append(cliente_conta)

        