import random
import time
#nome = str(input('Digite seu nome: '))

#if nome == 'Murilo':
#    print('Que brlo nome!')
#elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
#    print('Seu nome é bem popular no Brasil')
#elif nome in 'Ana Cláudia Jéssica Juliana':
#    print('Belo nome feminino')
#else:
#   print('Seu nome é bem normal')
#print('Tenha um bom dia!')

print('*****exercicio 36*****')
casa = float(input('Digite o valor da casa: R$ '))
salario = float(input('Digite o valor do seu salário: R$ '))
temp = int(input('Em quantos anos deseja pagar: '))

if casa /(12 * temp) <  salario * 0.3:
    print('Você poderá financiar a casa de {:.2f}R$ com o valor mensal de {:.2f}'.format(casa, casa /(12 * temp)))
else:
    print('VocÊ não poderá financiar a casa de {:.2f}R$ as prestações de {:.2f} ultrapassam 30%({:.2f}) do seu salário de {:.2f}R$'.format(casa, casa /(12 * temp), salario * 0.3, salario))

print('\n*****exercicio 37*****\n')
n = int(input('Digite um número inteiro: '))
base = str(input('Qual será a base de conversão, binário, octal ou hexadecimal '))

if base == 'binario':
    print('{} convertido para binário é {}'.format(n, bin(n)))
elif base == 'octal':
    print('{} convertido para octal é {}'.format(n, oct(n)))
elif base == 'hexadecimal':
    print('{} convertido para hexadecimal é {}'.format(n, hex(n)))
else:
    print('Digite corretamente!')

print('\n*****exercicio 38*****\n')
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

if n1 > n2:
    print('O maior número é {} e o menor é {}'.format(n1, n2))
elif n2 > n1:
    print('O maior número é {} e o menor é {}'.format(n2, n1))
else:
    print('Os dois números tem o mesmo valor')

print('\n*****Exercicio 39*****\n')
birth = int(input('Digite o ano de seu nascimento: '))

if 2019 - birth < 18:
    print('Ainda faltam {} anos para seu alistamento'.format((2019 - birth) - 18))
elif 2019 - birth == 18:
    print('Já está na hora do seu alistamento')
else:
    print('Já passaram {} anos do seu alistamento'.format((2019 - birth) - 18))
    
print('\n*****exercicio 40*****\n')
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: ' ))

if (nota1 + nota2) / 2 < 5:
    print('REPROVADO')
elif (nota1 + nota2) / 2 >= 5 and (nota1 + nota2) / 2 <= 6.9:
    print('RECUPERAÇÃO')
elif (nota1 + nota2) / 2 >= 7:  
    print('APROVADO')

print('\n*****exercicio 41*****\n')
atleta = int(input('Digite sua idade: '))

if atleta <= 9:
    print('MIRIM')
elif atleta >= 10 and atleta <= 14:
    print('INFANTIL')
elif atleta >= 15 and atleta <= 19:
    print('JUNIOR')
elif atleta == 20:
    print('SENIOR')
else:
    print('MASTER')

print('\n*****exercicio 42*****\n')
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: ' ))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1<(r2 + r3) and r2<(r1 + r3) and r3<(r1 + r2):
    print('Essas retas podem formar um triângulo')
    if r1 == r2 == r3:
        print('O triângulo formado será equilátero')
    elif r1 != r2 != r3 != r1:
        print('O triângulo formado será escaleno')
    else:
        print('O triângulo formado será isóceles')
else:
    print('Essas retas não podem formar um triângulo')

print('\n*****exercicio 43*****\n')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso * pow(altura,2)

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')

print('\n*****exercicio 44*****\n')
produto = float(input('Digite o prelo do produto: '))
pag = int(input("""Digite a condição de pagamento :
-1 para pagamento à vista em dinheiro/cheque
-2 para pagamento à vista no cartão
-3 para pagamento em até 2x no cartão
-4 para pagamento em 3x ou mais no cartão"""))

if pag == 1:
    preco = produto - (produto * 0.1)
    print('O preço será de {}R$'.format(preco))
elif pag == 2:
    preco = produto - (produto * 0.05)
    print('O preço será de {}R$'.format(preco))
elif pag == 3:
    print ('O preço será de {}R$'.format(produto))
elif pag == 4:
    preco = produto + (produto * 0.2)
    print('O preço será de {}R$'.format(preco))

print('\n*****exercicio 45*****\n')
print('-=' * 15)
print('JOKENPÔ')
print('-=' * 15)

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções são
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogador = int(input('Qual será sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 11)
print('O computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0: #pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 1: #papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: #tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')

    
