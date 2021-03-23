#números primos com cores
n=int(input('Digite um número: '))
cont=0

for i in range(1,n+1):
    if n%i==0:
        cont+=1
        #print('\033[0;33;34m')
        print(' ',end=' ')
        print('divisível por:', end='')
        
    else:
        print(' ',end=' ')
    print(i, end='')
     
    
if cont==2:
    print('\n O número {} foi divisivel apenas por 1 e por ele mesmo e por isso ele É PRIMO!'.format(n,cont))
elif cont!=2:
    print('\n O número {} foi divisivel {} vezes e por isso ele NÃO É PRIMO!'.format(n,cont))
