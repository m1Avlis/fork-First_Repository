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

#Questão 3

print('Olá! Seja bem vindo a Copiadora do Mario Pereira.')

# Salva o serviço que o usuário deseja.
def escolha_servico(servicos):
    while True:
        global servico
        servico = input('Escolha o serviço desejado: \n'
        'DIG - Digitalização \n'
        'ICO - Impressão Colorida \n'
        'IPB - Impressão Preto e Branco \n'
        'FOT - Fotocópia \n'
        '>> ').upper()

        if servico in servicos:
            if servico == 'DIG':
                servico = 1.10
                break
            elif servico == 'ICO':
                servico = 1
                break
            elif servico == 'IPB':
                servico = 0.40
                break
            else:
                servico = 0.20
                break
        else:
            print('Opção inválida, escolha o tipo de serviço novamente.')

# Salva o número de páginas indicado pelo usuário.
def num_pagina():
    while True:
        global pagina
        try:
            pagina = int(input('Insira o número de páginas: '))
            if pagina > 20000:
                print('Não aceitamos tantas páginas de uma vez')
            else:
                break
        except ValueError:
            print('Por favor digite apenas números.')

# Pergunta ao usuário se ele deseja algum serviço extra.           
def servico_extra():
    while True:
        global extra
        try:
            extra = int(input('Deseja adicionar algum serviço? \n'
            '1 - Encadernação Simples - R$ 15,00 \n'
            '2 - Encadernação Capa Dura - R$ R$ 40,00 \n'
            '0 - Não desejo mais nada.'))

            if extra > 2:
                print('Opção inválida, digite novamente.')
            elif extra == 1:
                extra = 15
                break
            elif extra == 2:
                extra = 40
                break
            else:
                break

        except ValueError:
            print('Opção inválida, digite novamente.')


escolha_servico(['DIG','ICO','IPB','FOT'])
num_pagina()
servico_extra()

total = (servico * pagina) + extra
print(f'Valor Total: R$ {total:.2f}')



# Questão 4
# %%

print('Olá! Seja bem vindo a Livraria do Mario Pereira.')
print('-'*46)
print('-'*15 + ' MENU PRINCIPAL ' +'-'*15)

lista_livro = []
id_global = 0

