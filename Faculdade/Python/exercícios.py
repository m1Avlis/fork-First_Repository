#Exercício 1 - Crie uma função que receba uma número e retorne "Par" se o número for par e "Ímpar" caso contrário.
"""
n = int(input('Digite um número: '))
if n % 2 == 0:
    print('Par')
else:
    print('Ímpar')
"""
# Exercício 2 - Somar números em uma lista
#Minha resolução:
"""
lista = 2,4,6
soma = 0
for num in lista:
    soma += num
print(soma)
"""
#Gabarito exercício 2
"""
def soma_lista(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma
lista = [10,30,50]
resultado = soma_lista(lista)
print(resultado)"""

#Exercício 3 - Calcular o fatorial de um número usando o for
"""
n = int(input('Digite o número que deseja calcular o fatorial: '))
resultado = 1
for i in range(1, n+1):
    resultado *= i
print(resultado)
"""
# Gabarito exercício 3
"""
def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
n = 6
r = fatorial(n)
print(r)
"""

# Exercício 4 - Criar uma funçao que verifica se um numero é primo, e retorna True se for primo e False caso contrário.
"""
n = int(input('Digite o número que deseja verificar: '))
if n <= 1:
    print(False)
elif n == 2:
    print(True)
elif n % 2 == 0:
    print(False)
else:
    primo = True
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            primo = False
            break
print(primo)
"""
#Gabarito exercício 4

def primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5), 2):
        if n % i == 0:
            return False
    return True
n = int(input('Digite o número que deseja verificar: '))
print(primo(n))


# Crie um função que receba uma string e retorne o número de vogais prensentes nela.
# Não consegui resolver
"""
s = input('Digite o que quiser: ')

for i in range(1,len(s)):
    if i == 'a':
        v = 1
    v += i
print(f'Essa string tem {v} vogais.')
"""

#Exercício 7
"""
for i in range(1,101,):
    if i % 3 == 0:
        print(f'{i} Fizz')
    elif i % 5 == 0:
        print(f'{i} Buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print(f'{i} FizzBuzz')
"""

#Exercício 8 
# Não consegui resolver
"""
n = int(input('Digite um número: '))

if n > 1:
    print(n[0]+n[1])
"""

# Exercício 10
"""
from random import randint

n = randint(1,100)
num = int(input('Digite um número de 1 a 100: '))
t = 1
while num != n:
    if num > n:
        print('Você chutou alto')
        num = int(input('Digite um número de 1 a 100: '))
    else:
        print('Você chutou baixo')
        num = int(input('Digite um número de 1 a 100: '))
    t = t + 1
print(f'Você acertou! Precisou de {t} tentativas.')
"""
