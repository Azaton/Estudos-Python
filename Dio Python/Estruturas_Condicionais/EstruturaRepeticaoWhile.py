# Inicialização da variável de entrada
numero = int(input("Digite um número (0 para sair): "))

# Execução do loop enquanto o número digitado for diferente de zero
while numero != 0:
    # Realiza alguma operação com o número
    quadrado = numero ** 2
    print("O quadrado de", numero, "é", quadrado)
    
    # Solicita um novo número
    numero = int(input("Digite um número (0 para sair): "))

print("Programa encerrado.")
