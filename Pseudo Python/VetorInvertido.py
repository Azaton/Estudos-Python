# Preciso gerar o cenário onde um determinado vetor/lista, armazene os números conforme o usuário digita
# O usuário digita o número e da ENTER. Digita, aperta Ender e Digita novamente, infinitamente.
# ... Dado que o usuário digitou '00', Então o sistema pega todos os números que foram digitados e exibi também como resultado...
# ... E exibi os númmeros que foram digitos e também de forma invertida

# EM PYTHON 🤓

VNumero = []

while True:                                                   # Loop para receber os dados
    numero = input("Informe o número ('00' para sair): ")     # Solicitar a numero
    if numero == '00':                                        # Verificar se foi digitado '00' para sair
        break
                                                                     
    numero = int(numero)   # Converter a idade para inteiro, pois por padrão é string
    
    VNumero.append(numero) # Adicionar os dados nas respectivas listas
    
print("Números digitados:") # Exibir os números digitados
print(VNumero)

# Exibir os números digitados em ordem invertida
print("Números digitados (em ordem invertida):")
print(VNumero[::-1])