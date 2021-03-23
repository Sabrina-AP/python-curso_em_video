#aumentos múltiplos %
sal = float(input('Qual o salário do funcionário? R$'))
if sal<=1250:
    print('O novo salário é de R${:.2f}. '.format(sal+((15*sal)/100)))
else:
    print('O novo salário é de R${:.2f}. '.format(sal+((10*sal)/100)))
