####### EXERCÍCIO: SISTEMA BANCÁRIO #######

# Funcionalidades: Depósito, Saque, Extrato, Sair
# Não permitir valor negativo ou entrada "0" ou maior que "4"
# Deposito não tem limite.
# Regra: 3 saques diários, com limite de R$ 500 por saque.
# Para resetar o dia, pare o programa e recomece as operações.
# Exibir o saldo atual já préconfigurado na variável "saldo" da conta.
# Não existe usuário, senha, validação de AG/CC.
# Exibir histórico em "Extrato"

saldo = 5000
limite = 500
extrato = []
numero_saques = 0
limite_saques = 3

menu = '''
================== MENU INICIAL ======================
\n
Selecione a operação:
\n
1 - Depósito
2 - Saque
3 - Extrato
4 - Sair
'''

while True:
    print(menu)
    
    opcao = input("Digite o número da operação desejada: ") # Chama a ação pelo usuário
    
    if opcao == "1":                                         # Se for "1"
        valor = float(input("Digite o valor do depósito: ")) # Chama a ação pelo usuário
        if valor >= 0:                                       # Se for valor menor que "0", vai pro else
            saldo += valor                                   # Atribuição e adição de valor
            extrato.append(valor)                            # Adiciona o valor do depósito realizado à lista "Extrato"
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido. O valor do depósito deve ser positivo.")
        
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))                             # Solicita ao usuário o valor do saque
        if valor >= 0:                                                                # Verifica se o valor é não negativo
            if valor <= saldo and valor <= limite and numero_saques < limite_saques:  # Verifica se o valor está menor que os demais e limites de saques
                saldo -= valor                                                        # Atualiza o saldo com o valor sacado
                extrato.append(-valor)                                                # Adiciona o valor do saque (negativo) à lista extrato
                numero_saques += 1                                                    # Incrementa o número de saques realizados
                print("Saque realizado com sucesso.")
            else:
                print("Valor de saque inválido. Verifique se o valor está dentro do limite disponível ou se você excedeu o número máximo de saques.")
        else:
            print("Valor inválido. O valor do saque deve ser positivo.")
        
    elif opcao == "3":
        print("Extrato:")
        for operacao in extrato:                          # Percorre a lista extrato
            if operacao > 0:                              # 
                print(f"Depósito: R$ {operacao:.2f}")     # Exibe depósitos
            else:                                         # 
                print(f"Saque: R$ {-operacao:.2f}")       # Exibe saques (valor negativo)
        print(f"Saldo atual: R$ {saldo:.2f}")             # Exibe o saldo atual
        
    elif opcao == "4":
        break                                             # Encerra o loop e sai do programa
    
    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada.") # Se não 1, 2, 3, ou 4, então cai aqui e volta no "While"