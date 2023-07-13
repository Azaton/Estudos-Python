classe = input("Digite o nome da classe que você joga: ")
habilidade = input("Digite a principal habilidade da classe: ")

texto = '''
================== GAME NEW ======================\n
Diablo 4 é um jogo altamente antecipado pelos fãs da franquia. 
No jogo, uma das classes disponíveis é a "{classe}", que se destaca pela sua principal habilidade, {habilidade}.
'''
# Substitui as variáveis na string tripla usando o método format
texto_formatado = texto.format(classe=classe, habilidade=habilidade)

# Imprime o texto formatado
print(texto_formatado)
