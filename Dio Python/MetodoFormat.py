######### Método Format #########
nome = input("Digite o nome: ")
idade = input("Digite a idade: ")
profissao = input("Digite a profissão: ")

print("Nome: {}, Idade: {}, Profissão: {}".format(nome, idade, profissao))
print(f"Nome: {nome}, Idade: {idade}, Profissão: {profissao}")

######### Formatar strings com f-string #########
valor = float(input("Digite um valor: "))

formatted_valor = f"O valor digitado é: {valor:.2f}" # Usando f-string para formatar o valor (considerar dois dígitos após o ponto)
formatted_valor = f"O valor digitado é: {valor:10.2f}" # Coloca 10 espaços em branco

print(formatted_valor) # Imprimindo o valor formatado
