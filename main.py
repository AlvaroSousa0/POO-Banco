import banco, conta, cliente

Santander = banco.Banco("Santader")


c1 = cliente.Cliente("José", 472)
Santander.novo_cliente_corrente(c1, 1945361)

c2 = cliente.Cliente("Pedro", 923)
Santander.novo_cliente_poupanca(c2, 423)

print(Santander.autenticar(c1, c1.conta))
c1.conta.depositar(35135)

