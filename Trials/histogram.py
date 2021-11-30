import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics

sal1 = 1000
sal2 = 1500

sal3 = 1500
sal4 = 2000

sal5 = 2000
sal6 = 2500

sal7 = 2500
sal8 = 3000

sal9 = 3000
sal10 = 3500

sal1 = (sal1 + sal2)/2
sal2 = (sal3 + sal4)/2
sal3 = (sal5 + sal6)/2
sal4 = (sal7 + sal8)/2
sal5 = (sal9 + sal10)/2
lista1 = [sal1,sal2,sal3,sal4,sal5]

f1 = 15
f2 = 22
f3 = 30
f4 = 18
f5 = 15
lista2 = [f1, f2, f3, f4, f5]

completa = [sal1,sal1,sal1,sal1,sal1,sal1,sal1,sal1,sal1,sal1,
            sal1,sal1,sal1,sal1,sal1,
            sal2,sal2,sal2,sal2,sal2,sal2,sal2,sal2,sal2,sal2,
            sal2,sal2,sal2,sal2,sal2,sal2,sal2,sal2,sal2,sal2,
            sal2,sal2,
            sal3,sal3,sal3,sal3,sal3,sal3,sal3,sal3,sal3,sal3,
            sal3,sal3,sal3,sal3,sal3,sal3,sal3,sal3,sal3,sal3,
            sal3,sal3,sal3,sal3,sal3,sal3,sal3,sal3,sal3,sal3,
            sal4,sal4,sal4,sal4,sal4,sal4,sal4,sal4,sal4,sal4,
            sal4,sal4,sal4,sal4,sal4,sal4,sal4,sal4,
            sal5,sal5,sal5,sal5,sal5,sal5,sal5,sal5,sal5,sal5,
            sal5,sal5,sal5,sal5,sal5,3500]

df = pd.DataFrame(list(zip(lista1, lista2)), 
                  columns = ['Salários-M', 'Frequencia'])
print(df)

def calculo1(dop,top):
    fop = dop * top
    return fop

plt.hist(completa, bins=5)
plt.title('Histograma de Salários')
plt.xlabel('Salários')
plt.ylabel('Frequência')
plt.show()


som2 = f1+f2+f3+f4+f5
r1 = calculo1(sal1, f1)
r2 = calculo1(sal2, f2)
r3 = calculo1(sal3, f3)
r4 = calculo1(sal4, f4)
r5 = calculo1(sal5, f5)

som1 = r1+r2+r3+r4+r5
som2 = f1+f2+f3+f4+f5

medias = [r1,r2,r3,r4,r5]
frequencias = [f1,f2,f3,f4,f5]
média = statistics.median([sal1, sal2, sal3, sal4, sal5])
moda = statistics.mode(completa)

print(f'Média Salarial: {som1/som2}')
print(f'Moda Salarial: {2200.0}')
print(f'Mediana Salarial: {2216.7}')


