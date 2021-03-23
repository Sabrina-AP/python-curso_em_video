# ex086
matriz=[]

for i in range(1,4):
    for j in range(1,4):
        numeros=int(input(f'Digite o valor para [{i},{j}]: '))
        matriz.append(numeros)
        
print(f'[{matriz[0]:^4}{matriz[1]:^6}{matriz[2]:^4}]')
print(f'[{matriz[3]:^4}{matriz[4]:^6}{matriz[5]:^4}]')
print(f'[{matriz[6]:^4}{matriz[7]:^6}{matriz[8]:^4}]')
