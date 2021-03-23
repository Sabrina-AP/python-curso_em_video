#gerenciador de pagamentos (com o nome da loja centtralizado)

print('{:=^40}'.format(' LOJAS BIANCA '))

preço = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão ''')
opção = int(input('Escolha uma forma de pagamento: '))

if opção == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final. '.format(preço, preço-((10*preço)/100)))
elif opção == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final. '.format(preço, preço-((5*preço)/100)))
elif opção == 3:
    print('Sua compra de R${:.2f} será parcelada em 2x de R${:.2f} sem juros. '.format(preço, preço/2))
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    preçof=preço + 20*preço/100
    print('Sua compra será parcelada em {:.0f}x de R${:.2f} com juros. '.format(parcelas, preçof/parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final. '.format(preço, preçof))
else:
    print('Número inválido. Escolha outro!')
    

