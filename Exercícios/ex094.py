c=''
l=[]
soma=midade=0
lista=[]
while c!='N':
    nome=input('Nome: ')
    sexo=input('Sexo [M/F]: ').upper()
    idade=int(input('Idade: '))
    dic={'Nome': nome, 'Idade': idade, 'Sexo': sexo}
    l.append(dic)
    c=input('Deseja continuar [S/N]? ').upper()
#print(l)

qpessoas=len(l)
print(f'- O grupo tem {qpessoas} pessoas')


for i in l:
    if i['Idade']!=0:
        soma+=i['Idade']
        
    if i['Sexo']=='F':
        lista.append(i['Nome'])
    
midade= soma/len(l)  
                     
print(f'- A média de idade é de {midade} anos')

print(f'- As mulheres cadastradas foram: ', end='')
for j in lista:
    print(f'{j}',end=' ')

print(f'\n- A lista das pessoas que estão acima da média:')
for i in l:
     if i['Idade']>midade:
        for k,v in i.items():
            print(f'{k} = {v};', end=' ')
        print('\n')
