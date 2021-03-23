#primeiro e último nome de uma pessoa
nome = input('Digite seu nome completo: ').title().strip()
print('Muito prazer em te conhecer, {}! '.format(nome)) 
print('Seu primeiro nome é {} '.format(nome.split()[0]))
print('Seu último nome é {} '.format(nome.split()[len(nome.split())-1]))
