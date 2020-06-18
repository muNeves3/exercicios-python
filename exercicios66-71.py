from random import randint
#Loop infinito == (while True:)
"""n = s = 0
while True:
        n = int(input('Digite um número: '))
        if n == 999:
            break
        s += n
print('A soma vale {}'.format(s))
print(f'A soma vale {s} --> fstrings """
print('****exercicio 66*****')
n = s = cont = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Você digitou {cont} números')
print(f'A soma foi de {s}')

print('\n****exercicio 67*****\n')
tab = int(input('Qual tabuada será vista? '))
aux = 1
while True:
    if tab < 0:
        break
    while aux < 11:
        print(f'{tab} * {aux} == {tab * aux}')
        aux += 1
    tab = int(input('Qual tabuada será vista? '))
    aux = 1
    
print('\n****exercicio 68*****\n')
from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar [P/I]?')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, total {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCê VENCEU!')
            v += 1
        else:
            print('VOCê PERDEU!')
            break
    elif tipo == 'I':
          if total % 2 != 0:
              print('VOCê VENCEU!')
              v += 1
          else:
            print('VOCê PERDEU!')
            break
    print('Denovo!')
print(f'Você venceu {v} vezes')
            
print('\n****exercicio 69*****\n')
print('-'*15)
print('CADASTRO')
print('-'*15)
contidade = 0
cont = 0
conthomem = 0
while True:
    idade = int(input('Idade: '))
    if idade > 18:
        contidade += 1
    sexo = str(input('Sexo: [M/F] ')).upper()
    if sexo == 'M':
        conthomem += 1
    if sexo == 'F' and idade < 20:
        cont += 1
    if sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]'))
    print('-'*15)
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    print('-'*15)
    if continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] '))
    if continuar == 'N':
        break
print(f'Existem {contidade} pessoas com mais de 18 anos')
print(f'Existem {conthomem} homens cadastrados')
print(f'Existem {cont} mulheres com menos de 20 anos cadastradas')

print('\n****exercicio 70*****\n')
cont1000 = total = baratop = cont = 0
baraton = ''
print('-'*15)
print('LOJÃO')
print('-'*15)

while True:
    nomep = str(input('Nome do produto: '))
    preço = float(input('Preço: '))
    if cont == 1 or preço < baratop :
        baraton = nomep
        baratop = preço
    if preço > 1000:
        cont1000 += 1
    going = ' '
    while going not in 'SN':
        going = str(input('Quer continuar? [S/N] ' )).upper()
    print('-'*20)
    total += preço
    cont += 1
    if going == 'N':
        break
print('-'*25)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {cont1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {baraton} custando {baratop:.2f}')

print('\n****exercicio 71*****\n')
#50 20 10 1
print('-'*25)
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print('-'*25)
valor = int(input('Que valor você quer sacar? '))
total = valor
cedula = 50
totalced = 0
while True:
    if total >= cedula:
        total -= cedula
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0
        if total == 0:
            break


