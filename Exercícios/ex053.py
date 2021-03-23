#palíndromo (com split e join)
frase=input('Digite uma frase: ').strip().upper()
parte=frase.split()
completa=''.join(parte)
inversa=completa[::-1].strip().upper()
if inversa==completa:
    print('{} é o inverso de {}, então {} é um palíndromo. '.format(inversa, completa, frase))
elif inversa!=completa:
    print('{} é o inverso de {}, então {} não é um palíndromo. '.format(inversa, completa, frase))

#OU
frase=input('Digite uma frase: ').strip().upper()
parte=frase.split()
completa=''.join(parte)
inversa=''
for letra in range(len(completa)-1,-1,-1):
    inversa+=completa[letra]

if inversa==completa:
    print('{} é o inverso de {}, então {} é um palíndromo. '.format(inversa, completa, frase))
elif inversa!=completa:
    print('{} é o inverso de {}, então {} não é um palíndromo. '.format(inversa, completa, frase))
