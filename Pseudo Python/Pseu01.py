# receber dois números inteiros
# fazer 4 operações matemáticas (somar, subtrair, dividir e multiplicar)
# Exibir o resultado

# algoritmo "Operações Matemáticas"

# var
# Num1, Num2, Num3 : inteiro
# NumReal : real

# Escreva "Digite o primeiro número " = Num1
# Escreva "Digite o segundo número " = Num2

#   Imprimir ("A soma é " Num3 = Num1 + Num2)
#   Imprimir ("A subtração é " Num3 = Num1 - Num2)
#   Imprimir ("O valor multiplicado é " Num3 = Num1 * Num2)
#   Imprimir ("A divisão é " NumReal = Num1 / Num2)

# Entrada de dados
Num1 = int(input("Digite o primeiro número: "))
Num2 = int(input("Digite o segundo número: "))

# Operações matemáticas
soma = Num1 + Num2
subtracao = Num1 - Num2
multiplicacao = Num1 * Num2
divisao = Num1 / Num2

# Saída de resultados
print("A soma é", soma)
print("A subtração é", subtracao)
print("O valor multiplicado é", multiplicacao)
print("A divisão é", divisao)