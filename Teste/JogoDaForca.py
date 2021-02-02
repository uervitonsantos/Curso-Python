import random


plv = random.choices(['casa', 'mesa', 'vila', 'moro', 'noite', 'vida'])

print('============= * INICIO DO JOGO * =============')

letra1 = input('Digite uma letra: ')

while plv != letra1:
    letra1 = input('Digite a palavra: ')

    if plv == letra1:
        print('============= * VOCÊ VENCEU O JOGO, PARABENS * =============')

    else:
        print('============= * FIM DO JOGO, TENTE NOVAMENTE * =============')

