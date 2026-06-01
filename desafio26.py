frase = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra O apareceu {frase.lower().count('o')} vezes na frase. ')
print(f'Aprimeira letra O apareceu na posição {frase.find('o') + 1} ')
print(f'A ultima letra O apareceu na posição {frase.rfind('o') + 1}')