""" Algoritmo que permite o preenchimento de 20 cartelas
    de um sorteio. A cartela tem 6 números para cada aposta
    de um range de numeros de 1 a 60"""
# import dos metodos
from random import sample
from time import sleep

# variavel que recebe uma lista
jogos = list()

# variavel que recebe o valor 20 que é numero de jogadas solicitadas
n = 20
cont = 0
"""loop que percore os numeros de 1 a 60 criando uma lista de 6 numeros aleatórios, 
    Zera a lista a cada passagem, imprime o numero da jogada e o jogo a cada 0.2 segundos"""

for i in range(n):
    a = sorted(sample(range(1, 61), 6))
    if a not in jogos:
        jogos.append(a)
        cont += 1
        jogos.append(a[:])
    print(f'Jogada número: {i + 1}: {a}')
    sleep(0.2)
