import random
from operator import itemgetter #pesquisei na internet e o sorted
l=[]
for a in range(0,4):
    a=random.randint(0,6)
    l.append(a)
    
dic={'Jogador 1':l[0],'Jogador 2':l[1],'Jogador 3':l[2],'Jogador 4':l[3]}
for k,v in dic.items():
    print(f'O {k} tirou {v} \n')
print(10*'=~~=')
listacomdicordenado=sorted(dic.items(), key=itemgetter(1)) #pesquisei na internet e o import dele
listacomdicordenado.sort(reverse=True)

print('')
for j,i in enumerate(listacomdicordenado):
    print(f'{j+1}º Lugar: {i[0]} com {i[1]} pontos. \n')
