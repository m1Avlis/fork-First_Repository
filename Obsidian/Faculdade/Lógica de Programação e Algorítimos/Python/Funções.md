
O [[Python]] carrega nativamente uma gama de funções, com funcionalidades variadas. No entanto, é possível criar novas funções no python.
Criar funções é uma maneira de modularizar e separar os códigos em blocos que executam uma determinada ação.

A definição de um função segue o padrão das funções nativas do python, iniciando-se pela expressão [def], seguido pelo nome da função e logo após abre-se parêntesis, finalizando com dois pontos. 

Dentro dos parêntesis são passados os parâmetros da função, e logo abaixo, obrigatoriamente indentados, devem estar as instruções da referida função.

Vejamos a seguir:
```python
def soma(a,b):
	return sum(a,b)
```

Um função pode não ter nenhum argumento, basta que entre os parêntesis não seja inserida nenhuma instrução. Por outro lado, caso seja inserido algum parâmetro para a função, no momento em que ela for invocada, será obrigatório a entrada dos parâmetros declarados.

É possível também tornar um argumento opcional, atribuindo um valor pra ele no ato da declaração da função. Exemplo:
```python
def soma(a,b=0):
	return sum(a,b)

```
Neste caso, se o usuário não passar o valor de [b], o python utilizará o valor default atribuído no ato da declaração da função.

Caso seja necessário inserir novos parâmetros em uma função, será preciso reescrever as linhas de comando. Para evitar esse retrabalho, pode-se utilizar o parâmetro [args].
### Args

O parâmetro [args] é uma variável convencionada com esse nome, que tem como objetivo carregar um ou mais valores. Na verdade, a variável pode ter qualquer nome, desde que seja precedida por um asterístico, e que seja declarada após os parâmetros obrigatórios.
Vejamos a seguir.
```python

def soma(a, b, *args):
	return (a + b + *args)

soma(10, 20, 30, 40, 50)

#Saída Terminal: 150
```

Podemos observar que, na chamada da função soma, foram passados 5 valores, e ainda assim foi possível realizar o cálculo, isto porque os valores inseridos a mais foram armazenados no parâmetro [args] em forma de [[|lista]].
### Kwargs

Além do [args], existe um outro parâmetro especial que pode ser inserido em um função. O parâmetro [kwargs], esse parâmetro especial tem a capacidade de se comportar como um [[|dicionário]], ou seja, chave/valor.

Assim como o [args], o [kwargs] deve ser declarado por último em uma função, e tem como exigência de sintáxe, ser precedido de **dois** asterísticos.
```python

def calc_imposto(preco, tx_base, **kwargs):
	imposto = preco * tx_base

	for i in kwargs:
		print(i, kwargs[i])
		imposto += preco * tx_base
	return imposto

calc_imposto(100, 0.03, municipio=0.08, estadual=0.10, nacional=0.009)

```

Observa-se que, na chamada da função [calc_imposto] foram passados três valores além dos parâmetros obrigatórios, e que esses valores estão em formato de um dicionário, ou seja, uma chave sucedida de um valor. Exemplo, o imposto de [municipio] recebe [0.08].

Podemos ainda representar o mesmo código de forma mais organizada e eficiente, criando de fato o dicionário antes de chamar a função. Vejamos a seguir:
```python
def calc_imposto(preco, tx_base, **kwargs):
	imposto = preco * tx_base

	for i in kwargs:
		print(i, kwargs[i])
		imposto += preco * tx_base
	return imposto

impostos = {
	"municipio":0.08, 
	"estadual":0.10, 
	"nacional":0.009
}
calc_imposto(100, 0.03, **impostos)
```

Note que, quando chamo o dicionário [impostos] dentro dos parâmetros da função [calc_imposto], ele está precedido de dois asterísticos, pois desta forma o [[|python]] irá entender que se trata de um [kwargs] e irá acessar todos os valores presentes nesse dicionário.