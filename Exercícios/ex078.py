#78 aula 17 listas (USO DO ENUMERATE)
valores=[]
for i in range(0,5):
    v=int(input(f'Digite um valor para a posição {i}: '))

    valores.append(v)
         
print(f'Você digitou os valores {valores}')

maximo=max(valores)


print(f'O maior valor digitatado foi {maximo} nas posições ', end='')

for c, d in enumerate(valores):
    if d==maximo:
        print(f'{c}', end='...')



minimo=min(valores)

print(f'\nO menor valor digitatado foi {minimo} nas posições ', end='')

for c, d in enumerate(valores):
    if d==minimo:
        print(f'{c}', end='...') 


