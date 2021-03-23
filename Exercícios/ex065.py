#65 Maior e Menor valores (nós usamos com lista)
cont=soma=n=0
c='S'
ln=[]
maior=menor=0
while c=='S':
    n=int(input('Digite um número: '))
    c=input('Quer contiuar? [S/N]: ').strip().upper()
    soma+=n
    cont+=1
    ln.append(n)
    ln.sort()
    
maior=ln[-1]
menor=ln[0]
média=soma/cont
print('Você digitou {} números e a média foi {:.2f}. '.format(cont,média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))


#ou sem ista:
#if cont==1
#   maior=menor=n
#else:
#    if n>maior:
#        maior=n
#    if n<menor
#   menor=n
