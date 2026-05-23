n1 = int(input('Digite um numero: '))
n2 = int(input('Outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di= n1 // n2
p = n1 ** n2
print(f'A soma é {s}, \n a multiplicação é {m} \n e a divisão é {d:.3f}', end = ' === ')
print(f'A divisão inteira é {di} e a potencia é {p}')
