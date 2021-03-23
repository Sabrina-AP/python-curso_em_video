#Progressão artmaetic v3 

n=int(input('Digite o primeiro termo: '))
r=int(input('Digite a razão: '))
cont=1
n2=int(input('\nQuantos termos você quer? '))
print(n, end=' ')
n3=True
while n3!=0:
    if cont!=1:
        n3=int(input('\nDigite quantos termos a mais você quer ou "0" (zero) para sair: '))
        n2+=n3
    while cont < n2:
        n+=r
        cont+=1
        print('- {}'.format(n), end=' ')
    if (n3==0 or n3=='zero'):
        print('Encerrado. Foram mostrados {} termos.'.format(cont))
    else:
        print('pause')


   
