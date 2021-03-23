#073 MUNDO 3: tuplas

nome=('Bianca', 'Sabrina', 'Wilson', 'Selmaria', 'Laura', 'Nick', 'Dick', 'Ilda','Ailde','Nara')

print(f'Lista de nomes: {nome} \n')

print(f'Os cinco com maiores notas são: {nome[:5]} \n')
print(f'Os quatro ultimos são: {nome[6:]} \n')
print(f'Em ordem alfabetica, temos: {sorted(nome)} \n')
print(f'Posição da Laura: {nome.index("Laura")+1}º posição')

