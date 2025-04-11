# Exercicio 1

# n = int(input('Insira um valor: '))
# i = 0
# while i <=n:
#     print(i)
#     i +=1 

# Exercicio 2

# while True:
#     num1 = int(input('Digite um número: '))
#     num2 = int(input('Digite outro número: '))
#     print(f'{num1} + {num2} = {num1 + num2}')
#     escolha = input('Deseja realizar mais uma soma?\n[ S ]- Sim\n[ N ]- Não').strip().lower()[0]

#     while escolha not in 'sn':
#         print('Opção inválida. Tente novamente.')
#         escolha = input('Deseja realizar mais uma soma?\n[ S ]- Sim\n[ N ]- Não').strip().lower()[0]
        
#     if escolha == 'n':
#         break
    
# Exercicio 3

# senhacorreta = 1234

# while True:

#   senha = int(input('Insira sua senha: '))

#   if senha != senhacorreta:
#     print('“Senha Incorreta. Digite novamente a senha”.')
#     
# print('Senha Correta!!')

# Exercicio 4

# lista = []
# while True:
#     num = int(input('Digite um número: '))
#     lista.append(num)
        
#     if num == 0:
#         lista.pop()
#         break       


# print(f'O maior número é: {max(lista)}')
# print(f'O menor número é: {min(lista)}')


# Exercicio 5

# num = int(input('Insira um valor para saber a tabuada: '))
# cont = 1

# while cont <= 10:
#     print(f'{num} x {cont} = {cont * num}')
#     cont += 1


# Exercicio 6

# from math import prod
# pares = []
# impares = []
# while True:
#     num = int(input('Digite um número: '))
#     if num == -1:
#         break
#     if num % 2 == 0:
#         pares.append(num)
#     else:
#         impares.append(num)

# print(f'O produto dos números pares é: {prod(pares)}')
# print(f'O produto dos números ímpares é: {prod(impares)}')


# Exercicio 7


# cont = 1
# salarios = []
# filhos = []
# qtd = 0
# while cont < 4:
#     sal = float(input(f'Insira o salário do {cont}° funcionário: '))
#     filho = int(input(f'Insira quantos filhos o {cont}º funcionário tem: '))
#     cont += 1
#     salarios.append(sal)
#     filhos.append(filho)
#     if sal <= 1500:
#         qtd += 1
    
# print(f'A média dos salários é: R${sum(salarios)/(cont -1):.2f}')
# print(f'A média de filhos é: {sum(filhos)/(cont - 1)}')
# print(f'O maior salário é: R${max(salarios):.2f}')
# print(f'A porcentagem de funcionários com o salário até R$1500,00 é: {100*qtd/(cont - 1):.2f}%')


# Exercicio 8

chaves = 0
senhor_madruga = 0
kiko = 0
chiquinha = 0
nulo = 0
branco = 0
votos = 0

while True:
    voto = int(input("""Insira o seu voto: 
                     [ 1 ]- Chaves
                     [ 2 ]- Senhor Madruga
                     [ 3 ]- Kiko
                     [ 4 ]- Chiquinha
                     [ 5 ]- Nulo
                     [ 6 ]- Branco
                     [ 0 ]- Sair"""))
    while voto not in '1234560':
        print('Opção inválida, tente novamente.')
        break
    votos += 1
    if voto == 1:
        chaves += 1
    elif voto == 2:
        senhor_madruga += 1
    elif voto == 3:
        kiko += 1
    elif voto == 4:
        chiquinha += 1
    elif voto == 5:
        nulo += 1
    elif voto == 6:
        branco += 1
    elif voto == 0:
        break

print(f'O candidato Chaves teve {chaves} votos.')
print(f'O candidato Senhor Madruga teve {senhor_madruga} votos.')
print(f'O candidato Kiko teve {kiko} votos.')
print(f'O candidato Chiquinha teve {chiquinha} votos.')
print(f'A votação teve {nulo} votos nulos.')
print(f'A votação teve {branco} votos brancos.')
print(f'A porcentagem de votos nulos é: {nulo*100/votos}%')
print(f'A porcentagem de votos brancos é: {branco*100/votos}%')
