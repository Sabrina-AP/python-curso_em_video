#67 tabuada v3

while True:
    t=int(input('Quer ver a tabuada de qual valor? '))
    if t < 0:
        print('Encerrado!')
        break
    for i in range(0, 11):
        tabuada=t*i
        print(f'{t} x {i:^2} = {tabuada}')
    print(40*'~')
    
