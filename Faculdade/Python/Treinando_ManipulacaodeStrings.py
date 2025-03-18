"""
dados = {}

while True:
    frase = input('Digite as frases:')
    if frase == "":
        break
    if frase not in dados:
        dados[frase] = 1
    else:
        dados[frase] += 1

for i, j in dados.items():
    print(i, "->", j)

print('1 - Consultar por ID\n2 - Consultar por Nome\n3 - Consultar por Autor\n4 - Consultar por Editora\n5 - Voltar\nEscolha uma opção: ')
"""
print('-'*46)
print('-'*11,' MENU CADASTRAR LIVRO ','-'*11)