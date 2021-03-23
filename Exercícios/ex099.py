#ex99 Funções parte 1


def maior(*num):
    print(f'\nAnalisando os valores passados: ', end=' ')
    for i in num:
        print(i, end=' ')
    print(f'foram informados {len(num)} ao todo. ')
    print(f'\nO maior número é {max(num)}')
    


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(6)
maior(0)

