# ex 84

lista=[]
maxim=[]
minim=[]
cont=0
while True:
    nome=input('Nome: ')
    peso=float(input('Peso: '))
    continuar=input('Quer continuar? [S/N]: ')
    lista.append(nome)
    lista.append(peso)
    cont+=1
    if continuar in 'Nn':
        break

print(f'Ao todo, você cadastrou {cont} pessoas. ')


for i,j in enumerate(lista):
    if j==max(lista[1::2]):
        maximo=j
        pessoamax=lista[i-1]
        maxim.append(pessoamax)


    elif j==min(lista[1::2]):
        minimo=j
        pessoamin=lista[i-1]
        minim.append(pessoamin)
        

if len(maxim)>0:
    print(f'O maior peso foi de {maximo}kg. Peso de', end=' ')
    for pesado in maxim:
        print(f'[{pesado}]', end=' ')
if len(minim)>0:
    print(f'\nO menor peso foi de {minimo}kg. Peso de', end=' ')
    for leve in minim:
        print(f'[{leve}]', end=' ')

