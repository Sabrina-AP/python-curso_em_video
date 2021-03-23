#66 Vários números com fag(baandeira, flag, break, interrupção do while)

cont=0
soma=0

while True:
    n=int(input('Digite um valor (0 zero para parar): '))
    if n==999:
        break
    soma+=n
    cont+=1
print(f'A soma dos {cont} valores foi {soma}!')
