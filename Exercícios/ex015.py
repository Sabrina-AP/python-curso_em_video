#Aluguel de carros
d = int(input('Quantos dias alugados? '))
k = int(input('Quantos Km rodados? '))
pd = float(input('Qual o valor por dia? R$'))
pk = float(input('Qual o valorr por km rodado? R$'))
print('O total a pagar é de R${:.2f}. '.format((d*pd+k*pk)))
