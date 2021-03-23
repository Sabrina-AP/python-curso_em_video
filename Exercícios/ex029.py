#radar eletrônico (nós adaptamos para minutos de estudo)
min = int(input('Quantos minutos você já estudou inglês hoje? '))
if min>=60:
    print('Ótimo! Pode realizar suas outras atividades! ')
else:
    print('Estude por mais {}min! '.format(60-min))
