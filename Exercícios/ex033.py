#maior e menor valores
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))

#menor valor
if v1<=v2<=v3 or v1<=v3<=v2:
    print('O menor valor é {} '.format(v1))
if v2<=v3<=v1 or v2<=v1<=v3:
    print('O menor valor é {} '.format(v2))
if v3<=v2<=v1 or v3<=v1<=v2:
    print('O menor valor é {} '.format(v3))

#maior valor
if v1>=v2>=v3 or v1>=v3>=v2:
    print('O maior valor é {} '.format(v1))
if v2>=v3>=v1 or v2>=v1>=v3:
    print('O maior valor é {} '.format(v2))
if v3>=v2>=v1 or v3>=v1>=v2:
    print('O maior valor é {} '.format(v3))





    
        
    
