#alistamento militar com codigo para ano atual
from datetime import date

gênero = input('Indique se você é M (masculino) ou F (feminino): ').upper()

if gênero == 'M':
        nasc = int(input('Digite o ano do seu nascimento: '))
        anoatual=date.today().year
        idade = anoatual-nasc
        anoa = nasc + 18
        print('Quem nasceu em {} tem {} ano(s) em {} '.format(nasc, idade, anoatual))
        if idade==18:
                print('Você está em idade de se alistar, e deve se alistar agora em {}.'.format(anoa))
        elif idade<18:
                print('Falta(m) {} ano(s) para você se alistar.'.format(18-idade))
                print('Você não está em idade de se alistar, e deverá se alistar em {}'.format(anoa))
        else:
                print('Você deveria ter se alistado há {} ano(s).'.format(idade-18))
                print('Você já passou da idade de se alistar, e deveria ter se alistado em {}.'.format(anoa))
elif gênero == 'F':
        print('Você é mulher e não tem obrigação de se alistar.')
else:
        print('Dado inválido! Digite F ou M ')
