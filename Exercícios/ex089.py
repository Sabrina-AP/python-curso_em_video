0#ex089

boletim=[[],[[],[]],[]]

while True:
    nome=input('Nome: ')
    nota1=int(input('Nota1: '))
    nota2=int(input('Nota2: '))
    continuar=input('Quer continuar? [S/N]: ')
    boletim[1][0].append(nota1)
    boletim[1][1].append(nota2)    
    media=(nota1+nota2)/2
    boletim[0].append(nome)
    boletim[2].append(media)
    if continuar=='n':
        break
print(boletim[0],boletim[1],boletim[2])
print(f'       Nº            Nome           Média')    
for i in range(0,len(boletim[0])):
    print(f'{i:^15}{boletim[0][i]:^15} {boletim[2][i]:^15}')
while True:
    aluno=int(input('Mostrar nota de qual aluno? (999 interrompe): '))
    if aluno==999:
        break
    print(f'Notas de {boletim[0][aluno]} são {boletim[1][0][aluno]}, {boletim[1][1][aluno]}')
    

   
   
   
