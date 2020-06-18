import math
#from math import sqrt, ceil
#n1 = int(input('Digite um número: '))
#raiz = sqrt(n1)

#print('A raiz de {} == {}'.format(n1, ceil(raiz)))

import math
import random
#import pygame
print('*****Exercício 16*****')

n1 = float(input('Digite um número real: '))

print('A porção inteira de {} é {:.0f}'.format(n1,n1))

print('\n*****Exercício 17*****\n')

cat_op = float(input('Digite a medida do cateto oposto: '))
cat_adj = float(input('Digite a medida do cateto adjacente: '))

print('Com um cateto oposto de {} e um adjacente de {} a hipotenusa vale {:.2f}'.format(cat_op, cat_adj, math.hypot(cat_adj, cat_op)))

print('\n*****Exercício 18*****\n')

angle = float(input('Digite a medida de um ângulo: '))

print('O seno de {} é {}, seu cosseno é {} e sua tangente {}'.format(angle, math.sin(angle), math.cos(angle), math.tan(angle)))

print('\n*****Exercício 19*****\n')

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

sorteado = [aluno1, aluno2, aluno3, aluno4]

print('O aluno sorteado foi {}'.format(random.choice(sorteado)))

print('\n*****Exercício 20*****\n')

aluno11 = str(input('Digite o nome do primeiro aluno: '))
aluno22 = str(input('Digite o nome do segundo aluno: '))
aluno33 = str(input('Digite o nome do terceiro aluno: '))
aluno44 = str(input('Digite o nome do quarto aluno: '))

sequence = [aluno11, aluno22, aluno33, aluno44]
random.shuffle(sequence)

print('A sequencia de alunos foi:\n ')
print(sequence)

print('\n*****Exercicio 21*****\n')

#pygame.init()
#pygame.mixer.music.load('Música')
#pygame.mixer.music.play()
#pygame.event.wait()

