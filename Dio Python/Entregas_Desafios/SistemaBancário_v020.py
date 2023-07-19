# ------     EXERCÍCIO: SISTEMA BANCÁRIO     ------ #
##### Sistema Bancário Otimizado com Funções ######

##### Desafio: Precisamos deixar nosso código mais modularizado,
# para isso vamos criar funções para as operações existentes: sacar,
# depositar e visualizar histórico. Além disso, para a versão 2 precisamos
# criar duas novas funções: Criar Usuário (Cliente do Banco) e Criar Conta Corrente (vincular com usuário)

# NOVAS FUNÇÕES: Cadastrar Usuários, Conta Bancária, Listar Usuários

###### FUNÇÃO CADASTRO DE USUÁRIOS
# Regra 01: só pode operar no sistema (sacar, depositar e extrato) após o usuário logar no sistema.
# Regra 02: Para o "cadastrado do usuário", a pessoa deve informar: num_cpf (000.000.000-00), nome (string), dt_nascimento (DD/MM/AAAA), endereco.
# Regra 03: O cpf é o ID do usuário para ele se identificar para se logar no sistema. É limitado com no mínimo e máximo 11 dígitos (só números).
# Regra 04: num_agencia é fixo = 0001.
# Regra 05: num_conta é sequencial é gerado automáticamente e aleatória, iniciando em 1 e são 10 dígitos.
# Regra 06: Cada usuário recebe saldo = 5000 e limite de saque = 3
# Regra 07: Para cada Saque ou Depósito, o valor deve debitar ou somar no saldo total do usuário.
# Regra 08: O programa não deve permitir cadastrar 2 cpfs (não permitir cpf duplicado).

###### FUNÇÃO SAQUE
# # Argumentos: saldo, valor, extrato, limite, numero_saque, limite_saques.
# Retorno: saldo e extrato
# O saque debita da conta do respectivo usuário logado no sitema

###### LISTA_ENDEREÇO
# O "endereco" é uma lista que recebe: logradouro (string), número (ninteiro) - bairro(string) - cidade (string), estado (string que recebe dois caracateres no mínimo / máximo)
# O usário informa o endereço em partes

###### FUNÇÃO DEPÓSITO
# Argumentos: saldo, valor, extrato
# Retorno: saldo e extrato
# # O depósito acrescenta valor ao saldo do usuário

###### FUNÇÃO LISTAR CONTA E USUÁRIO
# Esta função serve para verificar: o total do saldo de cada usuário
# Ao consultar, deve exibir: cpf, conta e saldo da conta (de cada usuário, listado um abaixo do outro)

import random

usuarios = []

class Usuario:
    def __init__(self, cpf, nome, dt_nascimento, endereco):
        self.cpf = cpf
        self.nome = nome
        self.dt_nascimento = dt_nascimento
        self.endereco = endereco
        self.num_agencia = "0001"
        self.num_conta = str(random.randint(1000000000, 9999999999))
        self.saldo = 5000
        self.limite = 500
        self.extrato = []
        self.numero_saques = 0
        self.limite_saques = 3

def main():
    exibir_menu = True
    
    while True:
        if exibir_menu:
            print("\n=== MENU PRINCIPAL ===")
            print("1 - Cadastrar Usuário")
            print("2 - Realizar Operação")
            print("3 - Listar Contas")
            print("4 - Sair")
        
        opcao = input("Digite o número da operação desejada: ")
        
        if opcao == "1":
            cadastrar_usuario()
            exibir_menu = True
        elif opcao == "2":
            cpf = input("Digite o CPF do usuário: ")
            usuario = None
            for user in usuarios:
                if user.cpf == cpf:
                    usuario = user
                    break
            if usuario is not None:
                realizar_operacao(usuario)
                exibir_menu = True
            else:
                print("Usuário não encontrado.")
                exibir_menu = False
        elif opcao == "3":
            if len(usuarios) == 0:
                print("Não existe conta cadastrada. Cadastre uma conta para listar.")
                exibir_menu = False
            else:
                listar_contas()
                exibir_menu = True
        elif opcao == "4":
            break
        else:
            print("Operação inválida. Por favor, selecione novamente a operação desejada.")
            exibir_menu = False

def cadastrar_usuario():
    cpf = input("Digite o CPF do usuário: ")
    if cpf_valido(cpf):
        if cpf_existe(cpf):
            print("CPF já cadastrado. Não é permitido cadastrar o mesmo CPF mais de uma vez.")
            return
        nome = input("Digite o nome do usuário: ")
        dt_nascimento = input("Digite a data de nascimento do usuário (DD/MM/AAAA): ")
        endereco = cadastrar_endereco()
        usuario = Usuario(cpf, nome, dt_nascimento, endereco)
        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")
    else:
        print("CPF inválido. O CPF deve conter 11 dígitos numéricos.")

def cpf_valido(cpf):
    return cpf.isdigit() and len(cpf) == 11

def cpf_existe(cpf):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return True
    return False

def cadastrar_endereco():
    logradouro = input("Digite o logradouro: ")
    numero = input("Digite o número: ")
    bairro = input("Digite o bairro: ")
    cidade = input("Digite a cidade: ")
    
    while True:
        estado = input("Digite o estado (sigla): ")
        if len(estado) == 2:
            break
        else:
            print("O estado deve conter exatamente dois caracteres.")
    
    return [logradouro, numero, bairro, cidade, estado]

def deposito(usuario, valor):
    usuario.saldo += valor
    usuario.extrato.append(valor)
    print("Depósito realizado com sucesso.")

def saque(usuario, valor):
    if valor <= usuario.saldo and valor <= usuario.limite and usuario.numero_saques < usuario.limite_saques:
        usuario.saldo -= valor
        usuario.extrato.append(-valor)
        usuario.numero_saques += 1
        print("Saque realizado com sucesso.")
    else:
        print("Valor de saque inválido. Verifique se o valor está dentro do limite disponível ou se você excedeu o número máximo de saques.")

def extrato(usuario):
    print("\nExtrato:")
    for operacao in usuario.extrato:
        if operacao > 0:
            print(f"Depósito: R$ {operacao:.2f}")
        else:
            print(f"Saque: R$ {-operacao:.2f}")
    print(f"Saldo atual: R$ {usuario.saldo:.2f}")

def listar_contas():
    print("\nListagem de contas e saldos:")
    for usuario in usuarios:
        print(f"CPF: {usuario.cpf}, Conta: {usuario.num_conta}, Saldo: R$ {usuario.saldo:.2f}, Endereço: {', '.join(usuario.endereco)}")

def realizar_operacao(usuario):
    exibir_menu = True
    
    while exibir_menu:
        print("\n====== MENU INICIAL ======")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Extrato")
        print("4 - Sair")

        opcao = input("Digite o número da operação desejada: ")

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: "))
            if valor >= 0:
                deposito(usuario, valor)
            else:
                print("Valor inválido. O valor do depósito deve ser positivo.")

        elif opcao == "2":
            valor = float(input("Digite o valor do saque: "))
            if valor >= 0:
                saque(usuario, valor)
            else:
                print("Valor inválido. O valor do saque deve ser positivo.")

        elif opcao == "3":
            extrato(usuario)

        elif opcao == "4":
            exibir_menu = False

        else:
            print("Operação inválida. Por favor, selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()