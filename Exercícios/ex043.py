#índice de massa corporal
peso = float(input('Qual o seu peso? (kg): '))
altura = float(input('Qual é a sua altura? (m): '))
imc = peso/(altura**2)

print('Seu IMC é {:.2f}. '.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso. ')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal. ')
elif 25 <= imc < 30:
    print('Você está sobrepeso. ')
elif 30 <= imc < 40:
    print('Você está com obesidade. ')
elif imc >= 40:
    print('Você está com obesidade mórbida. ')
