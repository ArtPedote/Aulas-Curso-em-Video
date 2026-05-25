import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é igual a {math.ceil(raiz)} ')

# Ou eu posso usar somente a funcionalidade que eu desejar ex:

from math import sqrt
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {raiz:.2f} ')

