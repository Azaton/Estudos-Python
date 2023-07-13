# AULA "Tipos de Operadores com Python"

print(10 % 7) # módulo
print(2 ** 3) # Exponenciação -- 2 ao cubo
print(10-2*5) # Parêntesis, Expoêntes, Multiplicações e Divisões, Somas e Subtrações (da esquerda para direita)

valor1 = float(input("Digite o valor: ")) # declara a variável tipo flutuante e pede para o usuário inputar os números
valor2 = float(input("Digite o segundo valor: "))
soma = valor1 + valor2
print(soma)

### WHILE TRUE ####
# Um loop infinito que fica pedindo entrada do tipo numérico. Diferente disso, da erro e insiste até colocar números

while True:
    try:
        valor1 = float(input("Digite o valor: "))
        break
    except ValueError:
        print("Valor inválido. Digite apenas números.")

while True:
    try:
        valor2 = float(input("Digite o segundo valor: "))
        break
    except ValueError:
        print("Valor inválido. Digite apenas números.")

soma = valor1 + valor2
print("A soma é:", soma)