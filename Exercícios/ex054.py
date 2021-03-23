#Grupo de maioridade
'''from datetime import date
cont = 0
for a in range(1,8):
    ano = int(input('Digite o {}º ano de nascimento: '.format(a)))
    idade = date.today().year - ano
    if idade>= 21:
        cont += 1
if cont<=1:
    print ('{} pessoa atingiu a maioridade e {} pessoas não atingiram a maioridade.'.format(cont,7-cont))
elif cont>1 and (7-cont>1):
    print ('{} pessoas atingiram a maioridade e {} pessoas não atingiram a maioridade.'.format(cont,7-cont))
elif cont>=6:
    print ('{} pessoas atingiram a maioridade e {} pessoa não atingiu a maioridade.'.format(cont,7-cont))'''

#OU
from datetime import date
totmaior = 0
totmenor = 0
for a in range(1,8):
    ano = int(input('Digite o {}º ano de nascimento: '.format(a)))
    idade = date.today().year - ano
    if idade>= 21:
        totmaior += 1
    elif idade<21:
        totmenor += 1
if totmaior<=1:
    print ('{} pessoa atingiu a maioridade e {} pessoas não atingiram a maioridade.'.format(totmaior,totmenor))
elif totmaior>1 and (totmenor>1):
    print ('{} pessoas atingiram a maioridade e {} pessoas não atingiram a maioridade.'.format(totmaior,totmenor))
elif totmenor<=1:
    print ('{} pessoas atingiram a maioridade e {} pessoa não atingiu a maioridade.'.format(totmaior,totmenor))
