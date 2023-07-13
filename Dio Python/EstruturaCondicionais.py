# Estruturas Condicionais + Desvio de Controles
#  

import sys


saldo = 5000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")
    
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrado: "))

# Desvio através de opções
if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção inválida")

# Idade

MAIOR_IDADE = 18

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
    
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")
    
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")
    
# IF aninhado
conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    
    if saldo >= saque:
        print("Saque realizado com sucsso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Não é possível realizar o saque, saldo insuficiente")

elif conta_universitaria:
    
    if saldo >= saque:
        print("Saque realizado com sucesso!")        
    else:
        print("Saque realizado com sucesso")    

elif conta_especial:
    print("Conta especial selecionada!")
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")
