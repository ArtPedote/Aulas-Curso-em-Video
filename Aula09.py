frase = '  Curso em Video Python  '
print(frase[1:19:2])
print(len(frase.strip()))
print(frase.split())
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.find('Android'))


frase = 'Curso em Video Python'
print(frase.count('o'))
print(frase.count('O'))

frase = 'Curso em Video Python'
print(frase.upper().count('O'))
print(frase.lower().find('video'))

frase = 'Curso em Video Python'
print(frase.replace('Python', 'Java'))

frase = 'Curso em Video Python'
dividido = frase.split()
print(dividido[2] [3])