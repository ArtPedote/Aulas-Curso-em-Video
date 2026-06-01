nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print(f'Muito prazer em te conhecer {n[0]}')
print(f'Seu primeiro nome é {n[0]}')
print(f'E o seu ultimo nome é {n[ len(n) - 1]}')

#OU

nome = str(input('Digite seu nome completo: ')).split()
print(f'Muito prazer em te conhecer {nome[0]}')
print(f'Seu primeiro nome é {nome[0]}')
print(f'E o seu ultimo nome é {nome[- 1]}')

'''A as listas em python aceitam índices negativos pra encontrar seus últimos elementos.
A função .split() já elimina os espaços em branco. Por isso a função .strip() se faz redundante nesse contexto.'''