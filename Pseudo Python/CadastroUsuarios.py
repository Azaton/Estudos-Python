# algoritmo "VETORES"

# Declarar 5 variáveis do tipo literal, mas em vetor
# VNome : vetor[1..5] de 'literal'
# VIdades : vetor[1..5] de 'inteiro'

# inicio

# para i de 1 até 5 faça
# Escreval ("Informe seu nome")
# Leia(vetorNomes[i])
# fimpara

# fimalgoritmo

# Algoritmo "VETORES"

# Declarar 5 variáveis do tipo literal, com vetor e em Python
# Declarar listas (vetores) para armazenar os nomes e idades

# Declarar listas para armazenar os nomes e idades
# Algoritmo "VETORES"

# Declarar listas para armazenar os nomes e idades
# Algoritmo "VETORES"

# Declarar listas para armazenar os nomes e idades
VNome = []
VIdades = []

# Variável para verificar se o nome foi encontrado
nome_encontrado = False

# Loop para receber os dados
while True:
    # Solicitar o nome
    nome = input("Informe seu nome ('xx' para sair): ")
    # Verificar se foi digitado 'xx' para sair
    if nome == 'xx':
        break

    # Verificar se o nome é 'Mendes'
    if nome == 'Mendes':
        nome_encontrado = True
        print("*** - ENCONTRADO - ***")
        print("Nome:", nome)
        break
    
    # Solicitar a idade
    idade = input("Informe sua idade ('00' para sair): ")
    # Verificar se foi digitado '00' para sair
    if idade == '00':
        break
    
    # Converter a idade para inteiro
    idade = int(idade)
    
    # Adicionar os dados nas respectivas listas
    VNome.append(nome)
    VIdades.append(idade)

# Exibir os dados inseridos anteriormente
if nome_encontrado:
    print("Dados inseridos anteriormente:")
    for i in range(len(VNome)):
        print("Nome:", VNome[i], "| Idade:", VIdades[i])