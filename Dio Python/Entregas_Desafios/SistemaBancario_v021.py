## DESAFIO 02: Sistema Bancário Otimizado com Funções

## Precisamos deixar nosso código mais modularizado, para isso vamos criar funções
## para as operações existentes: sacar, depositar e visualizar histórico.
## Além disso, para a versão 2 precisamos criar duas novas funções:
## Criar Usuário (Cliente do Banco) e Criar Conta Corrente (vincular com usuário)

import random   # Lib de números aleatórios para a geração das contas de forma automatizada
import datetime # Lib para trabalhar com datas e horas DD/MM/AAAA para o dt_nascimento

usuarios = []   # Cria uma lista vazia para armazenar os usuários

class Usuario:  # Classe que representa o "Usuário do Sistema", um tipo de objeto que terá suas próprias características (atributos)
    def __init__(self, cpf, nome, dt_nascimento, endereco): # Construtor (Método), iniciala os atributos da classe especificados aqui
        self.cpf = cpf             # self. para referir a instância específica desta classe "Usuario"
        self.nome = nome
        self.dt_nascimento = dt_nascimento
        self.endereco = endereco   # Atribui o endereço ao usuário
        self.num_agencia = "0001"  # Agência é fixa, conforme o desafio
        self.num_conta = "1" + str(random.randint(100000000, 999999999))  # Gera um número de conta aleatório
        self.saldo = 5000       # Define um saldo inicial de 5000
        self.limite = 500       # Define um limite de saldo de 500
        self.extrato = []       # Lista para armazenar as transações do usuário
        self.numero_saques = 0  # Número de saques efetuados pelo usuário
        self.limite_saques = 3  # Limite máximo de saques para o usuário

def main():
    exibir_menu = True                          # Mantêm a exibição do menu apos retorno das opções

    while True:                                 #
        if exibir_menu:                         
            print("\n=== MENU PRINCIPAL ===")   #
            print("1 - Cadastrar Usuário")      #
            print("2 - Realizar Operação")
            print("3 - Listar Contas")          # Lista usuários cadastrados e seus atributos
            print("4 - Sair")                   # Fecha o sistema

        opcao = input("Digite o número da operação desejada: ")

        if opcao == "1":
            cadastrar_usuario()                       # Chama a def cadastrar_usuário() - função para cadastrar um usuário
            exibir_menu = True                        # Mantêm a exibição do menu apos retorno das opções
        elif opcao == "2":                            # 
            cpf = input("Digite o CPF do usuário: ")  #
            usuario = None
            for user in usuarios:                     # Percorre a lista de usuários
                if user.cpf == cpf:                   # Verificado se o atributo cpf do usuário atual é igual ao CPF digitado pelo usuário
                    usuario = user                    # Se já está, então não cadastra (pois já existe) e vai pro "break"
                    break
            if usuario is not None:                   # Verificar se tem usuário cadastro
                realizar_operacao(usuario)            # Chama a função para realizar operações
                exibir_menu = True
            else:
                print("Usuário não encontrado.")     
                exibir_menu = False
        elif opcao == "3":
            if len(usuarios) == 0:
                print("Não existe conta cadastrada. Cadastre uma conta para listar.")
                exibir_menu = False
            else:
                listar_contas()      # Chama a função para listar as contas
                exibir_menu = True
        elif opcao == "4":
            break                    # Sai do loop principal
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

        while True:  # Dado que a data não está correta, Então "break" e force digitar corretamente
            dt_nascimento = input("Digite a data de nascimento do usuário (DD/MM/AAAA): ")
            try:     # Essa conversão é feita para garantir que a data informada pelo usuário esteja no formato correto e seja uma data válida.
                data = datetime.datetime.strptime(dt_nascimento, "%d/%m/%Y")  # Chama funções da lib Datetime para padronizar o formato a ser inputado
                break                                                         # Se não atender
            except ValueError:                                                # Quebra e força o usuário inputar corretamente
                print("Data de nascimento inválida. Digite no formato DD/MM/AAAA.")

        endereco = cadastrar_endereco()                         # Chama a função para cadastrar um endereço
        usuario = Usuario(cpf, nome, dt_nascimento, endereco)   # Cria uma instância com os atributos (valores) inseridos
        usuarios.append(usuario)                                # Adiciona o usuário à lista de usuários
        print("Usuário cadastrado com sucesso!")
    else:
        print("CPF inválido. O CPF deve conter 11 dígitos numéricos.")

def cpf_valido(cpf):
    return cpf.isdigit() and len(cpf) == 11

def cpf_existe(cpf):            # verificar se já existe um usuário cadastrado com o CPF fornecido
    for usuario in usuarios:    # Percorre a lista de usuários e 
        if usuario.cpf == cpf:  # Compara o CPF de cada usuário com o CPF fornecido.
            return True         # Se encontrar um usuário com o mesmo CPF = retornaa True, indicando que o CPF já está cadastrado. 
    return False                # Caso contrário, retorna False, indicando que o CPF não existe na lista de usuários cadastrados.

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
        print(f"CPF: {usuario.cpf}, Nome: {usuario.nome}, Conta: {usuario.num_conta}, Saldo: R$ {usuario.saldo:.2f}, Endereço: {', '.join(usuario.endereco)}")

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
                deposito(usuario, valor)  # Chama a função para fazer um depósito
            else:
                print("Valor inválido. O valor do depósito deve ser positivo.")

        elif opcao == "2":
            valor = float(input("Digite o valor do saque: "))
            if valor >= 0:
                saque(usuario, valor)  # Chama a função para fazer um saque
            else:
                print("Valor inválido. O valor do saque deve ser positivo.")

        elif opcao == "3":
            extrato(usuario)     # Chama a função para exibir o extrato

        elif opcao == "4":
            exibir_menu = False  # Sai do loop interno

        else:
            print("Operação inválida. Por favor, selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa
