import random
#nome = str(input('Qual é seu nome? '))
#if nome == 'Murilo':
#   print('Que belo nome')
#else:
#    print('Prazer em te conhecer {}'.format(nome))

#nota1 = float(input('Digite a primeira nota: '))
#nota2 = float(input('Digite a segunda nota: '))

#media = (nota1 + nota2) / 2

#print('A média obtida foi de {:.1f}'.format(media))
#if media >= 6:
#    print('Sua média é boa!')
#else:
#    print('Sua média é ruim!')

#print('Parabéns!' if media >= 6 else 'Estude mais!')

print('\n*****Exercício 28*****\n')

sorteado = random.randrange(6)

n = int(input('Digite um número de 0 à 5: '))
if n>5 or n<0:
    print('Digite um número de 0 à 5')
if n == sorteado:
    print('Parabéns, você acertou o número que é {}'.format(sorteado))
else:
    print('Você errou o número, era {}'.format(sorteado))

print('\n*****Exercício 29*****\n')

velocidade = int(input('Digite a velocidade dos eu veículo: '))
if velocidade > 80:
    print('Você está indo muito rápido, a multa será de {}$'.format(7 * (velocidade - 80)))
else:
    print('Sua velocidade está normal')

print('\n*****Exercício 30*****\n')

num = int(input('Digite um número: '))
if num % 2 == 0:
    print('O número é par')
else:
    print('O número é impar')

print('\n*****Exercício 31*****\n')

dist = int(input('Qual a distância da sua viagem em quilômetros? '))
if dist < 200:
    print('O preço da sua passagem será {:.2f}$'.format(dist * 0.5))
else:
    print('O preço da sua passagem será {:.2f}$'.format(dist * 0.45))

print('\n*****Exercício 32*****\n')
ano = int(input('Digite o ano à ser analizado: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto')

print('\n*****Exercício 33*****\n')
a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
c = float(input('Digite outro número: '))

menor = c

if a<c and a<b:
    menor = a
if b<c and b<a:
    menor = b

maior = c

if a>c and a>b:
    maior = a
if b>c and b>a:
    maior = b

print('O maior número é {} e o menor é {}'.format(maior, menor))

print('\n*****Exercício 34*****\n')
salario = float(input('Informe o salário do funcionário: '))
if salario > 1250:
    print('O salário aumentado será de {}'.format(salario * 0.1))
else:
    print('O salário aumentado será de {}'.format(salario * 0.15))

print('\n*****Exercício 35*****\n')
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: ' ))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1<(r2 + r3) and r2<(r1 + r3) and r3<(r1 + r2):
    print('Essas retas podem formar um triângulo')
else:
    print('Essas retas não podem formar um triângulo')
