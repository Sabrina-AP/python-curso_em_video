'''sorteando uma ordem na lista'''
import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceirp aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista) #embaralhar
print('A ordem de apresentação será {} '.format(lista))


