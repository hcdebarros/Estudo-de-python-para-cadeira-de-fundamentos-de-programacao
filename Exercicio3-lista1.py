# Questão 03: Filtrando Produtos por Faixa de Preço
# • Contexto: Elabore uma lista de dicionários, onde cada dicionário representa um
# produto com seu nome e preço. O usuário deseja filtrar essa lista para obter apenas
# os produtos dentro de uma determinada faixa de preço. O usuário irá entrar com
# o valor mínimo e o valor máximo para realizar a pesquisa de melhores preços que
# se encaixam no orçamento.
# • Exemplo de Saída: Produtos na faixa de preço: [{'nome': 'Teclado Mecânico',
# 'preco': 180.0}, {'nome': 'Webcam', 'preco': 85.0}]


minimo = float(input('Insira o valor mínimo: '))
maximo = float(input('Insira o valor máximo: '))


produtos = [
    {'Placa Mãe': 750}, {'Processador': 1300}, {'Placa de Vídeo': 4500}, 
    {'Memória RAM': 600}, {'NVME-M2': 600}, {'Fonte': 500}, {'HD 1TB': 350}, 
    {'Teclado Mecânico': 250}, {'Mouse Gamer': 200}, {'Monitor 24"': 1200}, 
    {'Headset': 300}, {'Webcam Full HD': 250}, {'Cadeira Gamer': 1200}, 
    {'Estabilizador': 450}, {'Notebook': 3500}, {'Roteador Wi-Fi 6': 600}, {'Impressora': 700}
]

produtos_no_preco = []

for i in produtos:
    valor = list(i.values())[0]
    if minimo < valor < maximo:
        produtos_no_preco.append(i)

print(produtos_no_preco)