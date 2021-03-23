#custo da viagem
#d = float(input('Qual a distância da viagem em Km? '))
#if d<=200:
#    print('O preço da sua passagem é de R${:.2f} '.format(d*0.50))
#else:
#    print('O preço da sua passagem é de R${:.2f} '.format(d*0.45))

#ou
d = float(input('Qual a distância da viagem em Km? '))
if d<=200:
    preço = d*0.50
else:
    preço = d*0.45
print('O preço da sua passagem é de R${:.2f} '.format(preço))
