import abc

class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float) -> None:
        self. agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor) -> None: ...


    def depositar(self, valor):
        self.saldo += valor

    
class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float) -> None:
        super().__init__(agencia,conta,saldo)
        self.limite = 200

    def sacar(self, valor): 
        if valor > self.saldo:
            valor -= self.saldo
            self.saldo = 0
            self.limite -= valor
            print(f' Seu saldo é: {self.saldo}\n'
                  ,f'Limite especial restante é:{self.limite}\n'
                  ,f'Limite especial usado foi de: {valor}')
        else:
            self.saldo -= valor
            print(f'Seu saldo restante é: {self.saldo}')


class ContaPoupanca(Conta):
    def __init__(self, agencia: int, conta: int ,saldo: float) -> None:
        super().__init__(self, agencia,conta,saldo)


    def sacar(self, valor):
        if valor > self.saldo:
            print('Vocẽ não tem saldo suficiente \n'
                  f'Saldo disponível: {self.saldo}')
        else:
            self.saldo -= valor
            print(f'Saldo restante: {self.saldo}')