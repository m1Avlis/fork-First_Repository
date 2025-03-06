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
"""
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
"""

# Exercício 5 - Crie um função que receba uma string e retorne o número de vogais prensentes nela.
# Não consegui resolver
"""
vogais = 'aeiouAEIOU'
contador = 0
texto = input('Digite um texto qualquer: ')
for letra in texto:
    if letra in vogais:
        contador += 1
print(contador)
"""
# Gabarito exercício 5
"""
def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador
"""
#Exercício 6 - Crie uma tábuada
"""
n = int(input('Digite um número: '))
c = 1
while c <= 10:
    print(f'{c}x{n}={c*n}')
    c+= 1
"""
# Gabarito exercício 6
"""
def tabuada(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
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
#Gabarito exercício 7
"""
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
"""
#Exercício 8 - Somar digitos de números
"""
n = int(input('Digite um número maior do que 10: '))
soma = 0
while n < 10:
    n = int(input('Digite um número maior do que 10: '))
while n > 0:
    soma += n % 10
    n = n // 10
print(soma)
"""
#Gabarito exercício 8

#Exercício 9 - Verificar se uma string é um palíndromo
texto = input('Digite um texto qualquer: ')

texto = texto.lower().replace(" ", "")
print(texto == texto[::-1])

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
#Gabarito exercício 10
"""
import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    while True:
        palpite = int(input("Digite um número entre 1 e 100: "))
        tentativas += 1
        if palpite < numero_secreto:
            print("Tente um número maior.")
        elif palpite > numero_secreto:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
"""
