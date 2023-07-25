# Desafio: Identificando Pedidos Veganos
# Enunciado: https://dev.azure.com/Personal-Scrum/Agile%20Master/_workitems/edit/157

numPedidos = int(input())

pedidos = [] # Lista para armazenar os pedidos

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())    
    
    while True:                                  # Entra no loop: se "S" ou "N" para definir se o item é vegano
        ehVegano_input = input(" ").lower()      # Converte para minúsculo
        if ehVegano_input == 's':
            ehVegano = True
            break
        elif ehVegano_input == 'n':
            ehVegano = False
            break
        else:
            print("Opção inválida. Digite 'S' para sim ou 'N' para não.")

    pedidos.append((i, prato, ehVegano, calorias))        # Adiciona os detalhes do pedido à lista de pedidos

for itens in pedidos:
    num, prato, ehVegano, calorias = itens     # Lista (tupla) com quatro elementos
    print(f"Item {num}: {prato} ({'Vegano' if ehVegano else 'Nao-vegano'}) - {calorias} calorias")