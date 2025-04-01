# EXERCICIO 1


# valor = float(input("Digite o valor de sua compra."))
# while valor < 0:
#     print("Valor inválido.")
#     valor = float(input("Digite o valor novamente."))

# pag = int(input("Digite 1 para pagamento à vista e 2 para pagamento a prazo"))

# while pag != 1 and pag != 2:
#     print("Método de pagamento inválido")
#     pag = int(input("Digite 1 para pagamento à vista e 2 para pagamento a prazo"))

# if pag == 1:
#     if valor > 200:
#         taxa = 0.9
#         pagamento = valor*taxa
#     else:
#         taxa = 0.95
#         pagamento = valor*taxa
# else:
#     if valor <= 100:
#         taxa = 0
#         pagamento = valor
#     else:
#         taxa = 0.98
#         pagamento = valor*taxa

# desc = valor-pagamento

# print("O valor do desconto foi: R$", desc, "e o valor final da compra é: R$", pagamento)



# EXERCICIO 2

# nome = str(input("Digite o nome do aluno"))
# n1 = float(input("Insira a primeira nota do aluno"))
# n2 = float(input("Insira a segunda nota do aluno"))
# n3 = float(input("Insira a terceira nota do aluno"))

# media = (n1+n2+n3)/3

# if media >= 7.0:
#     print("Nome: ", nome, "Média = ", media, "Classificação = Aprovado")

# elif media >= 5 and media < 7:
#     print("Nome: ", nome, ", Média = ", media, ", Classificação = Recuperação")

# else:
#     print("Nome: ", nome, "Média = ", media, "Classificação = Reprovado")




# EXERCICIO 3




# salario = float(input("Insira seu salário"))

# if salario <= 20000:
#     imposto = 0
#     print("HAPPY NATION, LIVING IN A HAPPY NATION, imposto devido = R$", imposto)

# elif salario >20000 and salario < 50000:
#     imposto = salario *0.1
#     print("Xiiii..... Imposto = R$", imposto)
# else: 
#     imposto = salario * 0.2
#     print("Aqui acabou, imposto devido = R$", imposto)




# EXERCICIO 4


# renda = float(input("Insira sua renda"))
# pont = int(input("Insira sua pontuação de crédito"))

# if renda >= 2000 and pont >= 600:
#     print("Elegível")
# elif renda >= 1500 and pont >= 500:
#     print("Elegível, mas com restrições")
# else:
#     print("Não elegível")



# EXERCICIO 5

# dist = float(input("Insira a distância em quilômetros"))
# peso = float(input("Insira o peso da carga em quilogramas"))

# frete = 2*dist

# if peso <= 100:
#     taxa = 0.5*peso
# else:
#     taxa = 0.75*peso

# frete = frete+taxa

# print(f"Valor total = R${frete}")



# EXERCICIO 6



# valor = float(input("Digite o valor consumido (em reais)"))
# sats = int(input("Qual seu nível de satisfação? Digite 1 para Ótimo, 2 para bom e 3 para ruim"))

# match sats:

#     case 1:
#         fac = "Ótimo"
#         taxa = 0.15*valor
#         preço = valor*1.15

#     case 2:
#         fac = "Bom"
#         taxa = 0.1 * valor
#         preço = valor*1.1

#     case 3:
#         fac = "Ruim"
#         taxa = 0.05 * valor
#         preço = valor*1.05

#     case _:
#         print("Valor inválido")

# print(f"A gorjeta foi de {taxa} \n O valor total da conta foi de = {preço} \n O nível de satisfação foi: {fac}")



# EXERCICIO 7



# ladoa = float(input("Insira a medida do lado A"))
# ladob = float(input("Insira a medida do lado B"))
# ladoc = float(input("Insira a medida do lado C"))


# if ladoa + ladob <= ladoc:
#     print("Não é um triângulo")
#     exit()

# if ladoa + ladoc <= ladob:
#     print("Não é um triângulo")
#     exit()

# if ladob + ladoc <= ladoa:
#     print("Não é um triângulo")
#     exit()

# if ladoa == ladob == ladoc:
#     print("É um triângulo equilátero")

# elif ladoa == ladob or ladoa == ladoc or ladoc == ladob:
#     print("É um triângulo isoscéles")

# else:
#     print("É um triângulo escaleno")



# EXERCICIO 8


# ano_nasc = int(input("Digite o ano de seu nascimento"))

# idade = 2025 - ano_nasc

# if idade < 16:
#     print("Não pode votar")
# elif 16 <= idade <18 or idade >= 70:
#     print("Voto facultativo")
# else:
#     print("Voto obrigatório")



# EXERCICIO 9


# diaria = int(input("Insira quantas diárias você permaneceu"))
# tipo_quarto = int(input("Qual o quarto escolhido? Insira 1 para stardard, 2 para luxo e 3 para suíte"))

# while tipo_quarto != 1 and tipo_quarto != 2 and tipo_quarto != 3:
#     print("Opção inválida")
#     tipo_quarto = int(input("Qual o quarto escolhido? Insira 1 para stardard, 2 para luxo e 3 para suíte"))

# if tipo_quarto == 1:
#     valor = diaria * 10
# elif tipo_quarto == 2:
#     valor = diaria * 15
# else:
#     valor = diaria * 20

# print(f"Valor total da taxa = R${valor:.2f}")


# EXERCICIO 10


# valor = float(input("Insira o valor do imóvel"))
# tipo_imovel = int(input("Qual o tipo de residência? Insira 1 para residencial e 2 para comercial"))

# while tipo_imovel != 1 and tipo_imovel != 2:
#     print("Opção inválida, tente novamente.")
#     tipo_imovel = int(input("Qual o tipo de residência? Insira 1 para residencial e 2 para comercial"))

# if valor > 500000:
#     if tipo_imovel == 1:
#         preco = valor * 1.06
#     else:
#         preco = valor * 1.04
# else:
#     if tipo_imovel == 1:
#         preco = valor * 1.05
#     else:
#         preco = valor * 1.03

# preco = preco - valor
# print(f"A comissão do vendedor será de: R${preco:.2f}")



# EXERCICIO 11


# nome = str(input("Insira o nome do produto"))
# preco_unt = float(input("Insira o valor do produto"))
# qtd = int(input("Insira a quantidade adquirida"))

# valori = preco_unt * qtd

# if 10 <= qtd < 50:
#     valorf = valori * 0.95
# elif 50 <= qtd < 100:
#     valorf = valori * 0.9
# elif qtd >= 100:
#     valorf = valori * 0.85
# else: 
#     print()

# print(f"Nome do produto: {nome} \n Valor total da compra = R${valori:.2f} \n Desconto = R${valori - valorf:.2f} \n Valor após o desconto: R${valorf:.2f}")



# EXERCICIO 12


# tempo = int(input("Insira a quantos meses você está associado"))
# forma = int(input("Insira a forma de pagamento. Escolha 1 para dinheiro e 2 para cartão"))

# while forma != 1 and forma != 2:
#     print("Método de pagamento inválido")
#     forma = int(input("Insira a forma de pagamento. Escolha 1 para dinheiro e 2 para cartão"))

# if tempo >= 12:
#     if forma == 1:
#         desc = 0.85
#     else:
#         desc = 0.9
# else:
#     if forma == 1:
#         desc = 0.9
#     else: 
#         desc = 0.95

# valor = float(input("Insira o valor da mensalidade"))

# valor = valor * desc

# print(f"Valor total = R$ {valor:.2f}")



# EXERCICIO 13


tipo = str(input("Insira o tipo de produto: \n eletrônico \n vestuário \n livro"))
sub_tip = str(input("Insira o subtipo do produto"))
