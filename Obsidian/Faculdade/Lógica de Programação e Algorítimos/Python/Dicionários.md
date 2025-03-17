
Dicionários nada mais são do que conjuntos de pares [chave/valor].

As chaves podem ser dos tipos **string, int e float**, embora não seja aconselhado utilizar o tipo float como uma chave.

Os valores podem ser de qualquer tipo dentro do [[Python]], inclusive listas e até mesmo outros dicionários.

A ordem no dicionário importa, sempre iniciando com a chave e depois o valor. Exemplo:

```python
dicionario = {"chave": "valor"}
```

No dicionário, diferente das [[Listas]], não acessamos os valores através de índices, e sim através das chaves, ou melhor, do nome das chaves. Exemplo:

```python
dados_mario = {"nome": "Mario", "sobrenome": "Pereira", "idade": 29}

print(dados_mario["nome"])
```
Saída Terminal: Mario

### Métodos

Os dicionários também possuem métodos, abaixo seguem alguns deles:

[.Keys()] - Retorna as chaves de um dicionário.
[.Values()] - Retorna os valores de um dicionários.
[.Items()] - Retorna todos as chaves e seus respectivos valores de um dicionário em formato de [[Tuplas]].

### Prós

A utilização do modelo de estrutura de um dicionário, pode melhorar muito o desempenho do programa, e deixar o código mais bonito e legível.

Como exemplo, vamos fazer um exercício:

1. Crie um programa que, solicita uma fruta ao usuário e retorna o valor respectivo da fruta.

| FRUTA   | VALOR   |
| ------- | ------- |
| Maçã    | R$ 1,50 |
| Pera    | R$ 1,25 |
| Goiaba  | R$ 2,15 |
| Abacaxi | R$ 3,20 |
| Jaca    | R$ 5,80 |
| Laranja | R$ 0,65 |
| Limão   | R$ 1,25 |
| Banana  | R$ 2,75 |
| Uva     | R$ 1,90 |
	Exemplo 1: Sem usar o dicionário.

```python
fruta = input('Entre com a fruta desejada: ')
 

if fruta == 'Maçã':
print('R$ 1,50')
elif fruta == 'Pera':
print('R$ 1,25')
elif fruta == 'Goiaba':
print('R$ 2,15')
elif fruta == 'Abacaxi':
print('R$ 3,20')
elif fruta == 'Jaca':
print('R$ 5,80')
elif fruta == 'Laranja':
print('R$ 0,65')
elif fruta == 'Limão':
print('R$ 1,25')
elif fruta == 'Banana':
print('R$ 2,75')
elif fruta == 'Uva':
print('R$ 1,90')
else:
print('Digite uma fruta válida.')
```

	Exemplo 2: Usando o dicionário.
```python
fruta = input('Entre com a fruta desejada: ')

frutas = {
	'Maçã': 'R$ 1,50',
	'Pera': 'R$ 1,25',
	'Goiaba': 'R$ 2,15',
	'Abacaxi': 'R$ 3,20',
	'Jaca': 'R$ 5,80',
	'Laranja': 'R$ 0,65',
	'Limão': 'R$ 1,25',
	'Banana': 'R$ 2,75',
	'Uva': 'R$ 1,90'
}
if fruta in frutas:
	print('O preço da fruta é: ',frutas[fruta])
else:
	print('Digite um valor válido.')
```

Como podemos observar nas demonstrações acima, a utilização dos dicionários não só deixam o código mais limpo e organizado, como também melhora seu desempenho, pois não será necessário realizar várias comparações para encontrar a fruta digitada pelo usuário. Por outro lado, o programa acessa diretamente um elemento dentro do dicionário.


