#83 aula 17 listas

expressao=input('Digite a expressão: ')

listal=listall=[]
a=1


for l,m in enumerate(expressao):
    if m == '(': 
        listal.append(l)
    elif m==')':
        listall.append(l)
if len(listal)==len(listall):
    c=len(listal)
    for i in range(0,c):
        if listal[i]<listall[i]:
            a+=2
          
if a%2==0:    
    print('Sua expressão está válida!')  
else:
    print('Sua expressão não está válida por causa de parênteses!')

#SABRINA FEZ DE OOUTRO JEITO MAIS RESUMIDO SEM ENUMERATE


print(45*'=')


#prof. guanabara
expr=(input('Digite a expressão: '))
pilha=[]
for simb in expr:
    if simb=='(':
        pilha.append('(')
    elif simb==')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('Sua expressão esta valida')
    print(pilha)
    print(len(pilha))
else:
    print('Sua expressão está errada')
    print(pilha)
    print(len(pilha))


      
        
          
                
           
