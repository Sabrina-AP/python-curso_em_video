#64 tratando vários valores v1 (o da sabrina esta diferente)

n=int(input('Digite um número ou 0 (zero) para sair: '))
cont=soma=0

while n!=0:
    cont+=1
    soma+=n
    n=int(input('Digite um número ou 0 (zero) para sair: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))

#esse jeito ou subtraindo no cont e na soma, sao truques e o exercicio 66 tem outra forma melhor de resolução
