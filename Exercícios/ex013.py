#Reajuste salarial
s = float(input('Qual é o salário do Funcionário? R$'))
a = int(input('Qual o percentual de reajuste? '))
print('Um funcionário que ganhava R${:.2f}, com {:.2f}% de aumento, passa a ganhar R${:.2f}.'.format(s, a, s+((s*a)/100)))
