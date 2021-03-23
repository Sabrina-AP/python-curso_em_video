#075 MUNDO 3: tuplas


n1=int(input('Digite umm números: '))
n2=int(input('Digite umm números: '))
n3=int(input('Digite umm números: '))
n4=int(input('Digite umm números: '))
tupla=(n1,n2,n3,n4)
print(tupla)
print(f'Apareceu o numero 9, {tupla.count(9)} vez(es)')
if 3 in tupla:
    print(f'A posição que foi digitado o número 3 foi na posição {tupla.index(3)+1}')
else:
    print('Não apareceu numero 3')
#s=[]

#for i in tupla:
 #   if i%2==0:
  #      s.append(i)

#print(f'Os números pares: {s}')

'''print('Os números pares são: ', end='')

if n1%2==0:
    print(f'{n1}',end=' ')
if n2%2==0:
    print(f'{n2}',end=' ')
if n3%2==0:
    print(f'{n3}',end=' ')
if n4%2==0:
    print(f'{n4}')
'''

#ou
if n1%2==0 or n2%2==0 or n3%2==0 or n4%2==0:
    print('Os números pares são: ', end='')
else:
    print('Não há números pares')
for i in tupla:
    if i%2==0:
        print(f'{i}',end=' ')
    
