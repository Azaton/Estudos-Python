# Indentação e Blocos de Comando
# O que delimita é a estética, o bloco pela intentação
# Onde começa e termina, através da estética


def sacar():
    saldo = 500

    valor = float(input("Informe o valor: "))

    if valor <= saldo:
        saldo -= valor
        print("Valor Sacado:", valor)
    else:
        print("Não é possível sacar. Saldo insuficiente.")

    print("Saldo restante:", saldo)

sacar()
