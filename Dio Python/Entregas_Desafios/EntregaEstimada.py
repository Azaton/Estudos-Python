#def calcularEntrega(nomeRestaurante, tempoEstimadoEntrega): # Função que recebe dois parâmetros: Restaurante e Tempo
#    return f"O restaurante {nomeRestaurante} entrega em {tempoEstimadoEntrega} minutos." # Interpolação de Strings

#def ProgramaEstimativa(): # Iniciando o programa
#    nomeRestaurante = input("Digite o nome do restaurante: ")
#    tempoEstimadoEntrega = int(input("Digite o tempo estimado de entrega em minutos: "))

#    mensagemDentrega = calcularEntrega(nomeRestaurante, tempoEstimadoEntrega)
#    print(mensagemDentrega) 

#if __name__ == "__main__":
#    ProgramaEstimativa()
   
    
    
# Imprimir a saída no padrão definido no enunciado deste desafio.
# Dica: Para simplificar a formatação, utilize o conceito de interpolação de strings.

nomeRestaurante = str(input())
tempoEstimadoEntrega = int(input())

mensagemEntrega = f"O restaurante {nomeRestaurante} entrega em {tempoEstimadoEntrega} minutos."
print(mensagemEntrega)