#ex 085

numeros=[[],[]]


for i in range(1,8):
    valor=int(input(f'Digite o {i}º valor: '))
    
    
    if valor%2==0:
        numeros[0].append(valor)
        numeros[0].sort()
    else:
        numeros[1].append(valor)
        numeros[1].sort()
       
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores impares digitados foram: {numeros[1]}')
    
    
