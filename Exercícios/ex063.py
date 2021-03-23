#63 SequÊncia de Fibonacci
n=int(input('Quantos termos você quer mostrar? '))
cont=2
t1=0
t2=1
print(' 0 - 1', end=' - ')

while cont < n:
    cont+=1
    t=t1+t2
    print(t, end= ' - ')
    t1=t2
    t2=t
print('FIM')
    
    
            
