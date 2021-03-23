#70 Estatísticas em produtos

tot=pmais=0
barato=[]
while True:
    produto=input('Nome do produto: ').upper().strip()
    preço=float(input('Preço: R$ '))
    continuar=' '
    while continuar not in 'SN':
        continuar=input('Quer continuar? [S/N]: ').upper().strip()[0]
    tot+=preço
    if preço>1000:
        pmais+=1     
    barato.append(preço)
    barato.sort()
    if preço==barato[0]:
        produtob=produto
        preçob=preço
    if continuar=='N':
        break
print(f'O total da compra foi R$ {tot:.2f}.')
print(f'Temos {pmais} produto(s) custando mais de R$ 1000,00.')
print(f'O produto mais barato foi {produtob} que custa R$ {preçob:.2f}.')
    
