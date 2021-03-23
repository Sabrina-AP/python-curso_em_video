#074 MUNDO 3: tuplas

#lista=[]
#for i in range(1,6):

    #print(f'n{i}= {random.randint(0,100)}')
    
 #   lista.append(random.randint(0,100))
#print(f'os numeros sorteados foram: {lista}')

import random
tupla=(random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100))
print(f'Os elementos da tupla são: {tupla}')
print(f'O maior número é: {max(tupla)}')
print(f'O menor número é: {min(tupla)}')

