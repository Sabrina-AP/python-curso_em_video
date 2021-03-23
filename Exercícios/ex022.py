#analisador de tetos
nome = input('Digite seu nome completo: ').strip() #elimina apenas espaços inuteis antes e depois
print('Analisando seu nome:')
print(nome.title())
print(nome.find('er'))
print('Seu nome em maiúculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
p = nome.split()[0] #split separa conforme os espaços do texto
print('Seu primeiro nome é {} e ele tem {} letras'.format(p.capitalize(),len(p)))

#OU
#nomesep = nome.split() 
#nomej = ''.join(nomesep)
#print('Seu nome tem ao todo {} letras'.format(len(nomej)))
#print('Seu primeiro nome é {} e ele tem {} letras'.format(nomesep[0],len(nomesep[0])))
