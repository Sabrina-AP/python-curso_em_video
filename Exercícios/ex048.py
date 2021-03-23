#soma ímpares múltiplos de três (com contagem e soma no FOR)
soma=0
c=0
for n in range(1,501):
    if n%2==1 and n%3==0:
        c+=1
        soma+=n
print('A soma de todos os {} valores solicitados é {}'.format(c, soma))
