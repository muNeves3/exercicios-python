print('\n*****Desafio 5*****\n')

n1 = int(input('Digitre um número inteiro: '))

print(' o antecessor de {} é {} e seu sucessor é {}'.format(n1, n1 -1, n1 +1))

print('\n*****Desafio 6*****\n')

n2 = float(input('Digite um numero: '))

print('O dobro de {} é {}, seu triplo é {} e sua raiz quadrada é {:.3f}'.format(n2, n2 * 2, n2 * 3, n2 **(1/2)))

print('\n*****Desafio 7*****\n')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

print('A média das notas {} e {} é: {} '.format(nota1, nota2, (nota1 + nota2)/2))

print('\n*****Desafio 8*****\n')

metro = float(input('Digite uma medida em metros: '))

print('A medida {} equivale a {} centímetros e {} milímetros'.format(metro, metro * 100, metro * 1000))

print('\n*****Desafio 9*****\n')

n3 = int(input('Digite um número: '))

for c in range (0,11):
    print('{} * {} == {}'.format(n3, c, n3 * c))

print('\n*****Desafio 10*****')

cash = float(input('Quantos reais você tem na carteira? '))

print('com {:.2f} reais você pode comprar {:.2f} dólares no valor de 3.27 cada'.format(cash, cash /3.27))

print('\n*****Desafio 11*****\n')

l = float(input('Qual a largura da sua parede? '))
c = float(input('Qual o comprimento da sua parede? '))

print('com o total de {} m² de área, sua parede precisará de {} litros de tinta, considerando que cada litro pinte até 2m² de área'.format(l * c, (l * c) / 2))

print('\n*****Desafio 12*****\n')

product = float(input('Informe o preço do produto: '))

print('O valor de um produto de {:.2f} com 5% de desconto é: {:.2f}'.format(product, product -(product * 0.05)))

print('\n*****Desafio 13*****')

salario = float(input('Informe seu salário? '))

print('Seu salário de {} com o aumento de 15% vai para: {}'.format(salario, salario + (salario * 0.15)))

