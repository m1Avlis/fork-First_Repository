
select * from aluno;
select * from professor;
select * from disciplina;
select * from nota;

--Não consegui resolver
select * from aluno
where data_nascimento > 2005

select * from nota
where nota > 8.0

select nome_disciplina, nome_professor
from disciplina join professor on disciplina.id_professor = professor.id_professor

select a.nome_aluno as 'Nome Aluno', d.nome_disciplina as 'Disciplica', n.nota as 'Nota'
from aluno a join nota n on a.id_aluno = n.id_aluno
join disciplina d on d.id_disciplina = n.id_disciplina

select nome_disciplina
from disciplina join professor
on disciplina.id_professor = professor.id_professor
where especialidade = 'Matemática'

select a.nome_aluno as 'Nome Aluno', d.nome_disciplina as 'Disciplica', n.nota as 'Nota'
from aluno a join nota n on a.id_aluno = n.id_aluno
join disciplina d on d.id_disciplina = n.id_disciplina
where nota < 7.0

alter table nota
change nota nota_aluno decimal(10,2)

/*É obrigatório colocar o group by quando é inserida uma conta no select*/
select nome_aluno as Aluno, avg(nota_aluno) as Média
from nota join aluno
on nota.id_aluno = aluno.id_aluno
group by nome_aluno 
order by nome_aluno asc;

select nome_disciplina as Disciplica, count(id_nota) as 'Quantidade de Avaliações' 
from nota join disciplina
on nota.id_disciplina = disciplina.id_disciplina
group by nome_disciplina
order by nome_disciplina asc;

select distinct especialidade
from professor;

select nota_aluno 
from nota
limit 5;

select nome_aluno from aluno
union
select nome_professor from professor;

select nome_aluno as Aluno, nota_aluno as 'Nota Obtida'
from aluno join nota
on aluno.id_aluno = nota.id_aluno
