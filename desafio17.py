co = float(input('Digite o numero de cateto oposto: '))
ca = float(input('Digite o numero do cateto adjascente: '))
hipo = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa do triangulo é {hipo:.2f} ')

#OU

from math import hypot
co = float(input('Digite o numero de cateto oposto: '))
ca = float(input('Digite o numero do cateto adjascente: '))
hipo = hypot(co, ca)
print(f'A hipotenusa do triangulo é {hipo:.2f} ')