#primeira e última ocorrencia de uma string
frase = input('Digite uma frase: ').upper().strip()
letra = input('Qual letra você quer saber se existe na frase? ').upper().strip()
print('A letra {} aparece {} vezes na frase '.format(letra, frase.count(letra)))
print('A primeira letra {} apareceu na posição {} '.format(letra, frase.find(letra)+1))
print('A última letra {} apareceu na posição {} '.format(letra, frase.rfind(letra)+1))
