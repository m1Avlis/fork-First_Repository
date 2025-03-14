""" Exercício 1
if 2+2 < 4:
    print('verdadeiro')
else:
    print('falso')
"""
""" Exercício 2
if (7//3) == (1+1):
    print('verdadeiro')
else:
    print('falso')
"""
""" Exercício 3
if (3**2) + (4**2) == 25:
    print('verdadeiro')
else:
    print('falso')
"""
"""Exercício 4
if 2+4+6 > 12:
    print('verdadeiro')
else:
    print('falso')
"""
""" Exercício 5
if 1387 % 19 == 0:
    print('verdadeiro')
"""
"""Exercício 6
if 31 % 2 == 0:
    print('Verdadeiro')
"""
""" Exercício 7
if min(34, 29,31) < 30:
    print('verdadeiro')
"""

"""Exercício 8
idade = 61
if idade > 60:
    print('Você tem direito aos benefícios!')
"""
"""Exercício 9
dano = 11
escudo = 0
if dano > 10 and escudo == 0:
    print('Você está morto!')
"""
"""Exercício 10
norte = False
sul = False
leste = False
oeste = True
if norte == True or sul == True or leste == True or oeste == True:
    print('Você escapou!')
"""
"""Exercício 11
ano = 2024
if ano % 4 == 0:
    print('Pode ser um ano bissexto.')
else:
    print('Definitivamente não é um ano bissexto.')
"""
"""Exercício 12
cima = True
baixo = False
if cima == True and baixo == True:
    print('Decida-se!')
else:
    print('Você escolheu um caminho!')
"""

a = int(input('Escreva o primeiro valor: '))
b = int(input('Escreva o segundo valor: '))
c = int(input('Escreva o terceiro valor: '))

if a <= 0 or b <= 0 or c <= 0:
    print('Não é possível formar um triângulo.')
    exit()
if a == b and b == c or c == a and a == b:
    print('Triângulo Equilátero')
elif a == b and a != c or b == c and b != a or c == a and c != b:
    print('Triângulo Isósceles')
elif a != b and b != c or a != c and c != b:
    print('Triângulo Escaleno')