lista = []

print('Bem vindo a lista de mercado do Nagibão')
print('As regras são as seguintes [i] para inserir itens')
print('As regras são as seguintes [a] para apagar itens')
print('As regras são as seguintes [l] para listar itens')

while True:
    opcao = input('Informe a opção desejada:\n [i]nserir \n [a]pagar \n [l]ista :\n ')

    if opcao == 'i':
   
        add = input('Digite o item que deseja adicionar: ')
        lista.append(add)
        continuar = input('Deseja continuar? [s/n] ')
        if continuar != 's':
            break
        print('Lista Atual: ',lista)

    elif opcao == 'a':
    
        remove = input('Digite o item que deseja remover: ')
        lista.remove(remove)
        continuar = input('Deseja remover mais algum item? ')
        if continuar != 's':
            break
        print('Lista Atual: ',lista)

    elif opcao == 'l':
        print('Itens na lista:')
        for index, item in enumerate(lista, 1):
            print(f'{index}. {item}')

print('Sua lista final é:', lista)



