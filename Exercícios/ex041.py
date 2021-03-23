#classificando atletas
from datetime import date
nasc=int(input('Digite o ano do seu nascimento: '))
idade=date.today().year-nasc
if idade<=9:
    print('Uma pessoa de {} ano(s) entra na categoria: MIRIM'.format(idade))
elif idade<=14:
    print('Uma pessoa de {} ano(s) entra na categoria: INFANTIL'.format(idade))
elif idade<=19:
    print('Uma pessoa de {} ano(s) entra na categoria: JÚNIOR'.format(idade))
elif idade<=25:
    print('Uma pessoa de {} ano(s) entra na categoria: SÊNIOR'.format(idade))
elif idade>25: #o último poderia ser else
    print('Uma pessoa de {} ano(s) entra na categoria: MASTER'.format(idade))

