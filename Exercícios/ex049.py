#tabuada (com FOR e fizemos codigo para aparecer todas as tabuadas)
##t=int(input('Digite um número para ver sua tabuada: '))
##for i in range(0,11):
##    r=t*i
##    print('{} x {:2} = {}'.format(t, i, r))
        
for t in range(0,11):    
    for i in range(0,11):
        r=t*i
        print('{} x {:2} = {}'.format(t, i, r))
    print(' '*2)
       
    
