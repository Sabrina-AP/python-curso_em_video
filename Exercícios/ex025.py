#procurando uma string dentro de outra
nome = input('{}Qual o seu nome completo?{} '.format('\033[0:31:42m','\033[m')).strip()
nome = nome.title()
print('Seu nome tem Silva? {} '.format('Silva' in nome))

#ou
#print('Seu nome tem Silva? {} '.format((nome.find('Silva')!= -1) == True))

