# EXERCICIO 1

# qtd_alunos = int(input('Insira a quantidade de alunos '))
# soma_media = 0

# for i in range(1,qtd_alunos + 1):
#     qtd_notas = int(input(f'Digite a quantidade de notas do {i}º aluno '))
#     nota = 0

#     for a in range(1, qtd_notas + 1):
#         notas = float(input(f'Insira a {a}ª nota do aluno '))
#         nota += notas
#         media = nota/qtd_notas

#     print(f'A média do {i}º aluno é: {media:.2f}')
#     soma_media += media
#     media_turma = soma_media / qtd_alunos

# print(f'A média geral da turma é: {media_turma:.2f}')

# EXERCICIO 2

# from math import prod as pr
# from time import sleep
# prod = 1
# while True:
#     num = int(input('Digite um número inteiro positivo: '))

#     if num > 0:
#         for i in range(num,0,-1):
#             prod *= i
#         break
#     else: 
#         print('O número inserido é inválido. ')
#         print('Tente novamente...')
#         sleep(1)
# print(f'{num}! = {prod}')

# soma = sum(int(digito) for digito in str(prod))
# print(f'A soma dos digitos de {num}! = {soma}')

# prod_dig = pr(int(digito) for digito in str(prod))
# print(f'O produto dos algarismos de {num}! = {prod_dig}')

# media_dig = soma / len(str(prod))
# print(f'A média dos dígitos de {num}! = {media_dig}')

# pares = sum(1 for digito in str(prod) if int(digito) % 2 == 0)
# impares = sum(1 for digito in str(prod) if int(digito) % 2 != 0)

# print(f'{num}! tem {pares} números pares nos dígitos do seu resultado')
# print(f'{num}! tem {impares} números ímpares nos dígitos do seu resultado')


# EXERCICIO 3

# from random import randint

# contador1 = 0
# contador2 = 0
# contador3 = 0
# contador4 = 0
# contador5 = 0
# contador6 = 0
# soma1 = 0
# soma2 = 0

# while True:
#     qtd_lancamentos = int(input('Insira a quantidade de lançamentos do dado'))

#     if qtd_lancamentos > 0:
#         for i in range(qtd_lancamentos,0,-1):
#             cont = randint(1,6)
#             if cont == 1:
#                 contador1 += 1
#             elif cont == 2:
#                 contador2 += 1
#             elif cont == 3:
#                 contador3 += 1
#             elif cont == 4:
#                 contador4 += 1
#             elif cont == 5:
#                 contador5 += 1
#             else:
#                 contador6 += 1
#             soma1 += cont
#         for i in range(qtd_lancamentos,0,-1):
#             cont2 = randint(1,6)
#             if cont2 == 1:
#                 contador1 += 1
#             elif cont2 == 2:
#                 contador2 += 1
#             elif cont2 == 3:
#                 contador3 += 1
#             elif cont2 == 4:
#                 contador4 += 1
#             elif cont2 == 5:
#                 contador5 += 1
#             else:
#                 contador6 += 1
#             soma2 += cont2
#         break
#     else: 
#         print('O número inserido é inválido. ')
#         print('Tente novamente...')
#         sleep(1)

# soma3 = soma1 + soma2

# porc1 = (contador1*100) / qtd_lancamentos
# porc2 = (contador2*100) / qtd_lancamentos
# porc3 = (contador3*100) / qtd_lancamentos
# porc4 = (contador4*100) / qtd_lancamentos
# porc5 = (contador5*100) / qtd_lancamentos
# porc6 = (contador6*100) / qtd_lancamentos

# print(f'Face 1: {contador1} ({porc1:.2f}%)')
# print(f'Face 2: {contador2} ({porc2:.2f}%)')
# print(f'Face 3: {contador3} ({porc3:.2f}%)')
# print(f'Face 4: {contador4} ({porc4:.2f}%)')
# print(f'Face 5: {contador5} ({porc5:.2f}%)')
# print(f'Face 6: {contador6} ({porc6:.2f}%)')
# print(f'A soma dos resultados = {soma3}')

# EXERCICIO 4

