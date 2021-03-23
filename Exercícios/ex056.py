#analisador completo
lidades=[]
cont=0
soma=0

for i in range(1,5):
    nome = input('Digite o nome: ').upper().strip()
    idade = int(input('Digite a idade: '))
    sexo = input('Digite sexo (M ou F): ').upper().strip()    
    lidades.append(idade)   
    soma+=idade
    media=soma/i
    if sexo=='F' and idade<20:
        cont+=1
    if sexo=='M' and idade==max(lidades):
        homemmaisvelho=nome
        idadehmaisvelho=idade #quando for usar dados do IF criar variável dentro do IF ex essa idade
    print('='*25)
    
print('A média entre as idades {}, {}, {} e {} anos é {:.2f}'.format(lidades[0],lidades[1],lidades[2],lidades[3], media))

print('O nome do homem mais velho é {} e possui {} anos'.format(homemmaisvelho, idadehmaisvelho))

if cont<=1:
    print('A quantidade de mulheres que têm menos de 20 anos é de {} mulher'.format(cont))
else:
    print('A quantidade de mulheres que têm menos de 20 anos é de {} mulheres'.format(cont))
