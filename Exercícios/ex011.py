#pintando parede
#alt gr + numero para fazer o m²
L = float(input('Largura da parede: '))
A = float(input('Altura da parede: '))
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m². '.format(L, A, L*A))
print('Para pintar essa parede, você precisará de {}l de tinta. '.format(((L*A)/2)*1))
