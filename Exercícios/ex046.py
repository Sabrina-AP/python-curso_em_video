#contagem regressiva
from time import sleep
c=int(input('De quantos segundos você que a contagem regressiva: '))
c=c+1
for i in range(c,0,-1):
    c-=1
    print(c)
    sleep(1)
print('buum!!!')
