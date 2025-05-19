# Questão 04: Encontrando o Aluno com a Maior Média
# • Contexto: Você tem um dicionário que armazena o nome de alunos como chaves
# e uma lista de suas notas em diferentes disciplinas como valores. Você deseja
# identificar o aluno com a maior média geral. Adicionar 20 alunos e suas
# respectivas notas.
# • Exemplo de Saída: O aluno com a maior média é Ana com média 9.10

nome_media = ''
maior_media = 0

alunos = {
    'Alice': [8.5, 7.0, 9.0, 6.5],
    'Bruno': [6.0, 5.5, 7.0, 8.0],
    'Carla': [9.5, 9.0, 8.5, 10.0],
    'Daniel': [7.0, 6.5, 6.0, 7.5],
    'Eduarda': [10.0, 9.5, 10.0, 9.0],
    'Felipe': [4.5, 6.0, 5.5, 6.5],
    'Gabriela': [8.0, 8.5, 9.0, 8.0],
    'Henrique': [5.0, 6.5, 5.5, 6.0],
    'Isabela': [7.5, 8.0, 7.0, 7.5],
    'João': [6.0, 6.0, 5.5, 6.5],
    'Karla': [9.0, 8.5, 9.5, 8.0],
    'Lucas': [7.0, 6.0, 6.5, 7.0],
    'Marina': [10.0, 9.5, 9.5, 9.0],
    'Nathan': [5.5, 5.0, 6.0, 5.5],
    'Olívia': [8.0, 7.5, 8.5, 9.0],
    'Pedro': [6.5, 7.0, 6.0, 6.5],
    'Quésia': [9.5, 9.0, 10.0, 9.5],
    'Rafael': [7.0, 6.5, 7.5, 6.0],
    'Sara': [8.5, 9.0, 8.0, 9.0],
    'Tiago': [6.0, 5.5, 6.5, 6.0]
}

for nome, notas in alunos.items():
    media = sum(notas)/len(notas)
    if media >= maior_media:
        maior_media = media
        nome_media = nome

print(f'O(A) aluno(a) com a maior média é {nome_media} com média {maior_media}')
