numPedidos = int(input())

pedidos = []  # Lista para armazenar os pedidos

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    
    ehVegano = None                 
    while ehVegano is None:                                          # Quando "None", o loop é executado até que o usuário insira uma opção válida
        ehVegano_input = input("O prato é vegano? (S/N): ").lower()  # Lower converte para minusculo, para evitar erros
        if ehVegano_input == 's':                                    # Se "S", termina e acrescenta via "pedidos.append"
            ehVegano = True
        elif ehVegano_input == 'n':
            ehVegano = False
        else:
            print("Opção inválida. Digite 'S' para sim ou 'N' para não.")   # Se não for S ou N, volta e força o usuário digitar uma entrada válida
            
    pedidos.append((i, prato, ehVegano, calorias))                          # Adiciona os detalhes do pedido à lista de pedidos

for itens in pedidos:
    num, prato, ehVegano, calorias = itens     # Lista (tupla) com quatro elementos
    print(f"Pedido {num}: {prato} ({'Vegano' if ehVegano else 'Nao-vegano'}) - {calorias} calorias")    
    
# informacoes_pedidos = [ # Criando uma lista com as informações formatadas de cada pedido
#    f"Item {num}: {prato} ({'Vegano' if ehVegano else 'Nao-vegano'}) - {calorias} calorias"
#    for num, prato, ehVegano, calorias in pedidos]

# resultado = "\n".join(informacoes_pedidos) # Utilizando a função join para juntar as informações dos pedidos em uma única string, separada por quebra de linha

# print(resultado)