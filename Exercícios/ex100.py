#ex100 Funções parte 1

import random
numeros=[]


def sorteio(*num):
    for i in num:
        numeros.append(i)
       
    print(f'\n Sorteando 5 valores da lista: ', end=' ')
    for j in numeros:
         print(j, end=' ')
    print('Pronto!')
   
def somaPar():
    soma=0
    print(f'Somando os valores pares de ', end= ' ')  
    for k in numeros:
        if k%2==0:
            print(k, end=' ')
            soma+=k
    print(f'temos, {soma}')      
  
    
    
sorteio(random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10))
somaPar()

# ou no lugar de *num criar uma lista
        
    




