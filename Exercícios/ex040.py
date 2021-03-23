#clássico da média
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media=(nota1+nota2)/2
if media<5:
    print('O aluno que tirou {:.1f} e {:.1f} tem média {:.1f} e portanto está reprovado. '.format(nota1, nota2, media))
elif media>=7:
    print('O aluno que tirou {:.1f} e {:.1f} tem média {:.1f} e portanto está aprovado. '.format(nota1, nota2, media))
elif 5<=media<=6.9:
    print('O aluno que tirou {:.1f} e {:.1f} tem média {:.1f} e portanto está de recuperação. '.format(nota1, nota2, media))
    

