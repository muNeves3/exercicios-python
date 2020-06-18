from time import sleep
from datetime import date
#for i in range (começo, fim, quantos irá pular(passo)):
#    print(i)

print('*****exericio 46*****')
for i in range (10 , 0, -1):
    print(i)
    sleep(0.005)
print('BOOOM')

print('\n*****exericio 47*****\n')
for a in range (1, 51):
    if (a % 2) == 0:
        print(a)
print('\n*****exericio 48*****\n')
soma = 0
for b in range (1, 501):
    if (b % 2) != 0 and (b % 3) == 0:
        print(b)
        soma += b
        print('soma == {}'.format(soma))
        
print('\n*****exericio 49*****\n')
tabuada = int(input('Digite um número para obter sua tabuada: '))
for c in range (1, 11):
    print('-=' *10)
    print('{} * {:2} == {}'.format(c, tabuada, tabuada * c))
    print('-=' *10)

print('\n*****exericio 50*****\n')
soma = 0
for d in range (1, 7):
    n = int(input('Digite um número inteiro:  '))
    if n % 2 == 0:
        soma += n
print(soma)

print('\n*****exericio 51*****\n')
pa = int(input('Digite um número: '))
razao = int(input('Digite a razão da PA: '))
aux = 0
for e in range (pa, (pa *10)+ 1, razao):
    aux += pa
    print(aux)
print('\n*****exericio 52*****\n')
cousin = int(input('Digite um número: '))
aux = 0
for f in range (1, cousin + 1):
    if cousin % f == 0:
        aux += 1
if aux == 2:
    print('É primo')
else:
    print('Não é primo')
print('\n*****exericio 53*****\n')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Palíndromo!')
else:
    print('Não é um palíndromo')

print('\n*****exericio 54*****\n')
atual = date.today().year
maior = 0
menor = 0
for g in range (1, 8):
    birth = int(input('Digite a data do nascimento da {}º pessoa: '.format(g)))
    idade = atual - birth
    if idade >= 21:
        print('Essa pessoa tem a maioridade')
        maior += 1
    else:
        print('Essa pessoa não tem a maioridade')
        menor += 1
print('Ao total tivemos {} pessoas maiores de idade e {} menores de idade'.format(maior, menor))
  
print('\n*****exericio 55*****\n')
maior = 0
menor = 0
for h in range (1, 6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(h)))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg e o menor foi de {}'.format(maior, menor))

print('\n*****exericio 56*****\n')
idadeF = 0
media = 0
maiorH = 0
anome = ''
for i in range (1, 5):
    print('-='*10)
    print('{}º pessoa'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: '))
    print('-='*10)
    media += idade
    if sexo == 'Masculino' and i == 1:
        maiorH = idade
        anome = nome
    if sexo == 'Masculino' and idade > maiorH:
        maiorH = idade
        anome = nome
    if sexo == 'Feminino' and idade < 21:
        idadeF += 1
        
print('O homem mais velho é {} com {} anos'.format(anome, maiorH))
print('A média das idades foi {}'.format(media / 4))
print('Existem {} mulheres com menos de 20 anos'.format(idadeF))
