#ex 95

dic={}
gols=[]
total=0
todos=[]
partidas=[]
continuar='S'
mostrar=''

while continuar!='N':
    nome=input('Nome do Jogador: ')
    npartidas=int(input('Quantas partidas ele jogou? '))
    partidas.append(npartidas)
    for i in range(0, npartidas):
        q=int(input(f'Quantos gols na partida {i}? '))
        gols.append(q)
        total+=q
        dic['Nome']=nome
        dic['Gols']= gols
        dic['Total']=total
        
    todos.append(dic.copy())
    total=0
    gols=[]
    continuar=input('Quer continuar? [S/N] ').upper()

print(10*'=~~')
print('cod    nome      gols       total')
for i,j in enumerate(todos):
    print(f'{i:>3}', end='      ')
    for k, v in j.items():
        print(f'{v:>3}', end='      ')
    print('\n')
    print(10*'=~~')


while mostrar!=999:
    print(40*'~~')
    mostrar=int(input('Mostrar dados de qual jogador? [parar 999]: ' ))
        
    if mostrar>=len(todos):
        print(f'Erro! Não existe esse jogador {mostrar}!')
    else:
        todos[mostrar]
        print(f'-LEVANTAMENTO DO JOGADOR {todos[mostrar]["Nome"]}-')
        for i in range(0,partidas[mostrar]):
            print(f'=>Na partida {i}, fez {todos[mostrar]["Gols"][i]} gols.')

print('<<volte sempre>>')
