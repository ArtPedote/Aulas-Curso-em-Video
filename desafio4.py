n = input('Write something: ')
print(f'The type primitive this is {type(n)}')

print(f'Is a number? {n.isnumeric()}')

print(f'Is a alphabet? {n.isalpha()}')

print(f'Is a alpha numeric? {n.isalnum()}')

print(f'Is a special character? {n.isupper()}')

print(f'Is a space? {n.isspace()}')


#Todos os is:
#alfabetico - isalpha 
#numerico - isnumeric
#só tem espaços - isspace
#alfabético e numérico - isalnum
#está em maiúsculas - isupper
#está em minúculas - islower
#está só com a primeira letra em maiúsulas - istitle
