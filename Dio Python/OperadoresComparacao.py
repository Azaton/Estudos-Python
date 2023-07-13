# AULA "Tipos de Operadores com Python"
# Imagina que precisamos valir se o usuário pode ou não sacar, dependendo do valor que tem em conta
# Se o saque for maior que o saldo, não deve ser permitido

saldo = float(input("Informe o saldo: "))
saque = float(input("Qual será o valor do Saque? "))

print(saldo == saque) # verifica se é igual
print(saldo != saque) # verifica desigualdade. Se sim, então TRUE
print(saldo >= saque) # verifica se saldo é maior-igual ao saque
print(saldo < saque)