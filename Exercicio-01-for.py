
qtd_alunos = int(input('Insira a quantidade de alunos '))
notas_alunos = {}

for i in range(1,qtd_alunos + 1):
    qtd_notas = int(input(f'Digite a quantidade de notas do {i}º aluno '))
    notas_alunos[i] = [] 
    for a in range(1, qtd_notas + 1):
        notas = float(input(f'Insira a {a}ª nota do aluno '))
        notas_alunos[i].append(notas)
        
print("\nNotas dos alunos:")
for aluno, notas in notas_alunos.items():
    print(f"Aluno {aluno}: {notas}")