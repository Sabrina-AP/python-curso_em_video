#69 Análise de dados do grupo

maisde18=homens=mulheres20=0

while True:
    idade=int(input('Idade: '))
    sexo=continuar=' '
    while sexo not in 'MF' or continuar not in 'SN': #garantir que digitos errados nao passarão
        sexo=input('Sexo [M/F]: ').strip().upper()[0]
        continuar=input('Quer continuar? [S/N]: ').strip().upper()[0]
    print(35*'-')
    
    if idade>18:
        maisde18+=1
    if sexo=='M':
        homens+=1
    elif sexo=='F' and idade<20:
        mulheres20+=1
        
    if continuar=='N':
        break
print(f'Total de pessoas com mais de 18 anos: {maisde18}')
print(f'Ao todo temos {homens} homem(ns) cadastrado(s)')
print(f'E temos {mulheres20} mulher(es) com menos de 20 anos.')

