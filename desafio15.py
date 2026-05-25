dias = int(input('Quantos dias o cliente andou com o carro? '))
km = float(input('Quantos Km foram percorridos? '))
a = (dias * 60) + (km * 0.15)
print(f'O total a se pagar é de R${a:.2f} ')