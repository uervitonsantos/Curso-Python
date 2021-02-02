lista = []
for i in range(1):
    numero = list(input("Digite um número: "))
    if i == 0 or numero > lista[-1]:
        lista.append(numero)

    else:
        pos = 0
        while pos < len(lista):
            if numero <= lista[pos]:
                lista.insert(pos, lista)
                break
            pos += 1

    print("Lista atual:", list(lista))
print(f'='*30)
