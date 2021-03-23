#81 aula 17 listas
valores=[]
continuar='S'
while continuar!='N':
    valor=int(input('Digite um valor: '))
    continuar=input('Quer continuar? [S/N] ').upper()
    valores.append(valor)
    valores.sort(reverse=True)

print(f'Você digitou {len(valores)} elementos')
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
