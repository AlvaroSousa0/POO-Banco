import banco, conta, cliente

Santander = banco.Banco()
Itau = banco.Banco()


c1 = cliente.Cliente("José", 472)
Santander.novo_cliente_corrente(c1, 1945361)

c1.conta.depositar(35135)

print()