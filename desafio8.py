medida = float(input('Digite uma distancia em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida}m para Km é {km}km e para Hm é {hm}hm e para dam é {dam}dam! ')
print(f'O valor de {medida}m para Dm é {dm}dm e para centimetros é {cm:.0f}cm e para milimetros é {mm:.0f}mm! ')


#              KM HM DAM M DM CM MM
#               1  0  0  0  0  0  0
# Se for maior (divisão) se for menor (multiplicação)

# :.0f (nenhuma casa decimal)
# :.1f(somente uma casa decimal)
# :.2f(somente duas casas decimais)
# :.3f(somente três casas decimais)
# e assim por diante.
