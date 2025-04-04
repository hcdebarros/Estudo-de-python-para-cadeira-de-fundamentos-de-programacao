
qtd_alunos = int(input('Insira a quantidade de alunos '))
soma_media = 0

for i in range(1,qtd_alunos + 1):
    qtd_notas = int(input(f'Digite a quantidade de notas do {i}º aluno '))
    nota = 0

    for a in range(1, qtd_notas + 1):
        notas = float(input(f'Insira a {a}ª nota do aluno '))
        nota += notas
        media = nota/qtd_notas

    print(f'A média do {i}º aluno é: {media:.2f}')
    soma_media += media
    media_turma = soma_media / qtd_alunos

print(f'A média geral da turma é: {media_turma:.2f}')