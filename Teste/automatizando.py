# -*- coding: utf-8 -*-

fileName = input('Digite o nome do arquivo: ')
fileName = fileName + ".txt"
arq1 = open(fileName, 'w')
arq1.write('Esse texto é a realização de um teste')
arq1.close()
arq1 = open(fileName, 'r')
print(arq1.read())
arq1.close()
