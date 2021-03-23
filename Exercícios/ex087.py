# ex 087
matriz=[[]]

for i in range(1,4):
    for j in range(1,4):
        numeros=int(input(f'Digite o valor para {i,j}: '))
        matriz.append(numeros)
        if numeros%2==0:
            matriz[0].append(numeros)
print(f'{matriz[1]:^6}{matriz[2]:^6}{matriz[3]:^6}')
print(f'{matriz[4]:^6}{matriz[5]:^6}{matriz[6]:^6}')
print(f'{matriz[7]:^6}{matriz[8]:^6}{matriz[9]:^6}')


print(f'A soma dos valores pares é {sum(matriz[0])}')
print(f'O maior número da segunda linha é {max(matriz[4],matriz[5], matriz[6])}')
print(f'A soma dos valores da terceira coluna é {matriz[3]+matriz[6]+matriz[9]}')
