#analizando triângulos
s1 = float(input('Digite o valor do primeiro segmento: '))
s2 = float(input('Digite o valor do segundo segmento: '))
s3 = float(input('Digite o valor do terceiro segmento: '))
if s1+s2>s3 and s2+s3>s1 and s1+s3>s2:
    print('Esses segmentos podem formar um triângulo" ')
else:
    print('Esses segmentos NÃO podem formar um triângulo" ')
