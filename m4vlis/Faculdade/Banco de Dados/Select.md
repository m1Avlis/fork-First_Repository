O select é o comando mais utilizado no dia a dia de um profissional da área de dados. O domínio desse comando está altamente atrelado ao sucesso na carreira.

É um comando que permite realizar consultas nas tabelas de um [[Banco de Dados]], segue abaixo a demostração do select na sua forma mais básica:

```mysql
select * from tabela
```

No exemplo acima, podemos ver a utilização do comando select, nesse caso "*" quer dizer que queremos todas as colunas da tabela, logo após vem o 'from' que é seguido da tabela a qual queremos realizar a consulta.

No dia a dia, dificilmente será utilizado o '*', sendo substituído pelo nome da coluna que desejamos obter como resposta. Exemplo:

```mysql
select nome_aluno from Alunos
```


### Subqueries

Subconsultas ou subqueries são linhas de comando **select** aninhadas dentro de outros comandos (select, insert, update ou delete), inclusive dentro de outras subqueries.

#### Regras das Subqueries:

1. O select de uma subquery sempre será declarado entre parêntesis;
2. Pode estar inserida em uma lista de select, ou seja, um encadeamento de selects, utilizando as cláusulas where ou having da query externa;
3. Pode estar inserida na lista de select para ampliar o conjunto de valores que serão analisados através do filtro where ou having (query externa);
4. Em aninhamentos normais, a subquery mais interna possui precedênciana execução, ou seja, será executada primeiro.


#### Casos de aplicação das Subqueries:

1. Como um filtro, sendo declarada dentro de uma cláusula where.
2. Atuando como uma nova coluna, sendo declarada dentro de um select.
3. Funcionando como uma nova tabela, sendo declarada dentro da cláusula from ou do comando join.

Exemplo:

_Uma empresa deseja descobrir todos os clientes que residem na cidade
de Curitiba. Ao consultarmos a tabela Cliente, percebemos que tem apenas o ‘id’ da cidade (chave estrangeira). 

```sql
select nome, cidadeId from cliente
where cidadeId =
(select id from cidade where nomecidade = ‘Curitiba’);
```


[^1]: **Nota**
	
	Cabe ressaltar que o uso do símbolo de igualdade (=) é limitado, e permite apenas a comparação de um único valor. Caso necessite comparar com mais valores, deve ser utilizado o operador **in**.
	Exemplo:

```sql
select nome, cidadeId from cliente where cidadeId
in (select id from cidade where nomecidade = ‘Curitiba’ or nomecidade = 'Rio de Janeiro');
```
