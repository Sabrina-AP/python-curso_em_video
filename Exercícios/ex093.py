dic={}
gols=[]
total=0
nome=input('Nome do Jogador: ')
npartidas=int(input('Quantas partidas ele jogou? '))
for i in range(0, npartidas):
    q=int(input(f'Quantos gols na partida {i}? '))
    gols.append(q)
    total+=q
    dic['Nome']=nome
    dic['Gols']= gols
    dic['Total']=total
print(10*'=~~')
print(dic)
print(10*'=~~')

for k,v in dic.items():
    print(f'O campo {k} tem o valor {v}')
print(10*'=~~')
print(f'O jogador {nome}, jogou {npartidas} partidas.')

for i in range(0,npartidas):
    print(f'=>Na partida {i}, fez {gols[i]} gols.')
print(f'Foi um total de {total} gols.')
    



