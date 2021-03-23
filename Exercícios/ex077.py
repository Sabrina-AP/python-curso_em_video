#077 MUNDO 3: tuplas

t=('casa', 'baralho', 'borboleta', 'teclado', 'cachorro', 'parque', 'orelha')

for i in t:
    print(f'\n Na palavra {i.upper()} temos', end=' ') 
    for j in i:
        if j in ('aeiou'):
            print(f'{j}',end=' ')
        

#\ =alt92
