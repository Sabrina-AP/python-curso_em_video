#80 aula 17 listas (PARA QANTOS ELEMENTOS QUUISERMOS/////REFAZER)
valores=[]

for i in range(0,7):
    valor=int(input('\nDigite um valor: '))
    valores.append(valor)
    print('Adicionado na posição', end=' ')
    if valores[-1]==max(valores):
        print('final da lista')
    for j in range(len(valores)):
        if valores[-1]<valores[j]:
            valores.insert(j, valores[-1])
            valores.pop()
            print(f'{valores.index(valor)}')   
        
        
print(f'\nOs valores digitados em ordem foram {valores}')
