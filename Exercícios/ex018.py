'''sen, cosseno, tangente'''
from math import radians, sin, cos, tan
a = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {:.1f} tem o SENO de {:.2f}. '.format(a, sin(radians(a))))
print('O ângulo de {:.1f} tem o COSSENO de {:.2f}. '.format(a, cos(radians(a))))
print('O ângulo de {:.1f} tem o TANGENTE de {:.2f}. '.format(a, tan(radians(a))))
