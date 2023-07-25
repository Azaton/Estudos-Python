# Atividade: Criar as condições para aplicar o cupom de desconto (10% ou 20%).

def main():                         # Inicia o programa
    n = int(input())                # N recebe a quantidade de itens que serão adicionados ao pedido

    total = 0

    for i in range(1, n + 1):           # Se o usuário digitar 2 ou mais pedidos, o sistema faz o loop para pegar o nome do produto e valor
        pedido = input().split()        # Divide a String em duas partes (por espaço) e o valor deve ser float 00.00 (R$ 00,00)
        if len(pedido) != 2:            # Dado que é 2, então divide em duas partes. Se diferente de 2, da "erro" e apresenta mensagem
            print("Entrada inválida. Informar o nome e o valor do pedido separados por espaço.")
            return

        nome = pedido[0]                # Recebe o valor "Nome" e armazena na primeira posição
        valor = float(pedido[1])        # Recebe o valor "Valor" e armazena na segunda posição (num formato numérico)
        total += valor

    cupom_desconto = input()
    if cupom_desconto == "10%":                # Espera que o usuário digite exatamente "10%" para assumir qual a matemátia
        total_com_desconto = total * 0.9       # Se o valor for "10%", o programa calcula o valor total com desconto aplicando um desconto de 10%   
    elif cupom_desconto == "20%":
        total_com_desconto = total * 0.8
    else:
        print("Cupom de desconto inválido. Escolha entre '10%' ou '20%'.")
        return

    print(f"Valor total: {total_com_desconto:.2f}")     

if __name__ == "__main__":
    main()                          # Fecha o programa