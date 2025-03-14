# ESTRUTURAS DE REPETIÇÃO
"""
x = 1
while x <= 5:
    print(x)
    x = x + 1
"""
# Exemplo de variável contadora
"""
inicial = int(input('Qual valor deseja inicar a contagem?'))
final = int(input('Qual valor deseja finalizar a contagem?'))

x = inicial
while x <= final:
	if x % 2 == 0:
		print(x)
	x = x + 1
"""

# Exemplo de variável acumuladora
"""
soma = 0
cont = 1

while (cont <= 5):
    x = float(input(f'Digite a {cont}ª nota:'))
    soma = soma + x
    cont = cont + 1
media = soma / 5
print(f'Média final: {media}')
"""
"""
#Exemplo do uso dos operadores especiais
soma = 0
cont = 1

while (cont <= 5):
    x = float(input(f'Digite a {cont}ª nota:'))
    soma += x #Equivale a soma = soma + 1
    cont += 1 #Equivale a cont = cont + 1
media = soma / 5
print(f'Média final: {media}')
"""

#Exemplo de utilização da instrução Break
"""
print('Digite uma mensagem que iriei repetir para você!')
print('Para encerrar escreva "sair"')
while True:
	texto = input('')
	print(texto)
	if texto == 'sair':
		break
print('Encerrando o programa...')
"""

# Exemplo de utilização da instrução continue:
"""
while True:
	nome = input('Qual o seu nome?')
	if nome != 'Lenhadorzinho':
		continue
	senha = input('Qual a senha?')
	if senha ==  'UnInTer':
		break
print('Acesso concedido')
"""

# Exercício tabuada - Estruturas de repetição aninhadas
"""
num = 1
while num <= 10:
	print(f'Tábuada do {num}:')
	print("") # Apenas para adicionar uma linha de espaço.
	for i in range(1,11):
		print(f'{num}x{i}={num*i}')
	num += 1
	print("") # Apenas para adicionar uma linha de espaço.
"""