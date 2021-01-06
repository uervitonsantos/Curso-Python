# É possível usat a cláusula else para encerrar o loop while

x = 0

while x < 10:
    print('O valor de x nesta iteração é: ', x)
    print(' x ainda é menor que 10, somando 1 a x')
    x += 1

else:
    print('O valor de x nesta iteração é: ', x)
    print('Loop concluído!')
