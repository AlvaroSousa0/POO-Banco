import conta
import cliente


class Banco:
    def __init__(self, agencias:list[int] | None = None,
                 contas: conta.Conta | None = None, cliente: cliente.Cliente | None = None) -> None:
        self.agencias = agencias or []
        self.contas = contas or []
        self.cliente = cliente or []


    