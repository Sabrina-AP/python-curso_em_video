#ler o maior e o menor peso
#l=[]

#for p in range(1,6):
#    peso = float(input('Digite o peso da {}º pessoa: '.format(p)))
#    l.append(peso)


#for i in l:
#    if i==max(l):
#        maior=i
#    elif i==min(l):
#        menor=i
#print('O maior peso foi de {}kg. E o menor peso foi de {}kg'.format(maior, menor)) 

l=[]

for p in range(1,6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(p)))
    l.append(peso)

maior = max(l)
menor = min(l)
       
print('O maior peso foi de {}kg. E o menor peso foi de {}kg'.format(maior, menor)) 
    

'''OU:
lpesos = []
for c in range(1, 6):
    peso = float(input('Digite o {}º peso: '.format(c)))
    lpesos.append(peso)
lpesos.sort()
print('O menor peso lido foi {}kg'.format(lpesos[0]))
print('O maior peso lido foi {}kg'.format(lpesos[4]))﻿'''


