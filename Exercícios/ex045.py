#game: pedra, papel e tesoura (com tempos de pausas e usando índice (ITENS) de tuplas)

##import random
##from time import sleep
##
##print('''Suas opções:
##[0] PEDRA
##[1] PAPEL
##[2] TESOURA''')
##eu = int(input('Qual é a sua jogada? '))
##if eu==0:
##    eu='PEDRA'
##elif eu==1:
##    eu='PAPEL'
##elif eu==2 :
##    eu='TESOURA'
##
##print('JO')
##sleep(1)
##print('KEN')
##sleep(1)
##print('PO...')
##sleep(1)
##
##c = random.randint(0,2)
##if c==0:
##    c='PEDRA'
##elif c==1:
##    c='PAPEL'
##elif c==2 :
##    c='TESOURA'  
## 
##print(20*'=-')
##print('Computador jogou {}'.format(c))
##print('Jogador jogou {}'.format(eu))
##print(20*'=-')
##
##
##if eu==c:
##    print('Empatou!')
##elif (c=='PEDRA' and eu=='TESOURA') or (c=='TESOURA' and eu=='PAPEL') or (c=='PAPEL' and eu=='PEDRA'):
##    print('Computador venceu!')
##elif (eu=='PEDRA' and c=='TESOURA') or (eu=='TESOURA' and c=='PAPEL') or (EU=='PAPEL' and c=='PEDRA'):
##    print('Jogador venceu!')
##else:
##    print('Valor inválido tente novamente!')

#Ou: 
for i in range(0,100):
    from random import randint
    itens = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0,2)
    #print(itens[computador])
    print('''Suas opções:
    [0] PEDRA
    [1] PAPEL
    [2] TESOURA''')
    jogador = int(input('qual é a sua jogada? '))
    print('-='*11)
    print('computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-='*11)
    if computador==0:
        if jogador==0:
            print('EMPATE')
        elif jogador==1:
            print('Jogador venceu!')
        elif jogador==2:
            print('Computador venceu!')
    elif computador==1:
        if jogador==0:
            print('Computador venceu!')
        elif jogador==1:
            print('EMPATE')
        elif jogador==2:
            print('Jogador venceu!')
    elif computador==2:
        if jogador==0:
            print('Jogador venceu!')
        elif jogador==1:
            print('Computador venceu!')
        elif jogador==2:
            print('EMPATE!')
    print(25*'=*=')
input()
       
