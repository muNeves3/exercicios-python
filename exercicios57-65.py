import random
# = 1
#par = 0
#impar = 0
#while n != 0:
#    n = int(input('Digite um valor: '))
#   if n != 0:
#        if n % 2 == 0:
#            par += 1
#       else:
#          impar += 1
#print('Fim')
#print('Voce digitou {} pares e {} ìmpares'.format(par, impar))
        
print('*****exercicio 57*****')
sexo = str(input('Digite seu sexo [M/F]: ')).upper()

while sexo != "M" and sexo != "F":
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
print('Fim')

print('\n*****exercicio 58*****\n')
randomico = random.randrange(11)
tentativa = int(input('Tente adivinhar o número entre 0 e 10: '))
while tentativa != randomico:
    tentativa = int(input('Tente adivinhar o número entre 0 e 10: '))
print('Você acertou!')

print('\n*****exercicio 59*****\n')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('DIgite o segundo número: ' ))
aux = 0
while aux != 5:
    aux = int(input("""Você quer:
    [1]somar
    [2]multiplicar
    [3]saber qual é o maior
    [4]colocar novos números
    [5]sair do programa
    """))
    if aux == 1:
        print('{} + {} == {}'.format(n1, n2, n1 + n2))
    elif aux == 2:
        print('{} * {} == {}'.format(n1,n2, n1 * n2))
    elif aux == 3:
        if n1 > n2:
            print('{} > {}'.format(n1,n2))
        else:
            print('{} > {}'.format(n2, n1))
    elif aux == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('DIgite o segundo número: ' ))
    elif aux == 5:
        print('Fim')
    else:
        print('Opção inválida')

print('\n*****exercicio 60*****\n')
fatorial = int(input('Digite um número: '))
aux = fatorial
aux2 = 1
while aux > 0:
    print('{}'.format(aux),end='')
    print('x' if aux > 1 else ' = ',end='')
    aux2 *= aux
    aux -= 1
print('{}'.format(aux2))

print('\n*****exercicio 61*****\n')
pa = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
first = pa
aux = 1
while aux < 11:
    print('{} '.format(first),end='')
    first += razao
    aux+=1
print('Fim')

print('\n*****exercicio 62*****\n')
pa = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
first = pa
aux = 1
quant = 10
termos = 10
while termos != 0:
    while aux <= quant:
        print('{} '.format(first),end='')
        first += razao
        aux+=1
    termos = int(input('Quer mostrar mais quantos termos? '))
    quant += termos
print('\nFim')

print('\n*****exercicio 63*****\n')
termos = int(input('Quantos numeros da sequencia quer mostrar? '))
cont = 3
start = 0
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2),end='')
while cont <= termos:
    t3 = t1 + t2
    print('-> {}'.format(t3),end='')
    cont += 1
    t1 = t2
    t2 = t3
print('\nFim')

print('\n*****exercicio 64*****\n')
n = int(input('Digite um número: '))
cont = 0
aux = n - 999
while n != 999:
    n = int(input('Digite um número: '))
    cont +=1
    aux += n  
print('Você digitou {} numeros'.format(cont))
print('A soma deles foi {}'.format(aux))
print('Fim')

print('\n*****exercicio 65*****\n')
maior = 0
menor = 0
cont = 0
aux = 0
media = 0
continua = 'S'
while continua == 'S':
    n = int(input('Digite um número: '))
    aux += n
    cont +=1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    continua = str(input('Você quer continuar a digitar? [S/N] ')).upper()
media = aux/cont   
print('A media dos numeros foi {}'.format(media))
print('O maior foi {}, e o menor {}'.format(maior, menor))
            

    
