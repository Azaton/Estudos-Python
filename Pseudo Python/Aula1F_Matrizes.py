# algoritmo "Matrizes" - Aula 1.F

# var
# cinema : vetor[1..10, 1..10] de literal
# i,j : inteiro

# inicio

#   para i de 1 ate 10 faça
#       para j de 1 ate 10 faça
#           cinema[i,j] <- "0"
#       fimpara
#   fimpara

# repita
# Escreval ("1 - Reservar")
# Escreval ("2 - Layout do Cinema")
# Escreval ("3 - Sair")
# Leia (opcao)

# escolha opcao
#   caso "1"    
#       Escreval("Fila")
#       Leia (fila)
#       Escreval("Poltrono")
#       Leia (poltrona)
#       
#       se cinema[fila,poltrono] = "0" entao
#          cinema[fila,poltrono] <- "x" 
#       senao
#           Escreval ("Poltrona já ocupada")
#       fimse

#   caso "2"    
#       para i de 1 ate 10 faça
#           para j de 1 ate 10 faça
#               cinema[i,j] <- "0"
#           fimpara
#       fimpara
# fimescolha

# Algoritmo "Matrizes"

# Criar a matriz do cinema como uma lista aninhada
# Algoritmo "Matrizes"

# Criar a matriz do cinema como uma lista aninhada
cinema = [['0' for _ in range(10)] for _ in range(10)]

# Função para exibir o layout do cinema
def exibir_layout():
    print("Layout do Cinema:")
    for i in range(10):
        for j in range(10):
            print(cinema[i][j], end=' ')
        print()

# Loop para preencher a matriz com "0"
for i in range(10):
    for j in range(10):
        cinema[i][j] = '0'

# Exibir o layout inicial do cinema
exibir_layout()

# Loop principal para exibir o menu e realizar ações
while True:
    print("1 - Reservar")
    print("2 - Exibir vagas disponíveis")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        fila = int(input("Fila: "))
        poltrona = int(input("Poltrona: "))

        if cinema[fila][poltrona] == '0':
            cinema[fila][poltrona] = 'x'
            print("Reserva realizada com sucesso!")
        else:
            print("Poltrona já ocupada")

    elif opcao == "2":
        vagas_disponiveis = 0
        for i in range(10):
            for j in range(10):
                if cinema[i][j] == '0':
                    vagas_disponiveis += 1
        print("Vagas disponíveis:", vagas_disponiveis)

    elif opcao == "3":
        break

    # Exibir o layout atualizado do cinema após cada ação
    exibir_layout()










