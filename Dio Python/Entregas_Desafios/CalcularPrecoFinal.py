
# Calcular o preço final do pedido (total dos hambúrgueres + total das bebidas).
# Calcular o troco do pedido, considerando o preço final e o valor pago pelo usuário.
# Imprimir a saída no formato especificado neste desafio.

# TESTE #1
valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

totalHamburguer = valorHamburguer * quantidadeHamburguer
totalBebida = valorBebida * quantidadeBebida
precoTotalPedido = totalHamburguer + totalBebida
troco = valorPago - precoTotalPedido

print(f"O preço final do pedido é R$ {precoTotalPedido:.2f}. Seu troco é R$ {troco:.2f}.")