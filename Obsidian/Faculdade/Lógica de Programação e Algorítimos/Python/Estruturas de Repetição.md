
As estruturas de repetição ou laços de repetição, são funções que permitem que uma mesma linha de código seja executada diversas vezes, a depender de uma condição especificada. No [[Python]], temos diversas funções para executar um laço de repetição.


# WHILE (Enquanto)

While é uma estrutura de repetição que, vai executar um determinada ação, *enquanto* uma condição for verdadeira.

Exemplo:
```python
x = 1
while x <= 5:
	print(x)
	x = x + 1
```

Explicando a estrutura:

| while  |    x     |    <=    |    5     |        :         |
| :----: | :------: | :------: | :------: | :--------------: |
| função | iterador | operador | condição | fim da estrutura |

O iterador mencionado acima, também é conhecido como variável de controle. São elas que vão carregar o valor para atender a condição.

As variáveis de controle podem ser de dois tipos:

- Contadoras: Acrescentam valores constantes em uma variável.
- Acumuladoras: Acumulam totais, como um somatório.

#### Exemplo de variável contadora:

```python
inicial = int(input('Qual valor deseja inicar a contagem?'))
final = int(input('Qual valor deseja finalizar a contagem?'))

x = inicial
while x <= final:
	if x % 2 == 0:
		print(x)
	x = x + 1
```

#### Exemplo de variável acumuladora:

```python
soma = 0
cont = 1

while (cont <= 5):
    x = float(input(f'Digite a {cont}ª nota:'))
    soma = soma + x
    cont = cont + 1
media = soma / 5
print(f'Média final: {media}')
```


### Operadores especiais de atribuição

São formas simplificadas de estruturar as variáveis dentro dos laços de repetição, e seguindo as boas práticas de escrita em python, os códigos devem ser escritos dessa maneira. Abaixo segue uma tabela de conversão:


Operador - Exemplo - Equivalente

‘+= | x += 1 | x = x + 1’
‘-= | x -= 1 | x = x - 1’
‘*= | x *= 2 | x = x * 2’
‘/= | x /= 2 | x = x / 2’
‘**= |x **= 2 | x = x ** 2’
‘//= | x //= 4 | x = x // 4’


Exemplo do uso dos operadores especiais

```python
soma = 0
cont = 1

while (cont <= 5):
    x = float(input(f'Digite a {cont}ª nota:'))
    soma += x #Equivale a soma = soma + 1
    cont += 1 #Equivale a cont = cont + 1
media = soma / 5
print(f'Média final: {media}')
```


### Validação de dados de entrada

Utilizando o While, é possível prender forçar o usuário a digitar apenas valores que atendam as condições solicitadas no [[input]].

Exemplo:

```python
x = int(input('Digite um número maior do que zero'))
while x <= 0:
	x = int(input('Digite um número maior do que zero'))
print (f'Você digitou {x}. Encerrando o programa...')
```

No exemplo acima podemos ver que, o usuário só consegue prosseguir quando não atende a condição do while, ou seja, quando digita um valor maior do que zero. Dessa forma, o usuário será obrigado a atender ao que está sendo solicitado no input.


### Instruções que podem ser utilizadas no While


#### Break

Essa instrução é utilizada para interromper abruptamente a estrutura de repetição, caso uma condição seja atendida.

Exemplo:

```python
print('Digite uma mensagem que iriei repetir para você!')
print('Para encerrar escreva "sair"')
while True:
	texto = input('')
	print(texto)
	if texto == 'sair':
		break
print('Encerrando o programa...')
```

Perceba que no exemplo acima, a condição é True, que é um operador booleano e faz com que o laço continue sendo executado, criando um loop infinito.
*Esse tipo de condição só está sendo especificada porque nesse exemplo podemos utilizar o Break para sair da estrutura de repetição.*


#### Continue

Essa instrução é utilizada para retornar o laço de repetição para o início a qualquer momento, independente do estado da variável de controle da condicional do laço.

Exemplo:

```python
while True:
	nome = input('Qual o seu nome?')
	if nome != 'Lenhadorzinho':
		continue
	senha = input('Qual a senha?')
	if senha ==  'UnInTer':
		break
print('Acesso concedido')
```


#### Valores Truthy e Falsey


Dados não booleanos (True e False), também podem ser entendidos como verdadeiro e falso pelo Python.

- Falsey/False
Número zero (int ou float) e string vazia. Nesses dois casos o python entende como falso.

- Truthy/True
Qualquer outro dado, diferente dos especificados acima, o python considera como verdadeiro.

Exemplo:

```python
nome = ''

while not nome:
	nome = input('Digite seu nome')
valor = int(input('Digite um número qualquer'))
if valor:
	print('Você digitou um número diferente de zero.')
else:
	print('Você digitou zero.')
```

Note que, no exemplo acima, a variável 'nome' começa vazia, e dentro do while  ela seria lida como *falsey*, e pularia a estrutura de repetição, por isso o 'not' transforma a variável em *truthy* (verdadeira), fazendo o loop da estrutura de repetição. Dessa maneira, a condição só é atendida quando o usuário digita alguma coisa. 

Da mesma forma, no if não é explicitada nenhuma condição, apenas a variável valor, que contém o número digitado pelo usuário. Como o zero é lido como falso pelo python, o if só será atendido quando o usuário digitar uma valor maior do que zero.

# FOR (Para)

O **For** é mais uma estrutura de repetição disponível no Python, da mesma maneira que o **while**, executará um determinado comando enquanto uma condição for atendida.

Sua principal diferença do **while**, é que geralmente é utilizado quando se tem em mente quantas vezes o loop deverá ser executado.

Estrutura do **For**

```python
for i in range(6):
	print(i)

```

Explicando a estrutura:

|  for   |    i     |    in    |   range   |      (      |        6        |      )      |  :  |
| :----: | :------: | :------: | :-------: | :---------: | :-------------: | :---------: | :-: |
| função | iterador | operador | intervalo | obrigatório | Num. repetições | obrigatório | Fim |

É possível na estrutura do for, escolher por onde ele vai começar a execução, até onde ele vai executar e o passo da execução. Todas essas seleções são passadas dentro dos parêntesis.

|  (  |       0        |          6          |       1       |  )  |
| :-: | :------------: | :-----------------: | :-----------: | :-: |
|     | Número inicial | Quantidade de loops | Passo do loop |     |
Onde:

	Número Inical: É o número que irá inicar a contagem.
	Quantidade de Loops: É até quando o loop será executado.
	Passo do Loop: É de quantos em quantos números deve ser executado. Poderia ser por exemplo de 2 em 2, ou mais.


### Varredura de Strings

O **for** é uma ótima ferramenta para fazer varredura de strings, sendo possível ler e executar outras funções a partir do seu resultado.

Exemplo:
```python
frase = 'Lógica de Programação e Algorítmos'
for i in range(0, len{frase}, 1):
	print(frase[i], end="")

```

Nesse exemplo, o **for** é utilizado para passar por cada carácter contido na variável frase, e printar na tela cada string.

Utilizando o for para calcular a média dos pares dos número de 1 a 100:
```python
soma = 0
qtd = 0
for i in range(1,100)
	if i % 2 == 0:
		soma += i
		qtd += i
media = soma / qtd
print(f'A média dos pares de 1 até 100 é: {media}')

```

Exemplo de estruturas de repetição aninhadas:
```python
num = 1
while num <= 10:
	print(f'Tábuada do {num}:')
	print("") # Apenas para adicionar uma linha de espaço.
	for i in range(1,11):
		print(f'{num}x{i}={num*i}')
	num += 1
	print("") # Apenas para adicionar uma linha de espaço.
```