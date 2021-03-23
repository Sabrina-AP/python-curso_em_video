'''catetos e hipotenusa'''
from math import sqrt
c = float(input('Comprimento do cateto oposto: '))
a = float(input('Comprimento do cateto adjacento: '))
print('A hipotenusa vai medir {:.2f}. '.format(sqrt(a**2+c**2)))

'''ou'''

from math import hypot
c = float(input('Comprimento do cateto oposto: '))
a = float(input('Comprimento do cateto adjacento: '))
print('A hipotenusa vai medir {:.2f}. '.format(hypot(c, a)))
