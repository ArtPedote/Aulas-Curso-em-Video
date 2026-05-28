import random
a1 = input('Primero aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(f'A ordem de apresentação é {lista} ')

# OU

import random
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
ordem = random.sample([a1, a2, a3, a4], k=4)
print('A ordem dos alunos é {}' .format(ordem))