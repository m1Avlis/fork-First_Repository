from faker import Faker
import random

# Inicializar o gerador de dados fictícios
fake = Faker()

# Função para gerar dados para a tabela funcionario
def generate_funcionario_data(n):
    funcionarios = []
    for _ in range(n):
        nome = fake.name()
        cpf = fake.unique.random_number(digits=11)
        telefone = fake.phone_number()
        email = fake.email()
        senha = fake.password(length=8)
        login = fake.user_name()

        funcionarios.append(f"('{cpf}', '{nome}', '{telefone}', '{email}', '{senha}', '{login}')")
    return funcionarios

# Função para gerar dados para a tabela endereco
def generate_endereco_data(n):
    enderecos = []
    for i in range(n):
        rua = fake.street_name()
        numero = fake.building_number()
        complemento = fake.secondary_address() if random.choice([True, False]) else None
        bairro = fake.city()
        cep = fake.zipcode()
        cidade = fake.city()
        estado = fake.state_abbr()

        # Armazenando os dados do endereço em um dicionário
        enderecos.append({
            "id": i + 1,  # Atribuindo o id manualmente para usar nos outros inserts
            "rua": rua,
            "numero": numero,
            "complemento": complemento,
            "bairro": bairro,
            "cep": cep,
            "cidade": cidade,
            "estado": estado
        })
    return enderecos

# Função para gerar dados para a tabela pagamento
def generate_pagamento_data(n):
    pagamentos = []
    for _ in range(n):
        forma_pgto = random.choice(['cartão', 'pix', 'dinheiro'])
        data_pgto = fake.date_this_year()
        valor = round(random.uniform(100.00, 500.00), 2)
        status = random.choice(['pago', 'pendente'])

        pagamentos.append(f"('{forma_pgto}', '{data_pgto}', {valor}, '{status}')")
    return pagamentos

# Função para gerar dados para a tabela hotel
def generate_hotel_data(n, enderecos):
    hoteis = []
    for _ in range(n):
        nome = fake.company()
        categoria = random.choice(['1 Estrela', '2 Estrelas', '3 Estrelas', '4 Estrelas', '5 Estrelas'])
        telefone = fake.phone_number()
        email = fake.company_email()
        idendereco = random.choice(enderecos)["id"]  # Associando o id gerado do endereco

        hoteis.append(f"('{nome}', '{categoria}', '{telefone}', '{email}', {idendereco})")
    return hoteis

# Função para gerar dados para a tabela hospede
def generate_hospede_data(n, enderecos):
    hospedes = []
    for _ in range(n):
        nome = fake.name()
        cpf = fake.unique.random_number(digits=11)
        telefone = fake.phone_number()
        email = fake.email()
        idendereco = random.choice(enderecos)["id"]  # Associando o id gerado do endereco

        hospedes.append(f"('{cpf}', '{nome}', '{telefone}', '{email}', {idendereco})")
    return hospedes

# Função para gerar dados para a tabela reserva
def generate_reserva_data(n):
    reservas = []
    for i in range(n):
        data_reserva = fake.date_this_year()
        data_saida = fake.date_this_year()
        status = random.choice(['ativa', 'cancelada', 'concluída'])
        reservas.append({
            "id": i + 1,  # Gerar um id para cada reserva
            "data_reserva": data_reserva,
            "data_saida": data_saida,
            "status": status
        })
    return reservas

# Função para gerar dados para a tabela quarto
def generate_quarto_data(n):
    quartos = []
    for i in range(n):
        num_leitos = random.choice([1, 2, 3, 4])  # Gerando o número de leitos
        tipo = random.choice(['standard', 'luxo', 'suíte'])  # Gerando o tipo de quarto
        preco_diaria = round(random.uniform(100.00, 1000.00), 2)  # Gerando o preço da diária
        status = random.choice(['disponivel', 'bairro', 'manutenção'])  # Gerando o status do quarto

        # Adicionando os dados do quarto na lista de quartos
        quartos.append({
            "id": i + 1,  # Atribuindo id sequencial para cada quarto
            "numLeitos": num_leitos,
            "tipo": tipo,
            "precoDiaria": preco_diaria,
            "status": status
        })
    return quartos


# Função para gerar dados para a tabela reserva_quarto
def generate_reserva_quarto_data(num_reservas, reservas, quartos):
    reserva_quartos = []
    # Garantir que cada reserva tenha quartos diferentes
    for reserva in reservas[:num_reservas]:
        # Garantir que não haja repetições de idReserva e idQuarto
        quartos_reservados = random.sample(quartos, random.randint(1, 3))  # Cada reserva pode ter entre 1 e 3 quartos
        for quarto in quartos_reservados:
            reserva_quartos.append({
                "idReserva": reserva["id"],
                "idQuarto": quarto["id"]
            })
    return reserva_quartos


# Gerar dados para todas as tabelas
enderecos = generate_endereco_data(25)  # Gerar 10 endereços com IDs
funcionarios = generate_funcionario_data(50)  # Gerar 5 funcionários
pagamentos = generate_pagamento_data(100)  # Gerar 5 pagamentos
hoteis = generate_hotel_data(10, enderecos)  # Gerar 3 hotéis com endereços aleatórios
hospedes = generate_hospede_data(80, enderecos)  # Gerar 5 hóspedes com endereços aleatórios
reservas = generate_reserva_data(100)  # Gerar 10 reservas
quartos = generate_quarto_data(150)  # Gerar 10 reservas
reserva_quartos = generate_reserva_quarto_data(100, reservas, quartos)


# Exemplo de dados para a tabela quarto
#quartos = [
#    {"id": 1, "numLeitos": 2, "tipo": 'standard', "precoDiaria": 200.00, "status": 'disponivel'},
#    {"id": 2, "numLeitos": 4, "tipo": 'luxo', "precoDiaria": 500.00, "status": 'disponivel'},
#    {"id": 3, "numLeitos": 1, "tipo": 'suíte', "precoDiaria": 700.00, "status": 'disponivel'},
#]

# Gerar os inserts no formato SQL
def generate_sql_inserts():
    inserts = []

    # Tabela quarto
    inserts.append("INSERT INTO quarto (id, numLeitos, tipo, precoDiaria, status) VALUES")
    inserts.append(",\n".join([f"({quarto['id']}, {quarto['numLeitos']}, '{quarto['tipo']}', "
                              f"{quarto['precoDiaria']}, '{quarto['status']}')" for quarto in quartos]) + ";")

    # Tabela funcionario
    inserts.append("INSERT INTO funcionario (cpf, nome, telefone, email, senha, login) VALUES")
    inserts.append(",\n".join(generate_funcionario_data(25)) + ";")
    
    # Tabela endereco
    inserts.append("INSERT INTO endereco (id, rua, numero, complemento, bairro, cep, cidade, estado) VALUES")
    inserts.append(",\n".join([f"({endereco['id']}, '{endereco['rua']}', '{endereco['numero']}', "
                              f"'{endereco['complemento'] if endereco['complemento'] else 'NULL'}', "
                              f"'{endereco['bairro']}', '{endereco['cep']}', '{endereco['cidade']}', "
                              f"'{endereco['estado']}')" for endereco in enderecos]) + ";")
    
    # Tabela pagamento
    inserts.append("INSERT INTO pagamento (formaPgto, dataPgto, valorT, status) VALUES")
    inserts.append(",\n".join(generate_pagamento_data(100)) + ";")
    
    # Tabela hotel
    inserts.append("INSERT INTO hotel (nome, categoria, telefone, email, idendereco) VALUES")
    inserts.append(",\n".join(generate_hotel_data(10, enderecos)) + ";")
    
    # Tabela hospede
    inserts.append("INSERT INTO hospede (cpf, nome, telefone, email, idendereco) VALUES")
    inserts.append(",\n".join(generate_hospede_data(80, enderecos)) + ";")
    
    # Tabela reserva
    inserts.append("INSERT INTO reserva (dataReserva, dataSaida, status) VALUES")
    inserts.append(",\n".join([f"('{reserva['data_reserva']}', '{reserva['data_saida']}', '{reserva['status']}')"
                              for reserva in reservas]) + ";")
    
    # Gerar a inserção para a tabela reserva_quarto
    inserts.append("INSERT INTO reserva_quarto (idReserva, idQuarto) VALUES")
    inserts.append(",\n".join([f"({reserva_quarto['idReserva']}, {reserva_quarto['idQuarto']})" 
                              for reserva_quarto in reserva_quartos]) + ";")

    
    return "\n\n".join(inserts)

# Gerar o SQL para inserção
sql = generate_sql_inserts()

# Exibir o SQL gerado
print(sql)
