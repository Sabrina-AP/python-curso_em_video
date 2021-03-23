#PA (dentro do range pode usar variáveis)
p=int(input('Primeiro termo da PA: '))
r=int(input('Razão: '))
d=p+(10-1)*r
for i in range(p,d+r,r):    
    print(i, end='->')
print('ACABOU')

#ou
p=int(input('Primeiro termo da PA: '))
r=int(input('Razão: '))
print(p, end='->')
for i in range(1,10):    
    p+=r
    print(p, end='->')
print('ACABOU')
