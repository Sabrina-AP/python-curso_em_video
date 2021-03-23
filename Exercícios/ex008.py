#conversor de medidas
d = float(input('Digite uma distância em metros: '))
print('A medida de {:.1f}m corresponde a: '.format(d))
print('{}km'.format(d*(10**(-3))))
print('{}hm'.format(d*(10**(-2))))
print('{:.1f}dam'.format(d*(10**(-1))))
print('{:.0f}dm'.format(d*10))
print('{:.0f}cm'.format(d*(10**2)))
print('{:.0f}nm'.format(d*(10**3)))
