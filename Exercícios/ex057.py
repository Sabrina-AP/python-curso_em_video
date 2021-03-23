#Validação de dados: while para determinar se digitou apenas uma das opções válidas

'''s=input('Digite seu sexo [M/F]: ').upper().strip()[0]

while s!='M' and s!='F':
    s=input('Dado inválido. Digite novamente seu sexo [M/F]: ').upper().strip()
if s=='M':
    print('O sexo é masculino.')
elif s=='F':
    print('O sexo é feminino.')
'''


s=input('Digite seu sexo [M/F]: ').upper().strip()[0]

while s not in 'MF': #como a string é uma lista pode usar o IN ou NOT IN com o input
    s=input('Dado inválido. Digite novamente seu sexo [M/F]: ').upper().strip()
print('O sexo {} foi registrado com sucesso.'.format(s))

input()
