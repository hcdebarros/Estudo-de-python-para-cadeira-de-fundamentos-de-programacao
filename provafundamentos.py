# EXERCICIO 1


prod = 1
resto = impar = par = cont = 0

while True:
    num = int(input('Insira um número inteiro positivo: '))

    if num < 0:
        print('Valor não aceitável. Tente novamente.')
    else:
        break
for i in range(1,num+1):
    cont += i
    if i % 2 == 0:
        par += 1
    else:
        impar += 1

    prod *= i
print(f'Fatorial de {num} = {prod}')

while prod != 0:
    resto += prod % 10
    prod = prod //10

media = cont / num

print(f'A soma dos dígitos é: {resto}')
print(f'Pares: {par} número(s) e Ímpares: {impar} números()')
print(f'A  média dos dígitos é: {media:.2f}')


EXERCICIO 2


qtd = int(input('Insira a quantidade de produtos a serem cadastrados: '))
repor = ''
cont = 0

for i in range(qtd):
    nome = input(f'Insira o nome do {i+1}º produto: ')
    estoque = int(input(f'Insira a quantidade de produtos em estoque: '))
    valor = float(input('Insira o valor do produto: '))

    if estoque < 5:
        status = 'Alerta Crítico'
        cont += 1
        repor = repor + nome + '; '
    elif 5 <= estoque < 10:
        status = 'Necessidade de Reposição'
        cont += 1
        repor = repor + nome + '; '
    elif estoque > 50 and valor < 20:
        status = 'Produto Popular'
    else:
        status = 'Com estoque'
    
    print(f'Produto: {nome}\nStatus: {status}')

if cont == 0:
    print('Nenhum produto necessita de reposição.')
else:
    print(f'Produtos que precisam de reposição: {repor}')


EXERCICIO 3

campea = ''
notacampea = 0

qtd = int(input('Quantas quadrilhas irão participar? '))

for i in range(1,qtd+1):
    somanotas = 0
    nome = input(f'Insira o nome da {i}ª quadrilha: ')
    maior = 0
    menor = 10
    for j in range(1,6):
        nota = float(input(f'Insira a {j}ª nota: '))

        somanotas += nota
        if nota < menor:
            menor = nota
        if nota > maior:
            maior = nota
    
    somanotas = somanotas - maior - menor
    media = somanotas/3

    if media > notacampea:
        notacampea = media
        campea = nome
    
    print(f'A media da quadrilha {nome} foi: {media:.2f}')
print(f'A quadrilha campeã foi: {campea} com uma média de {notacampea:.2f}')