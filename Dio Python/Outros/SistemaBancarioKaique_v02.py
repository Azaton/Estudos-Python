from colorama import Fore as cor
import textwrap
import time

def menu():
    menu = cor.GREEN + '''  \n
    ----- menu ----- 
    [D] \tDepositar
    [S] \tSacar
    [E] \tExtrato
    [NC] \tNova Conta
    [LC] \tListar contas
    [NU] \tNovo Usuário
    [Q] \tSair
    ---------------- 
   \n Selecione a opção desejada:'''+ cor.RESET

    return input(menu).strip().upper()

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        print(cor.BLUE + 'Depósito Realizado com Sucesso' + cor.RESET)
        saldo += valor
        extrato += (cor.BLUE + f'\nDepósito: R${valor:.2f} \n' + cor.RESET)
    else:
        print(cor.RED + f'\n Operação inválida' + cor.RESET)

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques == limite_saques

    if excedeu_saldo:
        print(cor.RED + '\nFalha na Operação \nNão há saldo suficiente para essa operação' + cor.RESET)
    elif excedeu_limite:
        print(cor.RED + '\nFalha na Operação \nOperação excedeu o limite de R$500.00 por saque' + cor.RESET)
    elif excedeu_saques:
        print(cor.RED + '\nFalha na Operação \nOperação excedeu o limite de saques diário' + cor.RESET)

    elif valor > 0:
        saldo -= valor
        extrato += (cor.BLUE + f'\nSaque: R$ {valor:.2f}' + cor.RESET)
        numero_saques += 1
        print(cor.BLUE + 'Saque Realizado com Sucesso' + cor.RESET)

    else:
        print(cor.RED + '\nFalha na Operação \nValor inválido' + cor.RESET)

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('Carregando Extrato...')
    time.sleep(1)
    print(cor.BLUE + "***Extrato***" + cor.RESET)
    print(cor.RED + 'Não foi realizada nenhuma movimentação.' if not extrato else extrato + cor.RESET)
    print(cor.BLUE + f'\n Saldo total em conta: R${saldo:.2f}' + cor.RESET)
    print(cor.BLUE + '*************' + cor.RESET)

def criar_usuario(usuarios):
    cpf = input('Informe seu CPF (somente os números): ').strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(cor.RED + '\nEsse CPF já está cadastrado com um usuário existente' + cor.RESET)
        return

    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aa): ')
    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ')

    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print(cor.BLUE + 'Usuário criado com Sucesso!' + cor.RESET)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios=None):
    cpf = input('Informe o CPF do Usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(cor.BLUE + '\nConta Criada com Sucesso!' + cor.RESET)
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print(cor.RED + 'Fluxo de criação de conta encerrado.' + cor.RESET)

def lista_contas(contas):
    linhas = []
    for conta in contas:
        linha = f'''\
          Agência:\t{conta['agencia']}
          C/C\t\t{conta['numero_conta']}
          Titular:\t{conta['usuario']['nome']}
'''
        linhas.append(textwrap.dedent(linha))
        
    print('\n')
    print(''.join(linhas))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "D":
            valor = float(input('\nDigite o valor que você quer depositar: R$'))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "S":
            valor = float(input(f'\nQual valor você deseja sacar? R$'))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "E":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "NU":
            criar_usuario(usuarios)

        elif opcao == 'NC':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'LC':
            lista_contas(contas)

        elif opcao == "Q":
            print(cor.BLUE + '\nObrigado por utilizar nosso Sistema' + cor.RESET)
            time.sleep(1)
            break

        else:
            print(cor.RED + "Falha na Operação \nSelecione novamente uma opção válida" + cor.RESET)

main()