#ex98 Funções parte 1 (refazer pois é dificil)

import time

def cont(a,b,c):
    if int(c)==0:
        c=1
        
    if int(c)<0:
        c=c*(-1)
    print(f'\nContagem de {a} até {b} de {c} em {c}: ')
    time.sleep(1)

    if int(b)<=int(a):
       if int(c)>0: 
            c=-c
        
    if int(b)>=int(a):
        if int(c)<0:
            c=-c
        
    for i in range(a,b+c,c):
        print(i, end=' ')
        time.sleep(0.2)
    print('Fim!')


cont(1,10,1)
cont(10,0,-2)

print('\nAgora é sua vez de personalizar a contagem:')
i=int(input('Início: '))
f=int(input('Fim: '))
p=int(input('Passo: '))
cont(i,f,p)
