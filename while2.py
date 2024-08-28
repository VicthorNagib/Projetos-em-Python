
print('Bem vindo a calculadora do nagibão!')
print('Qual operação gostaria de fazer?')
print('Opções: \n 1) Adição \n 2) Subtração \n 3) Multiplicação \n 4) Divisão: ')
opcao = (input('Digite a opção de desejada: '))
if opcao == '1':
    while True:
        numero1 = int(input('Digite primeiro numero inteiro: '))
        numero2 = int(input('Digite segundo numero: '))
        total = numero1+numero2
        print(f'total da soma foi de {total}')

        continuar = input('Deseja continuar?  [S/N] ')
        if continuar != 's':
            break
elif opcao == '2':
        while True:
            numero1 = int(input('Digite primeiro numero inteiro: '))
            numero2 = int(input('Digite segundo numero: '))
            total = numero1-numero2
            print(f'total da subtração foi de {total}')

            continuar = input('Deseja continuar?  [S/N] ')
            if continuar != 's':
                break
elif opcao == '3':
            while True:
                numero1 = int(input('Digite primeiro numero inteiro: '))
                numero2 = int(input('Digite segundo numero: '))
                total = numero1*numero2
                print(f'total da multiplicação foi de {total}')

                continuar = input('Deseja continuar?  [S/N] ')
                if continuar != 's':
                    break
elif opcao == '4': 
                while True:
                    numero1 = int(input('Digite primeiro numero inteiro: '))
                    numero2 = int(input('Digite segundo numero: '))
                    total = numero1/numero2
                    print(f'total da divisão foi de {total}')

                    continuar = input('Deseja continuar?  [S/N] ')
                    if continuar != 's':
                        break
else:
    print('Erro')


 