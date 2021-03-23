#68 jogo par ou impar

from time import sleep
import random
print(40*'=-')
print('Vamos jogar par ou impar')
print(40*'=-')

soma=0
cont=0

while True:
    v=int(input('\nDiga um valor: '))
    piv=input('Par ou Ímpar? [P/I]: ').upper().strip()
    c=random.randint(0,11)
    soma=v+c

    if piv=='P' and soma%2==0:
        piv=pi='PAR'
    elif piv=='I' and soma%2!=0:
        piv=pi='ÍMPAR'
    elif piv!='P' and piv!='I':
        break
                    
    print(40*'-')
    print('Analisando...')
    sleep(3)
    print(f'Você jogou {v} e o computador {c}. A soma {soma} é {pi} e você escolheu {piv}. Então...')
    print(40*'=-')

    if piv==pi:
        cont+=1
 
    if piv==pi:
        print('PARABÉNS! Vamos jogar novamente!')
    elif piv!=pi:
        print('GAME OVER!', end=' ')
        if cont==1:
            print(f'Você venceu {cont} vez!')
        else:
            print(f'Você venceu {cont} vezes!')
    
   
