"""
tuplas
AS TUPLAS SÃO IMUTÁVEIS
 [0, 1, 2, 3]
[-4, -3, -2, -1]
lanche = ('hamburger', 'suco', 'pizza', 'pudim')

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('\n')

for cont in range (0, len(lanche)): pode mostrar a posição
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('\n')

for comida in enumerate(lanche): para mostrar a posição utiliza-se do enumerate
    print(f'eu vou comer {comida}')
print('comi pra caramba!')

print(sorted(lanche)) organiza a tupla

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c) #2, 5, 4, 5, 8, 1, 2
print(c.count(5)) #2 vezes
print(c.index(8)) # posição 4
print(c.index(2, 1)) # começa à partir da posição 1
del(c) #deleta a tupla """

print('\n*****exercicio 72*****\n')
zerovinte = ('zero', 'um', 'dois', 'três', 'quatro',
             'cinco', 'seis', 'sete', 'oito', 'nove',
             'dez', 'onze', 'doze', 'treze','catorze',
             'quinze', 'dezesseis', 'dezessete', 'dezoito',
             'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num >= 0 and num <= 20:
        break
    print('Tente novamente, ',end='')
print(f'Você digitou {zerovinte[num]}')

print('\n*****exercicio 73*****\n')
times = ('','Palmeiras', 'Flamengo', 'Internacional', 'Grêmio',
'São Paulo', 'Atlético-MG', 'Atlético-PR', 'Cruzeiro', 'Botafogo',
'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará SC',
'Vasco da Gama', 'Sport Recife', 'América-MG', 'EC Vitória', 'Paraná')
print(times[1:6])
print(times[17:])
print(sorted(times))
print(times.index('Chapecoense'))

print('\n*****exercicio 74*****\n')
from random import randint
n = (randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10),
     randint(1, 10) )
print(f'Valores sorteados: ')
for c in n:
    print(f'{c} ',end='')
print(f'O maior valor foi: {max(n)}')
print(f'O menor valor foi: {min(n)}')

print('\n*****exercicio 75*****\n')
numeros = (int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')))
print(f'Você digitou os valores {numeros}')
print(f'O número 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1} posição')
else:
    print(f'O valor 3 não foi encontrado')
print(f'Os valores pares digitados foram: ',end='')
for c in numeros:
    if c % 2 == 0:
        print(c,end='')

print('\n*****exercicio 76*****\n')
produtos = ('Teclado', 250,
            'Lápis', 1.50,
            'Caderno', 23.45,
            'Caneta', 2.50)
for i in range (0, len(produtos)):
        if i % 2 == 0:
            print(f'{produtos[i]:.<30}R$', end ='')
        else:
            print(f'{produtos[i]:>6.2f}')
        
print('\n*****exercicio 77*****\n')
palavras = ('Bom', 'Dia',               #== ['B','o','m']
            'Estudar', 'Trabalhar',
            'Focar')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos ',end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')

