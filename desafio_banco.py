import os

LIMITE = 500
LIMITE_SAQUES = 3

def boas_vindas():
    print('Olá, seja bem-vindo ao banco XYZ! Por favor, escolha uma opção:')
    opcoes = '1 - Depósito\n2 - Saque\n3 - Extrato\n0 - Sair'
    print(opcoes)

def deposito(saldo, valor, lista_extrato):
    saldo += valor
    lista_extrato.append(f'Depósito - R$ {valor:.2f}')
    print('Depósto realizado com sucesso!')
    input('Aperte enter para voltar ao menu principal...')
    return saldo

def saque(saldo, valor, saques_realizados, lista_extrato):
    if saques_realizados < LIMITE_SAQUES and saldo >= valor and valor <= LIMITE:
        saldo -= valor    
        lista_extrato.append(f'Saque - R$ {valor:.2f}')
        print('Saque realizado com sucesso!')
        saques_realizados +=1
    else:
        print('Saque não permitido.')

    input('Aperte enter para voltar ao menu principal...')
    return saldo, saques_realizados

def extrato(lista_extrato):
    for info in lista_extrato:
        print(f'{info}\n')

    input('Aperte enter para voltar ao menu principal...')
    

def main():
    lista_extrato = []
    opcao = -1
    saldo = 0
    saques_realizados = 0
    while opcao != 0:
        os.system('cls')
        boas_vindas()
        print(f'SALDO: R${saldo:.2f}')
        opcao = int(input())

        if opcao == 1:
            valor = float(input('Digite o valor a ser depositado: R$ '))
            saldo = deposito(valor=valor, saldo=saldo, lista_extrato=lista_extrato)
        elif opcao == 2:
            valor = float(input('Digite o valor que deseja sacar: R$ '))
            retorno_saque = saque(saldo=saldo, valor=valor, saques_realizados=saques_realizados, lista_extrato=lista_extrato)
            saldo = retorno_saque[0]
            saques_realizados = retorno_saque[1]
        elif opcao == 3:
            extrato(lista_extrato=lista_extrato)
        elif opcao == 0:
            print('Obrigado por ter usado o nosso sistema')
        else:
            print('Opção inválida. Por favor, tente novamente')
            print()

main()