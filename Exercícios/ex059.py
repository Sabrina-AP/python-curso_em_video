#solicite algo e faça aparecer menus de opções que realizam cálculos

op=0
while op!=5:
    n1=float(input('Digite o primeiro número: '))
    n2=float(input('Digite o segundo número: ')) #ou com o n1 e n2 fora do while
  
    op=int(input(''' Escolha uma opção: 
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    '''))
    
    if op==1:
        print('O resultado da soma dos números {} e {} é igual a {}'.format(n1,n2,n1+n2))
    elif op==2:
        print('O resultado da multiplicação dos números {} e {} é igual a {}'.format(n1,n2,n1*n2))
    elif op==3:
        if n1==n2:            
            print('Os números {} e {} são iguais'.format(n1,n2,n1))
        else:
             print('O maior número entre {} e {} é o {}'.format(n1,n2,max(n1,n2)))
    else:
        print('Dado inválido! Tente novamente!')
    print(25*'=*')
print('Programa encerrado...')
