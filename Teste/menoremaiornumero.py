lista = []

for i in range(1):
    numero = list(input("Digite um número: "))
    for chave, valor in enumerate(lista):
        if numero < valor:
            lista.insert(numero)
            break
    else:
        lista.append(numero)
print("Lista atual:", lista)
