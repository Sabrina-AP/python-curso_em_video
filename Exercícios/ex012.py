#calculando descontos
p = float(input('Qual o preço do produto? R$'))
d = int(input('Qual o percentual de desconto? '))
print('O produto que custava R${:.2f}, na promoção com {}% de desconto, custa: R${:.2f}.'.format(p, d, p-(p*d)/100))
