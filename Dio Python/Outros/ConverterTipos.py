# Aula: "Conversão de Tipos"
# Algumas vezes se faz necessário converter o tipo da variável.
# Ex.: variáveis do tipo string, que armazenam números e precisamos fazer alguma operação matemática com esse valor.

preco = 10
print(preco)

preco = float(preco)
print(preco)

preco = int(preco)
print(preco)

preco = (preco/2)
print(int(preco))

preco = (preco//2)
print(preco)

preco = 100.51
idade = 38
texto = f"idade {idade} preco {preco} preco {int(preco)}"
print(texto)