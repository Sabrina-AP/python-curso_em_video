#conversor de bases numéricas: estrutura aninhada
num = int(input('Digite um número inteiro para conversão: '))
base = int(input('''Escolha a base para conversão:
[1] para binário,
[2] para decimal e
[3] para hexadecimal
Sua opção:'''))

if base==1:
    print('O número {} na base binária é {}'.format(num, bin(num)[2:]))
elif base==2:
    print('O número {} na base octal é {}'.format(num, oct(num)[2:]))
elif base==3:
    print('O número {} na base hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Número inválido ')
    
