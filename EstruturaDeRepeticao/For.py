def loop_for_simples():
    tp = (2, 3, 4)
    for i in tp:
        print(i)


# Imprimir na tela os números pares dalista de números
def loop_for_lista():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in lista:
        if num % 2 == 0:
            print(num)


loop_for_simples()
loop_for_lista()
