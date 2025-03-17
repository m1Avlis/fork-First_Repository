
De maneira simplista, tuplas são assim como as [[Listas]], um conjunto de elementos, porém, tem a característica de serem [imutáveis].

Elas podem ser declaradas de duas formas, entre parêntesis, ou fora de parêntesis. Exemplo:
```python
tupla_1 = (2, "Mario", 29, 1996, "Casado")
tupla_2 = 2, "Mario", 29, 1996, "Casado"
```
As duas maneiras estão corretas.

Conforme demonstrado, é possível adicionar valores de todos os tipos dentro de uma tupla, inclusive listas e dicionários.

_Uma característica interessante é que, apesar das tuplas serem imutáveis, se houverem  objetos mutáveis dentro dela, como listas ou dicionários, é possível adicionar elementos dentro deles._ Exemplo:
```python

dados_mario = (29, "Casado", "Rio de Janeiro", ["João", "Laura"])
print(dados_mario)
# Saída Console: (29, 'Casado', 'Rio de Janeiro', ['João', 'Laura'])

dados_mario[-1].append("Beatriz")
print(dados_mario)
# Saída Console: (29, 'Casado', 'Rio de Janeiro', ['João', 'Laura', 'Beatriz'])
```

