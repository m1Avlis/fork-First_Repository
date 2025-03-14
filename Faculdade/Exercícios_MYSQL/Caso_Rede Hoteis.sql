-- 1. Listar nome, cpf e telefone de todos os funcionarios.
select nome, cpf, telefone from funcionario;

-- 2. Listar nome, categoria, telefone e e-mail de um hotel, ordenando pelo nome.
select nome, categoria, telefone, email from hotel
order by nome;

-- 3. Listar todos os quartos disponíveis, incluindo numero de leitos, tipo e preço da diária.
select numLeitos, tipo, precoDiaria from quarto
where status = "Disponível";

-- 4. Listar todas as reservas de um hospede, incluindo identificação da reserva, data de entrada, data de saida e status da reserva,
-- hospede será identificado pelo CPF.

select cpf, id, dataReserva, dataSaida, status, count(id) from reserva
join hospede
on hospede.cpf = reserva.idHospede;


