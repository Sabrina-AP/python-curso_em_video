#fatorial
n=int(input('Digite um número inteiro: '))
f=0
nf=1
while f!=1:
    print('{}! = '.format(n), end='') #observar ordem que os prints serao impressos

    for i in range(0,n):
        f=n-i
        nf*=f #contagem só que para mutiplicação
        if f==1:     #esse if é só para imprimir a sequencia 4x3x2x1
            print('{}'.format(f), end='')
        else:
            print('{}'.format(f), end='x')
            
    if n==0:
        print('1.')
    elif n==1:
        print('.')
    else:
        print(' = {}.'.format(nf))
    print(20*'=*')
    n=int(input('Digite um número inteiro: '))
    f=0
    nf=1

#OU olhar do guanabara
   # FROM MATH IMPORT FACTORIAL
#f=factorial(n)
    
        
