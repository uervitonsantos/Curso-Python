import math


def numeroPrimo(num):
    """
    Verifica se um determinado numero é primo.
    """
    if (num % 2) == 0 and num > 2:
        print('Este número não é primo')
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            print('Este número não é primo')
    print('Este número:', num, 'é primo')


numeroPrimo(541)
