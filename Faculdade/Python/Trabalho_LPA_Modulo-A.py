# Questão 1:
"""print('Olá! Seja bem vindo a loja do Mario Pereira.')

vl = float(input('Insira o valor do produto: '))
qtd = int(input('Insira a quantidade do produto: '))
vl_total = qtd*vl

if vl_total >= 10000:
    vl_desconto = vl_total - (vl_total*0.11) #calcula o desconto de 11%
elif vl_total >= 6000 and vl_total < 10000:
    vl_desconto = vl_total - (vl_total*0.07) #calcula o desconto de 7%
elif vl_total >= 2500 and vl_total < 6000:
    vl_desconto = vl_total - (vl_total*0.04) #calcula o desconto de 4%
else:
    vl_desconto = vl_total 

print(f'O valor sem desconto foi de R${vl_total}.')
print(f'O valor com desconto foi de R${vl_desconto}')"""

# Questão 2:

print('Olá! Seja bem vindo a loja de gelados do Mario Pereira.')

print('------------------Cardápio------------------')
print('--------------------------------------------')
print('---| Tamanho | Cupuaçu (CP) | Açaí (AC) |---')
print('---|    P    |   R$  9.00   | R$ 11.00  |---')
print('---|    M    |   R$ 14.00   | R$ 16.00  |---')
print('---|    G    |   R$ 18.00   | R$ 20.00  |---')
print('--------------------------------------------')
vl = 0
vrl = 0
while True:

    sb = input('Qual o sabor desejado? (AC/CP): ').upper()
    sabores = ['AC','CP']
    while sb not in sabores:
        print('Sabor inválido, tente novamente.')
        sb = input('Qual o sabor desejado? (AC/CP): ').upper()
    if sb == 'AC':
        sb1 = 'Açaí'
    else:
        sb1 = 'Cupuaçu'

    tm = input('Qual o tamanho desejado? (P/M/G): ').upper()
    tamanhos = 'PMG'
    while tm not in tamanhos:
        print('Tamanho inválido, tente novamente.')
        tm = input('Qual o tamanho desejado? (P/M/G): ').upper()

# Verifica e atribui os valores de Açaí.

    if sb == 'AC' and tm == 'P':
        vlr = 11.00
        print(f'Você pediu um {sb1} tamanho {tm}: R${vlr}')
    elif sb == 'AC' and tm == 'M':
        vlr = 16.00
        print(f'Você pediu um {sb1} tamanho {tm}: R${vlr}')
    elif sb == 'AC' and tm == 'G':
        vlr = 20.00
        print(f'Você pediu um {sb1} tamanho {tm}: R${vlr}')

# Verifica e atribui os valores de Cupuaçu.

    if sb == 'CP' and tm == 'P':
        vlr = 9.00
        print(f'Você pediu um {sb1} tamanho {tm}: R${vlr}')
    elif sb == 'CP' and tm == 'M':
        vlr = 14.00
        print(f'Você pediu um {sb1} tamanho {tm}: R${vlr}')
    elif sb == 'CP' and tm == 'G':
        vlr = 18.00
        print(f'Você pediu um {sb1} tamanho {tm}: R${vlr}')
    vl += vlr

# Verifica se o cliente deseja pedir mais algum produto.

    pdd = input('Deseja mais alguma coisa? (S/N)').upper()
    pedidos = 'SN'
    while pdd not in pedidos:
        print('Opção inválida, tente novamente.')
        pdd = input('Deseja mais alguma coisa? (S/N)').upper()

    if pdd == 'N':
        print(f'Valor total a ser pago: R${vl}') # Programa será encerrado.
        break
    else: # Reinica o código para um novo pedido.
        continue

