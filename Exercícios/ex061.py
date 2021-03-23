#Progressão artmaetic v2

n=int(input('Digite o primeiro termo: '))
r=int(input('Digite a razão: '))
cont=1
print(n, end=' - ')

while cont < 10:
    n+=r
    cont+=1
    print(n, end=' - ')
print('Fim')
     
