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
