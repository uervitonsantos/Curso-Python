# Recebe o valor digitado pelo usuario e armazena na variavel "valor"
valor = int(input('Quanto deseja sacar? R$: '))
print('*'*30)

# Verifica se o valor digitado é maior que zero
if valor <= 0:
    print('Valor inválido')

# variaveis de armazenamento dos valores
total = valor
cedula = 50
total_cedula = 0

# verificação da quantidade de cedulas para para o valor digirado
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print('*' * 30)

