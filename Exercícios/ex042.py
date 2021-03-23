#analisando triângulos com end='' (mensagens na mesma linha)
s1=int(input('Digite o valor do segmento 1: '))
s2=int(input('Digite o valor do segmento 2: '))
s3=int(input('Digite o valor do segmento 3: '))

if s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
    print('Esses segmentos formam um triângulo ', end='')
    if s1==s2==s3:
        print('do tipo equilátero.')
    elif s1==s2 or s1==s3 or s2==s3:
        print('do tipo isósceles.')
    elif s1!=s2!=s3:
        print('do tipo escaleno.')
else:
        print('Esses segmentos NÃO formam um triângulo.')
