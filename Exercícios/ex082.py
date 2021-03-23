#82 aula 17 listas

lista=[]
pares=[]
impares=[]
continuar='S'

while continuar!='N':
    valor=int(input('Digite um valor: '))
    continuar=input('Quer continuar? [S/N] ').upper()
    lista.append(valor)

print(f'A lista completa é {lista}')


for i in lista:
    if i%2==0:
        pares.append(i)
    else:
        impares.append(i)
print(f'A lista de pares é {pares}', end='')
print(f'\nA lista de ímpares é {impares}', end='')
        

   
