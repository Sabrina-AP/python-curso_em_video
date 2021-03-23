#71 Simulador de caixa eletronica

cont50=cont20=cont10=cont1=0
while True:
    valor=int(input('Que valor você quer sacar? R$ '))
    if valor//50>0:
        cont50+=valor//50
        valor%=50
    if valor//20>0:
        cont20+=valor//20
        valor%=20
    if valor//10>0:
        cont10+=valor//10
        valor%=10
    if valor//1>0:
        cont1+=valor//1
        valor%=1  
    if  valor==0:
        break
if cont50>0:
    print(f'Total de {cont50:.0f} cédula(s) de R$ 50,00')
if cont20>0:
    print(f'Total de {cont20:.0f} cédula(s) de R$ 20,00')
if cont10>0:
    print(f'Total de {cont10:.0f} cédula(s) de R$ 10,00')
if cont1>0:
    print(f'Total de {cont1:.0f} cédula(s) de R$ 1,00')


#OU com repetições

while True: #esse segundo while garante que o programa só termine quando o usário digitr valor=0
    valor=int(input(f'\n Que valor você quer sacar? R$ '))
    ced=50
    tot=0
    if valor==0:
        break
    while True:
        if valor//ced>0:
            tot+=valor//ced
            valor%=ced
        else:
            if tot>0:
                print(f'Total de {tot} cédula(s) de R$ {ced}')
            if ced==50:
                ced=20
            elif ced==20:
                ced=10
            elif ced==10:
                ced=1
            tot=0
            
    

'''#OU
valor=int(input('\nQue valor você quer sacar? R$ '))
ced=50
tot=0
while True:
    if valor//ced>0:
        tot+=valor//ced
        valor%=ced
    else:
        if tot>0:
            print(f'Total de {tot} cédula(s) de R$ {ced}')
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=1
        tot=0
        if valor==0:
            break

            
#ou IGUAL ao do Guanabara
valor=int(input('\nQue valor você quer sacar? R$ '))
ced=50
tot=0
while True:
    if valor>=ced:
        valor-=ced
        tot+=1
    else:
        if tot>0:
            print(f'Total de {tot} cédula(s) de R$ {ced}')
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
             ced=1
        tot=0
        if valor==0:
            break
'''
