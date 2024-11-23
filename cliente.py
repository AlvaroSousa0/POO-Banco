import conta


class Cliente:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        self.conta: conta.Conta | None = None