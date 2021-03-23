from datetime import datetime

nome=input('Nome: ')
anodenascimento=int(input('Ano de nascimento: '))
idade= datetime.now().year-anodenascimento
carteiradetrabalho=int(input('Carteira de trabaho [0 não tem]: '))
if carteiradetrabalho==int(0):
    dicionario={'Nome': nome, 'Idade': idade, 'CPTS': carteiradetrabalho}
else:
    anodecontratação=int(input('Ano de contratação: '))
    salario=float(input('Salário: R$  '))
    idade2=anodecontratação-anodenascimento
    aposentadoria= idade2+35
    dicionario={'Nome': nome, 'Idade': idade, 'CPTS': carteiradetrabalho, 'Contratação': anodecontratação, 'Salário': salario, 'Aposentadoria': aposentadoria}

print(10*'=~=')
print(dicionario)
print(10*'=~=')
for k,v in dicionario.items():
    print(f'{k} tem o valor de {v}')
