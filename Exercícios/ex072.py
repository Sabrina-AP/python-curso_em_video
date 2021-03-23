#072 MUNDO 3: tuplas

num=(0,1,2,3,4,5,6,7,8,9,10)
ext=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
while True:
    tec=int(input('Digite um numero entre 0 e 10: '))
    while tec not in num:
        tec=int(input('Fora do intervalo. Digite um numero entre 0 e 10: '))
    for i in num:
        if tec==num[i]:
           print(f'O numero por extenso é {ext[i]}')
        

