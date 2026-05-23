print('Ola Mundo!')

nome = input('Qual seu nome? ')
print(f'Olá, {nome}!')

print('Digite sua data de nascimento abaixo: ')
while True:

    dia = input('Dia: ')
    mes = input('Mês: ')
    ano = input('Ano: ')
    resposta = input(f'Voce nasceu no {dia} no mes {mes} e no ano {ano}, certo? (s/n) ')

    if resposta.lower() == 's':
        print('Obrigado pela resposta!')
        break

    elif resposta.lower() == 'n':
        print('Voce deve ter digiitado algo errado, tente novamente!.\n')

    else:
        print('Resposta inválida, tente novamente!.\n)')



n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')
#n3 = int(input('Digite outro número: '))
#print(f'A soma é {n1 + n2}')
print(f'A soma é {int(n1) + int(n2)}')

n = input('Digite algo: ')

print(f'O tipo é {type(n)}')
print(f'O valor é {n}')
print(f'Isso é alfanumérico? {n.isalnum()}')
print(f'Isso é alfabético? {n.isalpha()}')
print(f'Isso é numérico? {n.isnumeric()}')
print(f'Isso tem apenas espaços? {n.isspace()}')
print(f'Isso é apenas maiusculo?{n.isupper()}')

n1 = int(input('Digite um numero: '))
n2 = int(input('Outro numero: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di= n1 // n2
p = n1 ** n2
print(f'A soma é {s}, \n a multiplicação é {m} \n e a divisão é {d:.2f}', end = ' === ')
print(f'A divisão inteira é {di} e a potencia é {p}')

ni = int(input('Escreva um numero inteiro:' ))
nn = ni - 1
nm = ni + 1
print(f'O seu numero é {ni} e seu sucessor é {nm} e seu antecessor é {nn}')

n = int(input('Escreva um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print(f'Seu numero é {n}; \n seu dobro é {d}; \n seu triplo é {t}; \ne sua raiz é {r}.')

p1 = float(input('Primeira nota: '))
p2= float(input('Segunda nota: '))
p3 = float(input('Terceira nota: '))
p4 = float(input('Quarta nota: '))
m = (p1 + p2) / 2
print(f'A media entre {p1:.1f}; \n {p2:.1f}; \n {p3:.1f} e; \n {p4:.1f} é: \n {m:.1f}')

medida = float(input('Digite uma distancia em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida}m para Km é {km}km e para Hm é {hm}hm e para dam é {dam}dam! ')
print(f'O valor de {medida}m para Dm é {dm}dm e para centimetros é {cm:.0f}cm e para milimetros é {mm:.0f}mm! ')

T = int(input('Escreva um numero inteiro e veja sua tabuada abaixo: '))
print('=' *12)
print(f'{T} x {1} = {T * 1}')
print(f'{T} x {2} = {T * 2}')
print(f'{T} x {3} = {T * 3}')
print(f'{T} x {4} = {T * 4}')
print(f'{T} x {5} = {T * 5}')
print(f'{T} x {6} = {T* 6}')
print(f'{T} x {7} = {T * 7}')
print(f'{T} x {8} = {T * 8}')
print(f'{T} x {9} = {T * 9}')
print(f'{T} x {10} = {T * 10}')
print('=' *12)

rs = float(input('Quanto dinheiro voce quer investir? R$ '))
d = rs / 5.03
e = rs / 5.84
print(f'Com {rs:.2f}R$ voce consegue comprar {d:.2f} dolares e {e:.2f} euros! ')

La = float(input('Largura da parede: '))
Al = float(input('Altura da sua parede: '))
a = La * Al 
t = a / 2
print(f'Sua parede tem a dimensão de {La} x {Al} e sua area é {a}m2')
print(f'A quantidade de tinta nescessaria para pintar a parede é de {t}L de tinta.')