# Recebe um texto e separa as vogais deste texto

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for vletra in texto:
    if vletra.upper() in VOGAIS:
        print(vletra, end="")
    
else:
    print() # Adiciona uma quebra de linha
    print("Final do laço") 
        