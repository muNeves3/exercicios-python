print('\n*****Exercício 22*****\n')
nome = str(input('Digite seu nome completo: ')).strip()

print(nome.upper())
print(nome.lower())
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
#ou nome.find(' ')

print('\n*****Exercício 23*****\n')
numero = int(input('Digite um número entre 0 e 9999: '))
u = numero // 1 %10
d = numero // 10 %10 
c = numero // 100 %10
m = numero //1000 %10
 
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centana: {}'.format(c))
print('Milhar: {}'.format(m))

print('\n*****Exercício 24*****\n')
cidade = str(input('Digiter o nome de uma cidade: ')).upper()
print('Essa cidade começa com SANTO? {}'.format('SANTO' in cidade))


print('\n*****Exercício 25*****\n')
nome1 = str(input('Digite seu nome: ')).upper()
print('Seu nome tem SILVA? {}'.format('SILVA' in nome1))

print('\n*****Exercício 26*****\n')
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "a" aparece {} vezes na frase'.format(frase.count('A')))
print('A letra "a" aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra "a" aparece pela última vez na posição {}'.format(frase.rfind('A')+1))


print('\n*****Exercício 27*****\n')
nome2 = str(input('Digite seu nome completo: '))
aux = nome2.split()
aux1 = nome2.find(' ')
#print('Seu primeiro nome é {}'.format(aux[0]))
print('Seu primeiro nome é {}'.format(nome2[:aux1]))
print('Seu último nome é {}'.format(aux[len(aux)-1]))


