nome = input("Digite um nome: ")

primeiro_caractere = nome[0]
print("Primeiro caractere:", primeiro_caractere)

tres_primeiros_caracteres = nome[:3] 
print("Três primeiros caracteres:", tres_primeiros_caracteres) #

caracteres_indice_2_5 = nome[2:6] 
print("Caracteres do índice 2 ao 5:", caracteres_indice_2_5)

caracteres_indice_2_ate_final = nome[2:]
print("Caracteres do índice 2 até o final:", caracteres_indice_2_ate_final)

ultimo_caractere = nome[-1]
print("Último caractere:", ultimo_caractere)

tres_ultimos_caracteres = nome[-3:]
print("Três últimos caracteres:", tres_ultimos_caracteres)

string_invertida = nome[::-1]
print("String invertida:", string_invertida)

caracteres_indices_pares = nome[::2]
print("Caracteres nos índices pares:", caracteres_indices_pares)

caracteres_indices_impares = nome[1::2]
print("Caracteres nos índices ímpares:", caracteres_indices_impares)

string_maiuscula = nome.upper()
print("String em maiúsculas:", string_maiuscula)
