
É uma função do [[Python]] que permite fazer verificações. A tradução de IF é SE, ou seja, o programa será executado SE a condição for verdadeira.

O IF segue a seguinte estrutura:

```python
if (condição):
	print('resultado')
```
Abrimos a função digitando IF em letras minúscula, em seguida o parêntesis é opcional, sendo possível colocar a condição dentro ou fora de parêntesis. Nas condições são usados os operadores abaixo:

‘>’-> Maior
‘<’   -> Menor
‘>=’  -> Maior ou Igual
‘<=’  -> Menor ou Igual
‘==’  -> Igual
‘!=’  -> Diferente
and -> e
or  -> ou
True -> Verdadeiro
False -> Falso

Ao final no IF, após a condição é obrigatório encerrar com dois ponto (:). Podemos observar na demonstração da estrutura que a linha abaixo da instrução do IF está endentada (tabulada), essa é mais uma obrigatoriedade da função, tudo que está dentro da endentação deverá ser executado caso a condição for atendida.

O IF permite ainda mais algumas variações, sendo possível utilizar o else ou elif. Sendo o else utilizado para executar uma determinada ação caso a condição for falsa. Já o elif, permite adicionar uma segunda condição ao if. Segue abaixo uma demonstração do uso de else e elif:

```python
if 2 + 2 == 4:
	print('Igual')
elif 2 + 2 != 4:
	print('Diferente')
else:
	print('Nenhum dos dois')
```