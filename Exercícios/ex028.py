#jogo da adivinhação (com tempo para pensar)
from random import randint
from time import sleep
print(26*('-=-'))
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print(26*('-=-'))
x = int(input('Em que número eu pensei? '))
y = randint(0,5) #com parenteses considera até o número 5, mas com colchetes não.

print('PROCESSANDO... ')
sleep(3)

if y == x:
    print('Parabéns! Você acertou! O número que eu pensei foi {}! '.format(y))
else:
    print('Errou! Eu pensei no número {} e não no {}! '.format(y, x))
4
