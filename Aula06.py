n = input('Write semething: ')
print(f'Your type is {type(n)}')
print(f'Your value is {n}')
print(f'This is an alphanumeric? {n.isalnum()}')
print(f'This is alphabetic? {n.isalpha()}')
print(f'This is a numeric?{n.isnumeric()}')
print(f'This have only spaces? {n.isspace()}')

#Todos os is:
#alfabetico - isalpha 
#numerico - isnumeric
#só tem espaços - isspace
#alfabético e numérico - isalnum
#está em maiúsculas - isupper
#está em minúculas - islower
#está só com a primeira letra em maiúsulas - istitle
#bool é Treu or False