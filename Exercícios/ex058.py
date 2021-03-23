#melhorando exercicio 28
import random
from time import sleep
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('processando...')
sleep(2)
c=random.randint(0,10)
eu=int(input('Qual número pensei? '))
tentativas=0
while c!=eu:
    print('processando...')
    sleep(3)
    if c<eu:
        eu=int(input('É menor. Tente novamente: '))
    elif c>eu:
        eu=int(input('É maior. Tente novamente: '))
    tentativas+=1
#if c==eu:
tentativas+=1
print('O número que eu pensei foi {}. Você ganhou tentando {} vezes!'.format(c,tentativas))


#ou usar acertou =False e while not acertou (exercicio 58)    
        
