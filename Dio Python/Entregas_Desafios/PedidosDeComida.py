# Atividade: Criar as condições para aplicar o cupom de desconto (10% ou 20%).

def main():                         # Inicia o programa
    n = int(input())

    total = 0

    for i in range(1, n + 1):           # 
        pedido = input().split()        # Divide a String em duas partes.
        if len(pedido) != 2:            # Dado que é 2, então divide em duas partes. Se diferente de 2, da "erro" e apresenta mensagem
            print("Entrada inválida. Por favor, Informar o nome e o valor do pedido separados por espaço.")
            return

        nome = pedido[0]
        valor = float(pedido[1])
        total += valor

    cupom_desconto = input()
    if cupom_desconto == "10%":             # Espera que o usuário digite exatamente "10%" para assumir qual a matemátia
        total_com_desconto = total * 0.9    # Se o valor for "10%", o programa calcula o valor total com desconto aplicando um desconto de 10%   
    elif cupom_desconto == "20%":
        total_com_desconto = total * 0.8
    else:
        print("Cupom de desconto inválido. Escolha entre '10%' ou '20%'.")
        return

    print(f"Valor total: {total_com_desconto:.2f}")     

if __name__ == "__main__":
    main()                                        # Fecha o programa