#ex 088
import random
cont=0
palpite=[]#não precisa dessa linha  
palpites=[]
qtjogos=int(input('Quantos jogos você quer que eu sorteie? '))
print(f' -=-=-= Sorteando {qtjogos} jogos =-=-=-')



for j in range(0,qtjogos):
    for i in range(0,6):
        p=random.randint(1,60)
        if p not in palpites:
            palpites.append(p)
        palpites.sort()
    palpite.append(palpites)  #não precisa dessa linha  
    print(f'\nJogo {j+1}: {palpite[j]}') #não precisa desse[j]  
    palpites.clear()
