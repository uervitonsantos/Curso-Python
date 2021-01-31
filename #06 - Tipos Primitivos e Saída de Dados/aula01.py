class media:
    def __init__(self):
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        n3 = int(input('Digite o terceiro valor: '))

        md = int((n1 + n2 + n3) / 3)

        print('A media entre os valores {}, {}, {} é igual a: {}'.format(n1, n2, n3, md))


media()
