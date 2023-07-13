# --------- AULA "Tipos de Operadores com Python"------------ # 
# Operador "E"

saldo = 1000 # saldo na conta corrrente
limite = 300 # limite permitido para o saque
saque = float(input("Qual será o valor do Saque? ")) # solicita para o usuário o valor que ele deseja retirar

print(saque <= limite and saque <= saldo )

# ----------------------------------------------------------- # 
# Operador "Negação"

contatos_emergencia = []
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

print(not valor1 > valor2)      # primeiro compara
print(not contatos_emergencia)  # uma lista sem elementos é "falto", mas a operação é not, então é TRUE
print(not "")                   # String vazia, sem sequência é falso

# ----------------------------------------------------------- # 
# Operador com Parênteses
# Conta especial pode SACAR além do limite, mas NÃO PODE sacar além do SALDO DISPONÍVEL
# AND = ambos os resultados tem que ser TRUE para ser TRUE
# OR = para ser TRUE apenas um tem que ser TRUE

saldo = 2000          # Saldo na Conta Corrente
limite = 500          # Limite permitido para o saque
conta_especial = True # O valor TRUE representa que a conta é especial e pode sacar além do limite

saque = float(input("Qual será o valor do Saque? ")) # solicita para o usuário o valor que ele deseja retirar

print("Pode efetuar o saque?", ((saque <= limite or conta_especial) and (saque <= saldo)))
print("Pode efetuar o saque?", ((saque <= limite) and (saque <= saldo)))
# print(saque >= limite and saque <= limite or conta_especial and saldo >= saque)