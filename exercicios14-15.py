print('*****Exercício 14*****')

temp = float(input('Digite a temperatura em Celsius: '))

print('A temperatura de {} graus Celsius corresponde à {} Fahrenheit'.format(temp, (temp * 1.8) + 32))
             
print('\n*****Exercício 15*****\n')

dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros o carro percorreu? '))

print('O total a pagar é de {}'.format((60 * dias) + (0.15 * km)))
