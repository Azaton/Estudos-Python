def main():
    n = int(input("Digite o número de pedidos: "))
    
    total = 0
    
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor       
        
    escolha_cupom = input("Digite o cupom de desconto (10% ou 20%): ")
    
    if escolha_cupom == "10%":
        total -= total * 0.1
    elif escolha_cupom == "20%":
        total -= total * 0.2
        
    print(f"Valor total: {total:.2f}")

if __name__ == "__main__":
    main()