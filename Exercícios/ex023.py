#separando dígitos de um número
num = int(input('Informe um número inteiro: '))
n = str(num)
print('Analisando o número {} '.format(num))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {} '.format(u))
print('Dezena: {} '.format(d))
print('Centena: {} '.format(c))
print('Milhar: {} '.format(m))


#ou (com limitações)
#print('Unidade: {} '.format(num[3]))
#print('Dezena: {} '.format(num[2]))
#print('Centena: {} '.format(num[1]))
#print('Milhar: {} '.format(num[0]))

#ou (com limitações)
#print(len(num))
#print('Unidade: {} '.format(num[len(num) - 1]))
#print('Dezena: {} '.format(num[len(num) - 2]))
#print('Centena: {} '.format(num[len(num) - 3]))
#print('Milhar: {} '.format(num[len(num) - 4]))
