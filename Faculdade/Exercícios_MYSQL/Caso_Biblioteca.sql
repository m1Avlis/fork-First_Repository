--CASO BIBLIOTECA

select * from Livros;
select * from Autores;
select * from Usuarios;
select * from Emprestimos;

select titulo, nome
from Livros inner join Autores
on Livros.id_autor = Autores.id_autor;

select titulo, nome
from Emprestimos
inner join Livros on Emprestimos.id_livro = Livros.id_livro
inner join Usuarios on Emprestimos.id_usuario = Usuarios.id_usuario;

select titulo
from Livros
inner join Emprestimos on Livros.id_livro = Emprestimos.id_livro
where data_devolucao is null;

select distinct ano_publicacao from Livros;

select titulo from Livros
limit 2;

select titulo, 
	case
		when ano_publicacao > 2000 then 'Moderno'
		else 'Antigo'
	end as 'Classificação'
from Livros;

SELECT titulo, ano_publicacao,
    CASE
        WHEN ano_publicacao < 2000 THEN 'Antigo'
        ELSE 'Moderno'
    END AS Classificacao
FROM Livros;

select nome from Autores
union select nome from Usuarios;

select nome from Autores
union all select nome from Usuarios;

select titulo, nome
from Livros inner join Autores
on Livros.id_autor = Autores.id_autor;

select t.titulo as 'Título Livro', n.nome as 'Nome Autor'
from Livros t inner join Autores n
on t.id_autor = n.id_autor;

select titulo, ano_publicacao from Livros
where ano_publicacao > 1950