#aprovando emprestimo: estrutura aninhada
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
ano = int(input('Em quantos anos voê vai pagar? '))
prest = casa/(ano*12)
if prest<=(30*salario)/100:
    print('Empréstimo concedido! ')
else:
    print('Empréstimo NÃO concedido! ')






