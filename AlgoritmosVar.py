# algoritmo "Trabalhando com Tipos de Variáveis"
# var
# > nome, sobrenome, nomeCompleto: literal
# inicio
# > Escreval ("Informe o seu nome: ")
# > Leia (nome)
# > Escreval ("Informe o seu sobrenome: ")
# > Leia (sobrenome)
# > nomeCompleto <- nome + " " = + sobrenome /aqui é o processamento para armazenar
# > Escreval (nomeCompleto)
# fimalgoritmo

# Início do código em Python *_* executar no terminal: python Algoritmos.py

nome = input("Informe o seu nome: ")
sobrenome = input("Informe o seu sobrenome: ")

nomeCompleto = nome + " " + sobrenome  # Soma o input dos dois resultados

print(nomeCompleto)