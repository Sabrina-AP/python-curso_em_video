#076 MUNDO 3: tuplas
t=('banana', '2,00', 'morango', '10,00','pêra', '1,50', 'abacaxi', '5,00')

for i in range(0,len(t)):
    if i%2==0:
        print(f'{t[i]:.<20} R$ {t[i+1]:>5}')
  
#for i in t:
 #   for j in t[i]:
  #      print(i)

