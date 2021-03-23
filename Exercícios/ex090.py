#dic={}
c=''

nome = input('Digite um nome: ')
nota = int(input('Digite a nota: '))

if nota >= 7:
    s='Aprovado'
else:
     s='Reprovado'
dic={'Nome':nome, 'Nota':nota, 'Situação':s}


for k, v in dic.items():
    print(f'{k} é igual a {v}')

print(dic)
