#soma dos pares
soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite o {}º número: '.format(c)))
    if n%2==0:
        soma += n
        cont += 1
if cont <= 1:
    print('Você digitou {} número par e a soma é {}.'.format(cont, soma))
else:
    print('Você digitou {} números pares e a soma é {}.'.format(cont, soma))


