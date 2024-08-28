senha = 707070
agencia = 1010
conta = 1520

print('Olá, seja bem vindo ao sistema báncario.')
print('Para acessar o sistema tenha em mãos sua senha, agencia e conta:')



saldo = 1500
saque = 0
pix = 0 
tentativas = 0
max_tentativas = 3
bloqueado = False

while not bloqueado:
    agencia_digitada = int(input('Informe sua agência: '))
    conta_digitada = int(input('Informe sua conta: '))
    senha_digitada = int(input('Informe sua senha: '))

    if agencia == agencia_digitada and conta == conta_digitada and senha == senha_digitada:
        print('Acesso permitido')
        
        acao = int(input('\nDigite\n(1) - Saldo \n(2) - Pix\n(3) - Depositar \nInforme a Opção desejada: '))
        if acao == 1:
            print(f'Seu atual é de: R${saldo}')
        
        elif acao == 2: 
            pix_transferencia = int(input('Informe o valor desejado de transferencia: '))
            print(f'Valor de R$: {pix_transferencia} transferido com sucesso')
            print(f'Seu saldo atual é de R$:{saldo - pix_transferencia}')

        elif acao == 3: 
            depositar = int(input('Informe o valor que deseja depositar: R$'))
            print(f'O valor de {depositar} foi efetuado com sucesso')
            print(f'Seu saldo atual é de R$: {saldo + depositar}')
    else: 
        tentativas += 1
        if tentativas >= max_tentativas: 
            print('Acesso Bloqueado devido à quantidade de erros! ')
            bloqueado = True
            break
        else:
            print(f'Senha incorreta \nTotal de {tentativas} tentativas erradas \nTente novamente.\n')
            

           







