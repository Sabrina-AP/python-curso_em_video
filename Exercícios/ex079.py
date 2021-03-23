#79 aula 17 listas

valores=[]

continuar='S'
while continuar!='N':
    valor=int(input('Digite um valor: '))
    print('Valor adicionado com sucesso...')
    continuar=input('Quer continuar? [S/N] ').upper()
    if valor not in valores:
        valores.append(valor)
        valores.sort()
 
print(f'Você digitou os valores: {valores}')
#colocar o .sort aqui não funcionou
    
        

