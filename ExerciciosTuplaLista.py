# EXERCICIO 1
# Crie uma tupla preenchida com os 10 números. Depois mostre:
# a) Apenas os 5 primeiros números.
# b) Em ordem crescente.


# tupla= (10,5,8,5,2,1,9,4,11,25)

# print(tupla[0:5])
# print(sorted(tupla[0:5]))



# EXERCICIO 2 
# Crie um programa que leia quatro valores pelo teclado e armazenar em um tupla.
# No final mostre:
# a) Quantas vezes apareceu o número 5.
# b) Em que posição foi digitado o primeiro valor 3.
# c) Quais números digitados são pares.


# cont = 0
# num1 = int(input('Digite o primeiro número: '))
# num2 = int(input('Digite o segundo número: '))
# num3 = int(input('Digite o terceiro número: '))
# num4 = int(input('Digite o quarto número: '))
# tupla=(num1,num2,num3,num4)

# contador_cinco = tupla.count(5)

# if 3 in tupla:
#     indice_tres = tupla.index(3)
#     print(f'O três aparece na posição {indice_tres}')
# else:
#     print('O 3 não aparece em nenhuma posição')

# print(f'Tiveram {contador_cinco} número(s) 5')
# print('Números pares: ', end = '')
# for i in tupla:
#     if i % 2 == 0:
#         print(i, end = ' ')

# EXERCICIO 3
# Crie um programa que tenha uma tupla com várias palavras. Mostre para cada
# palavra, quais são as suas vogais.


# tupla = ('Amargo', 'Doce', 'Salgado', 'Azedo', 'Picante')

# for i in tupla:
#     lista = []
#     for a in i.lower():
#         if a in 'aeiou':
#             lista.append(a)
            
#     print(f'{i}, suas vogais: {lista}')


# EXERCICIO 4
# Crie um programa que tenha uma tupla totalmente preenchida com uma
# contagem por extenso de zero a vinte. O programa deverá ler um número pelo
# teclado (entrar com 0 a 20 ) e mostrá-lo por extenso.

# tupla_extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
#     "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")


# num = int(input('Digite un número entre 0 e 20: '))

# print(tupla_extenso[num])


# EXERCICIO 5
# Crie um programa que tenha uma tupla única com nomes de produtos e seus
# respectivos preços na sequencia. No final, mostre uma listagem de preços
# organizando os dados em forma tabular.

